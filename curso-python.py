a=1

b=2

c=3

#testetetetetetetete

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


numero=1
if(numero==1):
   print('numero e igual a 1')

numero=2

if(numero==1):
   print('numero eh igual a 1')
else:
   print('numero nao eh igual a 1')

nome="bruno"

if("z" in nome):
	print("nome tem a letra z ")
elif("b" in nome):
	print("nome tem a letra B")
else:
	pass

for x in range(0,5):
	print("valor de x eh:",x)


for letra in nome:
	print('letras no nome: ', letra)

# Uma lista de instrumentos musicais
instrumentos = ['Baixo', 'Bateria', 'Guitarra']
# Para cada nome na lista de instrumentos
for instrumento in instrumentos:
# mostre o nome do instrumento musical
 print instrumento
a=1

if(a > 1):
	print('teste')

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
"""

Novo curso de python

"""

