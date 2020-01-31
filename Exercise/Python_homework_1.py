# Дано 3 числа. Визначити чи всі числа непарні. Числа вводяться з клавіатури

def check(digit):
    if digit % 2 != 0:
        print(digit, " is odd.")
    else:
        print(digit, " is even.")



first = int(input("Enter first digit: "))
second = int(input("Enter second digit: "))
third = int(input("Enter third digit: "))

check(first)
check(second)
check(third)

# Дано три числа. Якщо перше число більше третього, то поміняти іх місцями.

if first > third:
    first, third = third, first

print(first, " ", second, " ", third) 

# Відомо, що 1 дюйм дорівнює 2.54 см. 
# Розробити програму, що переводить дюйми в сантиметри и навпаки. 
# Діалог с користувачем реалізувати через систему меню.

inch = 2.54

print("1. from inches to centimeters\n2. From centimeters to inches")

choise = int(input("Enter your choise: "))
data = float(input("Enter weight: "))

if choise == 1:
    print("In ", data, " inches = ") 
    data *= inch
    print(data, " centimeters.")
elif choise == 2:
    print("In ", data, " centimeters = ") 
    data /= inch
    print(round(data, 2), " inches.")


#Протягом тижня вимірювали температуру повітря. Знайти кількість днів, коли температура перевищувала 10o С

counter = 0

for item in range(8):
    day_temperature = float(input("Enter temperature for day: "))
    if day_temperature > 10:
        counter += 1

print("the temperature exceeded 10 degrees ", counter, " times this week")