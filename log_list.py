Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['toyota','honda','izusu']
>>> gagrae.append('suzuki')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    gagrae.append('suzuki')
NameError: name 'gagrae' is not defined
>>> garage.append('suzuki')
>>> print(garade)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(garade)
NameError: name 'garade' is not defined
>>> print(garage)
['toyota', 'honda', 'izusu', 'suzuki']
>>> print(garage[2])
izusu
>>> garage.remove('honda')
>>> print(garage)
['toyota', 'izusu', 'suzuki']
>>> garage.insert(1,'Benz')
>>> print(garage)
['toyota', 'Benz', 'izusu', 'suzuki']
>>> del garage[2]
>>> print(garage)
['toyota', 'Benz', 'suzuki']
>>> print(garage[-1])
suzuki
>>> print(garage[-2])
Benz
>>> print(garage)
['toyota', 'Benz', 'suzuki']
>>> my car = garage.pop(-1)
SyntaxError: invalid syntax
>>> mycar = garage.pop(-1)
>>> print(mycar)
suzuki
>>> print(garage)
['toyota', 'Benz']
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'Benz', 'suzuki']
>>> garage[1] = 'tesla'
>>> print(garage)
['toyota', 'tesla', 'suzuki']
>>> print(len(garage))
3
>>> uesrs = ['z','r','t','b','n','p']
>>> users = ['e','a','u','p','o','s']
>>> users.sort()
>>> print(users)
['a', 'e', 'o', 'p', 's', 'u']
>>> users.sort(reverse=True)
>>> users
['u', 's', 'p', 'o', 'e', 'a']
>>> print(sorted(users))
['a', 'e', 'o', 'p', 's', 'u']
>>> print(users)
['u', 's', 'p', 'o', 'e', 'a']
>>> users = ['e','a','u','p','o','s']
>>> users.reverse()
>>> print(users)
['s', 'o', 'p', 'u', 'a', 'e']
>>> for u in users:
	print(u)

	
s
o
p
u
a
e
>>> for u in sorted(users):
	print(u)

	
a
e
o
p
s
u
>>> users.reverse()
>>> for u in users:
	print(u)

	
e
a
u
p
o
s
>>> for u in users:
	print('สวัสดี',u)
	print('สวัสดี'+u)

	
สวัสดี e
สวัสดีe
สวัสดี a
สวัสดีa
สวัสดี u
สวัสดีu
สวัสดี p
สวัสดีp
สวัสดี o
สวัสดีo
สวัสดี s
สวัสดีs
>>> 