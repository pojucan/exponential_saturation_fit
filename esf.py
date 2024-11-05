import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import least_squares

# Função do modelo capacitivo:
def modelo_exponencial_saturacao(t, A, t0):
    return A * (1 - np.exp(-t / t0))

# Função de erro que calcula a diferença entre o modelo e os dados reais
def erro(parametros, t, y):
    A, t0 = parametros
    return modelo_exponencial_saturacao(t, A, t0) - y

# Constante de tempo inicial:
t0_inicial = 3  

# Geração de dados para a escala de tempo (t) de 0 a 15 com passo de 100:
t = np.linspace(0, 15, 100)  

# Leitura do arquivo .csv do ensaio de absorção (limitando à 31 linhas e utilizando ponto como decimal):
# file_path = 'arquivo_com_dados_reais.csv'
file_path = 'dados_sinteticos.csv'
data = pd.read_csv(file_path, delimiter = ',', nrows = 31)

print(data)

# Extraindo a primeira coluna como eixo X:
x_real = data.iloc[:, 0]

# Lista de cores definidas para cada coluna:
colors = ['black', 'blue', 'green', 'orange']

# Traçar todas as colunas restantes como eixo Y:
plt.figure(figsize=(10, 5))

# Traçar todas as colunas (exceto a primeira que é o eixo X)
for i in range(1, data.shape[1]):  
    # Usa o nome da coluna para a legenda:
    plt.scatter(x_real, data.iloc[:, i], label=f'{data.columns[i]}', color = colors[i-1], s = 100)  

# Configurações do gráfico para traçar:
plt.xlabel('Tempo (t)', fontsize = 14, fontweight = 'bold')
plt.ylabel('Variação de Massa [%]', fontsize=14, fontweight = 'bold')
plt.xticks(fontsize = 12, fontweight = 'bold') 
plt.yticks(fontsize = 12, fontweight = 'bold')
plt.legend(fontsize = 10, loc = 'best')
plt.grid()
plt.show()

# Escolha de uma coluna específica para fazer o ajuste de curva:
coluna_escolhida = data.columns[3]

# Extração os dados da coluna escolhida:
y_real = data[coluna_escolhida] 

# Definição automática do valor máximo de A:
A_inicial = y_real.max()

# Parâmetros iniciais
parametros_iniciais = [A_inicial, t0_inicial]

# Ajuste dos parâmetros usando least_squares
result = least_squares(erro, parametros_iniciais, args=(x_real, y_real), method='trf')

# Extraindo os valores de A e t0 ajustados a partir do resultado do ajuste
A_ajustado, t0_ajustado = result.x

# Geração de dados ajustados com os parâmetros encontrados
y_ajustado = modelo_exponencial_saturacao(t, A_ajustado, t0_ajustado)

# Traçar os dados brutos e o ajuste
plt.figure(figsize=(10, 5))

# Traçar a coluna escolhida
plt.scatter(x_real, y_real, label=f'Dados Brutos: {coluna_escolhida}', color='green', s=100)

# Traçar a curva ajustada
plt.plot(t, y_ajustado, label=f'Ajuste: A = {A_ajustado:.2f}, t0 = {t0_ajustado:.2f}', color='red')

# Configurações do gráfico
plt.xlabel('Tempo (t)', fontsize=14, fontweight='bold')
plt.ylabel('Variação de Massa [%]', fontsize=14, fontweight='bold')
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
plt.legend(fontsize=12, loc='best')
plt.grid()
plt.show()

# Exibir os parâmetros ajustados e o relatório completo do ajuste
print(f"Parâmetros ajustados: A = {A_ajustado:.2f}, t0 = {t0_ajustado:.2f}")
print("\nRelatório de Otimização:")
print(f"Status de Convergência: {result.status}")
print(f"Mensagem de Otimização: {result.message}")
print(f"Erro final (custo): {result.cost:.4f}")
print(f"Número de Iterações: {result.nfev}")
print(f"Jacobian (última iteração):\n{result.jac}")
print(f"Covariância Estimada dos Parâmetros:\n{result.jac.T @ result.jac}")
