def display_all(this_dict):
  """ Displays the capital city of each country in the dictionary """
        for key in this_dict:
            print("%s is the capital city of %s" % (this_dict[key].title(), key.title()))


def get_capital_city(province_name, this_dict):
    """ Returns the capital of the given province """
    if isinstance(this_dict, dict):
        return this_dict.get(province_name, "Province Not Found")


def add_province(province_name, capital_city, this_dict):
    """ Adds a province key/value pair to this_dict """
    if isinstance(this_dict, dict):
        this_dict[province_name] = capital_city


def remove_province(province_name, this_dict):
    """ Removes a province key/value pair in this_dict """
    if isinstance(this_dict, dict):
        del this_dict[province_name]


def get_total_population(this_dict):
    """ Returns the total population of this_dict by summing up the population of each """
    total_population = 0

    for province_name in this_dict:
        total_population += this_dict[province_name]["population"]

    return total_population


def get_another_capital_city(province_name, this_dict):
    """ Returns the name of the capital city for the given province_name """

    if province_name in this_dict:
        return this_dict[province_name]["capital"]
    else:
        return "Province not found"


def get_largest_city(province_name, this_dict):
    """ Returns the name of the largest city for the given province_name """

    if province_name in this_dict:
        return this_dict[province_name]["largest"]
    else:
        return "Province not found"


def get_smallest_province(this_dict):
    """ Returns the name of the province with the smallest population """

    population = min((int(a["population"])) for a in this_dict.values())

    smallest_province = [b for b in this_dict if (int(this_dict[b]["population"])) == population]

    return "".join(smallest_province)


def get_largest_province(this_dict):
    """ Returns the name of the province with the largest population """

    population = max((int(a["population"])) for a in this_dict.values())

    largest_province = [b for b in this_dict if (int(this_dict[b]["population"])) == population]

    return "".join(largest_province)
