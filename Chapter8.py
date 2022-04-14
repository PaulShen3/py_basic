# 以下代码为第8章节相关学习代码
# 2022/1/29  9：35  author:沈嘉晨
# 章节内容：函数
# page 115-139

def greet_user():
    """显示简单的问候语"""
    print("Hello")

greet_user()

def greet_user(name):                           #name是一个形参
    """显示简单的问候语"""
    print(f"Hello,{name.title()}")
greet_user('jessi')                             #jessi是一个实参


#practice 8-1
def display_message():
    print("I learned function in this chapter.")

display_message()


#practice 8-2
def favorite_book(title):
    print(f"My favorite book is {title.title()}.")

favorite_book('Alice in Wonderland')

#传递实参，可使用位置实参和关键字实参，还可以使用列表和字典
#位置实参

def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')            #多次调用，提高效率

#关键字实参
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')

#默认值
def describe_pet(pet_name,animal_type = 'dog'):
    """显示宠物的信息"""
    print(f"\nI have a {animal_type.title()}.")
    print(f"My {animal_type.title()}'s name is {pet_name.title()}.")

describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet(animal_type='cat',pet_name='jerry')    #虽然是默认值，但当给定animal_type时还是可以令其为其他动物

#practice 8-3
def make_shirt(size,words):
    """T恤的尺码和字样"""
    print(f"\nThe size of this shirt is {size}.")
    print(f"The words on this shirt is {words.title()}.")

make_shirt("xxl","niubi")
make_shirt(size='xxl',words='niubi')

#practice 8-4
def make_shirt(size,words="I love Python"):
    """T恤的尺码和字样"""
    print(f"\nThe size of this shirt is {size}.")
    print(f"The words on this shirt is {words.title()}.")

make_shirt("l")
make_shirt("m")
make_shirt("xl",words="I love java")

#practice 8-5
def describe_city(city,country = "USA"):
    """城市所属国家"""
    print(f"{city.title()} is in {country}.")

describe_city("Los Angelos")
describe_city("Miami")
describe_city("Shanghai")

#返回值
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

#让实参变成可选的
def get_formatted_name(first_name,middle_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)

def get_formatted_name(first_name,last_name,middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()                   #将结果返回到函数调用行

musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)

#返回字典

def build_person(first_name,last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name,'last':last_name}
    return person

musician.title = build_person('jimi','hendrix')
print(musician)

def build_person(first_name,last_name,age=None):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=27)
print(musician)


# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# #这是一个无限循环!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name:")
#     l_name = input("Last name:")
#
#     formatted_name = get_formatted_name(f_name,l_name)
#     print(f"\nHello,{formatted_name}!")

def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\n Please tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello,{formatted_name}!")


def city_country(country_name,city_name):
    country_city_name = f"{city_name} {country_name}"
    return country_city_name.title()

while True:
    print("\nPlease tell me your country and city's name:")
    city_name = input("City name:")
    country_name = input("Country name:")
    city_name_country_name = city_country(country_name,city_name)
    print(f"{city_name_country_name}")

#传递列表

# def greet_users(usernames):
#     """向列表中的每位用户发出简单的问候"""
#     for username in usernames:
#         msg = f"Hello,{username.title()}"
#         print(msg)
# usernames = ['hannah','ty','margot']
# greet_users(usernames)

def greet_users(names):                         #这边定义一个函数greet_users,这里只是定义了一个函数
    for name in names:                          #遍历所有name
        msg = f"Hello,{name.title()}"
        print(msg)

usernames = ['hannah','ty','margot']            #这边usernames是一个列表，可以看作是函数里的names,每个人名就是一个name
greet_users(usernames)                          #调用函数


#在函数中修改列表
#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['phone case','robot pendent','dodecahedron']
completed_models = []

#模拟打印每个设计，直到没有未打印的设计为止
#打印每个设计后都将其移到completed_models中。
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)
#显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs,completed_models):
    """模拟打印每个设计直到没有未打印的设计为止
    打印每个设计后都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case','robot pendent','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

print_models(unprinted_designs[:],completed_models)     #不想清空原列表，可以在后面加上[:]
show_completed_models(completed_models)

#practice 8-9
def show_messages(msgs):
    for msg in msgs:
        print(msg)

msgs = ["I","am","Chris","Paul"]
show_messages(msg)

#practice 8-10,8-11略

#传递任意数量的实参
def make_pizza(*toppings):             #形参中的*让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
    """打印客户点的所有配料"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')

def make_pizza_2(size,*toppings):
    """打印客户点的配料和pizza的大小"""
    print(f"\nMking a {size}-size pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza_2(16,'pepperoni')
make_pizza_2(12,'mushroom','green peppers','extra cheese')


def build_profile(first,last,**user_info):   #两个*让python创建一个名为user_info的空字典，并将所有收到的名称值都放到这个字典中
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profile)


#将函数存储在模块中
#导入整个模块
# def make_pizza(size,*toppings):
#     """概述要制作的pizza"""
#     print(f"Making a {size}-size pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

#导入pizza
# import pizza
#
# pizza.make_pizza(16,'pepperoni')
# pizza.make_pizza(12,'mushroon','green pepper','extra cheese')

#导入特定的函数
from module_name import function_name
from modulle_name import function_0,function_1,function_2
