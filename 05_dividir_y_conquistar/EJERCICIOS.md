# Registro de ejercicios — Análisis y Diseño de Algoritmos / 05_dividir_y_conquistar

Nota: los notebooks anteriores de esta carpeta (ejercicios_dividir_y_conquistar_1, simulacro_dividir_y_conquistar_1, teoría) son previos a este registro y sus ejercicios no están catalogados aquí.

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-009 | Subsecuencia más larga con suma limitada | LC 2389 | Traducido (con requisito de complejidad O((n + m) · log n) agregado) | ordenamiento, sumas prefijas, búsqueda binaria | Fácil | simulacro_dividir_y_conquistar_2.ipynb |
| EJ-010 | Buscar en una matriz ordenada | LC 240 | Traducido (con requisito de complejidad menor que O(m · n) agregado) | dividir y vencer en matrices, búsqueda binaria | Media | simulacro_dividir_y_conquistar_2.ipynb |

## Bitácora

### 2026-10-14 — simulacro_dividir_y_conquistar_2.ipynb (simulacro, nuevo)
- Agregados: EJ-009, EJ-010
- De plataformas, dados por el profesor: EJ-009 (LC 2389), EJ-010 (LC 240), traducidos con los límites originales
- Desde semillas del profesor: ninguno
- Propuestos por Claude: ninguno
- Notas: simulacro para la clase del 2026-10-15. Instrucción general: resolver con dividir y vencer. Por pedido del profesor, cada enunciado declara la complejidad exigida, porque con los límites originales una solución ingenua también pasa los casos. Casos de estrés (`# caso grande`): EJ-009 casos 7–9 (n = m = 1000); EJ-010 casos 10–13 (matriz 300 × 300, objetivo ausente impar en una matriz de pares, valor en la esquina, objetivo por debajo del mínimo). Contra soluciones ingenuas la diferencia de tiempo es pequeña en Python (EJ-010: 200 búsquedas ingenuas 0,14 s frente a 0,04 s con dividir y vencer), así que el requisito de complejidad se verifica al revisar el código, no por tiempo. Salidas verificadas: EJ-009 contra fuerza bruta por combinaciones en 500 entradas aleatorias; EJ-010 contra búsqueda exhaustiva y contra una solución de dividir y vencer en 2000 matrices aleatorias, y se comprobó que todas las matrices de los casos cumplen el orden por filas y columnas.
