# Registro de ejercicios — Análisis y Diseño de Algoritmos / material_de_apoyo/programacion_dinamica

Nota: los parciales anteriores de esta carpeta (2025-2 y 2026-1) son previos a este registro y sus ejercicios no están catalogados aquí.

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-014 | Comparando sensores | Semilla del profesor (LCS) | Variación de LC 1143 (pregunta: coincidencia con tolerancia en vez de igualdad) | PD 2D sobre prefijos, LCS | Media | parcial_programacion_dinamica_20262.ipynb |
| EJ-015 | Ruta del dron | Semilla del profesor (rutas de (x1, y1) a (x2, y2)) | Variación de LC 64 (estructura: origen y destino arbitrarios, movimientos derecha, abajo y diagonal abajo-derecha, con bloqueos) | PD 2D en cuadrícula, tres vecinos | Media | parcial_programacion_dinamica_20262.ipynb |
| EJ-016 | Turnos con descanso | Semilla del profesor (tipo house robber sin la condición i−1 / i−2) | Variación de contexto de LC 2140 | PD 1D, tomar o dejar con salto variable | Media | parcial_programacion_dinamica_20262.ipynb |

## Bitácora

### 2026-11-03 — parcial_programacion_dinamica_20262.ipynb (parcial, nuevo)
- Agregados: EJ-014, EJ-015, EJ-016
- De plataformas, dados por el profesor: ninguno
- Desde semillas del profesor: EJ-014, EJ-015, EJ-016 (el profesor pidió una estructura tipo LCS, una de rutas en matrices de un punto a otro y una tipo house robber sin la condición de vecinos; escogió entre opciones propuestas por Claude)
- Propuestos por Claude: narrativas y variaciones concretas
- Notas: parcial del 2026-11-04, envío por correo antes de las 9:50 a.m. u 11:50 a.m. según el grupo (supuesto por Claude a partir de "8 y 10 a.m." y del parcial de greedy). Formato del simulacro 1 (Parte A 70 %, Parte B 30 %, sin lru_cache/cache). Modalidad: en pareja con un solo computador resuelven los 3 puntos; individualmente resuelven 2 de 3. Regla: no se programa un punto antes de explicarle al docente A.1 y A.2; el docente solo responde aprobado o no y lo controla él (sin firma ni hora en el notebook). Sin enlaces ni mención del problema base. Diferencia con material anterior: EJ-013 (simulacro) es LCS con igualdad sobre líneas; EJ-015 no tiene punto obligatorio y agrega la diagonal, a diferencia de los parciales 20252, 20261 y del final 20252. Límites bajados (series ≤ 300, cuadrícula ≤ 200 × 200, n ≤ 500) para que la memorización no supere el límite de recursión de Python (1000); comprobado con soluciones memo en todos los casos. Casos de estrés (`# caso grande`): EJ-014 casos 9–11 (300 × 300); EJ-015 casos 11–14 (200 × 200: todo en 1, diagonal cara, costos variados y muro con una sola abertura); EJ-016 casos 8–10 (n = 500). La recursión sin memo no termina: EJ-016 tarda 43 s con n = 40. Casos que separan soluciones ingenuas incorrectas: EJ-014 caso 1 (comparar con igualdad da 0). Entrada del árbol A.3 de EJ-014 cambiada a [5, 1, 8] / [2, 9, 4], d = 1, porque la original ([3, 8, 5] / [4, 9, 5]) daba un árbol en cadena sin solapamiento con la recurrencia estándar, EJ-016 caso 6 (house robber clásico daría 18 en vez de 11). Salidas verificadas: EJ-014 contra fuerza bruta en 400 entradas aleatorias, EJ-015 contra enumeración de todas las rutas en 400 cuadrículas aleatorias, EJ-016 contra enumeración de subconjuntos en 500 entradas aleatorias; tres salidas escritas a mano estaban mal y se corrigieron con las calculadas (incluido el costo del ejemplo del punto 2, que es 11).

### 2026-11-03 — parcial_programacion_dinamica_20262.ipynb (cambio en EJ-015)
- Agregados: ninguno
- Notas: por pedido del profesor, EJ-015 pasó de "moverse en las dos direcciones que acercan al destino, en cualquier cuadrante" a movimientos fijos derecha, abajo y diagonal abajo-derecha. Si el destino está en una fila o columna anterior al origen la respuesta es -1. La diagonal salta directo a la celda (las vecinas no tienen que estar libres). Nuevo ejemplo del enunciado con óptimo 8 frente a 10 de la ruta más diagonal; nueva entrada del árbol A.3 (mapa 2 × 3, 12 nodos, 6 distintos) porque un 3 × 3 con tres movimientos daba 31 nodos. 14 casos (10 + 4 grandes), verificados contra enumeración de todas las rutas en 600 cuadrículas aleatorias y con una solución memo dentro del límite de recursión. Modelo de pensamiento actualizado.
