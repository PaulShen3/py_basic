# #以下代码为第三章节列表相关学习代码
# #2022/1/10  12:45  author:沈嘉晨
#
# bicycles = ['trek','cannondale','redline','specialized']
# print (bicycles)
#
# #访问列表元素
# print(bicycles[0])
# print(bicycles[0].title())
# print(bicycles[1])
# print(bicycles[3])
#
# print(bicycles[-1])   #-1就是选取列表中最后一个元素
#
# message = f"My first bicycle was a {bicycles[0].title()}."
# print (message)
#
# #practice 3-1
# names = ['Paul','Lebron','Wade']
# print (names[0])
# print (names[1])
# print (names[2])
#
# #practice 3-2
#
# message2 = f"{names[0]},Hello"
# print (message2)
#
# #practice 3-3
# print(f"I would like to won a {bicycles[0]}.")
#
# 3.2 修改、添加、删除元素
#
# motorcycles = ['honda','yamaha','suzuki']
# print (motorcycles)
# motorcycles[0] = 'ducati'       #修改列表元素
# print (motorcycles)
#
# motorcycles = ['honda','yamaha','suzuki']
# print (motorcycles)
# motorcycles.append('ducati')      #使用.append('  ')可以在列表末尾添加元素
# print(motorcycles)

# #在列表中添加元素
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print (motorcycles)
#
# motorcycles.insert(0,'ducati')    #在首位插入元素,表中每个元素都右移一个单位
# print (motorcycles)
#
# del motorcycles[0]      #使用del删除元素，del motorcycles[0]为删除第一位元素,删除后就无法访问你
# print (motorcycles)
#
# #使用pop方法删除元素
# motorcycles = ['honda','yamaha','suzuki']
# print (motorcycles)
# popped_motorcycles = motorcycles.pop()         #pop是一种弹出思想，就是弹出末位的元素拿在手上，可以再赋值给其他变量
# print (motorcycles)
# print (popped_motorcycles)
#
# last_owned  = motorcycles.pop(0)               #弹出列表第0位的元素
# print (f"The last motorcycle I owned was a {last_owned.title()}.")
#

#根据值来删除元素
motorcycles = ['honda','yamaha','suzuki','ducati']
print (motorcycles)
motorcycles.remove('ducati')
print (motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)            #remove 只删除第一个指定的值，如果要删除的值重复出现需要用循环确保每个值都删除
print (motorcycles)
print (f"\nA {too_expensive.title()} is too expensive for me.")

#practice  3-4
invite_member = ['IU','Sxr','Dyx','Trump']
print (invite_member)

#practice 3-5
print (invite_member[3])
del invite_member[3]
invite_member.append('Szh')
# print (invite_member)
# print (f'{invite_member[0]},I invite you to come to have dinner with me.')
# print (f'{invite_member[1]},I invite you to come to have dinner with me.')
# print (f'{invite_member[2]},I invite you to come to have dinner with me.')
# print (f'{invite_member[3]},I invite you to come to have dinner with me.')

#practice 3-6
invite_member.insert(0,'A')
invite_member.insert(2,'B')
invite_member.append('C')
# print (invite_member)
# print (f'{invite_member[0]},I invite you to come to have dinner with me.')
# print (f'{invite_member[1]},I invite you to come to have dinner with me.')
# print (f'{invite_member[2]},I invite you to come to have dinner with me.')
# print (f'{invite_member[3]},I invite you to come to have dinner with me.')
# print (f'{invite_member[4]},I invite you to come to have dinner with me.')
# print (f'{invite_member[5]},I invite you to come to have dinner with me.')
# print (f'{invite_member[6]},I invite you to come to have dinner with me.')

# print ("Sorry everyone,because of the problem that something is wrong with the table ,only 2 guys are allowed to come.")
# person1 = invite_member.pop()
# print (f"{person1},I am sorry that you cannot come to have dinner with me.")
# person2 = invite_member.pop()
# print (f"{person2},I am sorry that you cannot come to have dinner with me.")
# person3 = invite_member.pop()
# print (f"{person3},I am sorry that you cannot come to have dinner with me.")
# person4 = invite_member.pop()
# print (f"{person4},I am sorry that you cannot come to have dinner with me.")
# person5 = invite_member.pop()
# print (f"{person5},I am sorry that you cannot come to have dinner with me.")
# print (invite_member)
#


#sort 方法排序（永久改变排序）
 cars = ['bmw','audi','toyota','subaru']
 cars.sort()
 print (cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print (cars)

#sorted 方法排序（临时排序）
cars = ['bmw','audi','toyota','subaru']
print ("Here is the original list:")
print (cars)
print ("\nHere is the sorted list:")
print(sorted(cars))
print ("\nHere is the original list:")
print (cars)

#倒着打印列表
print ("\nHere is the reverse list:")
cars.reverse()
print (cars)

#确定列表的长度
cars = ['bmw','audi','toyota','subaru']
len(cars)


#practice 3-8

tours = ['Beijing','Shenzheng','Guangzhou','Chengdu','Hongkong']
print (tours)
print (sorted(tours))
tours.reverse()
print (tours)
tours.sort()
print (tours)

#practice 3-9
len(tours)

#practice 3-10
girlfriends = ['fqy','iu','syx','zhn']
print (girlfriends)
girlfriends.sort()
print (girlfriends)
print (sorted(girlfriends))
girlfriends.reverse()
print (girlfriends)
print (girlfriends[0])
print (girlfriends[-1])