import control

# Definir la función de transferencia
num = [0.2383, 0.5988, 0.903]
den = [1.238, 0.5988, 1.903]
sys = control.tf(num, den)

# Verificar la estabilidad del sistema
is_stable = control.margin(sys)[0] > 0
print('El sistema es estable:', is_stable)
