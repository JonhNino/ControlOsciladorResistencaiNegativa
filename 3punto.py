import numpy as np
import matplotlib.pyplot as plt

# Definir la función de transferencia del sistema en lazo abierto
def G(s):
    return 1 / (s**2 + 1)

# Definir la función de transferencia del sistema en lazo cerrado
def H(s, Kp=0, Ti=0, Td=0):
    if Kp == 0 and Ti == 0 and Td == 0:
        # Lazo cerrado sin controlador
        return G(s) / (1 + G(s))
    else:
        # Lazo cerrado con controlador PID
        return (Kp*(1 + Ti*s + Td*s**2)*G(s)) / (1 + (Ti*s + Td*s**2 + Kp*G(s)))

# Definir los parámetros del controlador PID
Kp = 1.35
Ti = 2.5
Td = 0.37

# Definir el tiempo de simulación
t = np.linspace(0, 10, 1000)

# Graficar la respuesta al escalón del sistema en lazo cerrado sin controlador
plt.figure(figsize=(10,5))
plt.plot(t, [H(np.complex128(s)).real for s in t], label='Lazo cerrado sin controlador')

# Graficar la respuesta al escalón del sistema en lazo cerrado con controlador PID
plt.plot(t, [H(np.complex128(s), Kp, Ti, Td).real for s in t], label='Lazo cerrado con controlador')

# Configurar la gráfica
plt.title('Respuesta al escalón del sistema')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid()
plt.legend()

# Mostrar la gráfica
plt.show()
