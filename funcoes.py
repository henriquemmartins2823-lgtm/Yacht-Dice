import random
def rolar_dados(x):
    lista=[]
    lista=[0]*x
    for i in range(len(lista)):
        lista[i]=random.randint(1,6)
    return lista
def guardar_dado(rolado,estoque,guardar):
    listanovarolado=[]
    for i in range(len(rolado)):
        if i!=guardar:
            listanovarolado.append(rolado[i])
    estoque.append(rolado[guardar])
    listafinal=[]
    listafinal.append(listanovarolado)
    listafinal.append(estoque)
    return listafinal


