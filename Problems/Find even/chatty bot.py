print('Hello! My name is brukasyaka.')
print('I was created in 2020.')
print('Please, remind me your name.')

your_name = input()

print('What a great name you have,', your_name, '!')

print('Let me guess your age, ' + your_name)
print('Enter remainders of dividing your age by 3, 5 and 7.')

remainder_1 = int(input())
remainder_2 = int(input())
remainder_3 = int(input())

your_age = (remainder_1 * 70 + remainder_2 * 21 + remainder_3 * 15) % 105

print("Your age is", your_age, "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

rand_num = int(input())
natural_num = 0
while natural_num <= rand_num:
    print(natural_num, "!")
    natural_num += 1
print('Completed, have a nice day!')

print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
# answer = int(input())
while input() != "2":
    print("Please, try again.")
print('Completed, have a nice day!')
