import numpy as np
import matplotlib.pyplot as plt

def step(K):
    num = 1.35 * (1 + 1/(2.5 * s) + 0.37 * s)
    den = s**2 + s + 2.35 + K * num
    return 1/den

s = np.linspace(0, 10, 1000)

# Caso K = 0 (inestable)
y1 = step(0)
plt.plot(s, y1, label="K=0")

# Caso K = 1 (estable)
y2 = step(1)
plt.plot(s, y2, label="K=1")

# Caso K marginalmente estable
Kc = 3.85
y3 = step(Kc)
plt.plot(s, y3, label="K={}".format(Kc))

plt.xlabel("Tiempo (s)")
plt.ylabel("Respuesta del sistema")
plt.title("Simulación de sistema en lazo cerrado")
plt.legend()
plt.show()
