#para manejar intervalos consistentes, creamos un for que nos de 10 valores que usaremos enel .exe y guardamos en una lista
x1=500

x=[]
for i in range(0,10):
    xi=32.78
    x1+=xi
    x.append(x1)
#almacenamos las y's de forma manual en una lista
y=[5.03,4.87,4.73,4.6,4.48,4.37,4.26,4.17,4.08,3.99]
# esto lo colocamos en un .txt

x_e_y=open("xy.txt","w")
for i in range(10):
    texto=str(round(x[i]))+";"+str(y[i])+"\n"
    x_e_y.write(texto)


