# Proyecto Final 2025-2 — Análisis y Diseño de Algoritmos

> 📌 **Material de referencia de un semestre anterior (2025-2).** Este no es el proyecto final vigente de tu semestre — revísalo para hacerte una idea del formato, alcance y rúbrica que suele tener el proyecto final del curso.

## 🎮 Práctica: boop 4×4 con Minimax y Poda α–β

### 🎯 Objetivo general

Diseñar e implementar un agente de juego basado en Minimax con poda α–β que juegue una variante simplificada de *boop* sobre un tablero 4×4. El objetivo es evaluar, comparar y optimizar decisiones de búsqueda adversaria (profundidad, heurísticas, ordenamiento de jugadas, tablas de transposición), garantizando corrección, eficiencia y calidad de la función de evaluación.

### 🧩 Reglas simplificadas del juego (variante didáctica 4×4)

**Tablero y jugadores**
- Tablero 4×4 vacío al inicio.
- Dos jugadores: Naranja (MAX) y Morado (MIN).
- Cada jugador dispone de: 6 gatitos (kittens) y 4 gatos grandes (cats).

**Fases y turnos**
- Un turno consiste en colocar una pieza propia en una casilla vacía (no hay fase de movimiento).
- **Efecto boop** al colocar: todos los gatitos en las 8 celdas vecinas (Moore) se empujan 1 casilla alejándose de la pieza colocada, si la casilla de destino está libre; si está ocupada no se mueve, si sale del tablero, el gatito se retira (sale del juego).
- Los gatos grandes no son empujados por gatitos.
- Un gato grande sí empuja gatitos enemigos adyacentes (mismo efecto). Entre gatos grandes no hay empuje.

**Promoción a gato grande**
- Al finalizar tu turno, si has formado una línea de 3 gatitos propios (horizontal/vertical/diagonal), promocionas 1 de esos 3 gatitos a gato grande (tu elección).
- La línea de 3 se "consume" en una única promoción (no acumulable en el mismo turno).

**Condición de victoria**
- Gana el primer jugador que, al terminar su turno, tenga 2 gatos grandes alineados (horizontal/vertical/diagonal) en casillas consecutivas.
- Si se agotan las piezas y nadie logra condición de victoria, es empate.

### 🧠 Modelo algorítmico (Minimax + α–β)

**1) Representación de estado**
- Tablero: matriz 4×4 con valores en `{vacío, gatito N, gato N, gatito M, gato M}`.
- Reserva: piezas restantes por tipo y jugador (kittens, cats).
- Turno: jugador actual.
- Historial opcional: hash del estado (para tablas de transposición).

**2) Generación de jugadas**
- Todas las casillas vacías donde colocar (pieza por defecto: gatito, salvo que el jugador opte por colocar gato grande si le quedan; permitir ambas decisiones como jugadas distintas).
- Al simular la jugada:
  - Aplicar empujes según las reglas.
  - Detectar y aplicar promoción si se formó línea de 3 gatitos.
  - Comprobar victoria (2 gatos grandes consecutivos).

**3) Terminales**
- Victoria: estado con dos gatos grandes alineados del jugador que hizo la última jugada.
- Empate: sin piezas disponibles para colocar y sin victoria.
- Corte por profundidad: si se usa límite de profundidad, evaluar con heurística.

**4) Evaluación heurística** (cuando no se puede llegar a terminal)

La evaluación retorna un valor escalar desde la perspectiva de MAX (Naranja). Sugerencias de términos:

- 🐱 **Progreso hacia victoria**: `+∞` si MAX ya tiene 2 gatos grandes alineados; `−∞` si MIN lo tiene. Patrones de 1 gato grande con casilla adyacente libre alineable (`+w₁`).
- 🐾 **Potencial de promoción**: conteo de amenazas de 3 gatitos (dos en línea con hueco) ponderado (`+w₂` para MAX, `−w₂` para MIN).
- 🧱 **Control espacial / centralidad local**: piezas propias en celdas centrales (`+w₃`) para favorecer empujes efectivos.
- 💥 **Tácticas de empuje**: oportunidades de empujar gatitos enemigos fuera del tablero (`+w₄`). Riesgo de que te empujen (`−w₄`).

🎯 Ordena jugadas priorizando: (1) jugadas ganadoras inmediatas, (2) formaciones de doble amenaza, (3) empujes favorables, (4) centro ↔ esquinas.

**5) Poda α–β, límites y mejoras**
- α–β estándar con ordenamiento de jugadas (mejoras drásticas).
- Límite de profundidad adaptativo (p. ej., 6–10 plies en 4×4) y/o límite de tiempo.
- Iterative Deepening: profundidades crecientes con el mejor movimiento "aspirado".
- Tablas de transposición (hash tipo Zobrist): almacenar `(valor, profundidad, bound)`.
- Quiescence (opcional): extender hojas "inestables" con jugadas tácticas de empuje/promoción para reducir el *horizon effect*.

### 📊 Experimentos y comparación (precisión vs. tiempo; opcional)

Pedir a los equipos comparar configuraciones:
- Básico: Minimax puro vs. Minimax + α–β.
- Ordenamiento: heurístico simple vs. heurístico con clasificación por amenazas.
- Profundidad: `d = {4, 6, 8, 10}`.
- Optimizaciones: sin/con tablas de transposición; sin/con iterative deepening.
- Heurística: variantes con o sin términos de empuje / centralidad.

Métricas:
- ⏱️ Tiempo promedio por decisión.
- 🌲 Nodos/estados visitados.
- 🎯 Calidad de jugadas (torneos autocontenidos: engine vs. engine con distintas configuraciones).
- 📈 Curva profundidad→tiempo y profundidad→nodos.

### 🗺️ Visualización / Interfaz (sugerencias)

- Estado del tablero (grid 4×4) con íconos distintos para gatito/gato grande por color.
- Menú de navegación de opciones: posicionar gatito o gato; jugada IA.
- Visualización de estado de reservas.

### 🔬 Análisis esperado (algorítmico)

- Complejidad: analiza `b^d` (ramificación efectiva después de empujes y promociones) y cómo α–β reduce el espacio.
- Efecto del ordenamiento en el cutoff (muestra ratios de poda).
- Impacto de la quiescence en posiciones tácticamente "ruidosas".
- Tablas de transposición: tasa de hits, ahorro de nodos.
- Trade-offs:
  - Profundidad vs. latencia de respuesta.
  - Heurística rica vs. costo por evaluación.
  - Estabilidad de la evaluación vs. *horizon effect*.

### 📦 Entregables

- **Prototipo funcional (40%)**
  - Agente Minimax con α–β y parámetros configurables.
  - UI simple donde se pueda jugar humano vs. IA.
- **Presentación / Sustentación (60%)**
  - Explicación del modelo de estado, generación de jugadas, reglas de empuje.
  - Detalle del Minimax + α–β, mejoras implementadas y su justificación.
  - Función de evaluación: componentes, pesos, ejemplos.
  - Resultados experimentales y discusión de trade-offs.

---

Nota adicional del enunciado original: *"Opción III: se gradúan automáticamente 🎓"* — una broma del profesor, sin contenido evaluable real.
