#创建Dog类
class Dog:                                     #首字母大写的名称指的是类
    """一次模拟小狗的简单尝试"""

    def __init__(self,name,age):                #类中的函数称为方法，__init__是一个特殊的方法，每当根据类创建新实例都会自动运行
        """初始化属性name和age"""                     #self 是必备的，只需给出其他形参的值就可以了
        self.name = name                            #获取与形参name相关联的值，并将其赋值给变量name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

my_dog = Dog(name = 'Willie',age = 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

my_dog = Dog("Willie",6)
your_dog = Dog("Lucy",3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


#practice 9-1 & 9-2 餐馆
class Restaurant:
    """餐馆模拟"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """介绍餐馆信息"""
        print(f"The name of our restaurant is {self.restaurant_name}.")
        print(f"The type of our restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        """说明餐馆正在运营"""
        print("The restaurant is open now.")

my_restaurant = Restaurant("Peace",'Chinese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#practice 9-3 用户   #describe_user 和 greet_user
class User:

    def __init__(self,first_name,last_name,location):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location

    def describe_user(self):
        """介绍用户信息"""
        print(f"The name of the user is {self.first_name.title()} {self.last_name.title()}")
        print(f"The user is now living in {self.location.title()}")

    def greet_user(self):
        """给用户打招呼"""
        print("Welcome to our website!")

my_user = User('Chris','Paul','Sun')
my_user.describe_user()
my_user.greet_user()

#使用类和实例
class Car:
    """一次模拟汽车的简单会议"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值
           禁止将里程表读书往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
#
#  my_new_car.odometer_reading = 23
#  my_new_car.read_odometer()
#
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
my_used_car = Car('subaru','Outback',2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#practice 9-4
class Restaurant:
    """餐馆模拟"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """介绍餐馆信息"""
        print(f"The name of our restaurant is {self.restaurant_name}.")
        print(f"The type of our restaurant is {self.cuisine_type}.")

    def open_restaurant(self):
        """说明餐馆正在运营"""
        print("The restaurant is open now.")

    def read_served_number(self):
        print(f"There are {self.number_served} people served in this restaurant")
    def set_number_served(self,numbers):
        """设置就餐人数"""
        self.number_served = numbers

    def increment_number_served(self,number):
        """将里程表读数增加指定的量"""
        self.number_served += number


my_restaurant = Restaurant("Peace",'Chinese')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(25)
my_restaurant.read_served_number()
my_restaurant.increment_number_served(10)
my_restaurant.read_served_number()

#继承
#如果要编写的类是另一个现成类的特殊版本，可以使用继承
class Car:
    """一次模拟汽车的简单会议"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值
           禁止将里程表读书往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

class ElectricCar(Car):        #创建子类的时候父类必须包含在当前文件中，且位于子类前面
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性
           再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
#super()是一个特殊函数，能够调用父类的方法，这行代码让python调用car类的方法__init__()
#让ElectricCar实例包含这个方法中定义的所有属性，父类也成为超类，所以叫super
        self.battery_size = 75      #添加新属性，默认电池容量初始值为75

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"The car has a {self.battery_size}-kWh battery.")
my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#重写父类的方法
#假设Car类有一个名为fill_gas_tank()的方法，它对全电动汽车毫无意义
class ElectricCar(Car):        #创建子类的时候父类必须包含在当前文件中，且位于子类前面
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性
           再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        #super()是一个特殊函数，能够调用父类的方法，这行代码让python调用car类的方法__init__()
        #让ElectricCar实例包含这个方法中定义的所有属性，父类也成为超类，所以叫super
        self.battery_size = 75      #添加新属性，默认电池容量初始值为75

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"The car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


#将实例用作属性
class Car:
    """一次模拟汽车的简单会议"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值
           禁止将里程表读书往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):        #创建子类的时候父类必须包含在当前文件中，且位于子类前面
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性
           再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        #super()是一个特殊函数，能够调用父类的方法，这行代码让python调用car类的方法__init__()
        #让ElectricCar实例包含这个方法中定义的所有属性，父类也成为超类，所以叫super
        self.battery_size = Battery()      #添加新属性，默认电池容量初始值为75

my_tesla = ElectricCar('tesla','model s','2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()



#导入类
