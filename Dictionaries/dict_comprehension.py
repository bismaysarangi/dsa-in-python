import random
#new_dict = {key: value for key, value in myDict.items()}
city_names = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai']

cityTemps = {city:random.randint(20, 35) for city in city_names}
print(cityTemps)

above_27 = {city:temp for (city, temp) in cityTemps.items() if temp > 27}
print(above_27)