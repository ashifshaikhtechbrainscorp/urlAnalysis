import pandas as pd

data = pd.read_csv("scrapped_text20240304 - Copy.csv")

relatedKeywords = []
for word in data['50 specific_words']:
    wordString = word.replace('[','').replace(']', '').replace(', ', ',').replace("'", '')
    if wordString != '':
        for w in wordString.split(','):
            relatedKeywords.append(w)
            print(w)

print(list(set(relatedKeywords)))
# print(data['50 specific_words'].head(50))