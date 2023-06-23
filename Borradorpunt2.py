
import numpy as np
from scipy import signal


# definir parametros del sistema
L = 1
C = 1
R = -0.5
#u = 1
e = np.sqrt(L/C)


# Definir la matriz A
A = np.array([[0, 1/e], [-e, 0]])

# Definir la matriz B
B = np.array([[0], [1]])

# Definir la matriz C
C = np.array([[0, 1]])

# Definir la matriz D
D = np.array([[0]])

# # crear el sistema de espacio de estados
sys = signal.StateSpace(A, B, C, D)
#sys = StateSpace(A, B, C, D)

# obtener la función de transferencia
tf = sys.to_tf()

# Imprimir la función de transferencia
print(tf)

import matplotlib.pyplot as plt

# definir la entrada escalón unitario
t = np.linspace(0, 30, 1000)
u = np.ones_like(t)

# simular la respuesta del sistema
t, y, _ = signal.lsim(sys, u, t)

# graficar la respuesta del sistema
plt.plot(t, y)
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida')
plt.title('Respuesta del sistema a una entrada tipo escalón')
plt.show()
