def AASHTO(t34,t38,t4,t10,t50,t100,t200,fondo,ll,lp):

    # Cálculos básicos
    total = t34+t38+t4+t10+t50+t100+t200
    pasa4 = 100 - ((100*(t34+t38+t4))/total)
    pasa200 = ((100*fondo)/total)
    ip = ll-lp

    # Clasificación de grueso o fino
    if pasa200 < 35:
        tipo = 'fino'
    else:
        tipo = 'grueso'

    #Definición a
    if pasa200 < 35:
        a = 0
    elif pasa200 > 75:
        a = 40
    else:
        int(a) = pasa200 - 35

    #Definición b
    if pasa200 < 15 :
        b = 0
    elif pasa200 > 45 :
        b = 40
    else:
        int(b) = pasa200 - 15

    #Definición c
    if ll < 40:
        c = 0
    elif ll > 60:
        c = 20
    else:
        int(c) = ll - 35

    #Definición d
    if ip < 10:
        d = 0
    elif ip > 30:
        d = 20
    else:
        int(d) = ip - 10

    #Índice de grupo
    int(IG) = (0.2*a) + (0.005*a*c) + (0.01*b*d)

    #Clasificación del suelo
    if tipo = 'grueso':

        #SUELOS GRUESOS#

        #Verificación que cumpla los parámetros pasa #200
        try:
            pasa200 < 36
        except:
            print('Los parámetros no cumplen las normas AASHTO')
            break

        if IG <= 8:
            #Verificación que cumpla los parámetros de índice de plasticidad
            try:
                ip > 10
            except:
                print('Los parámetros no cumplen las normas AASHTO')
                break
            if ll <= 40:
                suelo = 'A-4'

        elif IG <= 12:
            #Verificación que cumpla los parámetros de índice de plasticidad
            try:
                ip > 10
            except:
                print('Los parámetros no cumplen las normas AASHTO')
                break
            if ll >= 41:
                suelo = 'A-5'

        elif IG <= 20:
            #Verificación que cumpla los parámetros de índice de plasticidad
            try:
                ip < 11
            except:
                print('Los parámetros no cumplen las normas AASHTO')
                break
            if ll <= 40:
                suelo='A-6'
            elif ll > 41:
                if ip < (ll-30):
                    suelo='A-7-5'
                else ip > (ll-30):
                    suelo='A-7-6'

        else:
            print('Los parámetros no cumplen las normas AASHTO')

    else:

        #SUELOS FINOS#
