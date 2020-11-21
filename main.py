import utilities_dict


def main():
    """ Main function of the Program"
    
    #PART A
    provinces = {"alberta": "edmonton",
                 "ontario": "toronto",
                 "quebec": "quebec city",
                 "nova scotia": "halifax",
                 "new brunswick": "fredericton",
                 "manitoba": "winnipeg",
                 "prince edward island": "charlottetown",
                 "saskatchewan": "regina",
                 "newfoundland and labrador": "st. john's",
                 "yukon": "whitehorse",
                 "nunavut": "iqaluit",
                 "northwest territories": "yellowknife",
                 "british columbia": "victoria"}

    print("The current dictionary contains:")
    utilities_dict.display_all(provinces)

    print("The capital of the yukon is:")
    utilities_dict.get_capital_city("yukon", provinces)

    print("Remove Manitoba from the list: ")
    utilities_dict.remove_province("manitoba", provinces)
    utilities_dict.display_all(provinces)

    print("Adding Manitoba back to the list: ")
    utilities_dict.add_province("manitoba", "winnipeg", provinces)
    utilities_dict.display_all(provinces)

    #PART B
    canada = {
        "alberta": {"capital": "edmonton", "largest": "calgary", "population": 3645257},
        "ontario": {"capital": "toronto", "largest": "toronto", "population": 12851821},
        "quebec": {"capital": "quebec city", "largest": "montreal", "population": 7903001},
        "nova scotia": {"capital": "halifax", "largest": "halifax", "population": 921727},
        "new brunswick": {"capital": "fredericton", "largest": "saint john", "population": 751171},
        "manitoba": {"capital": "winnipeg", "largest": "winnipeg", "population": 1208268},
        "prince edward island": {"capital": "charlottetown", "largest": "charlottetown", "population": 140204},
        "saskatchewan": {"capital": "regina", "largest": "saskatoon", "population": 1033381},
        "newfoundland and labrador": {"capital": "st. john's", "largest": "st. john's", "population": 514536},
        "yukon": {"capital": "whitehorse", "largest": "whitehorse", "population": 33897},
        "nunavut": {"capital": "iqaluit", "largest": "iqaluit", "population": 31906},
        "northwest territories": {"capital": "yellowknife", "largest": "yellowknife", "population": 41462},
        "british columbia": {"capital": "victoria", "largest": "vancouver", "population": 4400057}
            }

    print("The total population of all provinces in Canada is", utilities_dict.get_total_population(canada))

    capital = (utilities_dict.get_another_capital_city("yukon", canada))
    print("The capital city of %s is %s" % (capital[1].title(), capital[0]))

    largest_city = (utilities_dict.get_largest_city("quebec", canada))
    print("The largest city of %s is %s" % (largest_city[1].title(), largest_city[0]))

    print("The smallest province in Canada is", utilities_dict.get_smallest_province(canada))
    print("The largest province in Canada is", utilities_dict.get_largest_province(canada))


if __name__ == "__main__":
    main()
