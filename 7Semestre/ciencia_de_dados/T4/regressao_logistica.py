import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def executar_regressao_logistica(df):
    print("\n--- 3. Regressão Logística ---")
    X = df[['IDADE']]
    y = df['IS_SOLTEIRO']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    modelo = LogisticRegression()
    modelo.fit(X_train_scaled, y_train)
    y_pred = modelo.predict(X_test_scaled)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"Acurácia: {acc:.4f}")

    X_test_sorted = np.sort(X_test['IDADE'].values)
    X_test_sorted_scaled = scaler.transform(X_test_sorted.reshape(-1, 1))
    probabilidades = modelo.predict_proba(X_test_sorted_scaled)[:, 1]

    plt.figure(figsize=(10, 6))
    plt.scatter(X_test['IDADE'], y_test, color='blue', alpha=0.1, label='Dados Reais (0=Não Solteiro, 1=Solteiro)')
    plt.plot(X_test_sorted, probabilidades, color='red', linewidth=2, label='Probabilidade de ser Solteiro')
    plt.title('Regressão Logística: Probabilidade de ser Solteiro por Idade')
    plt.xlabel('Idade')
    plt.ylabel('Probabilidade / Classe')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('1regressao_logistica_curva.png')
    plt.close()
    
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Outro', 'Solteiro'], yticklabels=['Outro', 'Solteiro'])
    plt.title('Regressão Logística: Matriz de Confusão')
    plt.ylabel('Real')
    plt.xlabel('Previsto')
    plt.savefig('1regressao_logistica_matriz.png')
    plt.close()
    print("Gráficos de Regressão Logística salvos.")
