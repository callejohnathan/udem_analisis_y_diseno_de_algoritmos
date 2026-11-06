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
| EJ-017 | Palabras del teclado | LC 17 | Variación de LC 17 (restricción) | backtracking, generación | Fácil | recuperacion_bt_dc_pd_20262.ipynb |
| EJ-018 | Orden compatible | LC 526 | Variación de LC 526 (restricción) | backtracking, permutaciones | Media | recuperacion_bt_dc_pd_20262.ipynb |
| EJ-019 | Reparto de tareas | LC 1723 | Variación de LC 1723 (restricción) | backtracking, poda por cota | Difícil | recuperacion_bt_dc_pd_20262.ipynb |
| EJ-020 | Potencia enorme | LC 50 | Variación de LC 50 (restricción) | dividir y vencer, aritmética modular | Fácil | recuperacion_bt_dc_pd_20262.ipynb |
| EJ-021 | Mejor tramo | LC 53 | Variación de LC 53 (pregunta) | dividir y vencer, caso cruzado | Media | recuperacion_bt_dc_pd_20262.ipynb |
| EJ-022 | Perfil de la ruta | LC 1095 | Variación de LC 1095 (pregunta y restricción) | dividir y vencer, búsqueda binaria | Media | recuperacion_bt_dc_pd_20262.ipynb |
| EJ-023 | Escalera con peajes | LC 746 | Variación de LC 746 (restricción) | programación dinámica 1D | Fácil | recuperacion_bt_dc_pd_20262.ipynb |
| EJ-024 | Lotes con precio máximo | LC 1043 | Variación de LC 1043 (restricción) | programación dinámica, partición | Media | recuperacion_bt_dc_pd_20262.ipynb |
| EJ-025 | Vigilancia en anillo | LC 198 | Variación de LC 198 (estructura) | programación dinámica, casos circulares | Media | recuperacion_bt_dc_pd_20262.ipynb |

## Bitácora

### 2026-11-06 — recuperacion_bt_dc_pd_20262.ipynb (recuperación evaluada en sesión, nuevo)
- Agregados: EJ-017 a EJ-025
- De plataformas, dados por el profesor: ninguno
- Desde semillas del profesor: ninguno
- Propuestos por Claude: EJ-017 a EJ-025, todos variaciones aprobadas por el profesor
- Notas: no se envía; todo se revisa antes de terminar la sesión. Calentamientos (EJ-017, EJ-020 y EJ-023) a 0.5 fijos; los demás empiezan en 1.5 y bajan 0.1 por persona. El piso de 1.0 se tomó de la recuperación anterior. Cada enunciado exige su técnica, por decisión del profesor. Sin enlaces a la fuente en el notebook. Límites ajustados frente a la propuesta: EJ-017 a 6 dígitos para no inflar el notebook; EJ-023 y EJ-025 a n = 2000 para que la memoización quepa en el límite de recursión de Jupyter. Casos de estrés (`# caso grande`): EJ-017 caso 9; EJ-018 casos 11–13 (n = 15, hasta 1,9 s con backtracking); EJ-019 casos 9–11 (sin poda 6^10, unos 215 s estimados, frente a 0,16 s); EJ-020 casos 8–10 (b cercano a 10^18); EJ-021 casos 11–14 (O(n²) unos 1100 s estimados frente a 0,74 s); EJ-022 casos 7–9 (búsqueda lineal unos 141 s estimados frente a 0,80 s); EJ-023 casos 8–10; EJ-024 casos 9–11; EJ-025 casos 10–12. Salidas verificadas leyendo el notebook: soluciones con la técnica exigida; fuerza bruta en los casos pequeños y en entradas aleatorias (400 de EJ-020, EJ-021, EJ-023, EJ-024 y EJ-025; 60 de EJ-018 y EJ-019). También se comprobó que los perfiles de EJ-022 cumplen el orden pedido.

### 2026-10-02 — recuperacion_fb_bt_greedy_20262.ipynb (recuperación evaluada en sesión, nuevo)
- Agregados: EJ-004, EJ-005, EJ-006, EJ-007, EJ-008
- De plataformas, dados por el profesor: EJ-004 (CF 378A), EJ-005 (CF 1795A), EJ-006 (LC 784), EJ-007 (LC 1219), EJ-008 (CF 1849B), incluidos tal cual (traducidos)
- Desde semillas del profesor: ninguno
- Propuestos por Claude: ninguno
- Notas: encabezado igual al de la recuperación de EDD del mismo día (no se envía; evaluación en sesión hasta las 3:30 p.m.; cada punto vale 1.7 y baja 0.1 por persona hasta 1.0). Por decisión del profesor el encabezado exige la técnica de cada punto (1–2 fuerza bruta, 3–4 backtracking, 5 greedy con justificación). Sin enlaces a la fuente en el notebook. Dificultad desbalanceada (378A trivial frente a 1219 y 1849B), señalada al profesor. Casos de estrés (`# caso grande`): EJ-004 ninguno (solo hay 36 entradas posibles); EJ-005 casos 8–11 (torres de 20); EJ-006 caso 7 ("a1b2c3d4e5f6", 64 salidas; no se incluyó 2^12 = 4096 para no inflar el notebook); EJ-007 casos 8–9 (5×5 lleno, ~3 s con DFS en Python; 15×15 con 25 celdas en serpiente); EJ-008 casos 9–11 (n = 3·10^5, vidas hasta 10^9, k = 1 o 3): la simulación ingenua con montículo haría del orden de 10^14 ataques y no termina, frente a < 1 s del ordenamiento por residuo. En EJ-004 a EJ-007 los límites son de fuerza bruta/backtracking y no separan complejidades. Salidas verificadas: 1795A contra simulación BFS de los movimientos y contra la solución por cortes; 1849B contra simulación con montículo en 3000 entradas aleatorias; 784 y 1219 con soluciones propias.
