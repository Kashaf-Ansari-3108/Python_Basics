def greetHello(name, ending):
    print('Hello ' + name)
    print('Hello ' + name)
    print('Hello ' + name)
    print('Hello ' + name)
    print('Hello ' + name)
    print(ending)

def letterGenerator(name, date):
    st = f"Hi mam,\nThis is {name} and i will not come to school on {date}"
    print(st)

def average(a, b):
    return (a + b)/2

print('Executing function')
greetHello('Kashaf', 'Thank You!')
letterGenerator('Kashaf', '26th October')
letterGenerator('Harry', '20th October')
print(average(34, 23))
print('Done')