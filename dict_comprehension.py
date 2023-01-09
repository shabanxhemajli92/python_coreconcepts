"""
dictionary = {key:expression for (key,value) in iterable}
this is the formula for dictionary comprehension
"""

cities_in_f={"Ney York":34,"Boston":75,"Los Angeles":100,"Chicago":50}
warm_weather={key: ("Warm" if value >= 40 else "Cold") for (key,value) in cities_in_f.items()}
print (warm_weather)


cities_in_c = {key: ((value-32)*(5/9)) for key, value in cities_in_f.items()}
cities_in_c= {key: round(value, 2) for key, value in cities_in_c.items()}
print(cities_in_c)

weather ={"New york":"snowing","Boston ":"sunny","Chicago":"Cloudy"}
sunny_weather={key:value for (key,value) in weather.items() if value  == "sunny"}
print(sunny_weather)

"""
A dictionary comprehension is a way to create a new dictionary using an iterable in a single line of code. It is a concise and convenient way to create dictionaries, especially when you need to transform or filter the data in some way.
"""