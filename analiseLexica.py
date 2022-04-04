import re
entrada = input("Digite um Lexema: ")
lexema = entrada.replace(" ","")
print(lexema)
lexema = re.sub(r'#.*','',lexema)


lista = []
tabelaDeSimbolo = []
tabelaLetra = []


for i in range(len(lexema)):
    
    if lexema[i].isalpha():
        tabelaLetra.append(lexema[i])
        if lexema[i] in tabelaDeSimbolo:
            del tabelaDeSimbolo[-1]

        tabelaDeSimbolo.append(lexema[i])
        #dale = sorted(tabelaDeSimbolo)
        indexTabela = tabelaDeSimbolo.index(lexema[i])

        print('<id',indexTabela+1,'> ', end='')
        

    elif lexema[i].isdigit():
        lista.append(lexema[i])
        print('<digito', lexema[i]+'> ', end='')
    
    elif lexema[i] in ['=', '+', '*']:
        print('<'+lexema[i]+'> ', end='')

    else:
        print('<error> ', end='')

    

print("")
ct = 0
tab = sorted(set(tabelaLetra))
for v in (tab):
    ct+=1    
    print(ct, v)