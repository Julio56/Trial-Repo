# title = "HotDog"
# years = 80
# expert_status = True
# print("Nick is a professional " + title)
# print("He has been coding for " + str(years) + " years")
# print("Expert status: " + str(expert_status))
# print(f"Expert status: {expert_status}")

# #########################################################

# name = "Inigo Montoya"
# country = "Canada"
# age = 45
# hourly_wage = 500
# satisfied = True
# daily_wage = hourly_wage * 8
# print("My name is " + name + ", prepare to die. " + "I am " + str(age) + " years old.")
# print("I live in " + country + " and make " + str(hourly_wage) + " an hour teaching fencing lessons.")
# print(f"Inigo Montoya makes a nice living, at {daily_wage} per day.")
# print(f"People say Inigo is going to make a killing with fencing. {satisfied} story.")
# print(daily_wage * 3 + hourly_wage / 8)
# print(str(daily_wage) + " dollars is not enough to pay the rent in High Gardens.")

############################################################

# n = 9
# if n > 33: 
#     print("It is greater than 33.")
# elif n <= 8:
#     print("It is less than or equal to 25.")
# else:
#     print("I have no idea what the hell is going on around here.")

##################################################################

# animals = ["dog", "cat", "dolphin"]
# print(animals)

# print(animals[2])

# animals.append("wombat")
# print(animals)

# birds_sighted = {"dove": 3, "eagle": 5, "rodan": 33,}
# print(birds_sighted)
# print(birds_sighted["rodan"])

# # def say_hello():
# #     print("Hello!")

# # say_hello()

# # def say_SuperBowlChampion():
# #     print("Super Bowl Champion New York Football Giants!")

# # say_hello()
# # say_SuperBowlChampion()

# name = "Roy Batty"
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello(name)


# import os
# import csv

# csv_file = os.path.join("PyBook", "budget_data.csv")
# with open(csvpath, newline='') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         print(row)

# condition = 1
# while condition < 10:
#     print(condition)
#     condition += 1

# while True:
#     print("doing stuff")

###############################

# exampleList = [1,2,4,3,4,7,5,8,66,54,56]
# for eachNumber in exampleList:
#     print(eachNumber)
#     print('continue program')

# for x in range(1, 11):
#     print (x)

#######################################
### THIS IS FOR THE HOMEWORK!!! NUMBER OF MONTHS EQUATION!!
#######################################
import os
import csv

dates = []
value = []

# with open('RUTJC201904DATA3/hw/week3/Instructions/PyBank/Resources/budget_data.csv', 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))



csvpath = os.path.join('..' ,'RUTJC201904DATA3/hw/week3/Instructions/PyBank/Resources/budget_data.csv')
 
with open(csvpath, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    dates = []
    next(csv_reader)  # Header does not print
    for row in csv_reader:
        # print(row)]
        dates.append(row[0])
    print ("There are " + (str(len(dates)) + " months."))
    #print(dates)    

# print(str(len([0])))

# lines = [line for line in open(csvpath)]

# lines[0]


##### We are testing here!!!#####


