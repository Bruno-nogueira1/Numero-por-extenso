main = True

def numero_extenso(numero):
    numero = str(numero)
    tam = len(numero)   
    ok = False
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    unidade = ['um','dois','três','quatro','cinco','seis','sete','oito','nove']
    dez = ['onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
    decimal = ['dez','vinte','trinta','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
    centena = ['cento','duzentos','trezentos','quatrocentos','quinhentos','seiscentos','setecentos','oitocentos','novecentos']
    if numero == '0':
        print('Zero')
    if numero != '0':
        if tam == 1:
            for x in numeros:
                if x == numero:
                    print(unidade[numeros.index(x)])
        if tam == 2:
            for x in numeros:
                if not ok:
                    if numero[1] != '0':
                        if numero[0] == '1':
                            if x == numero[1]:
                                print(dez[numeros.index(x)])
                    if numero[1] == '0':
                        if x == numero[0]:
                            print(decimal[numeros.index(x)])
                    if numero[1] != '0':
                        if numero[0] != '1':
                            if x == numero[0]:
                                print(decimal[numeros.index(x)],end=' e ')
                                ok = True
                            if ok:
                                for x in numeros:
                                    if x == numero [1]:
                                        print(unidade[numeros.index(x)])
        if tam == 3:
            for x in numeros:
                if not ok:
                    ok = False
                    ok1 = True
                    ok2 = False
                    if numero[1] == '0' and numero[2] == '0':
                        ok1 = False
                        if numero[0] == '1':
                            print('cem')
                        else:
                            if x == numero[0]:
                                print(centena[numeros.index(x)])
                    if ok1:
                        if numero[0] == x:
                            print(centena[numeros.index(x)],end=' e ')
                            ok = True
                        while ok: 
                            for x in numeros:
                                if numero[1] == '0':
                                    if numero [2] == x:
                                        print(unidade[numeros.index(x)])
                                        ok = False
                                if numero[2] != '0':
                                    if numero[1] == '1':
                                        if x == numero[2]:
                                            print(dez[numeros.index(x)])
                                            ok = False
                                if numero[2] == '0':
                                    if x == numero[1]:
                                        print(decimal[numeros.index(x)])
                                        ok = False
                                if numero[2] != '0':
                                    if numero[1] != '1':
                                        if numero[1] != '0':
                                            if numero[1] == x:
                                                print(decimal[numeros.index(x)],end=' ')
                                                ok2 = True
                                            if ok2:
                                                if x == numero[2]:
                                                        print(unidade[numeros.index(x)])
                                                        ok = False
                                                        break


while main:
    numero =  int(input('Insira um número entre 0 e 999 para ser escrito por extenso:'))
    while not 0 <= numero < 1000:
        numero =  int(input('Insira um número entre 0 e 999 para ser escrito por extenso:'))
    numero_extenso(numero)
    continuar = int(input('''[1] Continuar
[2] Sair
'''))
    while not 0 < continuar < 3:
        continuar = int(input('''[1] Continuar
[2] Sair
'''))
    if continuar == 1:
        pass
    else:
        main = False