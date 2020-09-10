peliculas=['Batman','Spiderman','Harry Potter','Fast and furious']
for pelicula in peliculas:
    print(pelicula)

print('MC\'s')
mcs=list(('wos','trueno','aczino','Papo','Valles T','Bnet','Dtoke'))
for mc in mcs:
    print(mc)

years=list(range(2000,2020))
for year in years:
    print(year)

#indices
print('###############indices####################')
#empiezan desde 0
print(peliculas[1])
#se pueden iterar al revez con indices negativos
print(peliculas[-1])

# se pueden sacar un rango de objetos(Sublista)
print(mcs[0:3])

#Se puede sacar un rango(Sublista) a partir de un indica
print(mcs[3:])
#Se puede modificar el valor de un indice
mcs[3]='Carpediem'
print(mcs)


#Agregar elementos a lista
mcs.append('Skone')
print(mcs)

print('##Listado de Peliculas')

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")



#lista multidimencionales

contactos=[
    ['Joel','jalvarado@conauto.com.ec'],
    ['Isaias','isasias@conauto.com.ec'],
    ['jalvator','jalvator@conauto.com.ec'],
]

print(contactos[2][0])


for contacto in contactos:
    print("\n")
    for elemento in contacto:
        print( elemento)
    