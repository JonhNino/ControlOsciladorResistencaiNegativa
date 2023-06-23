import numpy as np
import matplotlib.pyplot as plt
import control

# Definición de la función de transferencia del sistema
num = [0.2383, 0.5988, 0.903]
den = [1.238, 0.5988, 1.903]
G = control.TransferFunction(num, den)

# Definición del vector de tiempos de simulación
t = np.linspace(0, 30, 1000)

# Caso estable: K = 1.0
K = 1.0
Gc = control.TransferFunction(K, 1)
sys = control.feedback(G*K, 1)
t, y = control.step_response(sys, T=t)
plt.plot(t, y, label="K = 1.0")

# Caso marginalmente estable: K = 1.273
K = 1.273
Gc = control.TransferFunction(K, 1)
sys = control.feedback(G*K, 1)
t, y = control.step_response(sys, T=t)
plt.plot(t, y, label="K = 1.273")

# Caso inestable: K = 1.3
K = 1.3
Gc = control.TransferFunction(K, 1)
sys = control.feedback(G*K, 1)
t, y = control.step_response(sys, T=t)
plt.plot(t, y, label="K = 1.3")
# Configuración de la gráfica
plt.legend()
plt.title("Respuesta al Criterio Routh – Hurwitz")
plt.show()
