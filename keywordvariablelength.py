# def person(name, *data):

#     print(name)
#     print(data)     # rest will get printed in tuple format



# person("Joyjeet", 21, "Asansol", 2589)


def person(name, **data):

    print(name)

    for i,j in data.items():
        print(i,j)


person("Joyjeet", age = 21, city = "Asansol", mob = 2589)