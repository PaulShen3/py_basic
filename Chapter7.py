# 以下代码为第七章节相关学习代码
# 2022/1/20  17：41  author:沈嘉晨
# 章节内容：用户输入和while循环
# page 101-114

message = input("Tell me something, and I will report it back to you:")
print(message)

name = input("Please tell me your name:")
print(f"\nMy name is {name.title()}")

prompt = "If you tell us who you are,we can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print(f"\nHello,{name.title()}")

height = input("How tall are you,in inches?")
height = int(height)

if height >= 48:
    print("\nYou are tall enougth to ride!")
else:
    print("\nYou will be able to ride when you are a little older.")

#求模运算符

4%3   #余1

number = input("Please input a number and I'll tell you whethere it's even or odd")
number = int(number)

if number % 2 == 0:
    print("\nIt's an even.")
else:
    print("\nIt's an odd.")

#practice 7-1
car = input("Which brand would you like to buy?")
print(f"Let me see if I can find you a {car.title()}.")

#practice 7-2
dinner_number = input("How many people will have dinner tonight?")
dinner_number = int(dinner_number)
if dinner_number > 8:
    print("Sorry,we didn't have that much places")
else:
    print("We have enough places")

#practice 7-3
a = input("请输入一个数:")
a = int(a)
if a % 10 == 0:
    print(f"{a} 是10的整数倍")
else:
    print(f"{a} 不是10的整数倍")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    if message != 'quit':
        print(message)

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = '\nPlease enter the name of a city you have visited:'
prompt += "\n(Enter 'quit' when you are finished.)"

#break用法例子
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#continue用法例子
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)

#practice 7-4

prompt = "\nPlease input the ingredients you want in your pizza:"
prompt += "\nEnter 'quit' to end the program."
while True:
    ingredient = input(prompt)
    if ingredient == 'quit':
        break
    else:
        print(f"I'll put {ingredient.title()} in your pizza!")

#practice 7-5

prompt = "\nPlease tell me how old are you?"
while True:
    age = input(prompt)
    age = int(age)
    if age <= 3:
        print("You are free to watch the movie.")
    elif age <= 12:
        print("It costs 10$.")
    elif age >12 :
        print("It costs 15$.")

#practice 7-6 略
#practice 7-7 写一个无限循环
a = 0
while a<1:
    print(a)


#使用while循环处理列表和字典
unconfirmed_users = ['alice','brain','candace']             #创建一个未验证用户列表
confirmed_users = []                                        #创建一个空列表用于储存已验证的用户

while unconfirmed_users:                                    #循环不断运行直至unconformed_users变成空的
    current_user = unconfirmed_users.pop()                  #使用pop每次一个从列表unconformed_users末尾删除未验证的用户
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#删除为特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name ?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
#调查结束，显示结果
print("\n--- Poll Result ---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}")

#practice 7-8
sandwich_orders = ['a','b','c']
finished_sandwiches = []
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order.title()} sandwich.")
    finished_sandwiches.append(current_order)
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

#practice 7-9 ...

#practice 7-10
places = {}
polling_active = True
while polling_active:
    name = input("What's your name?")
    place = input("Where would you like to go?")
    places[name] = place
    repeat = input("Would you like someone to travel with you?(yes/no)")
    if repeat == 'no':
        polling_active = False
for name,place in places.items():
    print(f"{name} would like to go to {place}.")