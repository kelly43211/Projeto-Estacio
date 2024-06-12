print('Bonjour')
print("Hola")


x="Hola"
print(x[2])

x="Hola"
print(x[-1])

x="Routers & Switches"
print(len(x))

msg="Legolas is a {} character."
print(msg.format("Elf"))



x=10
y=15

if x==10:
    print("x equals 10.")
    if y > 20:
        print("y is less than 20.")
    elif y < 20:
        print("y is less than 20.")
    else:
        print("y equals 20.")
else:
    print("x does not match.")   


x=20
y=55 

if x==20:
    print("x equals 20.")
    if y > 60:
        print("y is less than 60.")
    elif y < 60:
        print("y is less than 60.")
    else:
        print("y equals 60.")
else:
    print("x does not match.")          