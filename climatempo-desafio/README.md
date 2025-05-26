# 🌡️ Desafio ClimaTempo – Modelagem de Fenômenos Naturais

## 📌 Descrição do Desafio

Este projeto tem como objetivo modelar dois fenômenos naturais descritos pela empresa ClimaTempo:

- **Onda de calor**: Representada pela função $ T(t) = 35 + (1 - e^{-t/27}) + t \cdot e^{-34.33t} $, onde $ t $ é o tempo em meses.
- **Movimentos anômalos da Terra**: Representados pela escala Richter $ e(x) = 5.47 + 1.85e^{-x}\cos(\sqrt{8}x - 19.47) + (x - 1.365)e^{-34.33x} $, onde $ x $ é a velocidade em m/s.

### Objetivos:
- Plotar os gráficos das funções nos intervalos especificados.
- Identificar os pontos máximos e mínimos de cada função.
- Apresentar os resultados de forma clara e organizada.

---

## 🔧 Implementação

Para cumprir o desafio, implementei as soluções utilizando a linguagem **Python**, com suporte das bibliotecas:

- `numpy`: Para cálculos matemáticos avançados.
- `matplotlib`: Para visualização dos gráficos.
- `pandas`: Para armazenamento e análise dos dados gerados.

### 🌡️ Função T(t): Temperatura ao longo dos meses

A função $ T(t) $ foi calculada para valores de $ t $ entre **0 e 36 meses** (3 anos), representando o período de até três anos.

#### Duas abordagens foram utilizadas:

##### 1. Com **laço `for`**
Iterei sobre os valores de 0 a 36 meses manualmente, calculando $ T(t) $ para cada instante e armazenando os resultados em listas. Essa abordagem é mais intuitiva e fácil de entender, especialmente para quem está começando.

```python
meses = []
valores_T = []

for t in range(0, 37):
    T = 35 + (1 - np.exp(-t / 27)) + t * np.exp(-34.33 * t)
    meses.append(t)
    valores_T.append(T)
```

##### 2. Com **DataFrame do `pandas`**
Os resultados foram armazenados em um DataFrame do pandas, facilitando a manipulação e análise posterior dos dados.

```python
df = pd.DataFrame({'t (meses)': meses, 'T(t)': valores_T})
```

Além disso, usei métodos práticos do pandas para identificar os valores máximos e mínimos:

```python
print(df[df['T(t)'] == df['T(t)'].min()])
print(df[df['T(t)'] == df['T(t)'].max()])
```

Essa abordagem é mais prática e eficiente para trabalhar com grandes conjuntos de dados ou análises futuras.

---

### 🌋 Função e(x): Escala Richter em função da velocidade

A função $ e(x) $ foi calculada para valores de $ x $ entre **0 e 5 m/s**, com uso de `np.linspace` para maior precisão na plotagem.

```python
x = np.linspace(0, 5, 1000)
e = 5.47 + 1.85 * np.exp(-x) * np.cos(np.sqrt(8) * x - 19.47) + (x - 1.365) * np.exp(-34.33 * x)
```

Da mesma forma, os valores foram armazenados em um DataFrame do `pandas` para melhor análise:

```python
df_e = pd.DataFrame({'x (m/s)': x, 'e(x)': e})
print("Mínimo de e(x):", df_e['e(x)'].min())
print("Máximo de e(x):", df_e['e(x)'].max())
```

---

## 📈 Resultados Gráficos

Foram gerados gráficos claros e legíveis para ambas as funções:

- **Gráfico de T(t)**: Mostra a evolução da temperatura ao longo dos meses.
- **Gráfico de e(x)**: Representa a variação da escala Richter com relação à velocidade.

Ambos possuem:
- Títulos descritivos
- Eixos nomeados
- Grades
- Layout ajustado para boa visualização

---

## 📝 Conclusão

Este projeto permitiu aplicar conceitos de programação, matemática e visualização de dados para resolver um problema real envolvendo fenômenos naturais. Ao utilizar duas abordagens distintas para calcular $ T(t) $ — uma com laço `for` e outra com `pandas` — foi possível demonstrar diferentes formas de resolver o mesmo problema, destacando a importância de escolher a abordagem mais adequada conforme o contexto.

✅ O resultado final atende todos os critérios do desafio:
- Implementação correta das funções matemáticas
- Plotagem precisa dos gráficos
- Identificação dos pontos máximos e mínimos
- Código bem estruturado e documentado
- Apresentação visual clara

---

## 📁 Estrutura do Projeto

```
climatempo-desafio/
│
├── README.md            # Este arquivo
├── main.py              # Código-fonte principal
├── grafico_Tt.png       # Gráfico da função T(t)
└── grafico_ex.png       # Gráfico da função e(x)
```
