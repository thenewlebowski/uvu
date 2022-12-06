fob = {
    "foo": "bar",
    "bar": "foo"
}

try:
    print(fob["foobar"])
except KeyError:
    print("Key not found in dictionary fob")

x="Trui"
try:
    int(x)*str(x)
    print(x)
except NameError:
    print("Variable is not defined")
except ValueError:
    print("Not an integer: an exception has occurred:")


fob = {
    "product": 0
}

try:
    number = int(input("give me a string "))
    finalnumber = number/2
    print(finalnumber)
    fob['product'] = 0   
    print(fob['produc'])
except ValueError:
    print("I can't divide a string")
except KeyError: 
    print("Key not found in dictionary fob")
