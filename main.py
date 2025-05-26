import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#T(t) = 35 + (1 -e-t/27)+ te**-34,33t
#e(x) = 5,47 + 1,85e**x cos(√8x - 19,47)+(x - 1,365)e**-34,33x

# ----------------------------------------------------------
# PARTE 1 – Função T(t): Evolução da temperatura ao longo dos meses
# Fórmula: T(t) = 35 + (1 - e^(-t/27)) + t * e^(-34.33t)
# ----------------------------------------------------------

meses = []
valores_T = []

# Calcula T(t) para cada mês de 1 a 36
for t in range(1, 37):  # De 1 até 36 meses
    T = 35 + (1 - np.exp(-t / 27)) + t * np.exp(-34.33 * t)  # Aplica a fórmula
    meses.append(t)
    valores_T.append(T)

# Criação de um DataFrame para armazenar os valores calculados
df = pd.DataFrame({'t (meses)': meses, 'T(t)': valores_T})

# Impressão do menor e maior valor de T(t)
print("Valor mínimo de T(t):")
print(df[df['T(t)'] == df['T(t)'].min()])
print("Valor máximo de T(t):")
print(df[df['T(t)'] == df['T(t)'].max()])


# Gráfico da primeira função T(t)
# Após visualizar e comparar os valores impressos no console com o gráfico,
# feche a janela do gráfico para que a segunda parte do código (função e(x)) seja executada.
plt.figure(figsize=(10, 5))
plt.plot(df['t (meses)'], df['T(t)'], marker='o', linestyle='-', color='blue', label='T(t)')
plt.title('Gráfico de T(t) ao longo dos meses')
plt.xlabel('t (meses)')
plt.ylabel('T(t)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# ----------------------------------------------------------
# PARTE 2 – Função e(x): Energia em função da velocidade
# Fórmula: e(x) = 5.47 + 1.85 * e^(-x) * cos(√8 * x - 19.47) + (x - 1.365) * e^(-34.33 * x)
# ----------------------------------------------------------

# Gera 1000 valores de x igualmente espaçados entre 0 e 5 m/s
x = np.linspace(0, 5, 1000)

# Calcula e(x) aplicando a fórmula
e = (
    5.47 +
    1.85 * np.exp(-x) * np.cos(np.sqrt(8) * x - 19.47) +
    (x - 1.365) * np.exp(-34.33 * x)
)

# Cria DataFrame com os valores de x e e(x)
df_e = pd.DataFrame({'x (m/s)': x, 'e(x)': e})

# Exibe os valores mínimos e máximos de e(x)
print("Valor mínimo de e(x):")
print("Mínimo de e(x):", df_e['e(x)'].min())
print("Valor máximo de e(x):")
print("Máximo de e(x):", df_e['e(x)'].max())

plt.figure(figsize=(10, 5))
plt.plot(df_e['x (m/s)'], df_e['e(x)'], color='green', label='e(x)')
plt.title('Gráfico da velocidade e(x)')
plt.xlabel('x (m/s)')
plt.ylabel('e(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()