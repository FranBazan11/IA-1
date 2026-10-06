import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# ==============================================================================
# 1. GENERACIÓN DE DATOS (Punto 3)
# ==============================================================================
# Fijamos la semilla para garantizar reproducibilidad exacta
np.random.seed(42)

# Generamos 23 puntos aleatorios con coordenadas (x, y) en el intervalo [0, 5]
NUM_TOTAL = 23
points = np.random.uniform(low=0.0, high=5.0, size=(NUM_TOTAL, 2))

# Visualización de los 23 puntos iniciales
plt.figure(figsize=(7, 5))
plt.scatter(
    points[:, 0],
    points[:, 1],
    color="steelblue",
    edgecolor="black",
    s=70,
    label="Puntos generados (23)",
)
plt.title(
    "Punto 3: Distribución inicial de 23 puntos aleatorios en $[0, 5]$",
    fontsize=12,
)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.xlim(-0.2, 5.2)
plt.ylim(-0.2, 5.2)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# ==============================================================================
# 2. IMPLEMENTACIÓN DE K-MEANS DESDE CERO (Punto 3.1)
# ==============================================================================
# Criterio de partición: tomamos los primeros 20 puntos para entrenamiento
# y reservamos los últimos 3 puntos para evaluación posterior.
X_train = points[:20]  # Puntos 0 a 19 (entrenamiento)
X_test = points[20:]  # Puntos 20 a 22 (no entrenados)


class CustomKMeans:

  def __init__(self, k=2, max_iter=100, tol=1e-4):
    self.k = k
    self.max_iter = max_iter
    self.tol = tol
    self.centroids = None
    self.labels = None

  def _euclidean_distance(self, a, b):
    """Calcula la distancia euclídea entre cada punto de A y cada punto de B."""
    # a: (N, 2), b: (K, 2) -> broadcasting resulta en matriz de distancias (N, K)
    return np.linalg.norm(a[:, np.newaxis, :] - b[np.newaxis, :, :], axis=2)

  def fit(self, X):
    # Paso 1: Inicialización de centroides
    # Seleccionamos k puntos aleatorios del propio conjunto de datos
    random_idx = np.random.choice(len(X), size=self.k, replace=False)
    self.centroids = X[random_idx].copy()

    for iteration in range(self.max_iter):
      # Paso 2: Asignación de clústeres
      # Cada punto se asigna al centroide con menor distancia euclídea
      distances = self._euclidean_distance(X, self.centroids)
      self.labels = np.argmin(distances, axis=1)

      # Paso 3: Recálculo de centroides
      # El nuevo centroide es la media aritmética de los puntos asignados
      new_centroids = np.zeros_like(self.centroids)
      for cluster_id in range(self.k):
        cluster_points = X[self.labels == cluster_id]
        if len(cluster_points) > 0:
          new_centroids[cluster_id] = cluster_points.mean(axis=0)
        else:
          # Manejo de clúster vacío: reasignar a un punto aleatorio
          new_centroids[cluster_id] = X[np.random.choice(len(X))]

      # Paso 4: Criterio de parada (convergencia)
      # Si el desplazamiento de los centroides es menor a la tolerancia, detenemos
      shift = np.linalg.norm(new_centroids - self.centroids)
      if shift < self.tol:
        print(f"Convergencia alcanzada en la iteración {iteration + 1}.")
        self.centroids = new_centroids
        break

      self.centroids = new_centroids

    return self

  def predict(self, X):
    """Asigna nuevos puntos al clúster más cercano según los centroides aprendidos."""
    distances = self._euclidean_distance(X, self.centroids)
    return np.argmin(distances, axis=1)


# Instanciamos y entrenamos el modelo sobre los 20 puntos
kmeans_scratch = CustomKMeans(k=2, max_iter=100)
kmeans_scratch.fit(X_train)

# Predecimos la pertenencia de los 3 puntos restantes
test_labels = kmeans_scratch.predict(X_test)

# ==============================================================================
# 3. VISUALIZACIÓN FINAL DEL AGRUPAMIENTO
# ==============================================================================
plt.figure(figsize=(8, 6))

colors = ["#2b5c8f", "#d95f02"]  # Azul y Naranja contrastantes
cluster_names = ["Clúster 0", "Clúster 1"]

# Graficamos los 20 puntos de entrenamiento por clúster
for c in range(2):
  mask = kmeans_scratch.labels == c
  plt.scatter(
    X_train[mask, 0],
    X_train[mask, 1],
    c=colors[c],
    edgecolor="black",
    s=80,
    label=f"Puntos {cluster_names[c]} (N={mask.sum()})",
  )

# Graficamos la posición final de los centroides
plt.scatter(
  kmeans_scratch.centroids[:, 0],
  kmeans_scratch.centroids[:, 1],
  c="yellow",
  edgecolor="black",
  marker="*",
  s=320,
  linewidths=1.5,
  label="Centroides finales",
  zorder=5,
)

# Graficamos los 3 puntos no incluidos en el entrenamiento
plt.scatter(
  X_test[:, 0],
  X_test[:, 1],
  c="lightgray",
  edgecolor="crimson",
  linewidths=2,
  s=110,
  marker="s",
  label="3 Puntos fuera de entrenamiento (Test)",
  zorder=4,
)

# Líneas guía discontinuas desde los puntos test hacia su centroide asignado
for i, pt in enumerate(X_test):
  assigned_cluster = test_labels[i]
  centroid = kmeans_scratch.centroids[assigned_cluster]
  plt.plot(
    [pt[0], centroid[0]],
    [pt[1], centroid[1]],
    linestyle=":",
    color="crimson",
    alpha=0.8,
  )

plt.title("Punto 3.1: Agrupamiento K-Means ($k=2$) y Puntos no entrenados")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.xlim(-0.2, 5.2)
plt.ylim(-0.2, 5.2)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper right")
plt.tight_layout()
plt.show()

# ==============================================================================
# 4. COMPARACIÓN BREVE CON SCIKIT-LEARN
# ==============================================================================
# Usamos init='random' y n_init=1 con la misma semilla para contrastar directamente
sk_kmeans = KMeans(n_clusters=2, init="random", n_init=1, random_state=42)
sk_kmeans.fit(X_train)

print("--- Comparación de Centroides ---")
print("Centroides (Desde Cero):\n", np.round(kmeans_scratch.centroids, 4))
print("Centroides (scikit-learn):\n", np.round(sk_kmeans.cluster_centers_, 4))