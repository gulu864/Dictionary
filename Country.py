Country_code = {'India':'0091',
                'Nepal':'0977',
                'Australlia':'0025'}
print(Country_code)

print("Country code for india:",Country_code.get('India', 'Not found'))
print("Country code for Mexico:",Country_code.get('Mexico', 'Not found'))