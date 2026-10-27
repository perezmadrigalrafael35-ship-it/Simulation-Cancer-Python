import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 1. Definir la ecuación de Gompertz
def modelo_gompertz(N, t, r, K):
    dNdt = r * N * np.log(K / N)
    return dNdt

# 2. Parámetros del tumor
N0 = 10      # Células iniciales
K = 10000    # Capacidad de carga (tamaño máximo)
r = 0.5      # Tasa de crecimiento
t = np.linspace(0, 100, 100) # 100 días

# 3. Resolver la ecuación
solucion = odeint(modelo_gompertz, N0, t, args=(r, K))

# 4. Graficar
plt.plot(t, solucion, color='red', label='Crecimiento Tumoral')
plt.title('Simulacion de Crecimiento Tumoral (Gompertz)')
plt.xlabel('Dias')
plt.ylabel('Numero de Celulas')
plt.legend()
plt.grid(True)
plt.show()