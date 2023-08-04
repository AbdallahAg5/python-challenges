text = "hello there "
# print(text[0:2])
# print(text.strip()) # strip removes spaces from start and end 
# print(text.upper())
# print(len(text))
# print(text.replace("h","H"))
# print(text.lower())


age = 36
city = "Rabat"
txt = "My name is John, and I am {} and living in {}"
# print(txt.format(age,city))


# list shit
list = ["test1","test2","test3"]
list[0] = "test0"
list.append('hello there')
list.insert(1,'hello')
list.remove('test0')
# print(list[0:3])


# tuple 
tuple = {"test1","test2","test3"}
list = ["orange", "mango", "grapes"]
tuple.add('test4')
tuple.update(list)
tuple.remove("orange")
tuple.discard("mango")
# print(tuple)


# tuple
tuple1 = {"name":"Abdallah","age":15}
tuple1["name"] = 'Ziko'
tuple1['city'] = "Rabat"
tuple1.pop("city")
tuple1.clear()
print(tuple1)


# if statment
if 5 > 10:
    print('hi')
elif 5 < 10:
    print('hello')    
else:
    print('heyy')    


print('test1') if 5 == 5  else print('nothing')    


# loop 
num = 6
for i in range(num):
    print(i)


def function(arg1):
    print(arg1)


function('arg1')

