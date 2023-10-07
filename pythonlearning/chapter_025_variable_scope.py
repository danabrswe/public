# scope         = the region that a varible is recognized.
#               A variable is only available from niside the region it is created.
#               A global and locally scoped versions of a variable can be created.
#
# LEGB          = Local, Enclosing, Global, Built-in. The order in which versions of a variable is used if they share the same name.

name = "Abrahamsson"

def display_name():
    name = "Daniel"     # local version of "name" is used first. if no local version exists, the global version will be used and
                        # output will be "Abrahamsson".
    print(name)

display_name()