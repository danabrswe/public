# module =          a file containing python code. may contain functions, classes etc.
#                   used with modular programming, which is to separate a program into parts

import messages as msg
# from messages import hello, bye           # functions can be used directly (without preceding namespace)
# from messages import *                    # imports all public names and they can be accessed directly

msg.hello()
msg.bye()

help("modules")             # lists all available modules