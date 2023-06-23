import numpy as np
import matplotlib.pyplot as plt
import control as ctl

num = [-0.09846485666488719]
den = [1.0577182874793338, 1]
T = ctl.tf(num, den)

print('Función de Transferencia en Lazo Cerrado:')
print(T)

t, y = ctl.step_response(T)

plt.plot(t[t<=30], y[t<=30])
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida')
plt.title('Respuesta en Lazo Cerrado con Controlador PID')
plt.grid()
plt.show()
