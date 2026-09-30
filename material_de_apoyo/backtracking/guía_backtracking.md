# Guía de preguntas para abordar problemas de Backtracking (enfoque DFS)

Esta guía busca que, antes de siquiera pensar en código, ustedes puedan "leer" cualquier problema de backtracking respondiendo siempre la misma secuencia de preguntas. Si logran responder estas 7 preguntas con claridad, el problema ya está resuelto conceptualmente — el código es solo la traducción.

---

## Pregunta 1: ¿Qué tipo de respuesta se me está pidiendo?

Antes de pensar en opciones o en current, hay que aclarar qué se espera obtener al final:

- ¿Una solución cualquiera que sirva? (factibilidad)
- ¿Todas las soluciones posibles?
- ¿Contar cuántas soluciones existen?
- ¿La mejor solución según algún criterio?

Esto determina qué se hace cuando se llega al final de una construcción (se guarda, se cuenta, se compara, etc.), pero no cambia la lógica de exploración.

---

## Pregunta 2: ¿Cuáles son mis opciones?

Las opciones son los "ladrillos" con los que se puede construir una solución. Es la pregunta más importante porque de ahí sale todo lo demás.

Hay que identificar:
- **De dónde salen** las opciones (una lista dada, un rango de números, un conjunto de símbolos, las casillas de un tablero, etc.)
- **Si se repiten o no** (¿puedo volver a usar la misma opción más adelante, o una vez usada queda descartada?)
- **Si el orden importa** (¿generar [A, B] es distinto de generar [B, A], o es la misma solución?)

Ejemplo (sublista con suma objetivo k): mis opciones son cada uno de los elementos de la lista original. Cada uno de ellos puede o no formar parte de la sublista que estoy construyendo.

---

## Pregunta 3: ¿Qué representa "current"?

`current` es el **estado parcial** de la solución que se está construyendo en este momento del recorrido — no es la respuesta final, es "hasta dónde he llegado".

Dos ideas clave que suelen generar confusión:

- `current` no es una sola cosa fija: es un estado que **cambia con cada decisión** que tomo (agrego una opción) y que **vuelve a cambiar cuando deshago esa decisión** (backtrack).
- Cada vez que `current` cambia, representa un nodo distinto del árbol de posibilidades que estoy recorriendo. El árbol completo de backtracking es, en el fondo, "todos los `current` posibles que puedo llegar a construir".

Ejemplo (sublista con suma objetivo k): `current` es la sublista parcial que llevo armada hasta el momento (puede estar vacía, tener un elemento, dos, etc.), junto con la suma acumulada de esos elementos.

---

## Pregunta 4: ¿Cómo agrego una opción a current?

Aquí se define la **acción de decisión**: tomar una de las opciones disponibles y modificar `current` para reflejar que esa opción ya fue usada.

Preguntas que ayudan a definir esto:
- ¿Agregar la opción es tan simple como añadirla al final de una lista?
- ¿Agregar la opción cambia también otra cosa (una suma acumulada, una posición en el tablero, un conjunto de símbolos usados)?

Este paso es el que "empuja" el recorrido un nivel más profundo en el árbol.

---

## Pregunta 5: ¿Cuándo tengo que parar de agregar? (caso base)

Esta es la condición de parada de la recursión: el momento en que `current` ya no debe seguir creciendo, porque:

- Ya es una solución completa y válida, o
- Ya es imposible que se convierta en una solución válida (no tiene caso seguir explorando por esa rama).

Es fundamental separar estos dos casos porque llevan a acciones distintas:
- Si es una solución válida → se registra/cuenta/compara.
- Si es una rama inválida o sin esperanza → simplemente se detiene ahí, sin registrar nada.

Ejemplo (sublista con suma objetivo k): paro y registro si la suma acumulada es exactamente k. Paro sin registrar si la suma ya superó k (no tiene sentido seguir agregando elementos positivos) o si ya no quedan más elementos por considerar.

---

## Pregunta 6: ¿Cuáles son mis opciones válidas en este punto (poda)?

No siempre todas las opciones originales siguen estando disponibles en cada paso. Antes de intentar agregar una opción, conviene preguntarse si tiene sentido intentarla:

- ¿Esta opción ya fue usada y no se puede repetir?
- ¿Agregar esta opción rompe alguna restricción del problema de inmediato (sin necesidad de completar toda la solución para saberlo)?

Cuando se puede responder "no tiene caso intentar esta opción" sin necesidad de construir toda la solución, se está podando una rama — es decir, evitando explorar un subárbol completo que sabíamos que no iba a servir.

---

## Pregunta 7: ¿Cómo deshago la decisión? (el paso de "retroceso")

Este es el paso que le da el nombre a la técnica y el que más cuesta entender. Después de explorar todo lo que se podía explorar habiendo agregado una opción a `current`, hay que **devolver `current` al estado que tenía antes de agregar esa opción**, para poder probar la siguiente opción disponible desde ese mismo punto.

La pregunta que hay que hacerse es: *"si deshago exactamente lo que hice en la pregunta 4, ¿`current` queda igual que antes de tomar esta decisión?"*

Esto es lo que permite que un mismo punto del árbol pueda dar lugar a varias ramas distintas: primero exploro completamente la rama de la opción A, retrocedo, y luego exploro completamente la rama de la opción B, partiendo del mismo `current` original.

---

## El patrón completo, como una sola idea

En cada punto del recorrido, backtracking hace lo siguiente:

1. Reviso si estoy en un caso base (pregunta 5) → si sí, actúo en consecuencia y no sigo por esta rama.
2. Si no, recorro mis opciones válidas (preguntas 2 y 6), y para cada una:
   a. La agrego a `current` (pregunta 4).
   b. Repito este mismo proceso con el nuevo `current` (esto es la recursión).
   c. Deshago lo que agregué (pregunta 7), para dejar `current` listo para la siguiente opción.

---
