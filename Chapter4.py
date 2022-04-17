# #以下代码为第四章节列表相关学习代码
# #2022/1/12  14:36   author:沈嘉晨
#page 39-62


magicians = ['alice','david','carolina']
for magician in magicians:            #从magicians中取出一个名字并将其与变量magician相关联
    print (magician)                  #打印前面赋值给变量magician的名字

#for cat in cats:
#for dog in dogs:
#for item in list_of_item:
magicians = ['alice','david','carolina']
for magician in magicians:
    print (f"{magician.title()},that was a great trick!")
    print (f"I can't wait to see your next trick,{magician.title()}.\n")
print ("Thank you,everyone.That was a great magic show!")

#practice 4-1
pizzas = ['bishengke','bangyuehan','dameile']
for pizza in pizzas:
    print (f"I like {pizza.title()} pizza.")
print ("I really love pizza!")

#practice 4-2
animals = ['dog','cat','rabbit']
for animal in animals:
    print (f"A {animal.title()} would make a great pet.")
print ("Any of there animals would make a great pet!")

#创建数值列表
for value in range(1,5):        #使用range函数的时候，range(1,5)只会打印1，2，3，4，差一行。所以要打印5，需要range(1,6)
    print (value)

for value in range(1,6):
    print (value)

#调用range()函数的时候也可以只指定一个参数，这样它将从0开始，例如range(6)
for value in range(6):
    print (value)

#使用range()创建数字列表
numbers = list(range(1,6))
print (numbers)

even_numbers = list(range(2,11,2))    #range()从2开始数，然后不断+2直到达到或者超过终值11结束。
print (even_numbers)                  #range(初始值，终值，步长)

#创建一个列表，包含整数1-10的平方
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print (squares)

#简洁代码
squares= []
for value in range(1,11):
    squares.append(value ** 2)
print (squares)

#对数字列表执行简单的统计计算
digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
max(digits)
sum(digits)

#列表解析
squares = [value ** 2 for value in range(1,11)]    #for 循环为 for value in range(1,11),将值1-10提供给表达式value ** 2，此处for循环无冒号。
print (squares)

#practice 4-3
for value in range(1,21):
    print (value)

#practice 4-4
list_million = []
for value in range(1,10000001):
    list_million.append(value)
print (list_million)

#practice 4-5
min(list_million)
max(list_million)
sum(list_million)

#practice 4-6
odd_number = []
for i in range(1,20,2):
    odd_number.append(i)
print (odd_number)

#practice 4-7
aim_number = []                 #给空列表aim_number
for i in range(3,31):           #for循环3-30之间的数
    if i % 3 == 0:              #使用if语句，i%3==0表示被3除余数为0
    aim_number.append(i)        #将i赋值到列表aim_number中
print (aim_number)

#practice 4-8
cubes = []
for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)
print (cubes)

#practice 4-9
cube = [value ** 3 for value in range(1,11)]   #立方解析
print (cube)


# #2022/1/13  10:28   author:沈嘉晨
#page 53-61

#切片（就是生成列表的任意子集）
players = ['charles','martina','michael','florence','eli']
print (players[0:3])              #指定索引0和3，返回索引为0，1，2的元素
print (players[1:4])
print (players[:4])               #没有指定第一个索引就自动从列表开头开始
print (players[2:])               #没有指定第二个索引就自动切片到列表末尾

print (players[-3:])              #要最后三个元素

print("Here are the first three players on my team:")    #遍历切片，只遍历前三名队员
for player in players[:3]:
    print(player.title())

#复制列表
my_foods = ['pizza','falafei','carrot cake']
friend_foods = my_foods[:]          #不能直接用friend_foods = my_foods，print()会得到同一个列表
print ("My favourite foods are:")
print (my_foods)

print ("\nMy friend's favourite foods are:")
print (friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#practice 4-10
print("The first three items in the list are:")
print(my_foods[0:3])
print("Three items from the middle of the list are:")
print(players[1:4])
print("The last three items in the list are:")
print(players[-3:])

# 元组
# 不能修改的值为不可变的，不可变的列表为元组

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#尝试修改,报错
dimensions=(200,50)
dimensions[0]=250

#遍历元组中所有值
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

#修改元组变量  需要重新定义整个元组
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)