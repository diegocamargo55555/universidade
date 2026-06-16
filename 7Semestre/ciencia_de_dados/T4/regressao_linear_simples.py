import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def executar_regressao_simples(df):
    print("\n--- 1. Regressão Linear Simples ---")
    X = df[['ANO_CHEGADA']]
    y = df['IDADE']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    
    print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
    print(f"R²: {r2_score(y_test, y_pred):.4f}")

    plt.figure(figsize=(10, 6))
    plt.scatter(X_test, y_test, color='blue', alpha=0.5, label='Dados Reais')
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Linha de Regressão')
    plt.title('Regressão Linear Simples: Idade vs Ano de Chegada')
    plt.xlabel('Ano de Chegada')
    plt.ylabel('Idade')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('1regressao_linear_simples.png')
    plt.close()
    print("Gráfico 'regressao_linear_simples.png' salvo.")
