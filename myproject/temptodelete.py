class Car:
    id:int
    name:str

c = Car()
c.id = 0
c.name = "rushi"
print(c.name+" "+str(c.id))

print("Rushi")
for i in range(5):
    if i==3:
        continue
else:
    print(i)