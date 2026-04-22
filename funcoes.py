import random
def rolar_dados(x):
    lista=[]
    lista=[0]*x
    for i in range(len(lista)):
        lista[i]=random.randint(1,6)
    return lista


