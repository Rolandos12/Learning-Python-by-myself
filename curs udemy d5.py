#using loops create a program that calculates the average student height from a list
#without using sum() or len()

# students_heights=[170, 156, 178, 202, 166, 187]
# total_height=0
# for height in students_heights:
#     total_height+= height
# print(total_height)
#
# number_students=0
# for students in students_heights:
#     number_students+=1
# print(number_students)
#
# avarage= round(total_height/number_students)
# print(avarage)

#write a program that calculates the highest score form a List of scores
#not allowed to use max or min functions

# students_score = input("The list of students' scores is: ")
# students_score = students_score.split()
# students_score = [int(score) for score in students_score]
# highest_score = 0
#
# for score in students_score:
#     if score > highest_score:
#         highest_score = score
#
# print(f'The highest score is: {highest_score}')

#create a program that calculate only even numbers form 1 to 100, including 1 and 100
# eg. 1+2+4+6... +100
# total=0
# for number in range(2, 101, 2):
#     total+= number
# print(total)
#
# total2=0
# for number in range(1,101):
#     if number%2==0:
#         total2+=number
# print (total2)

#you are going to play FizzBuzz game, your program should print each number from 1 to 100 in turn. for every number divisible with 3 you should say Fizz
#for every number divisible with 5 will say Buzz and for every number divisible with both will say FizzBuzz
#eg. 3/3=fizz, 5/5=buzz, 15/5 or /3= fizzbuzz

# for number in range(1,101):
#     if number%3==0 and number%5==0:  #or number%15==0
#         print("FizzBuzz")
#     elif number%5==0:
#         print("Buzz")
#     elif number%3==0:
#         print("Fizz")
#     else: print(number)
# print(number)

#create a program that generate a random password form by letters, numbers and symbols
import random
import string

number_list=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# letters_lower= string.ascii_lowercase
# letters_upper= string.ascii_uppercase
# letters_split= ",".join(letters_lower).split(",")
# letters_split2= ",".join(letters_upper).split(",")
# letters_list=[letters_split+letters_split2]
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


symbols_list=["%", "#", "@", "!", "^", "*", "&", "$"]

print("Welcome to password generator made by me")
nr_letters= int(input("How many letters you need?: "))
nr_numbers= int(input("How many numbers you need?: "))
nr_symbols= int(input("How many symbols you need?: "))

password=[]
for char in range(1, nr_letters+1):
    random_letter=random.choice(letters)
    password+= random_letter

for char in range(1, nr_numbers+1):
    random_numbers= random.choice(number_list)
    password+= random_numbers

for char in range(1, nr_symbols+1):
    random_symbols= random.choice(symbols_list)
    password+=random_symbols

random.shuffle(password)

final_password=""
for char in password:
    final_password+= char

print(f"Your password is:  {final_password} ")


