cities_list = ['Banglore','Chennai','Hyderabad','Pune','Kolkata']

with open('./cities.txt','w') as f_cities:
    for city in cities_list:
        print(city, file=f_cities)
