# # Approach-1:
# import Animal
# import Bird
# Animal.fly()
# Animal.color()
#
# Bird.fly()
# Bird.color()
# Approach 2:
from Animal import *
fly()
color()   #here you are getting Bird related o/p because bird module is the latest implimentation
from Bird import *
fly()
color()