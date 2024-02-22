import therapuetic_diseases as td
item_set = [ 'cancer', 'liver', 'signs', 'symptoms', 'weight', 'changes', 'eye', 'prevention', 'early', 'loss', 'warning',
            'alzheimers', 'childrens', 'health', 'pregnancy', 'childbirth', 'aids', 'adhd', 'testosterone', 'hypogonadism',
            'adhd', 'testosterone', 'hepatitis', 'hypogonadism', 'low', 'type-i', 'diabetes', 'hepatitis-a', 'b' ]

therapuetic_diseases = td.get_therapuetic_diseases(item_set)

print(therapuetic_diseases)