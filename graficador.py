import matplotlib.pyplot as plt
import numpy as np

datos = open("xy.txt","r")
cadena = datos.readlines()

x = []
y = []

for i in range(len(cadena)):
    xn, yn = cadena[i].split(";")
    x.append(float(xn))
    y.append(float(yn))

plt.scatter(x, y)


coef = np.polyfit(x, y, 5) #determina los coeficientes del polinomio, en nuestro caso al tener un polinomio de grado 3, sacamos 4 coeficientes
poly1d_fn = np.poly1d(coef)
plt.plot(x, poly1d_fn(x), color="red", alpha=0.65)

# Imprime los parámetros del ajuste y el tipo de ajuste utilizado
print(f"Parámetros del ajuste: ", coef)
print(f"Tipo de ajuste utilizado: polinómico de grado {len(coef) - 1}")

# Calcula y muestra las distancias entre cada punto y la curva ajustada
distancias = np.abs(y - poly1d_fn(x))
labels = ["Y" + str(i+1) for i in range(len(distancias))]
for i in range(len(distancias)):
    plt.annotate(f"{labels[i]}: {distancias[i]:.4f}", xy=(x[i], y[i]), xytext=(x[i]+0.1, y[i]+0.1), fontsize=8)

for i in range(len(x)):
    plt.plot([x[i], x[i]], [y[i], poly1d_fn(x[i])], color="#99627A")

plt.xlabel('Masa (g)')
plt.ylabel('Frecuencia (?)')

# Imprime los parámetros del ajuste y el tipo de ajuste utilizado
print(f"Parámetros del ajuste: ", coef)
print(f"Tipo de ajuste utilizado: polinómico de grado {len(coef) - 1}")

# Guarda el gráfico en formato png con un nombre descriptivo
plt.savefig("ajuste_polinomico.png")

plt.show()

