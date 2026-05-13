import numpy as np

# 1. Definir escenarios y probabilidades
# Escenarios: Alto rendimiento, Bajo rendimiento
probabilidad = np.array([0.6, 0.4]) # P(Alto), P(Bajo)
rendimiento_inversion = np.array([1000, -500]) # Ganancias/Pérdidas
rendimiento_no_invertir = np.array([0, 0])

# 2. VE sin información (Decisión basada en promedio)
ve_inversion = np.sum(probabilidad * rendimiento_inversion)
ve_no_invertir = np.sum(probabilidad * rendimiento_no_invertir)
valor_esperado_sin_info = max(ve_inversion, ve_no_invertir)

# 3. VE con información perfecta
# Si sabemos que es "Alto" (inversión) o "Bajo" (no invertir)
ve_con_info = (probabilidad[0] * max(rendimiento_inversion[0], rendimiento_no_invertir[0]) +
               probabilidad[1] * max(rendimiento_inversion[1], rendimiento_no_invertir[1]))

# 4. Cálculo del VEIP
veip = ve_con_info - valor_esperado_sin_info

print(f"Valor Esperado sin info: ${valor_esperado_sin_info}")
print(f"Valor Esperado con info perfecta: ${ve_con_info}")
print(f"VEIP (Lo máximo a pagar por información): ${veip}")
