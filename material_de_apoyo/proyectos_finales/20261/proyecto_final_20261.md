# Proyecto Final 2026-1 — Análisis y Diseño de Algoritmos

> 📌 **Material de referencia de un semestre anterior (2026-1).** Este no es el proyecto final vigente de tu semestre — revísalo para hacerte una idea del formato, alcance y rúbrica que suele tener el proyecto final del curso.

## 🧭 Práctica Integradora: Rutas Óptimas y Seguras en Medellín

### 🎯 Objetivo general

Diseñar e implementar un sistema que permita calcular y visualizar rutas óptimas entre dos puntos de la ciudad de Medellín, considerando simultáneamente la distancia y el riesgo de acoso o inseguridad. El sistema debe ofrecer al usuario distintas estrategias algorítmicas y permitir la configuración de preferencias (prioridad por seguridad o rapidez), con el fin de comparar precisión, tiempo de cómputo y comportamiento de los algoritmos.

### 🧩 Contexto

Se proporciona un dataset geográfico que describe la red vial de Medellín: [`calles_de_medellin_con_acoso.csv`](./calles_de_medellin_con_acoso.csv) (en esta misma carpeta). Cada registro corresponde a un tramo de calle con los siguientes campos:

| Campo | Descripción |
|---|---|
| `name` | Nombre de la calle o segmento. |
| `origin` | Coordenadas geográficas del punto de inicio (long, lat). |
| `destination` | Coordenadas geográficas del punto final (long, lat). |
| `length` | Longitud del tramo (en metros). |
| `oneway` | Indica si la vía es unidireccional. |
| `harassmentRisk` | Valor entre 0 y 1 que indica el nivel de riesgo percibido. |
| `geometry` | Representación geométrica LINESTRING del tramo. |

A partir de estos datos, se debe construir un grafo dirigido y ponderado, donde cada arista tenga un costo definido por:

```
C(e) = α × length(e) + β × harassmentRisk(e)
```

donde `α` y `β` son pesos ajustables definidos por el usuario según su preferencia entre rapidez y seguridad.

### 🧠 Descripción del reto

El estudiante o grupo deberá:

1. **Modelar el grafo vial de Medellín** a partir del dataset proporcionado. Cada nodo representará un punto geográfico, y cada arista, un tramo de calle.
2. **Implementar dos algoritmos diferentes.** Algunas posibilidades son:
   - Dijkstra.
   - Bellman-Ford.
   - A*.
   - Greedy por vecino más cercano.
   - Backtracking con poda.
   - BFS/DFS adaptado a costos.
   - Algoritmo propio justificado.

   > **Nota:** No basta con llamar a una función de librería que resuelva todo el problema. Pueden usar librerías para carga, visualización o manipulación de datos, pero la lógica principal de los algoritmos debe ser implementada por el equipo.

3. **Permitir la personalización de la heurística:**
   - El usuario podrá ajustar los valores de `α` y `β`.
   - También podrá elegir si desea minimizar riesgo, minimizar distancia, o buscar un balance entre ambos.
4. **Medir y comparar el rendimiento de los algoritmos:**
   - Tiempo de ejecución total.
   - Número de nodos explorados.
   - Costo total de la ruta obtenida.
   - Comportamiento ante distintos valores de `(α, β)`.
5. **Visualizar los resultados sobre un mapa interactivo de Medellín**, donde:
   - Se destaquen las rutas generadas por cada algoritmo con colores diferenciados.
   - Se muestren los puntos de inicio, destino y las métricas relevantes.
   - Se permita interpretar visualmente la diferencia entre rutas seguras y rápidas.

### 🧮 Aspectos de diseño y análisis esperados

- Modelado correcto del grafo y justificación de las estructuras de datos elegidas.
- Análisis de complejidad temporal y espacial de cada algoritmo.
- Discusión alrededor de las técnicas de algoritmia usadas para la implementación.
- Comparación experimental con resultados medibles.
- Discusión de trade-offs entre precisión, tiempo, escalabilidad y facilidad de implementación.
- Integración de conceptos de análisis de algoritmos vistos en clase: complejidad, eficiencia, diseño recursivo, heurísticas y optimización.

### 🗺️ Sugerencias de herramientas

| Propósito | Librerías sugeridas |
|---|---|
| Manejo de datos geoespaciales | `geopandas`, `shapely`, `pandas` |
| Visualización geográfica | `folium`, `contextily`, `plotly.express`, `matplotlib` |
| Modelado de grafos | `networkx` (opcional) o implementación propia |
| Medición de rendimiento | `time`, `timeit`, `perf_counter` |

### 📦 Entregables

1. **Prototipo funcional** (entregable principal de código):
   - Implementación completa del sistema de rutas.
   - Interfaz simple con opciones de configuración (`α`, `β`, algoritmos a comparar).
   - Visualización del mapa de Medellín con rutas comparadas.
   - Archivo/interfaz de resultados experimentales (tabla o gráfico).
2. **Presentación y sustentación técnica:**
   - Exposición (máximo 30 minutos).
   - Debe incluir explicación detallada de los algoritmos implementados, análisis de complejidad, justificación de las técnicas aplicadas y análisis comparativo.

### 🧾 Rúbrica de evaluación

**1️⃣ Prototipo funcional — 40%**

| Subcomponente | Descripción | Peso |
|---|---|---|
| Modelado del grafo | Representación adecuada de la red vial, manejo correcto de pesos y direccionalidad. | 10% |
| Implementación de algoritmos | Correctitud, completitud y coherencia en la implementación de los algoritmos seleccionados. | 10% |
| Comparación funcional entre algoritmos | Evidencia experimental (tiempos, precisión, nodos explorados, variación con α/β). | 10% |
| Visualización geográfica | Claridad e interpretación visual de las rutas en mapa interactivo o gráfico. | 5% |
| Calidad técnica del código | Organización, documentación, legibilidad y uso adecuado de estructuras de datos. | 5% |

**2️⃣ Presentación / Sustentación — 60%**

| Subcomponente | Descripción | Peso |
|---|---|---|
| Explicación de los algoritmos | Presentación detallada del funcionamiento interno de cada algoritmo implementado. | 15% |
| Uso de técnicas de diseño vistas en clase | Referencia explícita a técnicas de divide y vencerás, programación dinámica, greedy, backtracking, o su combinación. | 10% |
| Análisis de complejidad | Evaluación y justificación de la complejidad temporal y espacial de cada enfoque. | 10% |
| Análisis de trade-offs | Reflexión comparativa sobre precisión vs. eficiencia, tiempo vs. seguridad, y complejidad vs. mantenibilidad. | 15% |
| Claridad y dominio conceptual | Capacidad para explicar, argumentar y responder preguntas técnicas durante la sustentación. | 10% |

### Dataset

El archivo [`calles_de_medellin_con_acoso.csv`](./calles_de_medellin_con_acoso.csv) en esta carpeta es el dataset requerido para este proyecto.
