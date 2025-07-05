print("Hello World")
a = 5
b = 6
c = int(a + b)

print(c)



# print('Hello','world')
d = "Hello"
f ="world"
g = d + f
print(g)

x = y = z = 576
print(x)
print(z)
print(y)
print("Hello","world")


f = "Awesome"
def myfunc():
 print("Python is " + f)
myfunc()

age = 21

txt = "My name is John, and I am {} years old"
print(txt.format(age))
txt = f"The price is {20 * 59} dollars"
print(txt)

item = ['babar','ali','irfan']
item.append(['Adeel','kuch','bhi'])
print(item)

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

fruits = ["apple", "banana", "cherry"]
y = list(fruits)
y[1] = "Babar"
print(y)

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']

test = fruits + tropical
for i in test:
 print(i)


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car = thisdict.get("brand")
x =thisdict["year"]


print(x)
print(car)

x = {'type' : 'fruit', 'name' : 'apple'}

y = dict(x)
# y = x.copy()

print(x)
print(y)

a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}

print(customers['c2']['name'])

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
print(myfamily['child2']['year'],myfamily['child3']['name'])

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x,y)

  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

  a = 234
  b = 45
  if a > b:
     print('hello')
  elif a == b:
    print('Babar Your not a success Man') 
  elif a < b:
    print('You Won the word')

month = 2

match month:
    case 1:
        print('Jan')
    case 2:
        print('Feb')

month = 2
match month:
   case 1 :
      print('jan')
   case 2 :
      print('Fb')

      
      

 
def myfunction():
    myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
for x in myfamily:
  print(x)
  if x == 'child2':
   break
 
myfunction()
    
fruits = ['Apple','Banana','grappes','cherry']
vagitable = ['Lesson','ptato','tamato']
mix = fruits + vagitable
for x in mix:
  
  if x == 'Lesson':
    break
  print(x)
  
  def my_func():
    print('Hello I am calling form in the function')
     
my_func()

def my_function(fname):
  print(fname)
  
my_function("Babar")
my_function("Babar")

my_function("Babar")

# def my_function(fname):
#    print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

cars = ['toyoto','carola','Honda','RongOver','BMW','LAmberGene']
cars.append('Mahran')
# print(cars)
for x in cars:
  print(x)
  
  
  
 
#   class FirstClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#         # Use f-string to insert values
#         test = f"My name is {self.name} and age is {self.age}"
#         print(test)

# # Create object of the class
# person = FirstClass("Ali", 21)

class FirstClass:
    def __init__(self , name ,age):
      self.name =name
      self.age =age
      test = f"My {self.name} and age is {self.age}"
      print(test) 
person = FirstClass("Ali",21)

a = ['whjf','wrf','erfh','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf','erf']
print(a)
