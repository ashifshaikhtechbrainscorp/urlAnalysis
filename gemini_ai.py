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
def get_related_keywords(item_set):
    model = genai.GenerativeModel('gemini-pro')
    # response = model.generate_content(f"""suggest some keywords or therauputic diseases or
    # dieseases strongly related to the following keywords below, the suggested keywords should be 1-2
    # words only and should have strong correlation with the keywords. The keywords are
    # {item_set}
    # Please suggest keywords which are in strong relation to given keywords and occur mostly with these keywords
    # or occurs in context of these keywords.""")
    #
    response = model.generate_content(f"""
    Give me indian drug name related to these keywords: {item_set}""")

    response_text = response.text.replace('* ', '').replace('\n', ',').replace('*','').replace('    - ', '').replace('- ', '')
    
    results = []
    for text in response_text.split(','):
       if text != '':
          results.append(text)

    return results