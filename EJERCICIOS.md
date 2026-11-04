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
