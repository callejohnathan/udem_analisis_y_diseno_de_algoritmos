# Registro de ejercicios — Análisis y Diseño de Algoritmos / material_de_apoyo/examenes_generales

Nota: los notebooks anteriores de esta carpeta (parciales, recuperaciones y supletorios 2025-2 y 2026-1) son previos a este registro y sus ejercicios no están catalogados aquí.

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-004 | Jugando con dados | CF 378A | Traducido | fuerza bruta, enumeración | Fácil | recuperacion_fb_bt_greedy_20262.ipynb |
| EJ-005 | Dos torres | CF 1795A | Traducido | fuerza bruta, cadenas | Fácil | recuperacion_fb_bt_greedy_20262.ipynb |
| EJ-006 | Mayúsculas y minúsculas | LC 784 | Traducido | backtracking, generación de combinaciones | Media | recuperacion_fb_bt_greedy_20262.ipynb |
| EJ-007 | Mina de oro | LC 1219 | Traducido | backtracking, DFS en cuadrícula | Media | recuperacion_fb_bt_greedy_20262.ipynb |
| EJ-008 | Monstruos | CF 1849B | Traducido | greedy, aritmética modular, ordenamiento | Media | recuperacion_fb_bt_greedy_20262.ipynb |

## Bitácora

### 2026-10-02 — recuperacion_fb_bt_greedy_20262.ipynb (recuperación evaluada en sesión, nuevo)
- Agregados: EJ-004, EJ-005, EJ-006, EJ-007, EJ-008
- De plataformas, dados por el profesor: EJ-004 (CF 378A), EJ-005 (CF 1795A), EJ-006 (LC 784), EJ-007 (LC 1219), EJ-008 (CF 1849B), incluidos tal cual (traducidos)
- Desde semillas del profesor: ninguno
- Propuestos por Claude: ninguno
- Notas: encabezado igual al de la recuperación de EDD del mismo día (no se envía; evaluación en sesión hasta las 3:30 p.m.; cada punto vale 1.7 y baja 0.1 por persona hasta 1.0). Por decisión del profesor el encabezado exige la técnica de cada punto (1–2 fuerza bruta, 3–4 backtracking, 5 greedy con justificación). Sin enlaces a la fuente en el notebook. Dificultad desbalanceada (378A trivial frente a 1219 y 1849B), señalada al profesor. Casos de estrés (`# caso grande`): EJ-004 ninguno (solo hay 36 entradas posibles); EJ-005 casos 8–11 (torres de 20); EJ-006 caso 7 ("a1b2c3d4e5f6", 64 salidas; no se incluyó 2^12 = 4096 para no inflar el notebook); EJ-007 casos 8–9 (5×5 lleno, ~3 s con DFS en Python; 15×15 con 25 celdas en serpiente); EJ-008 casos 9–11 (n = 3·10^5, vidas hasta 10^9, k = 1 o 3): la simulación ingenua con montículo haría del orden de 10^14 ataques y no termina, frente a < 1 s del ordenamiento por residuo. En EJ-004 a EJ-007 los límites son de fuerza bruta/backtracking y no separan complejidades. Salidas verificadas: 1795A contra simulación BFS de los movimientos y contra la solución por cortes; 1849B contra simulación con montículo en 3000 entradas aleatorias; 784 y 1219 con soluciones propias.
