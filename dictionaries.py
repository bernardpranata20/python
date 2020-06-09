persons = [{
    'nama' :"bernard",
    'umur' :'17'},
    {'nama' :"Un",
    'umur' :'17'}
]

for person in persons:
    for key, value in person.items():
        print(key, value)