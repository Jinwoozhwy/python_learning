# 3.列表简介
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 3.1.1 访问列表元素
print(bicycles[0])
print(bicycles[0].title())

# 3.1.2 索引从0而不是1开始
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])
# 使用-1返回列表最后一个元素

# 3.1.3 使用列表中的各个值
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)

# 3.2 修改、添加和删除元素
# 3.2.1 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2 在列表中添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles) # append()方法在列表末尾添加元素

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 在列表中插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles) # insert()方法在列表中插入元素

# 3.2.3 从列表中删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles) # del语句删除元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# 使用方法pop()删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
poped_motorcycle = motorcycles.pop()
print(poped_motorcycle) # pop()方法删除列表末尾的元素，并返回这个元素

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# 弹出列表中任何位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")
# pop()方法可删除列表中任何位置的元素

# 根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)  # remove()方法删除指定的值

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# 组织列表
invited_guests = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
print(invited_guests)
print(invited_guests[2] + " can't come to dinner.")

invited_guests = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
invited_guests[2] = 'weiting'
print(invited_guests)

invited_guests = ['zhangsan', 'lisi', 'weiting', 'zhaoliu']
print("I found a bigger table.")
invited_guests.insert(0, 'tiechui') # insert()方法在列表中插入元素
invited_guests.insert(2, 'yuanyuan')
invited_guests.append('xiaoming')
print(invited_guests)

print("I can only invite two people to dinner.")
popped_guest = invited_guests.pop()
print("Sorry, " + popped_guest + ", I can't invite you to dinner.")
popped_guest = invited_guests.pop()
print("Sorry, " + popped_guest + ", I can't invite you to dinner.")
popped_guest = invited_guests.pop()
print("Sorry, " + popped_guest + ", I can't invite you to dinner.")
popped_guest = invited_guests.pop()
print("Sorry, " + popped_guest + ", I can't invite you to dinner.")
popped_guest = invited_guests.pop()
print("Sorry, " + popped_guest + ", I can't invite you to dinner.")

print(invited_guests[0] + ", you're still invited.")
print(invited_guests[1] + ", you're still invited.")
print(invited_guests)
del invited_guests[0]
del invited_guests[0]
print(invited_guests)

# 3.3 组织列表
# 3.3.1 使用方法sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # sort()方法对列表进行永久性排序

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars) # sort()方法对列表进行永久性排序，reverse=True按字母顺序相反的顺序排列

# 3.3.2 使用函数sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) # sorted()函数对列表进行临时排序
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the sorted list again:")
print(cars)
print()

# 3.3.3 倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars) # reverse()方法倒着打印列表

# 3.3.4 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # len()函数确定列表的长度

travel_places = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'chengdu']
print(travel_places)
print(sorted(travel_places))
print(travel_places)
print(sorted(travel_places, reverse=True))
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.sort()
print(travel_places)
travel_places.sort(reverse=True)
print(travel_places)

print(len(invited_guests))

# 3.4 使用列表时避免索引错误
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) # 索引错误

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1]) # 使用-1返回列表最后一个元素

motorcycles = []
# print(motorcycles[-1]) # 索引错误