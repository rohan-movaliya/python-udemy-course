travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


def add_new_country(country, visits, cities):
    new_value = {}
    new_value["country"] = country
    new_value["visits"] = visits
    new_value["cities"] = cities
    travel_log.append(new_value)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
