#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Used to securely store your API key
genai.configure(api_key='AIzaSyAj3lnUVGrh9kJf5zjCHLsau0oGTzVPpG0')

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

def get_related_drugs(item_set):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"""
    Give me indian drug name related to these keywords: {item_set}""")

    response_text = response.text.replace('* ', '').replace('\n', ',').replace('*','').replace('    - ', '').replace('- ', '').replace('    ', '')
    
    results = []
    for text in response_text.split(','):
       if text != '':
          results.append(text)

    return results

def get_related_diseases(item_set):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(f"""suggest some keywords or therauputic diseases or diseases monitoring or
    dieseases strongly related to the following keywords below, the suggested keywords should be 10-12
    words only and should have strong correlation with the keywords. The keywords are {item_set}
    Please suggest keywords which are in strong relation to given keywords and occur mostly with these keywords
    or occurs in context of these keywords.""")
    
    response_text = response.text.replace('* ', '').replace('\n', ',').replace('*','').replace('    - ', '').replace('- ', '').replace('    ', '')
    
    results = []
    for text in response_text.split(','):
       if text != '':
          results.append(text)

    return results

def get_content_contaxual_score(advert, content):
  # prompt_text = f"""On a scale of 1 to 10 can you analyze this Advert and provide only a
  # numeric number \"{advert}\" and \"{content}\" promoting a specific product or solution
  # and a given informational content piece on a related topic, considering factors such as
  # thematic relevance, audience targeting, and messaging coherence."""
  # print(prompt_text)
  prompt_text = f"""On a scale of 1 to 10 can you analyze this Advert and provide only a
  numeric number \"{advert}\" and \"{content}\" 
  promoting a specific product or solution and a given informational content piece on a related topic, considering
  factors such as thematic relevance, audience targeting, and messaging coherence. Provide the response as a
  correlation on a scale of 1 to 10, with 10 indicating strong alignment and 1 indicating minimal or no correlation."""

  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(prompt_text, stream=True)
  # try:
  #   for chunk in response:
  #     print(chunk.text)
  #     print("_"*80)
  # except Exception as e:
  #   print(f'{type(e).__name__}: {e}')

  # print(response)
  # print(response['probability'])
  
  response.resolve()
  # print(response.prompt_feedback)
  # print(response.candidates)
  # try:
  #   # response_text = response.text
  #   return response.text
  # except Exception as e:
  #   print(f'{type(e).__name__}: {e}')
  response_text = response.text
  return response_text

advert = """Women are loosing weight fast with this OTC solution"""
# advert = """Seasame Oil a helpful cure for blood pressure problem"""
content = """Cardiovascular disease is the most prevalent cause of death worldwide.
High blood pressure or hypertension is a risk factor for heart disease, and it affects at least one out of
three people in the United States. As potentially damaging as it can be, hypertension is largely preventable.
Though many popular foods cause inflammation, oxidative stress, and chronic hypertension, others can lower or
prevent high blood pressure naturally.

Sesame Oil
Sesame oil has demonstrated beneficial effects on blood lipid concentrations and arterial blood pressure.
In a 2012 study, participants who consumed sesame oil achieved short- and long-term lower blood pressure
readings with noticeable differences within an hour of ingestion. The exact mechanism by which sesame oil
lowers blood pressure isn't clear. Researchers believe the antioxidants and healthy fats in the oil may
play a role."""


print(get_content_contaxual_score(advert, content))