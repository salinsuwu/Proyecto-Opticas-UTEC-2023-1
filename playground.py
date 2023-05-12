import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance

# cargar datos desde el archivo "xy.txt"
data = np.loadtxt("xy.txt", delimiter=";")
x, y = data[:, 0], data[:, 1]

# ajuste de curva polinómica de grado 3
coef = np.polyfit(x, y, 5)
poly1d_fn = np.poly1d(coef)

# plotear puntos y curva de ajuste
plt.scatter(x, y)
plt.plot(x, poly1d_fn(x), '--k')

# calcular la distancia entre cada punto y la línea de ajuste
distances = []
for i in range(len(x)):
    point = (x[i], y[i])
    dist = distance.euclidean(point, (x[i], poly1d_fn(x[i])))
    distances.append(dist)

# plotear líneas de distancia
for i in range(len(x)):
    plt.plot([x[i], x[i]], [y[i], poly1d_fn(x[i])], ':r')

# agregar etiquetas y mostrar el gráfico
plt.title("Curva de ajuste polinómico y distancia de los puntos a la curva")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
