import therapuetic_diseases as td

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

item_set = [ 'cancer', 'liver', 'signs', 'symptoms', 'weight', 'changes', 'eye', 'prevention', 'early', 'loss', 'warning',
            'alzheimers', 'childrens', 'health', 'pregnancy', 'childbirth', 'aids', 'adhd', 'testosterone', 'hypogonadism',
            'adhd', 'testosterone', 'hepatitis', 'hypogonadism', 'low', 'type i', 'diabetes', 'hepatitis-a', 'b' ]
item_set = [ 'blood', 'Sugar', 'Hepatitis-a', 'B', 'Overactive', 'Bladder', 'CHF', 'IBS-D' ]
therapuetic_diseases = td.get_therapuetic_diseases(item_set)

print(therapuetic_diseases)