# dictionary comprehension =    create dictionaries using an expression.
#                               can replace for loops and certain lambda functions

# dictionary = {key:expression for (key,value) in iterable}
# dictionary = {key:expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function for (key,value) in iterable}

# example 1
cities_in_F = {"New York":42, "Boston":75, "Los Angeles":100, "Chicago":50}
cities_in_C = {key:int(round((value-32)*5/9,0)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

weather = {"New York":"snowing", "Boston":"sunny","Los Angeles":"sunny","Chicago":"cloudy"}
sunny_weather = {key:value for (key,value) in weather.items() if value=="sunny"}
print(sunny_weather)

desc_cities = {key: ("warm" if value >= 55 else "cold") for (key,value) in cities_in_F.items()}
print(desc_cities)

def check_temp(value):
    if value >= 80:
        return "hot"
    elif value >= 55:
        return "warm"
    else:
        return "cold"
desc_cities = {key: check_temp(value) for (key,value) in cities_in_F.items()}
print(desc_cities)