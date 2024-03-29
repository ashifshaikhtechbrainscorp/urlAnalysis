# from collections import Counter
# from math import log
# from nltk import word_tokenize
# from nltk.corpus import brown, stopwords

# import nltk
# nltk.download('brown')

# def intersection(lst1, lst2):
#     lst3 = [value for value in lst1 if value in lst2]
#     return lst3

def excludedWords():
    return ('image', 'style', 'give', 'side', 'may', 'someone', 'told', 'said',
        'doctors', 'top', 'people', 'cells', 'baby','name', 'city','also', 'us','read','go','j','ratemds',
        'day','make','know','many','like','help','holidays','well','holiday','advertisement','ratemds','doctorfind','epoch')

# # Read the document (replace 'document.txt' with your article)
# article_text = """'
# The Link Between Stress and Arthritis - ArthritisLiving.today ArthritisLiving.todayMenuArthritis SymptomsArthritis CopingBlogSearchSearch The Relationship Between Stress and ArthritisFacebookPinterestMessengerTwitterEmail9 years ago| by Eric Patterson Photo Credit: OcusFocus / iStockphoto.comStress and ArthritisThink back to life around the time when your arthritis symptoms began. What was going on? How did you feel? Were there any major life changes going on? How was your stress?Now, think back to a recent time when you had a lot of stress. How were your arthritis symptoms? Did you notice any changes? Were they for the better or the worse?After you answered these questions, you probably began to uncover the relationship between stress and arthritis. Many people report the onset of their symptoms come immediately after a major life event or after an intensely stressful time. They also report that once the symptoms are established, they increase their levels of perceived stress. Things that would normally be easier to manage become major barriers or obstacles to overcome because of arthritis pain.The relationship between stress and arthritis is clear, and it is bidirectional. This means that stress can spark or worsen arthritis while arthritis can trigger or worsen stress. Experts in the field are constantly looking for ways to explain the link.Currently, they have two ideas regarding the biological explanation for the link, which each has to do with the bodyâ€™s response to stress. The targets are called cytokines and cortisol. Cytokines are a category of proteins released by cells. Some cytokines are related to inflammation associated with arthritis. Cortisol is a hormone that is released during periods of stress that inhibits the bodyâ€™s ability to repair cell damage.Stress/Arthritis SolutionsIn this case, the question remains: What can I do to improve my arthritis so that my stress is lower, and how do I lower my stress to improve my arthritis? The answer is a long one that is broken into two parts. Part one is to take care of your arthritis. Part two is to take care of your stress. Focusing on one or the other can result in you being overwhelmed and burned out, though. Because your time, efforts, and resources are limited, it is advantageous to seek out solutions that efficiently manage both steps simultaneously. Hereâ€™s how:The Big ThreeWith your physical health, there is nothing more important than the combination of sleep, diet, and exercise. When stress or arthritis are present, modifying one or all of these factors can lead to tremendously beneficial results. Having the right amount of sleep for you; an improved diet based on lean proteins, fruits, and vegetables; and increased, low-impact physical activity will make a positive difference in your mental health and physical health.You may think that increased physical activity will increase your arthritis pain, but reconsider this faulty notion. Consult your physician to find the recommended form of exercise for your level of pain. Swimming, walking, yoga or elliptical trainers could give you the profits of exercise without the pain. Overall, exercise is shown to reduce joint pain with consistent use. Studies also show exercise to be associated with the release of stress-reducing chemicals into the brain.Related Search Topics Back Arthritis Pain ReliefBack Pain Relief ArthritisTreatment Rheumatoid ArthritisRA and Fibromyalgia Treatments You May Also LikeIs Botox Therapy an Effective Treatment Option for Arthritis?Arthritis CopingIs Botox Therapy an Effective Treatment Option for Arthritis?4 years ago| by Miles MartinBotox injections for arthritis are an FDA approved treatment option to help prevent arthritic pain. Learn more to find out if it's the right option for you.Eating well helps you to feel well both mentally and physically. For your physical health, be sure to evade known foods that result in inflammation or increase discomfort. Ask your doctor to list foods you should avoid while you maintain a food journal to track poor food choices specific to your body. When you eat for energy rather than enjoyment, your body and mind reward you with a heightened ability to manage daily stress.With sleep, the evidence is everywhere. Sleeping helps your body and your mind reset and recuperate after a long day. Be aware, though. More sleep is not necessarily better. Investigate your sleep patterns to determine if your trends need to be shortened or extended. Experiment with different lengths of sleep gradually to ease your body through the process.Relaxation TechniquesIf stress is a concern in your life, relaxation techniques are a viable solution. Techniques come in many variations with near-endless options for customization. For your stress and arthritis, there is a version perfect for you. An added layer of benefit is that most relaxation techniques work to strengthen the body as well as the mind.Begin with a simple deep breathing technique. Diaphragmatic breathing means that you are using your diaphragm to inhale in a deeper way that increases the volume of air in your lungs. Increased air available floods your blood much-needed oxygen to feed your organs. When oxygen is sufficient, your heart can slow, which calms your entire being. If deep breathing has been a struggle, begin with the exhale. Push out all of the air from your lungs, pause, and then suck in as much air as your can to fill low in your lungs. Leave your shoulders still, and push out your stomach.Progressive muscle relaxation (PMR) is another relaxation technique that yields a two-fold value. By tensing and relaxing your muscles, you can stretch and move your joints in a way that relieves pain. To complete PMR, tense muscles in a part of your body by squeezing your hands into fists or squinting you eyes and forehead. Target the sources of your physical stress. After holding and feeling the tension, relax the muscles and feel the tension melt away. Experiment with different methods of tension in different locations to explore all the PMR has to offer.Find AcceptanceEvery day, people have added stress and discomfort in their life due to lack of acceptance of their current state. Yes. You can manage arthritis symptoms, and you can reduce your stress, but there is little chance that either will be completely eradicated. Because of this, you need to find acceptance.Bringing acceptance into your life does not mean that you are giving up or ending your battle with arthritis or stress. It does mean that you understand the influence that these issues present to your life. Acceptance helps to change your expectations of yourself and your world to be more practical and realistic. Some days you are going to be in pain. Some days your stress will be high. Denying these facts only amplify the unwanted effects.ConclusionArthritis and stress are painful in a literal and figurative way. Do not expend your energies inefficiently by trying to improve each individual. Working on the tips above will simultaneously lessen your physical pain and mental anguish while improving your overall well-being. By changing your life, the only risk is feeling better. Start feeling better today.FacebookPinterestMessengerTwitterEmailComments Recommended PostsBlogStiff, Painful Shoulder? It Might Be Shoulder ArthritisArthritis Symptoms8 Symptoms of Psoriatic Arthritis to Be Aware OfArthritis SymptomsCan Arthritis Cause Chest Pain?BlogHow Eating Better Can Help Arthritis SymptomsBlogFour Foods You Shouldnâ€™t Eat If You Have ArthritisBlogCould Botox Injections Help Osteoarthritis?you may also likeArthritis CopingManaging Arthritis in the MorningArthritis CopingOver-the-Counter Options for Treating Arthritis PainArthritis Coping8 Ways to Combat Arthritis-Related StiffnessArthritis CopingHow to Sleep With Arthritisconnect with usPrivacy PolicyTerms of UseAbout UsContact UsArthritisLiving.today Copyright Â© 2024. All Rights Reserved.

# """

# article_text = """
# How to Sleep With Arthritis - ArthritisLiving.today ArthritisLiving.todayMenuArthritis SymptomsArthritis CopingBlogSearchSearch How to Sleep With ArthritisFacebookPinterestMessengerTwitterEmail9 years ago| by Meredith Crowhurst Photo Credit: DNF-Style / iStockPhoto.comA Better Sleep Could Mean Less PainInsomnia or sleep disturbance is common in those who have osteoarthritis, occurring in more than half of older people with arthritis. Sufferers have trouble getting to sleep with arthritis, as well as staying asleep, waking early, and the sleep tends to be lighter, restless and unrefreshing.As people get older, they tend to spend more of their sleep time in the lighter phases of sleep, which means they are more likely to be disrupted by the pain and discomfort of arthritis. While the pain of arthritis is a factor in poor sleep, it is not the only cause.Getting a Better SleepIn fact, research has shown pain killers are not necessarily the answer to disturbed sleep. For some reason, insomnia and arthritis often just co-exist. Medications given for arthritis may also be making sleep difficult. Cortisone, for example, can cause insomnia and, while some painkillers may make you drowsy, they may make you fall asleep during the day, which can then make it difficult to fall asleep at night.Whatever the cause, improving sleep is important. Research indicates that the sleep deprivation amplifies the pain of arthritis and a bad nightâ€™s sleep is linked to worse arthritis pain the next day. The deep stages of sleep are also when the body releases hormones to repair muscle damaged during the day. Disrupted sleep can also affects other aspects of life, causing fatigue, thinking problems, difficulty concentrating, poor memory, headaches and disturbed mood.Related Search Topics Back Arthritis Pain ReliefBack Pain Relief ArthritisRheumatoid Arthritis TreatmentsRA and Fibromyalgia Treatments You May Also LikeThe Gout Diet: 7 Foods to Eat With GoutArthritis CopingThe Gout Diet: 7 Foods to Eat With Gout6 years ago| by Jeanie DavisMany healthy foods to eat with gout include dark leafy greens, cherries, beans, lentils, water, and certain proteins and dairy.While sleep medications can assist, they do have side effects. They also do not address the underlying causes for the sleep disturbance, which can lead to reliance on the sleep medication. Lifestyle modification and non-medication therapies have been shown to help.Some habits that can assist with sleep are:Avoid caffeine, in tea, coffee and soft drinks, especially after middayAvoid eating a large meal within three hours of bedtimeAvoid nicotine before bedtimeAvoid alcohol before bed, as it might make you sleepy but the quality of sleep is worseAvoid exercise three hours before bedtimeAvoid napping during the dayCreate a relaxing bedtime routine, going to bed and getting up at the same time every dayKeep the bedroom dark, cool and quietAvoid watching television, using your phone or tablet, or working in the bedroomTry taking a bath before bedIf you canâ€™t fall asleep, after 20 minutes get up and go back to bed when you feel sleepyGet adequate light exposure during the dayIt may help to create a sleep diary, recording your sleep patterns and what factors have helped and hindered you getting to sleep and staying asleep. Using a fitness tracker with a sleep recording device may also help you to understand better the quality of the sleep you are getting.If medication is keeping you awake, you might also need to talk to your doctor about altering your medications or the time of day you take them.Therapies to Help Get a Better SleepThere are some specific therapies shown to help with sleep:Yoga â€“ involves stretching, strengthening, balancing, breathing exercises and meditation. Yoga may help with sleep by reducing joint stiffness and promoting relaxation.Cognitive behavioral therapy (CBT) â€“ involves training the mind to change from negative unhelpful thinking to more positive useful thought patterns. Examples include changing the bedtime routine and counteracting negative thoughts in the evening. CBT is taught by psychologists and there are also online courses where you can learn techniques.Relaxation techniques â€“ relaxation exercises include deep breathing, controlled and timed breathing, mindfulness meditation, tai chi, and activities that focus the mind in the present. Relaxation can help calm the mind prior to bed. It can also help relax any stiff and aching muscles.Daily exercise â€“ gentle daily exercise can help. It can make you feel more fatigued at the end of the day, which can help with sleepiness. 20 minutes every day is good and can be spaced in two 10-minute segments. Low-impact exercises, such as walking, cycling or water aerobics are good.Medication - if sleep is very difficult, there may be a role for medication. Doctors may prescribe painkillers, anti-inflammatory medications, sedatives, or certain antidepressants that can have sedative effects. The type of medication will likely depend on the precise reason you are having trouble sleeping and must also take into consideration other medications you might be on.FacebookPinterestMessengerTwitterEmailComments Recommended PostsBlogWhat Are the Signs of Arthritis in the Back?BlogHow Eating Better Can Help Arthritis SymptomsArthritis Symptoms10 Carpal Tunnel Symptoms to Be Aware OfBlogCould Botox Injections Help Osteoarthritis?BlogGluten-Free Diet for Arthritis: 4 Foods That Can Help With InflammationArthritis SymptomsPsoriatic Arthritis: More Than Skin Deepyou may also likeArthritis Coping8 Ways to Combat Arthritis-Related StiffnessArthritis CopingIs Stem Cell Therapy for Arthritis an Effective Course of Treatment?Arthritis CopingHow Losing Excess Weight Can Help ArthritisArthritis CopingClinical Trials for Osteoarthritis, Rheumatoid and Psoriatic Arthritisconnect with usPrivacy PolicyTerms of UseAbout UsContact UsArthritisLiving.today Copyright Â© 2024. All Rights Reserved.
# """
# stop_words = set(stopwords.words('english'))

# article_words = article_text.split(' ')
# filtered_words = []
# for w in article_words:
#     if w.lower() not in stop_words and w.lower() not in ['you']:
#             filtered_words.append(w)

# article_text = ' '.join(filtered_words)   
# toks = word_tokenize(article_text.lower())

# # Compute term frequency (TF)
# tf = Counter(toks)

# words = word_tokenize(article_text)

# # words_to_skipped = ['Bad request','JavaScript']


# brown_words = []
# for w in brown.words():
#     if w.lower() not in stop_words and w.lower() not in ['you']:
#         brown_words.append(w)
# # filtered_words = [word.lower() for word in filtered_words1 if word.isalpha() and word.lower() not in more_words_to_be_filtered]

# # Calculate inverse document frequency (IDF) from a larger corpus (e.g., Brown corpus)
# freqs = Counter(w.lower() for w in brown_words)
# n = len(brown_words)

# # Compute TF-IDF scores
# for word in tf:
#     tf[word] *= log(n / (freqs[word] + 1))**2

# # Print the top relevant words
# for word, score in tf.most_common(10):
#     print(f'{score:.2f} {word} {len(word)}')



from collections import Counter
import math
import requests
import common_words as cw
import spacy
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

def extract_collocations(text):
    words = word_tokenize(text)
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(BigramAssocMeasures.likelihood_ratio, 10)  # Get top 10 collocations
    return bigrams

nlp = spacy.load("en_core_web_sm")

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
            custom_stopwords = set(cw.moreExcludedWords())
            stop_words = set(stopwords.words('english')) | custom_stopwords
            tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

            # Calculate term frequency
            term_freq = Counter(tokens)

            # Calculate maximum term frequency to normalize scores
            max_freq = max(term_freq.values())

            # Calculate relevance score for each term
            relevance_scores = {term: tf / max_freq for term, tf in term_freq.items()}

            # Sort terms by relevance score
            sorted_terms = sorted(relevance_scores.items(), key=lambda x: x[1], reverse=True)

            print(sorted_terms[:10])  # Return top 10 relevant keywords
        else:
            print(f"Failed to fetch URL: {url}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
extract_keywords_from_url("https://www.news-medical.net/news/20240218/Wastewater-clues-could-revolutionize-Alzheimers-detection.aspx")
# extract_keywords_from_url("https://www.news-medical.net/condition/Coronavirus-Disease-COVID-19")
# extract_keywords_from_url("https://www.news-medical.net/news/20240226/Healthcare-leaders-advocate-for-restoring-Canadas-hypertension-control-program.aspx")
# extract_keywords_from_url("https://www.msn.com/en-in/sports/other/chess-player-tania-sachdev-asked-internet-to-edit-her-pic-people-didn-t-disappoint/ar-BB1j134u?ocid=msedgntp&pc=HCTS&cvid=2a0dc6725dfc4e7eac4876928f9fafa3&ei=26")
# extract_keywords_from_url("https://www.cancer.gov/news-events/cancer-currents-blog/2023/tarlatamab-previously-treated-sclc")
