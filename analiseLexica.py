entrada = input("Digite um Lexema: ")
lexema = entrada.replace(" ","")
print(lexema)


lista = []
tabelaDeSimbolo = []
tabelaLetra = []


for i in range(len(lexema)):
    
    if lexema[i].isalpha():
        
        if lexema[i] in tabelaDeSimbolo:
            del tabelaDeSimbolo[-1]

        tabelaDeSimbolo.append(lexema[i])
        #dale = sorted(tabelaDeSimbolo)
        indexTabela = tabelaDeSimbolo.index(lexema[i])

        print('<id',indexTabela,'> ', end='')
        

    elif lexema[i].isdigit():
        lista.append(lexema[i])
        print('<digito', lexema[i]+'> ', end='')
    
    elif lexema[i] in ['=', '+', '*']:
        print('<'+lexema[i]+'> ', end='')

    else:
        print('<error> ', end='')

    tabelaLetra.append(tabelaDeSimbolo)

print("")
ct = 0 
for v in (tabelaDeSimbolo):
    ct =ct + 1
    print(ct, v)