import numpy as np
import control
epsilon=1
# Definir las matrices A y B
A = np.array([[0, 1/epsilon],[-1, 0]])
B = np.array([[0], [0]])
# Obtener el espacio de estados
sys = control.ss(A, B, np.eye(2), 0)
# Imprimir el espacio de estados
print(sys)
# Obtener la función de transferencia
tf_sys = control.tf(sys)
# Simulación del sistema para una entrada tipo escalón unitario
t, y = control.step_response(sys)
plt.plot(t, y)
plt.xlabel('Tiempo')
plt.ylabel('Salida')
plt.title('Respuesta del sistema linealizado a una entrada tipo escalón unitario')
plt.show()
