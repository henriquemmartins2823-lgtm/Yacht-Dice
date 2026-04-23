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
def calcula_pontos_full_house(x):
    lista_valores=[]
    soma=0
    for valores in x:
        if valores not in lista_valores:
            lista_valores.append(valores)
        soma+=valores
    if x.count(lista_valores[0])==3 and x.count(lista_valores[1])==2:
        return soma
    elif x.count(lista_valores[0])==2 and x.count(lista_valores[1])==3:
        return soma
    else:
        return 0
def calcula_pontos_quadra(x):
    soma=0
    booleano=False
    for valores in x:
        if x.count(valores)>=4:
            booleano=True
        soma+=valores
    if booleano==True:
        return soma
    else:
        return 0
def calcula_pontos_quina(x):
    booleano=False
    lista_valores=[1,2,3,4,5,6]
    for valores in lista_valores:
        if x.count(valores)>=5:
            booleano=True
    if booleano==True:
        return 50
    else:
        return 0
def calcula_pontos_regra_avancada(x):
    dic_regras={}
    dic_regras['cinco_iguais']=calcula_pontos_quina(x)
    dic_regras['full_house']=calcula_pontos_full_house(x)
    dic_regras['quadra']=calcula_pontos_quadra(x)
    dic_regras['sem_combinacao']=calcula_pontos_soma(x)
    dic_regras['sequencia_alta']=calcula_pontos_sequencia_alta(x)
    dic_regras['sequencia_baixa']=calcula_pontos_sequencia_baixa(x)
    return dic_regras
def faz_jogada(lista,categoria,cartela):
    lista_numeros=["1","2","3","4","5","6"]
    if categoria in lista_numeros:
        categoria=int(categoria)
        dic=calcula_pontos_regra_simples(lista)
        cartela["regra_simples"][categoria]=dic[categoria]
    else:
        dic=calcula_pontos_regra_avancada(lista)
        cartela["regra_avancada"][categoria]=dic[categoria]
    return cartela




                









