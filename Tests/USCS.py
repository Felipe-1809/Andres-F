def USCS(t34,t38,t4,t10,t40,t100,t200,fondo,ll,lp,d10,d30,d60):

    # Cálculos básicos
    total = t34+t38+t4+t10+t40+t100+t200+fondo
    pasa4 = 100 - ((100*(t34+t38+t4))/total)
    pasa200 = 100 - ((100*(t34+t38+t4+t10+t40+t100+t200))/total)
    ip = ll-lp

    #Cálculos de granulometría
    cc = (( d30 * d30 )/( d10 * d60 ))
    cu = d60 / d10

    #Cálculos de la carta de plasticidad
    u = 0.90 - (ll-8)
    a = 0.73 - (ll-20)

    #Inicialización de variables
    grueso = str('')
    tipo = str('')
    suelo = str('')
    caso1 = str('')
    caso2 = str('')
    caso3 = str('')

    #Clasificación del Suelo
    if pasa200 > 50:
        tipo == "fino"

    #Suelos finos
    if tipo == "fino":
        if ll > 50:
            if u > ip:
                if a < ip:
                    suelo = 'CH'
                else:
                    suelo = 'MH - OH'
        else:
            if u > ip:
                if a > ip:
                    suelo = 'ML-OL'
                else:
                    if 4 < ip:
                        if 7 > ip:
                            suelo = 'CL-ML'
                        else:
                            suelo = 'CL'

    #Suelos gruesos
    else:

        #Casos
        if pasa200 < 5:
            caso1 = "TRUE"
        elif pasa200 > 12:
            caso2 = "TRUE"
        else:
            caso3 = "TRUE"

        #Caso 1
        if caso1 == "TRUE":
            if 50 < pasa4:
                grueso == 'arena'
                if grueso == "arena":
                    if 1 < cc:
                        if cc < 3:
                            if 6 < cu:
                                suelo = 'SW'
                    else:
                        suelo = 'SP'
                else:
                    if 1 < cc:
                        if cc < 3:
                            if 4 < cu:
                                suelo = 'GW'
                    else:
                        suelo = 'GP'

        #Caso 2
        if caso2 == "TRUE":
            if 50 < pasa4:
                grueso = 'arena'
                if grueso == "arena":
                    if 1 < cc:
                        if cc < 3:
                            if 6 < cu:
                                first = 'S'
                    else:
                        first = 'S'
                else:
                    if 1 < cc:
                        if cc < 3:
                            if 4 < cu:
                                first = 'G'
                    else:
                        first = 'G'
            if ll > 50:
                if u > ip:
                    if a < ip:
                        second = 'C'
                    else:
                        second = 'M'
            else:
                if u > ip:
                    if a > ip:
                        second = 'M'
                    else:
                        if 4 < ip:
                            if 7 > ip:
                                second = 'C'
                            else:
                                second = 'C'
            suelo = first + second

        #Caso 3
        if caso3 == "TRUE":
            if 50 < pasa4:
                grueso = 'arena'
                if grueso == "arena":
                    if 1 < cc:
                        if cc < 3:
                            if 6 < cu:
                                suelo = 'Arenas bien gradadas'
                    else:
                        suelo = 'Arenas pobremente gradadas'
            else:
                if 1 < cc:
                    if cc < 3:
                        if 4 < cu:
                            suelo = 'Gravas bien gradadas'
                else:
                    suelo = 'Gravas pobremente gradadas'
            if ll > 50:
                if u > ip:
                    if a < ip:
                        suelo = 'arcillas de alta plasticidad'
                    else:
                        suelo = 'limos de alta plasticidad'
                else:
                    if u > ip:
                        if a > ip:
                            suelo = 'limos de baja plasticidad'
                        else:
                            if 4 < ip:
                                if 7 > ip:
                                    suelo = 'arcillas y limos de alta plasticidad'
                                else:
                                    suelo = 'arcillas de baja plasticidad'

    #Impresión de resultados
    if suelo == '':
        print('Este suelo no se acoje a los parámetros de Clasificación USCS')
    else:
        print("Este suelo corresponde a un:" + suelo)

#Interfaz
#print('Este programa a través de la granulometría ingresada da como resultado la clasificación bajo el sistema USCS')
#print('Orden de granulometría: t3/4, t3/8, t4, t10, t40, t100, t200, fondo')
#print('Orden de límites líquido y plástico: LL, LP')
#print('Orden de deciles: D10, D30, D60')
#t34, t38, t4, t10, t40, t100, t200, fondo = [int(x) for x in input("Ingrese la granulometría").split()]
#ll, lp = [int(x) for x in input("Ingrese los límites líquido y plástico").split()]
#d10, d30, d60 = [float(x) for x in input("Ingrese los deciles").split()]

#USCS(t34,t38,t4,t10,t40,t100,t200,fondo,ll,lp,d10,d30,d60)
USCS(0,0,25,0,45,0,22,8,18,6,0.081,0.21,0.28)
