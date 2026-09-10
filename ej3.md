## Enunciado Ejercicio N°3

3. La probabilidad de que un motor que sale de una fábrica con una *avería eléctrica* es de $10^{-3}$, y la probabilidad de que salga con una *avería mecánica* es de $10^{-5}$. Si existe un tipo de avería no se producen averías del otro tipo.
<br><br>Si el motor presenta *temperatura elevada* se enciende un *piloto luminoso* el 95% de las veces, cuando la *temperatura es reducida* el *piloto luminoso* se enciende el 99% de las veces, y a veces cuando la *temperatura se encuentra en un rango normal* el *piloto luminoso* se enciende erróneamente en un caso por millón.
<br><br>Cuando *no hay averías*, la *temperatura se eleva* en el 17% de los casos y es *reducida* el 5% de las veces. Si hay una *avería eléctrica*, la *temperatura se eleva* en el 90% de los casos y es *reducida* en el 1% de los casos. Finalmente cuando la *avería es mecánica*, la *temperatura está elevada* el 10% de los casos y *reducida* el 40% de las veces.
<br><br>Construya una Red Bayesiana y utilice inferencia por enumeración para calcular:

        3.1 La probabilidad de que el motor tenga una avería mecánica si se enciende el piloto.

        3.2 La probabilidad de que el motor tenga una avería mecánica si se enciende el piloto y la temperatura es elevada.

        # Resolución del Ejercicio Nro. 3: Red Bayesiana e Inferencia por Enumeración

## Resolución Ejericio N°3:
## 1. Construcción de la Red Bayesiana

### Nodos y Espacio de Estados
Se definen tres variables aleatorias discretas para modelar el sistema:

1. **Avería ($A$)**: Estado del motor respecto a fallas de fabricación.
   * $A = n$: Ninguna avería.
   * $A = e$: Avería eléctrica.
   * $A = m$: Avería mecánica.
   *(Los estados son mutuamente excluyentes y exhaustivos).*

2. **Temperatura ($T$)**: Estado térmico del motor.
   * $T = e$: Temperatura elevada.
   * $T = r$: Temperatura reducida.
   * $T = n$: Temperatura normal.

3. **Piloto Luminoso ($L$)**: Estado del indicador luminoso.
   * $L = 1$: Piloto encendido.
   * $L = 0$: Piloto apagado.



### Topología del Grafo Acíclico Dirigido (DAG)
La relación causal del sistema sigue una estructura en cadena:
* El tipo de **Avería ($A$)** altera la distribución de la **Temperatura ($T$)**.
* La **Temperatura ($T$)** condiciona la activación del **Piloto Luminoso ($L$)**.

$$A \longrightarrow T \longrightarrow L$$



### Tablas de Probabilidad Condicional (CPT)

#### 1. Distribución a Priori $P(A)$
A partir de $P(A = e) = 10^{-3} = 0.001$ y $P(A = m) = 10^{-5} = 0.00001$:

$$P(A = n) = 1 - 0.001 - 0.00001 = 0.99899$$

| Estado de $A$ | $P(A)$ |
| :--- | :--- |
| **$n$ (Ninguna)** | $0.99899$ |
| **$e$ (Eléctrica)** | $0.00100$ |
| **$m$ (Mecánica)** | $0.00001$ |

#### 2. Probabilidad Condicional $P(T \mid A)$
* **Sin avería ($A = n$):** $P(T=e \mid n) = 0.17$, $P(T=r \mid n) = 0.05 \implies P(T=n \mid n) = 1 - 0.17 - 0.05 = 0.78$.
* **Avería Eléctrica ($A = e$):** $P(T=e \mid e) = 0.90$, $P(T=r \mid e) = 0.01 \implies P(T=n \mid e) = 1 - 0.90 - 0.01 = 0.09$.
* **Avería Mecánica ($A = m$):** $P(T=e \mid m) = 0.10$, $P(T=r \mid m) = 0.40 \implies P(T=n \mid m) = 1 - 0.10 - 0.40 = 0.50$.

| $A$ | $P(T = e \mid A)$ | $P(T = r \mid A)$ | $P(T = n \mid A)$ |
| :--- | :---: | :---: | :---: |
| **$n$ (Ninguna)** | $0.17$ | $0.05$ | $0.78$ |
| **$e$ (Eléctrica)** | $0.90$ | $0.01$ | $0.09$ |
| **$m$ (Mecánica)** | $0.10$ | $0.40$ | $0.50$ |

#### 3. Probabilidad Condicional $P(L \mid T)$
* **Temperatura Elevada ($T = e$):** $P(L=1 \mid e) = 0.95 \implies P(L=0 \mid e) = 0.05$.
* **Temperatura Reducida ($T = r$):** $P(L=1 \mid r) = 0.99 \implies P(L=0 \mid r) = 0.01$.
* **Temperatura Normal ($T = n$):** $P(L=1 \mid n) = 10^{-6} = 0.000001 \implies P(L=0 \mid n) = 1 - 10^{-6} = 0.999999$.

| $T$ | $P(L = 1 \mid T)$ | $P(L = 0 \mid T)$ |
| :--- | :---: | :---: |
| **$e$ (Elevada)** | $0.95$ | $0.05$ |
| **$r$ (Reducida)** | $0.99$ | $0.01$ |
| **$n$ (Normal)** | $10^{-6}$ | $1 - 10^{-6}$ |



## Factorización de la Distribución Conjunta
Por la regla de la cadena para redes bayesianas:

$$P(A, T, L) = P(A) \cdot P(T \mid A) \cdot P(L \mid T)$$



## 3.1. Probabilidad de Avería Mecánica si se Enciende el Piloto: $P(A = m \mid L = 1)$

Aplicando el algoritmo de inferencia por enumeración, la variable oculta a marginalizar es $T \in \{e, r, n\}$:

$$P(A = a \mid L = 1) = \alpha \cdot P(A = a, L = 1) = \alpha \sum_{t \in \{e, r, n\}} P(A = a) \cdot P(T = t \mid A = a) \cdot P(L = 1 \mid T = t)$$

Donde $\alpha = \frac{1}{P(L = 1)}$ representa la constante de normalización.

### Términos de la distribución no normalizada

1. **Para $A = m$ (Avería Mecánica):**
   $$P(A = m, L = 1) = P(A = m) \sum_{t} P(T = t \mid m) \cdot P(L = 1 \mid t)$$
   $$P(A = m, L = 1) = 10^{-5} \cdot \left[ (0.10 \times 0.95) + (0.40 \times 0.99) + (0.50 \times 10^{-6}) \right]$$
   $$P(A = m, L = 1) = 10^{-5} \cdot [0.095 + 0.396 + 0.0000005] = 10^{-5} \times 0.4910005 = 4.910005 \times 10^{-6}$$

2. **Para $A = e$ (Avería Eléctrica):**
   $$P(A = e, L = 1) = P(A = e) \sum_{t} P(T = t \mid e) \cdot P(L = 1 \mid t)$$
   $$P(A = e, L = 1) = 10^{-3} \cdot \left[ (0.90 \times 0.95) + (0.01 \times 0.99) + (0.09 \times 10^{-6}) \right]$$
   $$P(A = e, L = 1) = 10^{-3} \cdot [0.855 + 0.0099 + 0.00000009] = 10^{-3} \times 0.86490009 = 8.6490009 \times 10^{-4}$$

3. **Para $A = n$ (Sin Avería):**
   $$P(A = n, L = 1) = P(A = n) \sum_{t} P(T = t \mid n) \cdot P(L = 1 \mid t)$$
   $$P(A = n, L = 1) = 0.99899 \cdot \left[ (0.17 \times 0.95) + (0.05 \times 0.99) + (0.78 \times 10^{-6}) \right]$$
   $$P(A = n, L = 1) = 0.99899 \cdot [0.1615 + 0.0495 + 0.00000078] = 0.99899 \times 0.21100078 = 0.2107876692$$

### Normalización
La probabilidad total de que el piloto esté encendido ($P(L = 1)$) es la suma de los tres casos:

$$P(L = 1) = (4.910005 \times 10^{-6}) + (8.6490009 \times 10^{-4}) + 0.2107876692 = 0.2116574793$$

Calculando la probabilidad a posteriori:

$$P(A = m \mid L = 1) = \frac{P(A = m, L = 1)}{P(L = 1)} = \frac{4.910005 \times 10^{-6}}{0.2116574793} \approx 2.3198 \times 10^{-5}$$

$$P(A = m \mid L = 1) \approx 0.00232\%$$


## 3.2. Probabilidad de Avería Mecánica si se Enciende el Piloto y la Temperatura es Elevada: $P(A = m \mid L = 1, T = e)$

### Simplificación por Independencia Condicional
Por las propiedades de d-separación en la red ($A \to T \to L$), la variable $L$ es condicionalmente independiente de $A$ dado $T$:

$$P(A = m \mid L = 1, T = e) = P(A = m \mid T = e)$$

Demostración por definición formal mediante enumeración sin variables ocultas:

$$P(A = a, T = e, L = 1) = P(A = a) \cdot P(T = e \mid A = a) \cdot P(L = 1 \mid T = e)$$

Dado que el factor $P(L = 1 \mid T = e) = 0.95$ es constante e idéntico para todos los valores de $A$, se cancela algebraicamente en el cociente de normalización.

### Términos de la distribución no normalizada

1. **Para $A = m$:**
   $$P(A = m, T = e, L = 1) = 10^{-5} \times 0.10 \times 0.95 = 9.50 \times 10^{-7}$$

2. **Para $A = e$:**
   $$P(A = e, T = e, L = 1) = 10^{-3} \times 0.90 \times 0.95 = 8.55 \times 10^{-4}$$

3. **Para $A = n$:**
   $$P(A = n, T = e, L = 1) = 0.99899 \times 0.17 \times 0.95 = 0.161336885$$

### Normalización
Sumando los valores para obtener la evidencia conjunta $P(T = e, L = 1)$:

$$P(T = e, L = 1) = (9.50 \times 10^{-7}) + (8.55 \times 10^{-4}) + 0.161336885 = 0.162192835$$

Calculando la probabilidad a posteriori:

$$P(A = m \mid L = 1, T = e) = \frac{9.50 \times 10^{-7}}{0.162192835} \approx 5.8572 \times 10^{-6}$$

$$P(A = m \mid L = 1, T = e) \approx 0.000586\%$$



## Resultados Consolidados

| Parámetro / Pregunta | Expresión Analítica | Notación Científica | Porcentaje |
| :--- | :--- | :---: | :---: |
| **Probabilidad de encendido del piloto** | $P(L = 1)$ | $0.211657$ | $21.17\%$ |
| **3.1 Avería mecánica con piloto encendido** | $P(A = m \mid L = 1)$ | $2.3198 \times 10^{-5}$ | **$0.00232\%$** |
| **3.2 Avería mecánica con piloto y $T$ elevada** | $P(A = m \mid L = 1, T = e)$ | $5.8572 \times 10^{-6}$ | **$0.000586\%$** |