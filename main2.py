my_file = open('nationsPop.txt', 'r')
lines = my_file.readlines()
country_data = []
for country_line in lines:
    country_line = country_line.strip()
    nations_pop_list = country_line.split(",")
    pop_dictionary = {'Name': (nations_pop_list[0]),
                      'Pop': int(nations_pop_list[1]),
                      'Change': float(nations_pop_list[2])
                      }
    country_data.append(pop_dictionary)

#prove that it worked
for nation in country_data:
    print(nation)
