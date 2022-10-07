#ejercicio 1
lista1= ["Sardinera", "Portitxol", "Granadella"]
print(lista1[-1])
lista1= ["Sardinera", "Portitxol", "Granadella"]
print(lista1[1])
lista1= ["Sardinera", "Portitxol", "Granadella"]
print(lista1[0])
print("")
tupla= ("Sardinera", "Portitxol", "Granadella")
print(tupla[-1])
tupla= ("Sardinera", "Portitxol", "Granadella")
print(tupla[0])
tupla= ("Sardinera", "Portitxol", "Granadella")
print(tupla[1])
print("")
lista1= ["Sardinera", "Portitxol", "Granadella"]
print(lista1)
print("")
lista1= ["Sardinera", "Portitxol", "Granadella"]
print(lista1[0])
print("")
lista2= ["Sardinera", "Barraca", "Grandalla"]
print(lista2[-1])
lista2= ["Sardinera", "Barraca", "Grandalla"]
print(lista2[0])
lista2= ["Sardinera", "Barraca", "Grandalla"]
print(lista2[1])
print("")
tupla= ("Sardinera", "Portitxol", "Granadella")
print(tupla[2])
print("")
len(lista1)
print(len(lista1))
len(tupla)
print(len(tupla))
print("")
lista1= ["Sardinera", "Portitxol", "Granadella"]
print(lista1.index("Portitxol"))
tupla= ("Sardinera", "Portitxol", "Granadella")
print(tupla.index("Sardinera"))
print("")
print("Sardinera" in lista1)
print("Barrca" in lista1)
print("")
lista1= ["Sardinera", "Portitxol", "Grandalla"] 
lista3=["Caleta"]
print(lista1 + lista3)
print("")
lista1=["Sardinera", "Portitxol", "Grandalla"] 
lista1.pop(2)
print(lista1)
print("")
lista1=["Sardinera", "Portitxol", "Grandalla"] 
print(lista1)
lista1.clear()
print(lista1)
print("")


#ejrecicio 2 diccionario
calas= { "playa": "Sardinera", "tipo": "piedras", "acceso": "camiando" }
print(calas)
print("")
print(type(calas))
print("")
print("playa" in calas)
print("")
interes= calas["playa"]
print(interes)
print("")
print(len(calas))
print("")
calas= { "playa": "Sardinera", "tipo": "piedras", "acceso": "camiando" }
print(calas)
calas["turismo"]= "poco"
print(calas)
print("")
calas= { "playa": "Sardinera", "tipo": "piedras", "acceso": "camiando" }
print(calas)
calas.clear()
print(calas)
print("")

#ejercicio2 sets
num= {1,2,3,4}
print(num)
print(type(num))
print("")
print("1" in num)
print("")
print(len(num))
print("")
num= {1,2,3,4}
print(num)
num.clear()
print(num)
print("")

#ejercicio3
lista= {2,4,6}
print(lista)
sum(lista)
print("")
from numpy import mean, array
v= array([2,4,6])
mean(v)
print(mean(v))