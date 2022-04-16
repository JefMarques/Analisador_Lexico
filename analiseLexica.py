import re   #Importando o biblioteca regex
entrada = input("Digite um Lexema: ")   #Entrada do Lexema
lexema = entrada.replace(" ","")    #Remover espaços caso tenha
print("Antes do Regex:",lexema)     
lexema = re.sub(r'#.*','',lexema)   #Remover linha de comentario caso tenha
print("Depois do Regex:",lexema)


tabelaDeSimbolo = [] 
tabelaLetra = []


for i in range(len(lexema)):    #for para analisar o lexema
    
    if lexema[i].isalpha():     #Analisa se cada item do lexema é letra
        tabelaLetra.append(lexema[i])   #Se for letra adiciona na lista
        if lexema[i] in tabelaDeSimbolo:    #Se for uma letra repetida 
            del tabelaDeSimbolo[-1]     #Deleta uma posição na lista

        tabelaDeSimbolo.append(lexema[i])   #Se for letra adiciona na lista
        indexTabela = tabelaDeSimbolo.index(lexema[i])  #O index de cada letra na lista

        print('<id',indexTabela+1,'> ', end='') 
        
        
    elif lexema[i].isdigit():   #Analisa se cada item do lexema é digito
        print('<digito', lexema[i]+'> ', end='')
    
    elif lexema[i] in ['=', '+', '*']:  #Analisa se o lexema tem esses operadores
        print('<'+lexema[i]+'> ', end='')

    else: #saida de erro caso o lexema possua algo fora do padrão
        print('<error> ', end='')

    

print("")
ct = 0  #contador para a tabela de simbolos
tab = sorted(set(tabelaLetra))  #Deixando a lista em ordem alfabetica e removendo itens repetidos
for v in (tab): #rodando a lista
    ct+=1    
    print(ct, v) 