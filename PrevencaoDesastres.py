# Importar as bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Carregar os dados do sensoriamento remoto
# Os dados podem ser obtidos de fontes como drones, satélites ou sensores terrestres
# Os dados devem conter informações sobre variáveis ambientais e climáticas, como temperatura, umidade, precipitação, vento, etc.
# Os dados devem ter uma coluna que indique se houve ou não um desastre natural na região e qual o tipo (deslizamento, inundação, incêndio, etc.)
# Neste exemplo, vamos supor que os dados estão em um arquivo CSV chamado "dados.csv"
dados = pd.read_csv("dados.csv")

# Explorar os dados
# Verificar o tamanho, as colunas, os tipos e os valores ausentes dos dados
print(dados.shape)
print(dados.columns)
print(dados.info())
print(dados.isnull().sum())

# Visualizar os dados
# Fazer alguns gráficos para entender a distribuição e a relação entre as variáveis
# Por exemplo, podemos fazer um histograma para ver a frequência de cada tipo de desastre natural
dados["desastre"].value_counts().plot(kind="bar")
plt.xlabel("Tipo de desastre")
plt.ylabel("Frequência")
plt.show()

# Podemos também fazer um gráfico de dispersão para ver a relação entre duas variáveis, como temperatura e umidade
plt.scatter(dados["temperatura"], dados["umidade"], c=dados["desastre"])
plt.xlabel("Temperatura")
plt.ylabel("Umidade")
plt.legend()
plt.show()

# Preparar os dados
# Separar os dados em variáveis independentes (X) e dependente (y)
X = dados.drop("desastre", axis=1)
y = dados["desastre"]

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar os dados para ter uma escala comum
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Aplicar o algoritmo de aprendizado de máquina
# Escolher um algoritmo adequado para o problema de classificação multiclasse
# Neste exemplo, vamos usar a regressão logística, que é um algoritmo simples e eficiente
model = LogisticRegression(multi_class="multinomial")

# Treinar o modelo com os dados de treino
model.fit(X_train, y_train)

# Fazer previsões com os dados de teste
y_pred = model.predict(X_test)

# Avaliar o modelo
# Usar métricas como acurácia, precisão, recall e f1-score para medir o desempenho do modelo
print(classification_report(y_test, y_pred))

# Usar também uma matriz de confusão para ver onde o modelo acertou e errou
print(confusion_matrix(y_test, y_pred))
