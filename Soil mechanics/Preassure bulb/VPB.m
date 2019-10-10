%This function develops the bulb preassure in a soil according to:
%%% q -> The load applied along a distance
%%% b -> The length where the load is applied

%Alpha and beta values were calculated as:
%%% Beta = atan((x_pos(j) - (b/2))/y_pos(i))
%%% Alpha = atan((x_pos(j) + (b/2))/y_pos(i)) - atan((x_pos(j) - (b/2))/y_pos(i))

% Other varibles
%%% Range x -> b times projected in the x-axis
%%% Range y -> b times projected in the y-axis
%%% Differential -> Precision level required

function VPB(q,b,ranx,rany,dif)
   
    %Development of the grid
    y = b * rany; %Range y
    x = b * ranx; %Range x

    dy = b / dif; %Differential y
    dx = b / dif; %Differential x
    
    canty = y / dy; %Elements in y
    cantx = x / dx; %Elements in x  
         
    x_pos = linspace(0,x,cantx); %Vector with coordinates x
    y_pos = linspace(0,y,canty); %Vector with coordinates y
    
    Matub = zeros(canty,cantx); %Inicialization of the matrix
    
    %Stress matrix
    for i=1: canty
        for j=1:cantx
            Matub(i,j) = (q/pi())*((atan((x_pos(j) + (b/2))/y_pos(i))-atan((x_pos(j) - (b/2))/y_pos(i)))+(sin(atan((x_pos(j) + (b/2))/y_pos(i))-atan((x_pos(j) - (b/2))/y_pos(i)))*cos(atan((x_pos(j) + (b/2))/y_pos(i))-atan((x_pos(j) - (b/2))/y_pos(i))+(2*(atan((x_pos(j) - (b/2))/y_pos(i)))))));
        end
    end 
   
    %Gradient's graphic (3d)
    figure(1)
    [xx,yy] = meshgrid(x_pos,-y_pos);
    mesh(xx,yy,Matub);
    colormap('jet');
    colorbar;
    title('Esfuerzo vertical')
    xlabel('Distancia horizontal')
    ylabel('Profundidad')
    zlabel('Esfuezo(x,y)')

    %Preassure bulb (2d)
    figure(2)
    contour(xx,yy,Matub);
    colormap('jet');
    colorbar;
    title('Bulbo de esfuerzos vertical')
    xlabel('Distancia horizontal')
    ylabel('Profundidad')
    zlabel('Esfuezo(x,y)')
