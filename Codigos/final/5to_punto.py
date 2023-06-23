import control
import matplotlib.pyplot as plt

# Definir la función de transferencia
num = [0.2383, 0.5988, 0.903]
den = [1.238, 0.5988, 1.903]
sys = control.tf(num, den)

# Obtener los polos y ceros
zeros = control.zero(sys)
poles = control.pole(sys)

# Graficar el Lugar de las Raíces
rlocus = control.rlocus(sys)

# Agregar los ceros y polos al gráfico
plt.plot(zeros.real, zeros.imag, 'o', markersize=10)
plt.plot(poles.real, poles.imag, 'x', markersize=10)

# Configurar el gráfico
plt.grid(True)
plt.xlabel('Real')
plt.ylabel('Imaginario')
plt.title('Lugar de las Raíces')
plt.show()


