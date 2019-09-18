def AASHTO(t34,t38,t4,t10,t50,t100,t200,fondo,ll,lp):

    #Cálculos básicos

    total=t34+t38+t4+t10+t50+t100+t200

    pasa4=100-((100*(t34+t38+t4))/total)
    pasa200=((100*fondo)/total)

    ip = ll-lp

    #Clasificación de grueso o fino

    if pasa200 < 35:
        x = 'suelo fino'
    else:
        x= 'suelo grueso'
