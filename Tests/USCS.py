def USCS(t34,t38,t4,t10,t50,t100,t200,fondo,ll,lp,d10,d30,d60):

    #Cálculos básicos

    total=t34+t38+t4+t10+t50+t100+t200

    pasa4=100-((100*(t34+t38+t4))/total)
    pasa200=((100*fondo)/total)

    ip = ll-lp

    cc=(( d30 * d30 )/( d10 * d60 ))

    #Clasificación de grueso o fino

    if pasa200 < 35:
        x = 'suelo fino'
    else:
        x= 'suelo grueso'
