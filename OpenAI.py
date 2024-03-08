import openai
import csv

# Set your OpenAI API key
openai.api_key = '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'

def get_ai_keywords(provided_keywords):
    prompt_text = f"""suggest some keywords or therapeutic diseases or diseases strongly related to the following keywords below, the suggested keywords should be 1-2 words only and should have strong correlation with the keywords. The keywords are {', '.join(provided_keywords)} Please suggest keywords which are in strong relation to given keywords and occur mostly with these keywords or occurs in context of these keywords, a maximum of 10 responses only in a form of list without numbering them."""

    # Generate completion
    response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt_text,
            temperature=0.7,
            max_tokens=100,  # Adjust the max_tokens to control the length of the advertisement
        )

    # Print the suggested keywords
    response_text = response.choices[0].text.strip()

    # Extract suggested keywords
    suggested_keywords = response_text.split('\n')
    # suggested_keywords = response_text.split('\n')
    suggested_keywords = [keyword.strip('1234567890. ') for keyword in suggested_keywords if keyword.strip()]

    return suggested_keywords

def get_ai_diseases(provided_keywords):
    prompt_text = f"Please identify diseases or health conditions related to the following keywords: {', '.join(provided_keywords)}. Give only short headings of 1 to 3 words and not entire description."

    # Generate completion
    response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt_text,
            temperature=0.7,
            max_tokens=100,  # Adjust the max_tokens to control the length of the advertisement
        )

    # Print the suggested keywords
    response_text = response.choices[0].text.strip()

    # Extract suggested keywords
    suggested_diseases = response_text.split('\n')
    # suggested_keywords = response_text.split('\n')
    suggested_diseases = [keyword.strip('1234567890. ') for keyword in suggested_diseases if keyword.strip()]

    return suggested_diseases[:10]

#
# provided_keywords = ['arthritis', 'stress', 'pain', 'life', 'body', 'physical', 'sleep', 'symptom', 'exercise', 'manage']
# #     # ['blood', 'pressure', 'high', 'heart', 'health', 'disease', 'stroke', 'prevention', 'hypertension', 'cause']
# response_ai = get_ai_diseases(provided_keywords)
# print(response_ai)


