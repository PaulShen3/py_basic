# 以下代码为第六章节相关学习代码
# 2022/1/19  12:36   author:沈嘉晨
# 章节内容：字典
#page 81~100

alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0            #字典名['新信息'] = xxx   可以直接加入字典
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {}                   #生成空字典

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#修改字典中的值
alien_0 = {'color':'green'}
print(f"The color of alien is {alien_0['color']}.")
alien_0 = {'color':'yellow'}
print(f"The color of alien is now {alien_0['color']}.")

#对以不同速度移动的外星人进行位置跟踪
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"The original position : {alien_0['x_position']}")

#向右移动外星人
#根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"The new position : {alien_0['x_position']}")

#删除键值对
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

#由类似对象组成的字典
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

alien_0 = {'color':'green','speed':'slow'}
point_value = alien_0.get('points','No point value assigned.')
print(point_value)

#practice 6-1
person_1 = {'first_name':'Chris','last_name':'Paul','age':36,'city':'Suns'}
print(person_1)

#practice6-2
data_prefer = {
    'Paul':3,
    'James':23,
    'Kobe':24,
    'Anthony':7,
    'Wade':3
    }
print(data_prefer)

#practice6-3略

#遍历字典
#遍历所有键值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
    }
for key, value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#遍历字典中的所有键
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for name in favorite_languages.keys():
    print(name.title())

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}!")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for name in sorted(favorite_languages.keys()):            #按首字母排序sorted()
    print(f"{name.title()}, thank you for taking the poll.")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#剔除重复项
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):       #for value in set(xxx.values()): 中set可以剔除重复项
    print(language.title())

#字典与集合
#可使用一对花括号直接创建集合，并在其中用逗号分割元素
languages = {'python','ruby','python','c'}
languages

#practice 6-4略

#practice 6-5
river_states = {'nile':'egypt','huangpu river':'shanghai','songhua river':'heilongjiang'}
for key,values in river_states.items():
    print(f"The {key.title()} runs through {values.title()}.")
for river in river_states.keys():
    print(river.title())
for state in river_states.values():
    print(state.title())

#practice 6-6                                                                                #有问题
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
people_lists = ['sarah','edward']
for people_list in people_lists:
    print(people_list.title())
    if people_list in favorite_languages.keys():
        print("Thank you!")
    else:
        print("We invite you to participate in our survey.")

#嵌套
aline_0 = {'color':'green','points':5}
aline_1 = {'color':'yellow','points':10}
aline_2 = {'color':'red','points':15}

alines = [aline_0,aline_1,aline_2]
for aline in alines:
    print(aline)

#创建一个用于储存外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人
print(f"Total number of aliens:{len(aliens)}")

#在字典中储存列表

#储存所点pizza的信息
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
    }

#概述所点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza"" with the following topppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jet':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}
for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

#在字典中储存字典
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        }
    }
for username ,user_info in users.items():
    print(f"\nUsername:{username.title()}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name : {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#practice 略


