print("\t---Miremos el grupo etario en el que te encuentras---")
edad= int(input("\tIngrese su edad: "))
if edad <= 12:
    print("\tEs un niño")
elif edad >= 13 and edad <= 17:
    print("\tEs un adolescente")
elif edad >= 18 and edad <= 59:
    print("\tEs un adulto")
else:
    print("\tEs un adulto mayor")
for i in range(1,11):
    print(i)
