# Registro de ejercicios — Análisis y Diseño de Algoritmos / 06_programacion_dinamica

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-011 | Diseños para el andén | Propio | Variación de Fibonacci / tiling (pregunta: dos piezas de 1 m distintas) | PD 1D, conteo | Fácil | simulacro_programacion_dinamica_1.ipynb |
| EJ-012 | Agenda del domiciliario | Propio | Variación de LC 198 House Robber (restricción: máx. 2 días seguidos) | PD con estado extra, maximización | Media | simulacro_programacion_dinamica_1.ipynb |
| EJ-013 | Revisión de cambios entre versiones | Propio | Variación de LC 1143 / LC 583 (pregunta: mínimo de borrados + inserciones sobre líneas) | PD 2D sobre dos secuencias, LCS | Media | simulacro_programacion_dinamica_1.ipynb |

## Bitácora

### 2026-11-03 — simulacro_programacion_dinamica_1.ipynb (simulacro, nuevo)
- Agregados: EJ-011, EJ-012, EJ-013
- De plataformas, dados por el profesor: ninguno
- Desde semillas del profesor: los tres (pidió emular la lógica de LCS, House Robber y Fibonacci, disfrazados para que no se reconozca el patrón)
- Propuestos por Claude: narrativas y variaciones concretas
- Notas: calificación 70 % planteamiento (A.1 significado del estado/clave-valor 20 %, A.2 recurrencia 15 %, A.3 árbol sin memo con solapamiento 20 %, A.4 complejidad 15 %) y 30 % implementación; se prohíbe lru_cache/cache. Sin línea de fuente en el notebook a propósito, para no delatar el problema base. Salidas verificadas: EJ-011 contra enumeración recursiva (n ≤ 8); EJ-012 contra fuerza bruta por subconjuntos en 500 entradas aleatorias; EJ-013 con tabla de PD (árbol de A.3 para [A,B,C] vs [B,C,D]: 20 nodos, 12 subproblemas distintos, respuesta 2). Los notebooks previos de esta carpeta son anteriores al registro y no están indexados. Modelo de solución del EJ-013 entregado al profesor fuera del repo.
