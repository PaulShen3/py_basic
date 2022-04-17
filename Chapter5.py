# 以下代码为第五章节相关学习代码
# 2022/1/18  17:45   author:沈嘉晨
# 章节内容：if 语句
#page 63~80

cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':                    #一个等号是陈述，两个等号是发问
        print(car.upper())
    else:
        print(car.title())

requested_poping = 'mushroons'
if requested_poping != 'anchovies':
    print("Hold the anchovies!")

age = 18
age == 18

#if-elif-else结构

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


age = 12
if age <4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

#如果只想执行一个代码块就用if-elif-else，如果要执行多个，就是用一些列独立的if语句

#practice 5-3
alien_color = 'green'
if alien_color == 'green':
    print("Add 5 points!")

#practice 5-4
alien_color = 'green'
if alien_color == 'green':
    print("Add 5 points!")
else:
    print("Add 10 points!")
#pracice 5-5 略

#practice 5-6
age = 18
if age < 2:
    print("He is a young baby.")
elif age < 4:
    print("He is a baby.")
elif age < 13:
    print("He is a child.")
elif age < 20:
    print("He is a teen.")
elif age < 65:
    print("He is an adult.")
else:
    print("He is an old.")

#practice 5-7
favourite_foods = ['banana','orange','coconut']
for favourite_food in favourite_foods:
    if favourite_food == 'banana':
        print("You really like bananas!")
    if favourite_food == 'apple':
        print("You really like apples!")

requested_popings = ['mushrooms','green peppers','extra cheese']
for requested_poping in requested_popings:
    if requested_poping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print(f"Adding {requested_poping}.")
print("\nFinished making your pizza!")

#确定列表是否为空
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")


avail_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avail_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry,we don't have {requested_topping}.")
print("\nFinished making your pizza!")

#practice 5-8
administration_names = ['admin','paul','lebron','curry','kobe']
for administration_name in administration_names:
    if administration_name == 'admin':
        print(f"Hello {administration_name},would you like to see a status report?")
    else:
        print(f"Hello {administration_name},thank you for logging in again.")

#practice 5-9
administration_names = ['admin','paul','lebron','curry','kobe']
for administration_name in administration_names:
    if administration_name == 'admin':
        print(f"Hello {administration_name},would you like to see a status report?")
    elif administration_name != 'admin':
        print(f"Hello {administration_name},thank you for logging in again.")
    else:
        print("We need to find some users!")

#practice 5-10   不太明白
current_users = ['paul','kobe','lebron','howard','wade']
new_users = ['curry','anthony','irving','paul','jordan']
for new_user in new_users:
    if new_user == 'paul':
        print("This name has been used.")
    else:
        print("This name has not been used.")

#practice 5-11
for value in range(1,10):
    if value == 1:
        print(f"{value}st")
    elif value == 2:
        print(f"{value}nd")
    elif value == 3:
        print(f"{value}rd")
    else:
        print(f"{value}th")
