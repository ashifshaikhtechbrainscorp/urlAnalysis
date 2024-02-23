import therapuetic_diseases as td
import requests
# [
#     { "key": "authenticated_mds", "label": "Authenticated_MDs" },
#     { "key": "demo:parents", "label": "Demo:Parents" },
#     { "key": "demo:seniors", "label": "Demo:Seniors" },
#     { "key": "demo:teen", "label": "Demo:Teen" },
#     { "key": "hepatitis-a", "label": "Hepatitis A" },
#     { "key": "hepatitis-b", "label": "Hepatitis B" },
#     { "key": "hepatitis-c", "label": "Hepatitis C" },
#     { "key": "ibs-c", "label": "IBS-C" },
#     { "key": "ibs-d", "label": "IBS-D" },
#     { "key": "meningitis-b", "label": "Meningitis B" },
#     { "key": "type-i-diabetes", "label": "Type I Diabetes" },
#     { "key": "type-ii-diabetes", "label": "Type II Diabetes" }
# ]

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

# item_set = [ 'cancer', 'liver', 'signs', 'symptoms', 'weight', 'changes', 'eye', 'prevention', 'early', 'loss', 'warning',
            # 'alzheimers', 'childrens', 'health', 'pregnancy', 'childbirth', 'aids', 'adhd', 'testosterone', 'hypogonadism',
            # 'adhd', 'testosterone', 'hepatitis', 'hypogonadism', 'low', 'type i', 'diabetes', 'hepatitis-a', 'b' ]
item_set = [ 'blood', 'Sugar', 'Hepatitis-a', 'B', 'Overactive', 'Bladder', 'CHF', 'IBS-D' ]
therapuetic_diseases = td.get_therapuetic_diseases(item_set)

for dieseases in therapuetic_diseases:
    drug_for_disease = get_drugs_for_disease(dieseases['label'])
    print(dieseases['label'], ':', drug_for_disease)

# print(therapuetic_diseases)