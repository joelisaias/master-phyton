numeros=[5,8,3,1,2]
mcs=list(('wos','trueno','aczino','Papo','Valles T','Bnet','Dtoke'))

print(numeros)
numeros.sort()
print(numeros)

#añadir elementos
mcs.append('Skone')
mcs.insert(0,'Chuty')
print(mcs)

#eliminar elementos
mcs.pop(2)
mcs.remove('wos')
print(mcs)

#reverso
print(numeros)
numeros.reverse()
print(numeros)

#buscar dentro de listas
print('Papo' in mcs)

#contar elementos
print(len(mcs))

#Cuantas veces aparece un elemento
print(mcs.count('Skone'))
mcs.append('Skone')
print(mcs.count('Skone'))

#Conseguir indice
print(mcs.index('Bnet'))

#unir listas
mcs.extend(numeros)

print(mcs)