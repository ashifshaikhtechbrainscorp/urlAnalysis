import json

# Open the JSON file
with open('therapuetic.json') as f:
    data = json.load(f)

# item_set = ['cancer', 'lung', 'colon', 'kidney', 'liver', 'metastatic', 'breast', 'ovarian', 'prostate', 'skin', 'blood', 'brain', 'general']
# Now 'data' contains the parsed JSON object
# You can access its contents as needed
# item_set = ['cancer', 'lung']
item_set = ['cancer', 'liver', 'signs', 'symptoms', 'weight', 'changes', 'eye', 'early', 'loss', 'warning']
therapuetic_data = []
for item in data:
    # print(item['key'], item['label'])
    if item['key'] in item_set:
        therapuetic_data.append(item)
    elif item['label'].lower() in item_set:
        therapuetic_data.append(item)
    else:
        thera_diesease = item['label'].lower().replace('&', '').replace('and', '').replace(' / ', '/').replace('  ', ' ')
        diesease_length = len(thera_diesease.split(' '))
        count = 0
        for diesease in thera_diesease.split(' '):
            if diesease != '':
                if diesease in item_set:
                    count = count + 1

        # print(diesease_length, thera_diesease.split(' '), count)
        
        if(count > 0 and diesease_length == count):
            therapuetic_data.append(item)

print(therapuetic_data)