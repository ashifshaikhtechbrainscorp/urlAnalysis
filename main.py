import nltk
import ssl
import joblib
import json
import certifi
import common_words as cw
from urllib.request import urlopen
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import requests
from bs4 import BeautifulSoup
import csv
import re
from datetime import datetime
import pandas as pd
# from selenium import webdriver
import urllib3
from nltk.tag import pos_tag
import spacy
from nltk.stem import WordNetLemmatizer
from collections import Counter
import Drugs

nlp = spacy.load('en_core_web_sm')

def get_drugs_for_disease(disease):
    # Define the OpenFDA API endpoint for drug label information
    endpoint = "https://api.fda.gov/drug/label.json"

    # Parameters for querying the OpenFDA API
    params = {
        'search': f'indications_and_usage:"{disease}"',  # Search for drugs with specified indication
        'limit': 10  # Limit the number of results to 10
    }

    # Make a GET request to the OpenFDA API
    response = requests.get(endpoint, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Extract drug names from the response
        drugs = []
        for result in data['results']:
            if 'generic_name' in result['openfda']:
                drugs.append(result['openfda']['generic_name'][0])

        return drugs
    else:
        # If the request was not successful, print an error message
        print("Error:", response.status_code)
        return None

related_terms = {
    'blood sugar': ['diabetes'],
    'heart disease': ['cardiovascular', 'cholesterol'],
    'weight loss': ['fitness', 'diet', 'exercise'],
    # we will add more related terms and their associated strong keywords as needed : AS
}

def extract_strong_keywords_and_scores(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()

            # Use SpaCy for noun chunk extraction
            doc = nlp(text)
            noun_chunks = [chunk.text.lower() for chunk in doc.noun_chunks]

            # Combine noun chunks into the text
            text += " ".join(noun_chunks)

            tokens = word_tokenize(text)
            tokens = [word.lower() for word in tokens]
            custom_stopwords = set(['people', 'said', 'help', 'image', 'mm','hg','cdc','ra','years','style', 'give', 'side', 'may', 'someone',
                                    'told', 'doctors', 'top', 'people', 'cells', 'holidays', 'well', 'better',
                                    'holiday', 'baby', 'name', 'city', 'also', 'us', 'read', 'go', 'j', 'ratemds',
                                    'ratemds', 'doctorfind', 'image', 'style', 'give', 'side', 'may', 'someone',
                                    'told', 'said', 'doctors', 'top', 'people', 'cells', 'baby', 'name', 'city',
                                    'also', 'us', 'read', 'go', 'j', 'ratemds', 'day', 'make', 'know', 'many', 'like',
                                    'help', 'advertisement', 'ratemds', 'doctorfind', 'epoch'])
            stop_words = set(stopwords.words('english')) | custom_stopwords
            tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
            term_freq = Counter(tokens)
            max_freq = max(term_freq.values())
            relevance_scores = {term: tf / max_freq for term, tf in term_freq.items()}
            sorted_terms = sorted(relevance_scores.items(), key=lambda x: x[1], reverse=True)

            # Additional part to extract strong keywords based on related terms
            strong_keywords = set()
            for term, strong_terms in related_terms.items():
                if term in text:
                    strong_keywords.update(strong_terms)

            # Return relevant keywords along with their scores and strong keywords
            return sorted_terms, strong_keywords

        else:
            print(f"Failed to fetch URL: {url}")
            return None, None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None, None

def extract_keywords_from_url(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract text from HTML
            text = soup.get_text()

            # Tokenize the text
            tokens = word_tokenize(text)

            # Convert tokens to lowercase
            tokens = [word.lower() for word in tokens]

            # Remove stopwords and non-alphabetic tokens
            custom_stopwords = set(['people', 'said','mm','hg','cdc','help','ra','year','image', 'style', 'give', 'side', 'may','someone', 'told',
            'doctors', 'top', 'people', 'cells','holidays','well','better','holiday','baby','name', 'city','also', 'us','read','go','j','ratemds',
            'ratemds','doctorfind','image', 'style', 'give', 'side', 'may', 'someone', 'told', 'said',
        'doctors', 'top', 'people', 'cells', 'baby','name', 'city','also', 'us','read','go','j','ratemds',
        'day','make','know','many','like','help','advertisement','ratemds','doctorfind','epoch'])
            stop_words = set(stopwords.words('english')) | custom_stopwords
            tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

            # Lemmatize tokens
            lemmatizer = WordNetLemmatizer()
            tokens = [lemmatizer.lemmatize(word) for word in tokens]

            # Convert tokens back to string
            text = ' '.join(tokens)

            # Calculate TF-IDF scores
            tfidf = TfidfVectorizer()
            tfidf_matrix = tfidf.fit_transform([text])

            # Get feature names
            feature_names = tfidf.get_feature_names_out()
            tfidf_scores = tfidf_matrix.toarray()[0]

            # Sort feature names based on tf-idf scores
            sorted_indices = (-tfidf_matrix[0]).toarray()[0].argsort()
            keywords = [(feature_names[index], tfidf_scores[index]) for index in sorted_indices[:10]]

            return keywords
        else:
            print(f"Failed to fetch URL: {url}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def find_specific_words_and_write_to_csv(column_values):

    try:
        count = 0
        for value in column_values:
            count = count + 1
            url = value

            if(count > -1):

            # Send a GET request to the URL
                response = requests.get(url, verify=False)
                if response.status_code != 200:
                    continue

            # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')
                more_words_to_be_filtered = cw.excludedWords()

                text = soup.get_text()
                text = re.sub(r'\s{2,}', ' ', text)
                text = ' '.join(text.split())

                words = word_tokenize(text)
            # words_to_skipped = ['Bad request','JavaScript']
                stop_words = set(stopwords.words('english'))

                filtered_words1 = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

                filtered_words = [word.lower() for word in filtered_words1 if word.isalpha() and word.lower() not in more_words_to_be_filtered]

                lemmatizer = WordNetLemmatizer()
                filtered_words = [lemmatizer.lemmatize(word) for word in filtered_words]

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                fdist = FreqDist(filtered_words)

            # Print the 10 most common words
                print("10 Most Common Words (", count, "):")
                spec_words = []
                for word, frequency in fdist.most_common(10):
                    spec_words.append(word)

            # Use spaCy for part-of-speech tagging
                doc = nlp(text)
                nouns = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]
                diseases = ['cancer','heart','obesity','kidney','arteritis','lung','arthritis','tumor','diabetes','fibromyalgia','stress']
            # Assign categories based on identified nouns
                drugs=[]

                categories = set()
                for word1 in spec_words:
                    if word1 in diseases:
                        drugs = get_drugs_for_disease(word1)

                drug_list = drugs
                result_dict = Drugs.predict_drug_names(drug_list)

                json_result = json.dumps(result_dict)

                for noun in nouns:
                    if 'disease' in noun:
                        categories.add('Health')
                    elif 'technology' in noun:
                        categories.add('Technology')
                    else:
                        categories.add('Other')

                csv_filename = 'scrapped_text' + datetime.now().strftime("%Y%m%d") + '.csv'
                keywords1 = extract_keywords_from_url(url)

                relevant_keywords, strong_keywords = extract_strong_keywords_and_scores(url)
                if relevant_keywords is not None and strong_keywords is not None:
                    # print("Top 10 relevant keywords:")
                    rel_kw_2 = (relevant_keywords[:10])

                    # print("\nStrong keywords based on related terms:")
                    # (strong_keywords)


                with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    # Check if the file is empty
                    if csvfile.tell() == 0:
                        csv_writer.writerow(['Timestamp', 'URL', 'specific_words', 'specified_kw_set2', 'Categories', 'Drugs_ifAny','Drugs_cN','Strong_KW_ifAny','Relevant_KW3']) #related KW and related categories to be added
                    csv_writer.writerow([timestamp, url, spec_words, keywords1, list(categories), list(drugs),json_result,strong_keywords,relevant_keywords])

                csv_file = csv_filename
                json_file = 'data.json'
                csv_to_json(csv_file,json_file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def csv_to_json(csv_file, json_file):
    # Read CSV file and convert it to a list of dictionaries
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Write the data to a JSON file
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# CSV file path made for URL list
csv_file = 'urlAnalysis3.csv'
column_name = 'URL'
df = pd.read_csv(csv_file)
column_values = df[column_name].tolist()

# dr = webdriver.Chrome()
ssl._create_default_https_context = ssl._create_unverified_context

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

find_specific_words_and_write_to_csv(column_values)
