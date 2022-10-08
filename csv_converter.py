import csv
list_of_country = []
list_of_names = []
name_ukrainians = []
name_usa = []
name_paris = []
name_india = []
usa = 0
paris = 0
india = 0
ukrainians = 0
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        list_of_country.append(row['country'].split(','))
        list_of_names.append(row['person'].split(','))
i = 0
while i <= len(list_of_names) - 1:
    if list_of_country[i] == ['Ukraine']:
        name_ukrainians.append(list_of_names[i])
        ukrainians += 1
        i += 1
    if list_of_country[i] == ['Paris']:
        name_paris.append(list_of_names[i])
        paris += 1
        i += 1
    if list_of_country[i] == ['USA']:
        name_usa.append(list_of_names[i])
        usa += 1
        i += 1
    if list_of_country[i] == ['India']:
        name_india.append(list_of_names[i])
        india += 1
        i += 1
    if i == 12:
        break
dict_of_result = {'Ukraine': {'people': name_ukrainians, 'count': ukrainians},
                  'USA': {'people': name_usa, 'count': usa},
                  'Paris': {'people': name_paris, 'count': paris},
                  'India': {'people': name_india, 'count': india}}
print(dict_of_result)
