def USCS(t34,t38,t4,t10,t40,t100,t200,fondo,ll,lp,d10,d30,d60):

    # Cálculos básicos
    total=t34+t38+t4+t10+t40+t100+t200
    pasa4 = 100 - ((100*(t34+t38+t4))/total)
    pasa200 = ((100*fondo)/total)
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

    #Clasificación del Suelo
    if pasa200 > 50:
        tipo = 'fino'

    #Suelos finos
    if tipo = 'fino':
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
            caso1 = TRUE
        elif pasa200 > 12:
            caso2 = TRUE
        else:
            caso3 = TRUE

        #Caso 1
        if caso1 = TRUE:
            if 50 < pasa4:
            grueso = 'arena'
                if grueso = 'arena':
                    if 1 < cc:
                        if cc < 3:
                            if 6 < cu:
                                first = 'SW'
                    else:
                        first = 'SP'
                else:
                    if 1 < cc:
                        if cc < 3:
                            if 4 < cu:
                                first = 'GW'
                    else:
                        first = 'GP'

        #Caso 2
        if caso2 = TRUE:
            if 50 < pasa4:
            grueso = 'arena'
                if grueso = 'arena':
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

        #Caso 3
        if caso3 = TRUE:
            if 50 < pasa4:
            grueso = 'arena'
                if grueso = 'arena':
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
