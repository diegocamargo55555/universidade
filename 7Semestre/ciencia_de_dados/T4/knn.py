import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def executar_knn(df):
    print("\n--- 4. KNN (K-Nearest Neighbors) ---")
    X = df[['IDADE', 'ANO_CHEGADA']]
    y = df['IS_SOLTEIRO']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    modelo = KNeighborsClassifier(n_neighbors=5)
    modelo.fit(X_train_scaled, y_train)
    y_pred = modelo.predict(X_test_scaled)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"Acurácia: {acc:.4f}")

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=['Outro', 'Solteiro'], yticklabels=['Outro', 'Solteiro'])
    plt.title(f'KNN (K=5): Matriz de Confusão\nAcurácia: {acc:.2%}')
    plt.ylabel('Real')
    plt.xlabel('Previsto')
    plt.tight_layout()
    plt.savefig('1knn_matriz.png')
    plt.close()
    print("Gráfico 'knn_matriz.png' salvo.")
