def AASHTO(t34,t38,t4,t10,t40,t100,t200,fondo,ll,lp):

    #Inicialización de variables
    general = ''

    # Cálculos básicos
    total = t34+t38+t4+t10+t40+t100+t200
    pasa10 = 100 - ((100*(t34+t38+t4+t10))/total)
    pasa40 = 100 - ((100*(t34+t38+t4+t10+t40))/total)
    pasa200 = ((100*fondo)/total)
    ip = ll-lp

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

    #Condiciones A-7
    a7 = ll-30

    #Índice de grupo
    IG = int((0.2*a) + (0.005*a*c) + (0.01*b*d))

    #División general
    if pasa200 < 35:
        general = str('grueso')
    else:
        general = 'fino'

    #Clasificación de finos
    if general = 'fino'
        if pasa200 >= 36:
            if ip <= 10:
                if IG <= 8:
                    if ll <= 40:
                        suelo = 'A-4'
                elif IG <= 12:
                    if ll >= 41:
                        suelo = 'A-5'
            elif ip >= 11:
                if IG <=20:
                    if ll <= 40:
                        suelo = 'A-6'
                    elif ll > 41:
                        if ip < a7:
                            suelo = 'A-7-5'
                        elif ip > a7:
                            suelo = 'A-7-6'
        else:
            suelo = 'desconocido'

    #Clasificación de gruesos
    if general == 'grueso'
        if IG = 0:
            if ip = 0:
                if ll = 0:
                    if pasa200 <= 10:
                        if pasa40 >= 51:
                            suelo = 'A-3'
            elif ip <= 6:
                if pasa200 <= 15:
                    if pasa40 <= 30:
                        if pasa10 <= 50:
                            suelo = 'A-1-a'
                if pasa200 <= 25:
                    if pasa40 <= 50:
                        suelo = 'A-1-b'
            elif ip <= 10:
                if pasa200 <= 35:
                    if ll <= 40:
                        suelo = 'A-2-4'
                    if ll >= 41:
                        suelo = 'A-2-5'
        if IG <= 4:
            if ip >= 11:
                if pasa200 <= 35:
                    if ll <= 40:
                        suelo = 'A-2-6'
                    elif ll >= 41:
                        suelo = 'A-2-7'
        else:
            suelo = 'desconocido'

    #Guardado de resultados y mensajes
    res = str(suelo)
    des = str('Este suelo no fue reconocido bajo parámetros AASHTO')
    sue = str('Este suelo es un ')
    gru = str(IG)
    fin = sue + res + str('(') + gru + str(')')

    #Impresión de resultados
    if suelo == 'desconocido':
        print(des)
    else:
        print(fin)

    #Ingreso de granulometría

    #Ejemplo:
    AASHTO(0,0,0,0,26,0,6,68,65,20)
    #AASHTO(t34,t38,t4,t10,t40,t100,t200,fondo,ll,lp)
