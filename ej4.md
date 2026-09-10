## Enunciado Ejercicio N°4 
4. Cada día se procesa un producto en secuencia en dos máquinas, M1 y M2. Una inspección se realiza después de que una unidad del producto se completa en cualquiera de las máquinas. 
<br><br>Hay un 5% de probabilidades de que una unidad sea desechada antes de inspeccionarla. Después de la inspección, hay un 3% de probabilidades de que la unidad sea desechada y un 7% de probabilidades de ser devuelta a la misma máquina para trabajarla
de nuevo. Si una unidad pasa la inspección en ambas máquinas es
buena.

        4.1 Dibuje la cadena de Markov que representa este problema y describa para cada estado si es transitorio, recurrente, o absorbente.

        4.2 Arme la matriz de transición

        4.3 Calcule la probabilidad de que una pieza que inicia el proceso en la máquina M1 sea desechada.

        4.4 Calcule la probabilidad de que una pieza de la máquina M2 sea terminada.

        4.5 Si los tiempos de procesamiento en las máquinas M1 y M2 son respectivamente de 20 y 30 minutos y los tiempos de inspección son respectivamente de 5 y 7 minutos, ¿cuánto tiempo tarda en ser procesada una pieza que inicia en la máquina M1?



## Resolución del Ejercicio Nro. 4: Cadenas de Markov Absorbentes

## Modelado y Corrección Conceptual

El modelo correcto para este problema consta de **6 estados** diferenciados:
* En cada máquina ($M_i$), la pieza tiene:
  * Probabilidad de descarte antes de inspección: $0.05$.
  * Probabilidad de avanzar a la inspección ($I_i$): $0.95$.
* En cada inspección ($I_i$), la pieza tiene:
  * Probabilidad de descarte: $0.03$.
  * Probabilidad de retrabajo (retorno a $M_i$): $0.07$.
  * Probabilidad de aprobación / avance: $1 - (0.03 + 0.07) = 0.90$.



## 4.1. Cadena de Markov y Clasificación de Estados

### Espacio de Estados
$$S = \{M_1, I_1, M_2, I_2, D, T\}$$

### Clasificación de Estados
* **$M_1$ (Procesamiento en Máquina 1):** Estado **transitorio**. La unidad sale hacia $I_1$ o es desechada a $D$.
* **$I_1$ (Inspección de Máquina 1):** Estado **transitorio**. La unidad puede ser devuelta a $M_1$, avanzar a $M_2$ o ir a $D$.
* **$M_2$ (Procesamiento en Máquina 2):** Estado **transitorio**. La unidad avanza a $I_2$ o es desechada a $D$.
* **$I_2$ (Inspección de Máquina 2):** Estado **transitorio**. La unidad puede retornar a $M_2$, completarse con éxito en $T$ o ir a $D$.
* **$D$ (Desechada / Scrap):** Estado **absorbente** (y recurrente). Una vez en este estado, la probabilidad de permanecer en él es $p_{DD} = 1.0$.
* **$T$ (Terminada / Buena):** Estado **absorbente** (y recurrente). Representa el producto final terminado con éxito ($p_{TT} = 1.0$).

### Diagrama de Transición de Estados

```text
       +---(0.07)---+             +---(0.07)---+
       |            |             |            |
       v   (0.95)   |             v   (0.95)   |
     [M1] -------> [I1] -------> [M2] -------> [I2] -------> [T] (1.0)
       |            |   (0.90)     |            |   (0.90)
(0.05) |            | (0.03) (0.05)|            | (0.03)
       +---------> [D] <-----------+------------+
                   (1.0)
```


## 4.2. Matriz de Transición ($P$)

Se define la matriz en **forma canónica** ordenando primero los 4 estados transitorios $\{M_1, I_1, M_2, I_2\}$ y luego los 2 estados absorbentes $\{D, T\}$:

$$P = \begin{pmatrix} Q & R \\ 0 & I \end{pmatrix}$$

$$P = \begin{pmatrix}
0.00 & 0.95 & 0.00 & 0.00 & \big| & 0.05 & 0.00 \\
0.07 & 0.00 & 0.90 & 0.00 & \big| & 0.03 & 0.00 \\
0.00 & 0.00 & 0.00 & 0.95 & \big| & 0.05 & 0.00 \\
0.00 & 0.00 & 0.07 & 0.00 & \big| & 0.03 & 0.90 \\
\hline
0.00 & 0.00 & 0.00 & 0.00 & \big| & 1.00 & 0.00 \\
0.00 & 0.00 & 0.00 & 0.00 & \big| & 0.00 & 1.00
\end{pmatrix}$$

### Submatrices

* **Submatriz $Q$ (transición entre estados transitorios):**
$$Q = \begin{pmatrix}
0.00 & 0.95 & 0.00 & 0.00 \\
0.07 & 0.00 & 0.90 & 0.00 \\
0.00 & 0.00 & 0.00 & 0.95 \\
0.00 & 0.00 & 0.07 & 0.00
\end{pmatrix}$$

* **Submatriz $R$ (transición desde estados transitorios a absorbentes):**
$$R = \begin{pmatrix}
0.05 & 0.00 \\
0.03 & 0.00 \\
0.05 & 0.00 \\
0.03 & 0.90
\end{pmatrix}$$



## 4.3. Probabilidad de que una pieza que inicia en $M_1$ sea Desechada

### 1. Matriz Fundamental $N = (I - Q)^{-1}$

Calculamos $I - Q$:
$$I - Q = \begin{pmatrix}
1.00 & -0.95 & 0.00 & 0.00 \\
-0.07 & 1.00 & -0.90 & 0.00 \\
0.00 & 0.00 & 1.00 & -0.95 \\
0.00 & 0.00 & -0.07 & 1.00
\end{pmatrix}$$

Dado que cada ciclo de máquina-inspección tiene un factor determinante:
$$\Delta = 1 - (0.95 \times 0.07) = 1 - 0.0665 = 0.9335$$

La inversa resulta:
$$N = (I - Q)^{-1} \approx \begin{pmatrix}
1.0712 & 1.0177 & 0.9812 & 0.9321 \\
0.0750 & 1.0712 & 1.0328 & 0.9812 \\
0.0000 & 0.0000 & 1.0712 & 1.0177 \\
0.0000 & 0.0000 & 0.0750 & 1.0712
\end{pmatrix}$$

*Interpretación de la fila 1:* Una pieza que arranca en $M_1$ pasa en promedio:
* $1.0712$ veces por $M_1$
* $1.0177$ veces por $I_1$
* $0.9812$ veces por $M_2$
* $0.9321$ veces por $I_2$

### 2. Matriz de Probabilidades de Absorción $B = N \cdot R$

$$B = \begin{pmatrix}
1.0712 & 1.0177 & 0.9812 & 0.9321 \\
0.0750 & 1.0712 & 1.0328 & 0.9812 \\
0.0000 & 0.0000 & 1.0712 & 1.0177 \\
0.0000 & 0.0000 & 0.0750 & 1.0712
\end{pmatrix}
\begin{pmatrix}
0.05 & 0.00 \\
0.03 & 0.00 \\
0.05 & 0.00 \\
0.03 & 0.90
\end{pmatrix}$$

Multiplicando fila por columna:
* Para inicio en $M_1$:
  $$B_{M_1, D} = (1.0712 \times 0.05) + (1.0177 \times 0.03) + (0.9812 \times 0.05) + (0.9321 \times 0.03) = 0.1611$$
  $$B_{M_1, T} = 0.9321 \times 0.90 = 0.8389$$

* Para inicio en $M_2$:
  $$B_{M_2, D} = (1.0712 \times 0.05) + (1.0177 \times 0.03) = 0.0841$$
  $$B_{M_2, T} = 1.0177 \times 0.90 = 0.9159$$

Matriz completa:
$$B \approx \begin{pmatrix}
0.1611 & 0.8389 \\
0.1170 & 0.8830 \\
0.0841 & 0.9159 \\
0.0359 & 0.9641
\end{pmatrix}
\begin{array}{l}
(M_1) \\ (I_1) \\ (M_2) \\ (I_2)
\end{array}$$

**Respuesta:** La probabilidad de que una pieza que inicia en la máquina $M_1$ sea desechada es:
$$P(\text{Desechada} \mid M_1) = \mathbf{0.1611 \quad (16.11\%)}$$



## 4.4. Probabilidad de que una pieza de la máquina $M_2$ sea Terminada

Tomando la fila correspondiente a $M_2$ y la columna del estado absorbente $T$ en la matriz $B$:
$$B_{M_2, T} = 1.0177 \times 0.90 = \mathbf{0.9159 \quad (91.59\%)}$$

**Respuesta:** La probabilidad de que una pieza que está en la máquina $M_2$ termine exitosamente el proceso es de **$91.59\%$**.



## 4.5. Tiempo Total Esperado de Procesamiento desde $M_1$

### Vector de Tiempos Unitarios por Estado ($\tau$)
* $t_{M_1} = 20\text{ minutos}$
* $t_{I_1} = 5\text{ minutos}$
* $t_{M_2} = 30\text{ minutos}$
* $t_{I_2} = 7\text{ minutos}$

$$\tau = \begin{pmatrix} 20 \\ 5 \\ 30 \\ 7 \end{pmatrix}$$

### Tiempo Medio Esperado
El vector de tiempos esperados de permanencia hasta la absorción es $T = N \cdot \tau$. Para una pieza que inicia en $M_1$ (primera componente):

$$T_{M_1} = (N)_{1, \bullet} \cdot \tau$$
$$T_{M_1} = (1.0712 \times 20) + (1.0177 \times 5) + (0.9812 \times 30) + (0.9321 \times 7)$$
$$T_{M_1} = 21.424 + 5.0885 + 29.436 + 6.5247 = \mathbf{62.47\text{ minutos}}$$

**Respuesta:** El tiempo medio esperado que tarda en ser procesada una pieza que inicia en $M_1$ (hasta salir por desecho o ser aprobada) es de **$62.47$ minutos** (aproximadamente **1 hora, 2 minutos y 28 segundos**).


