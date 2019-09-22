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
    u = 0.90 * (ll-8)
    a = 0.73 * (ll-20)

    #Inicialización de variables
    finos = str("")
    gruesos = str("")
    suelo = str("")
    granulometria = str("")
    atterberg = str("")
    first = str("")
    second = str("")

    #Estudio parte fina
    if pasa200 > 50:
        finos = "fino"
    #Estudio parte gruesa
    if pasa4 > 50:
        gruesos = "arena"

    #Límites de Atterberg - Suelo fino
    if finos == "fino":
        if u > ip:
            if ll > 50:
                if ip > a:
                    suelo = "CH"
                else:
                    suelo = "MH - OH"
            else:
                if ip > a:
                    if 4 < ip:
                        if ip < 7:
                            suelo = "CL - ML"
                        else:
                            suelo = "CL"
                    else:
                        print("Este suelo está bajo el índice de plasticidad de 4% y sobre la línea A")
                else:
                    suelo = "ML - OH"
        else:
            print("Este suelo sobrepasa la línea U")

    #Suelos gruesos
    else:
        #Casos
        if pasa200 > 5:
            atterberg = "TRUE"
        if pasa200 < 12:
            granulometria = "TRUE"

        #Granulometría
        if granulometria == "TRUE":
            if gruesos == "arena":
                if 1 < cc:
                    if cc < 3:
                        if cu > 6:
                            first = "SW"
                else:
                    first = "SP"
            else:
                if 1 < cc:
                    if cc < 3:
                        if cu > 4:
                            first = "GW"
                else:
                    first = "GP"
        #Atterberg
        if atterberg == "TRUE":
            if u > ip:
                if ip > a:
                    if ip > 4:
                        second = "C"
                    else:
                        print("Esta arcilla tiene un índice de plasticidad menor que 4% y sobre la línea A")
                else:
                    second = "M"
            else:
                print("Este suelo sobrepasa la línea U")

        #Creación de la variable Suelo
        if pasa200 < 5:
            suelo = first
        elif pasa200 > 12:
            suelo = first[1] + second
        else:
            suelo = str(first) + str(" - ") + str(first[1]) + str(second)

    #Impresión de resultados
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
#DEBERÍA DAR SP - SC
