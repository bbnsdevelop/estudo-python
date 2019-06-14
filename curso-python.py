a=1

b=2

c=3



d=a+b+c



print('soma', d)





lista=[1,2,3,4,"bruno", 15,50]

print(lista)



lista.append("python")



print(lista)



lista.append(100)



print(lista)

index= lista.index("bruno")

print("index", index)

print(lista.count(4))



lista.append(4)

print(lista.count(4))

lista.remove("python")

print(lista)

lista.remove(4)

print(lista)


lista.reverse()

print(lista)


numeros=[1,2,6,8,5,3,7,4,9]

print(numeros)


numeros.sort()

print(numeros)



# dicionarios


telefones={"bruno":999999999,"tacy":888888888, "teste":0000000000}



print(telefones)

telefones["rita"]=15151515155

print(telefones)


del telefones["rita"]

print(telefones)

#endereco =

pessoa={
 "nome": "bruno Batista",
 "endereco":{"rua":"Fagundes Varelas"}
}

print(pessoa)




#------------------------while

numero=15
while (numero>=0):
    print(numero)
    numero-=1
    print(numero)#executara sempre uma vez a mais

print('------')
numero = 20
while True:
    numero-=1
    print(numero)
    if(numero == 2):
        break

print('------')

numero=10
while True:
    numero-=1
    if(numero == 4):
        continue
    print(numero)
    if(numero == 2):
        break


