def AASHTO(t34,t38,t4,t10,t40,t100,t200,fondo,ll,ip):

    # Cálculos básicos
    total = t34+t38+t4+t10+t40+t100+t200
    pasa10 = 100 - ((100*(t34+t38+t4+t10))/total)
    pasa40 = 100 - ((100*(t34+t38+t4+t10+t40))/total)
    pasa200 = ((100*fondo)/total)

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
        a = int(pasa200 - 35)

    #Definición b
    if pasa200 < 15 :
        b = 0
    elif pasa200 > 45 :
        b = 40
    else:
        b = int(pasa200 - 15)

    #Definición c
    if ll < 40:
        c = 0
    elif ll > 60:
        c = 20
    else:
        c = int(ll - 35)

    #Definición d
    if ip < 10:
        d = 0
    elif ip > 30:
        d = 20
    else:
        d = int(ip - 10)

    #Índice de grupo
    IG = int((0.2*a) + (0.005*a*c) + (0.01*b*d))

    #Clasificación del suelo

        #SUELOS GRUESOS#

    if tipo == 'grueso':

        #Verificación que cumpla los parámetros pasa #200
        try:
            pasa200 < 36
        except:
            print('Los parámetros no cumplen las normas AASHTO L60')

        if IG <= 8:
            #Verificación que cumpla los parámetros de índice de plasticidad
            try:
                ip > 10
            except:
                print('Los parámetros no cumplen las normas AASHTO L67')

            if ll <= 40:
                suelo = 'A-4'

        elif IG <= 12:
            #Verificación que cumpla los parámetros de índice de plasticidad
            try:
                ip > 10
            except:
                print('Los parámetros no cumplen las normas AASHTO L77')

            if ll >= 41:
                suelo = 'A-5'

        elif IG <= 20:
            #Verificación que cumpla los parámetros de índice de plasticidad
            try:
                ip < 11
            except:
                print('Los parámetros no cumplen las normas AASHTO L87')

            if ll <= 40:
                suelo='A-6'
            elif ll > 41:
                if ip < (ll-30):
                    suelo='A-7-5'
                elif ip > (ll-30):
                    suelo='A-7-6'

        else:
            print('Los parámetros no cumplen las normas AASHTO L98')
            suelo = '¿?'

    else:

        #SUELOS FINOS#

     if IG == 0:
        if ip <= 6:
            if pasa200 <= 15:
                #Verificación que cumpla los parámetros de pasa #40 y pasa #200
                try:
                    pasa40 > 30
                    pasa10 > 50
                except:
                    print('Los parámetros no cumplen las normas AASHTO L113')

                suelo = 'A-1-a' #####

            elif pasa200 <= 25:
                #Verificación que cumpla los parámetros de pasa #40
                try:
                    pasa40 > 50
                except:
                    print('Los parámetros no cumplen las normas AASHTO L122')

                suelo = 'A-1-b' #####

            else:
                suelo = 'desconocido'

        elif ip == 0:
            #Verificación que cumpla los parámetros de pasa #40 y pasa #200
            try:
                pasa40 < 51
                pasa200 > 10
            except:
                print('Los parámetros no cumplen las normas AASHTO L135')
                suelo = 'desconocido'

            suelo = 'A-3' #####
        elif ip <= 10:

            #Verificación que cumpla los parámetros de pasa #200
            try:
                pasa200 > 35
            except:
                print('Los parámetros no cumplen las normas AASHTO L145')

            if ll <= 40 :
                suelo = 'A-2-4' #####
            elif ll  >= 41 :
                suelo = 'A-2-5' #####
            else:
                print('Los parámetros no cumplen las normas AASHTO L166')
                suelo = 'desconocido'
        else:
            print('Los parámetros no cumplen las normas AASHTO L155')
            suelo = 'desconocido'

     elif IG <= 4:
        #Verificación que cumpla los parámetros de pasa #200
        try:
            pasa200 > 35
            ip < 11
        except:
            print('Los parámetros no cumplen las normas AASHTO L164')

        if ll <= 40:
            suelo = 'A-2-6' #####
        elif ll >= 41:
            suelo = 'A-2-7' #####
        else:
            print('Los parámetros no cumplen las normas AASHTO L171')
            suelo = 'desconocido'
     else:
         print('Los parámetros no cumplen las normas AAHSTO L174')
         suelo = 'desconocido'

    resultado = 'Este suelo es ' + str(suelo)

    #Resultado final

    print(resultado)

AASHTO(0,0,25,0,45,0,22,8,18,12)
#AASHTO(t34,t38,t4,t10,t40,t100,t200,fondo,ll,ip):
