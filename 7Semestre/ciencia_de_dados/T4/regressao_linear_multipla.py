import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def executar_regressao_multipla(df):
    print("\n--- 2. Regressão Linear Múltipla ---")
    X = df[['ANO_CHEGADA', 'ANO_REGISTRO']]
    y = df['IDADE']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    modelo = LinearRegression()
    modelo.fit(X_train_scaled, y_train)
    y_pred = modelo.predict(X_test_scaled)
    
    print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
    print(f"R²: {r2_score(y_test, y_pred):.4f}")

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, color='purple', alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.title('Regressão Múltipla: Valores Reais vs Previsões (Idade)')
    plt.xlabel('Idade Real')
    plt.ylabel('Idade Prevista')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('1regressao_multipla.png')
    plt.close()
    print("Gráfico 'regressao_multipla.png' salvo.")
