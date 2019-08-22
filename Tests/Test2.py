#INICIALIZACION DE VARIABLES
contador=0
numeroes=0
total=0

while True:
    #INGRESO DE VARIABLES
    numeroes=input('Meta un número')
    #FINALIZACION DEL PROGRAMA
    if numeroes=='Listo':
        break
    else:
        #VERIFICACION DE VALIDEZ
        try:
            numero=float(numeroes)
            #ACUMULADO Y TOTAL
            contador=contador+1
            total=numero+total
        except :
            print("Por favor, meta un número")

#PROMEDIO Y RESULTADO
promedio=total/contador
print('Se ingresaron', contador, 'números', 'que dan un promedio de', promedio, 'y suman', total)
