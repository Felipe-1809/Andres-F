%Esta funci�n desarrolla el bulbo de esfuerzos verticales a partir de:
%%% q - como la carga distribuida
%%% b - la franja a lo largo de la cual se aplica la carga distribuida

%Los valores de alpha y betha fueron ingresado calculados como
%%%b=atan((x_pos(j) - (b/2))/y_pos(i))
%%%a=atan((x_pos(j) + (b/2))/y_pos(i))-atan((x_pos(j) - (b/2))/y_pos(i))

    b=6; %Par�metro - a modificar
    q=10; %Par�metro - a modificar
   
    %Divisi�n de la cuadr�cula
    y = 4 * b; %Rango y - a modificar
    x = 3 * b; %Rango x - a modificar

    dy = b / 100; %Diferencial y
    dx = b / 100; %Diferencial x
    
    canty = y / dy; %Cantidad de elementos en y
    cantx = x / dx; %Cantidad de elementos en x  
         
    x_pos=linspace(0,x,cantx); %Vector de coordenadas en x
    y_pos=linspace(0,y,canty); %Vector de coordenadas en y
    
    Matub=zeros(canty,cantx); %Inicializaci�n de la matr�z de con las ubicaciones
    
    %Matriz de esfuerzos
    for i=1: canty
        for j=1:cantx
            Matub(i,j) = (q/pi())*((atan((x_pos(j) + (b/2))/y_pos(i))-atan((x_pos(j) - (b/2))/y_pos(i)))+(sin(atan((x_pos(j) + (b/2))/y_pos(i))-atan((x_pos(j) - (b/2))/y_pos(i)))*cos(atan((x_pos(j) + (b/2))/y_pos(i))-atan((x_pos(j) - (b/2))/y_pos(i))+(2*(atan((x_pos(j) - (b/2))/y_pos(i)))))));
        end
    end 
   
%Gr�fico de resultados
figure(1)
[xx,yy] = meshgrid(x_pos,y_pos);
mesh(yy,xx,Matub);
colormap('jet');
colorbar;
title('Esfuerzo vertical')
xlabel('Profundidad')
ylabel('Distancia horizontal')
zlabel('Esfuezo(x,y)')

