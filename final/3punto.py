import numpy as np
import matplotlib.pyplot as plt
import control as ctl

num = [1, 0]
den = [1, 0, 1]
G = ctl.tf(num, den)

Kp = 0
Ki = 0
Kd = 0

t, y = ctl.step_response(G)
Kp_max = np.max(y)
Kp_critico = 0.6*Kp_max
Tu = t[np.argmax(y)]*2

Kp = Kp_critico
Ki = 1.2*Kp_critico/Tu
Kd = 0.5*Kp_critico*Tu

r = ctl.tf([1], [1, 0])
C = Kp + Ki/r + Kd*r
T = ctl.feedback(C*G, 1)
print('Función de Transferencia en Lazo Cerrado:')
print(T)

t, y = ctl.step_response(T)
u = Kp*(y[1]-y[0]) + Ki*y[0] + Kd*(y[1]-2*y[0]+0)/0.02 # calculate input u(t) from output y(t)

print('Input data u(t):')
print(u)
print('Output data y(t):')
print(*y, sep=',')


plt.plot(t[t<=30], y[t<=30])
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida')
plt.title('Respuesta en Lazo Cerrado con Controlador PID')
plt.grid()
plt.show()
