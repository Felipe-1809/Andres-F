def AASHTO(t34,t38,t4,t10,t40,t100,t200,fondo,ll,lp):

    # Cálculos básicos
    total = t34+t38+t4+t10+t40+t100+t200
    pasa10 = 100 - ((100*(t34+t38+t4+t10))/total)
    pasa40 = 100 - ((100*(t34+t38+t4+t10+t40))/total)
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
            print('Los parámetros no cumplen las normas AASHTO')


        if IG <= 8:
            #Verificación que cumpla los parámetros de índice de plasticidad
            try:
                ip > 10
            except:
                print('Los parámetros no cumplen las normas AASHTO')

            if ll <= 40:
                suelo = 'A-4'

        elif IG <= 12:
            #Verificación que cumpla los parámetros de índice de plasticidad
            try:
                ip > 10
            except:
                print('Los parámetros no cumplen las normas AASHTO')

            if ll >= 41:
                suelo = 'A-5'

        elif IG <= 20:
            #Verificación que cumpla los parámetros de índice de plasticidad
            try:
                ip < 11
            except:
                print('Los parámetros no cumplen las normas AASHTO')

            if ll <= 40:
                suelo='A-6'
            elif ll > 41:
                if ip < (ll-30):
                    suelo='A-7-5'
                elif ip > (ll-30):
                    suelo='A-7-6'

        else:
            print('Los parámetros no cumplen las normas AASHTO')
            suelo = '¿?'

    else:

        #SUELOS FINOS#

     if IG == 0:
        if ip <= 6:
            if pasa10 <= 50:
                #Verificación que cumpla los parámetros de pasa #40
                try:
                    pasa40 > 30
                except:
                    print('Los parámetros no cumplen las normas AASHTO')

                #Verificación que cumpla los parámetros de pasa #200
                try:
                    pasa200 > 15
                except:
                    print('Los parámetros no cumplen las normas AASHTO')

                suelo = 'A-1-a'
            elif pasa10 == (''):  #En caso que esté vacío
                #Verificación que cumpla los parámetros de pasa #40
                try:
                    pasa40 > 50
                except:
                    print('Los parámetros no cumplen las normas AASHTO')

                #Verificación que cumpla los parámetros de pasa #200
                try:
                    pasa200 > 25
                except:
                    print('Los parámetros no cumplen las normas AASHTO')

                suelo = 'A-1-b'
            else:
                print('Los parámetros no cumplen las normas AASHTO')
                suelo = ''
        elif ip == (''): #En caso que esté vacío
            #Verificación que cumpla los parámetros de pasa #40
            try:
                pasa40 < 51
            except:
                print('Los parámetros no cumplen las normas AASHTO')

            #Verificación que cumpla los parámetros de pasa #200
            try:
                pasa200 > 10
            except:
                print('Los parámetros no cumplen las normas AASHTO')

            suelo = 'A-3'
        elif ip <= 10:
            #Verificación que cumpla los parámetros de pasa #200
            try:
                pasa200 > 35
            except:
                print('Los parámetros no cumplen las normas AASHTO')

            if ll <= 40 :
                suelo = 'A-2-4'
            elif ll  >= 41 :
                suelo = 'A-2-5'
            else:
                print('Los parámetros no cumplen las normas AASHTO')
                suelo = '¿?'
        else:
            print('Los parámetros no cumplen las normas AASHTO')
            suelo = '¿?'
     elif IG <= 4:
        #Verificación que cumpla los parámetros de pasa #200
        try:
            pasa200 > 35
        except:
            print('Los parámetros no cumplen las normas AASHTO')

        #Verificación que cumpla los parámetros de índice de plasticidad
        try:
            ip < 11
        except:
            print('Los parámetros no cumplen las normas AASHTO')

        if ll <= 40:
            suelo = 'A-2-6'
        elif ll >= 41:
            suelo = 'A-2-7'
        else:
            print('Los parámetros no cumplen las normas AASHTO')
            suelo = '¿?'
     else:
         print('Los parámetros no cumplen las normas AAHSTO')
         suelo = '¿?'

    resultado = 'Este suelo es un ' + str(suelo)

    #Resultado final

    print(resultado)
