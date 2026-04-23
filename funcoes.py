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
def remover_dado(rolado,estoque,remover):
    listanovarolado1=rolado
    estoquenovo=[]
    for i in range(len(estoque)):
        if i==remover:
            listanovarolado1.append(estoque[i])
        else:
            estoquenovo.append(estoque[i])
    listafinal=[]
    listafinal.append(listanovarolado1)
    listafinal.append(estoquenovo)
    return listafinal
def calcula_pontos_regra_simples(x):
    dic={}
    valores=[1,2,3,4,5,6]
    for valor in valores:
        if valor not in x:
            dic[valor]=0
        else:
            d=x.count(valor)
            dic[valor]=d*valor
    return dic
def calcula_pontos_soma(x):
    soma=0
    for valores in x:
        soma+=valores
    return soma
def calcula_pontos_sequencia_baixa(x):
    combinacoes=[[1,2,3,4],[2,3,4,5],[3,4,5,6]]
    lista_validacao=[]
    booleano=False
    for lista in combinacoes:
        for valores in lista:
            if valores in x:
                lista_validacao.append(valores)
        if lista_validacao in combinacoes:
            booleano=True
        lista_validacao=[]
    if booleano==True:
        return 15
    else:
        return 0
def calcula_pontos_sequencia_alta(x):
    combinacoes=[[1,2,3,4,5],[2,3,4,5,6]]
    lista_validacao=[]
    booleano=False
    for lista in combinacoes:
        for valores in lista:
            if valores in x:
                lista_validacao.append(valores)
        if lista_validacao in combinacoes:
            booleano=True
        lista_validacao=[]
    if booleano==True:
        return 30
    else:
        return 0



                









