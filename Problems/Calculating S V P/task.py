# duration = int(input())
# food = int(input())
# flight_cost = int(input())
# hotel = int(input())
#
# print ((food * duration) + (flight_cost * 2) + (hotel * (duration - 1)))

# def f1(a, b):
#     return not a or b
# def f2(a, b):
#     return (a or b) and not (a and b)
# def f3(a, b):
#     return (a and b) or not (a or b)
# def f4(a, b):
#     return (a and not b) or (not a and b)
# def f5(a, b):
#     return a and not b

#def print_result(f):
    #print(f(True, True), f(True, False))
    #print(f(False, True), f(False, False))
    #print()

#print_result(lambda a, b: not a or b)
# print_result(f1)
#print_result(lambda a, b: (a or b) and not (a and b))
#print_result(lambda a, b: (a and b) or not (a or b))
#print_result(lambda a, b: (a and not b) or (not a and b))
#print_result(lambda a, b: a and not b)
# don't modify this code
# a stores an input value

pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingridient = input()

if ingridient in pasta:
 print("pasta time!")

if ingridient in apple_pie:
 print("apple pie time!")

if ingridient in ratatouille:
 print("ratatoulle time!")

if ingridient in chocolate_cake:
  print("chocolate cake time!")

if ingridient in omelette:
 print("omelette time!")
