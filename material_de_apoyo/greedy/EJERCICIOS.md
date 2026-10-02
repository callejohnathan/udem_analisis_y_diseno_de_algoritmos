# Registro de ejercicios — Análisis y Diseño de Algoritmos / material_de_apoyo/greedy

## Ejercicios

| ID | Título | Origen | Tratamiento | Temas (uso interno) | Dificultad | Archivo |
|----|--------|--------|-------------|---------------------|------------|---------|
| EJ-001 | Tramo de montaña más largo | LC 845 | Traducido | recorrido lineal, dos punteros, subarreglos | Media | ADA_parcial_greedy_20262.ipynb |
| EJ-002 | Botes de rescate | LC 881 | Traducido | greedy, ordenamiento, dos punteros, argumento de intercambio | Media | ADA_parcial_greedy_20262.ipynb |
| EJ-003 | Pilas de monedas | LC 1561 | Traducido | greedy, ordenamiento, argumento de intercambio | Media | ADA_parcial_greedy_20262.ipynb |

## Bitácora

### 2026-10-02 — ADA_parcial_greedy_20262.ipynb (parcial, nuevo)
- Agregados: EJ-001, EJ-002, EJ-003
- De plataformas, dados por el profesor: EJ-001 (LC 845), EJ-002 (LC 881), EJ-003 (LC 1561), incluidos tal cual (traducidos)
- Desde semillas del profesor: ninguno
- Propuestos por Claude: ninguno
- Notas: parcial presencial sin internet; sin enlaces a la fuente en el notebook. Fecha 2026-10-02, hora límite 9:50 a.m. u 11:50 a.m. según el grupo. 5 casos de prueba por punto, verificados con solución greedy y con fuerza bruta. LC 845 es más recorrido lineal que greedy en sentido estricto (señalado al profesor, que decidió mantenerlo). Casos de estrés agregados después (2 por punto, 7 casos en total por punto): EJ-001 una montaña de longitud 10⁴ y un arreglo creciente de 10⁴ sin montaña; EJ-002 50 000 personas que se emparejan todas (1 + 29 999) y 50 000 que no se emparejan (15 001, límite 30 000); EJ-003 99 999 pilas iguales y 99 999 pilas variadas. Se probaron contra soluciones ingenuas O(n²): en EJ-001 la ingenua (expandir desde cada posible cima) tarda ~2–8 s contra ~0,001 s, una diferencia moderada porque n ≤ 10⁴; en EJ-002 (buscar pareja lineal por persona) y EJ-003 (max/remove repetidos) la ingenua tarda ~1–4 min contra < 0,02 s. Salidas verificadas con dos implementaciones independientes. Los parciales anteriores de esta carpeta (p. ej. parcial_greedy_20261.ipynb) son previos al registro y no están indexados.
