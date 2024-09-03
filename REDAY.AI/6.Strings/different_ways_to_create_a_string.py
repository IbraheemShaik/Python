string1 = 'Hello, My name is Rocky'
print(string1)

string2 = "Hello, My name is Rocky"
print(string2)

string3 = '''Hello, My name is Rocky'''
print(string3)

string4 = """Hello, My name is Rocky"""
print(string4)

num = 155
string5 = str(num)
print(string5)

string6 = 'Hello' + ', ' + 'My name is Rocky'
print(string6)

name = 'My name is Rocky'
string7 = f'Hello, {name}!'
print(string7)

string8 = 'Hello, {}!'.format(name)
print(string8)

words = ['Hello', 'My name is Rocky']
string9 = ' '.join(words)
print(string9)

string10 = repr('Hello, My name is Rocky')
print(string10)

string11 = bytes('Hello, My name is Rocky', encoding='utf-8')
print(string11)

string12 = ''.join([chr(i) for i in range(60, 90)])
print(string12)

string13 = 'Hello! ' * 3
print(string13)
