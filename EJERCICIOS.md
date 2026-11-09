# Índice de ejercicios — Análisis y Diseño de Algoritmos

| ID | Origen | Idea central | Carpeta |
|----|--------|--------------|---------|
| EJ-001 | LC 845 | Recorrido lineal que extiende tramos estrictamente crecientes seguidos de decrecientes y mide el máximo; las mesetas rompen el tramo | material_de_apoyo/greedy |
| EJ-002 | LC 881 | Ordenar y emparejar con dos punteros el más pesado con el más liviano si caben juntos; si no, el pesado va solo | material_de_apoyo/greedy |
| EJ-003 | LC 1561 | Ordenar, descartar el tercio menor para el tercero y tomar cada segundo elemento desde arriba (el segundo mayor de cada trío) | material_de_apoyo/greedy |
| EJ-004 | CF 378A | Recorrer las 6 caras del dado y comparar distancias absolutas de a y b a cada cara | material_de_apoyo/examenes_generales |
| EJ-005 | CF 1795A | Concatenar s con t invertida y probar todos los cortes con ambas partes no vacías, verificando que no haya vecinos iguales | material_de_apoyo/examenes_generales |
| EJ-006 | LC 784 | Generar todas las combinaciones de mayúscula/minúscula decidiendo letra por letra (2^letras) | material_de_apoyo/examenes_generales |
| EJ-007 | LC 1219 | DFS con backtracking desde cada celda con oro, marcando visitadas y desmarcando al volver, para el camino simple de suma máxima | material_de_apoyo/examenes_generales |
| EJ-008 | CF 1849B | Reducir cada vida a su residuo (a-1) mod k + 1 y ordenar por residuo descendente y luego por índice | material_de_apoyo/examenes_generales |
| EJ-009 | LC 2389 | Ordenar, acumular sumas prefijas y, por consulta, búsqueda binaria de la última prefija ≤ consulta | 05_dividir_y_conquistar |
| EJ-010 | LC 240 | Buscar en matriz ordenada por filas y columnas descartando cuadrantes (columna media + búsqueda binaria, o escalera desde una esquina) | 05_dividir_y_conquistar |
| EJ-011 | Propio (var. Fibonacci) | Contar cubrimientos de una franja con dos piezas de 1 y una de 2: f(n) = 2f(n-1) + f(n-2), PD 1D | 06_programacion_dinamica |
| EJ-012 | Propio (var. LC 198) | Maximizar suma eligiendo elementos sin tomar más de dos consecutivos: PD con estado (posición, racha actual) | 06_programacion_dinamica |
| EJ-013 | Propio (var. LC 583 / LC 1143) | Mínimo de borrados + inserciones entre dos secuencias de líneas: PD 2D sobre prefijos (equivale a n + m − 2·LCS) | 06_programacion_dinamica |
| EJ-014 | Semilla del profesor (var. LC 1143) | LCS sobre dos series numéricas donde coinciden a[i], b[j] si abs(a[i] − b[j]) ≤ d: PD 2D sobre prefijos con la condición de coincidencia cambiada | material_de_apoyo/programacion_dinamica |
| EJ-015 | Semilla del profesor (var. LC 64) | Costo mínimo entre dos celdas (x1, y1) → (x2, y2) con movimientos derecha, abajo y diagonal abajo-derecha y celdas bloqueadas: PD 2D sobre el rectángulo con mínimo de tres vecinos | material_de_apoyo/programacion_dinamica |
| EJ-016 | Semilla del profesor (LC 2140) | Tomar o dejar cada elemento; tomar i salta d[i] posiciones: f(i) = max(f(i+1), p[i] + f(i+d[i]+1)) | material_de_apoyo/programacion_dinamica |
| EJ-017 | LC 17 (var.) | Generar palabras de un teclado telefónico decidiendo letra por letra y podando las que repiten la letra anterior | material_de_apoyo/examenes_generales |
| EJ-018 | LC 526 (var.) | Contar permutaciones con divisibilidad entre valor y posición, respetando posiciones ya fijas, con backtracking por posición | material_de_apoyo/examenes_generales |
| EJ-019 | LC 1723 (var.) | Asignar tareas a k trabajadores minimizando la carga máxima, con poda por mejor solución y pares incompatibles | material_de_apoyo/examenes_generales |
| EJ-020 | LC 50 (var.) | Exponenciación modular por mitades: a^b se obtiene de (a^(b//2))² mod m | material_de_apoyo/examenes_generales |
| EJ-021 | LC 53 (var.) | Subarreglo de suma máxima por mitades con caso que cruza el centro, devolviendo límites con desempate por menor inicio y fin | material_de_apoyo/examenes_generales |
| EJ-022 | LC 1095 (var.) | Hallar por búsqueda binaria el pico de un arreglo que sube y baja, y buscar cada consulta en ambos lados | material_de_apoyo/examenes_generales |
| EJ-023 | LC 746 (var.) | Costo mínimo para subir pagando por escalón, con saltos de 1, 2 o 3: mínimo de tres estados previos | material_de_apoyo/examenes_generales |
| EJ-024 | LC 1043 (var.) | Partir un arreglo en bloques ≤ k: cada estado prueba cada tamaño de último bloque, con valor max·tamaño − costo | material_de_apoyo/examenes_generales |
| EJ-025 | LC 198 (var. estructura, equivale a LC 213) | Tomar sin vecinos en un círculo: máximo de dos PD lineales, sin el primero o sin el último | material_de_apoyo/examenes_generales |
| EJ-026 | Clásico (par más cercano) | Comparar todos los pares de puntos y quedarse con la menor distancia euclidiana, O(n²) | 02_fuerza_bruta |
| EJ-027 | Clásico (TSP) | Fijar la ciudad de origen, recorrer todas las permutaciones de las demás y quedarse con el ciclo de menor costo | 02_fuerza_bruta |
| EJ-028 | Clásico (mochila 0/1) | Enumerar los 2ⁿ subconjuntos de objetos y quedarse con el de mayor valor que no exceda la capacidad | 02_fuerza_bruta |
