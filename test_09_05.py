# 2.2变量
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

a = "Jinwoo"
print(a)

a = "不是孤岛_"
print(a)

# 2.3字符串
name = "ada lovelace"
print(name.title())
# title()方法将每个单词的首字母都改为大写
print(name.upper())
# upper()方法将字符串改为大写
print(name.lower())
# lower()方法将字符串改为小写

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

print("Hello, " + full_name.title() + "!")
# 使用+来合并字符串

message = "Hello, " + full_name.title() + "!"
print(message)

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
# rstrip()方法删除字符串末尾的空白
favorite_language = favorite_language.rstrip()
print(favorite_language)

favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
# lstrip()方法删除字符串开头的空白
print(favorite_language.strip())
# strip()方法删除字符串两端的空白

message = "One of Python's strengths is its diverse community."
print(message)

message = 'One of Python\'s strengths is its diverse community.' # 使用转义字符\来处理单引号 One of Python\'s strengths is its diverse community.
print(message)

name = "Eric"
message = "Hello" + name + ", would you like to learn some Python today?"

name = "Eric"
name_1 = name.lower()
name_2 = name.upper()
name_3 = name.title()
print(name_1)
print(name_2)
print(name_3)

name = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
message = name + "once said," + "\"" + quote + "\""
print(message)

famous_person = "Albert Einstein"
message = famous_person + "once said," + "\"" + quote + "\""
print(message)

name = "\t\nWeiting Gao\n\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
print(name.lstrip().rstrip())

# 2.4数字
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

print(5 + 3)
print(10 - 2)
print(2 * 4)
print(16 // 2) # 除法运算符//返回一个整数 print(16 / 2)返回一个浮点数

num = 13
message = "My favorite number is " + str(num) + "."
print(message)

# 2.5注释
# 向大家问好
print("Hello Python people!")

# 2.6Python之禅
import this

