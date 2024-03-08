import json

def get_therapuetic_diseases(data_set, type):
    item_set = list(map(lambda x: x.lower(), data_set))

    # Open the JSON file
    with open('therapuetic.json') as f:
        data = json.load(f)

    # item_set = ['cancer', 'lung', 'colon', 'kidney', 'liver', 'metastatic', 'breast', 'ovarian', 'prostate', 'skin', 'blood', 'brain', 'general']
    # Now 'data' contains the parsed JSON object
    # You can access its contents as needed
    therapuetic_data = []
    for item in data:
        item_label = item['label'].lower()
        if item['key'] in item_set:
            therapuetic_data.append(item)
        elif item_label in item_set:
            therapuetic_data.append(item)
        elif item_label.replace('&', '').replace('and', '').replace(' / ', '/').replace('  ', ' ').replace("'", '') in item_set:
            therapuetic_data.append(item)
        elif item_label.replace('&', 'and') in item_set:
            therapuetic_data.append(item)
        elif item_label.replace('&', '') in item_set:
            therapuetic_data.append(item)
        elif item_label.replace('and', '&') in item_set:
            therapuetic_data.append(item)
        elif item_label.replace('and', '') in item_set:
            therapuetic_data.append(item)
        elif item_label.replace(' / ', '/') in item_set:
            therapuetic_data.append(item)
        elif item_label.replace('  ', ' ') in item_set:
            therapuetic_data.append(item)
        elif item_label.replace("'", '') in item_set:
            therapuetic_data.append(item)
        else:
            thera_diesease = item_label.replace('&', '').replace('and', '').replace(' / ', '/').replace('  ', ' ').replace('(', '/').replace(')', '')
            if thera_diesease in item_set:
                therapuetic_data.append(item)
            elif len(thera_diesease.split(' ')) == 1 and len(thera_diesease.split('/')) > 1:
                for diesease in thera_diesease.split('/'):
                    if diesease in item_set:
                        therapuetic_data.append(item)
            elif len(thera_diesease.split(' ')) > 1 and len(thera_diesease.split('/')) > 1:
                for diesease in thera_diesease.split('/'):
                    if len(diesease.split(' ')) > 1:
                        diesease_length = len(diesease.split(' '))
                        count = 0
                        for diesease_w in diesease.split(' '):
                            if diesease_w != '':
                                diesease_w = diesease_w.replace("'", '')
                                if diesease_w in item_set:
                                    count = count + 1

                        if(count > 0 and diesease_length == count):
                            therapuetic_data.append(item)
                    elif diesease in item_set:
                        therapuetic_data.append(item)

            elif len(thera_diesease.split(' ')) > 1:
                diesease_length = len(thera_diesease.split(' '))
                count = 0
                for diesease in thera_diesease.split(' '):
                    if diesease != '':
                        diesease = diesease.replace("'", '')
                        if diesease in item_set:
                            count = count + 1
                
                if(count > 0 and diesease_length == count):
                    therapuetic_data.append(item)
    
    therapuetic_label = []
    if type == 'label':
        for data in therapuetic_data:
            therapuetic_label.append(data['label'])

        therapuetic_data = therapuetic_label

    if type == 'key':
        for data in therapuetic_data:
            therapuetic_label.append(data['key'])

        therapuetic_data = therapuetic_label

    return therapuetic_data

print(get_therapuetic_diseases(['blood', 'pressure', 'colon', 'kidney', 'liver', 'heart', 'attack', 'ovarian',
                                'prostate', 'skin', 'blood', 'brain', 'general'], 'label'))