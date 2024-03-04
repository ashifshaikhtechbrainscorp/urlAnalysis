def excludedWords():
    return ('image', 'style', 'give', 'side', 'may', 'someone', 'told', 'said',
        'doctors', 'top', 'people', 'cells', 'baby','name', 'city','also', 'us','read','go','j','ratemds',
        'day','make','know','many','like','help','holidays','well','holiday','advertisement','ratemds','doctorfind','epoch')

def moreExcludedWords():
    return ['people', 'said', 'help', 'image', 'style', 'give', 'side', 'may', 'someone',
            'told', 'doctors', 'top', 'people', 'cells', 'holidays', 'well', 'better',
            'holiday', 'baby', 'name', 'city', 'also', 'us', 'read', 'go', 'j', 'ratemds',
            'ratemds', 'doctorfind', 'image', 'style', 'give', 'side', 'may', 'someone',
            'told', 'said', 'doctors', 'top', 'people', 'cells', 'baby', 'name', 'city',
            'also', 'us', 'read', 'go', 'j', 'ratemds', 'day', 'make', 'know', 'many', 'like',
            'help', 'advertisement', 'ratemds', 'doctorfind', 'epoch']


from nltk.corpus import wordnet

word_to_find_synonyms_for = "diabetes"
synonyms = set()
for synset in wordnet.synsets(word_to_find_synonyms_for):
    synonyms.update(synset.lemma_names())

print(f"Synonyms for '{word_to_find_synonyms_for}': {', '.join(synonyms)}")

