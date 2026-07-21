# Rúbrica — Calificación de Parciales

**Estructura:** cada parcial tiene 3 problemas de igual peso (cada uno = 1/3 de la nota del parcial)
**Typehints:** obligatorios en todos los problemas
**Análisis de complejidad:** se evalúa solo cuando el problema lo pide explícitamente

## Distribución de puntaje por problema

| Componente | % del problema | Qué se evalúa |
|---|---|---|
| **Enfoque / diseño de la solución** | 30% | Si identificaste correctamente la estructura y estrategia algorítmica que el problema requiere (por ejemplo, reconocer que se necesita backtracking con poda y no fuerza bruta pura, o que el problema tiene subestructura óptima para programación dinámica y no basta con un enfoque greedy) |
| **Implementación correcta** | 40%* | Que el código funcione según el enunciado, respetando la interfaz y las restricciones dadas (estructuras, métodos y tipos de retorno especificados) |
| **Casos borde y restricciones** | 15% | Que tu solución contemple los casos explícitos del enunciado (entrada vacía, tamaño mínimo, sin solución posible, restricciones de capacidad, etc.) |
| **Typehints + legibilidad** | 15% | Typehints correctos y completos + código legible |

*Cuando el problema pide análisis de complejidad, ese componente toma 10 puntos porcentuales del rubro de "Implementación" (que baja a 30%), para que el total del problema no cambie.

## Cómo se evalúa el Enfoque (30%) — importante leer con atención

El puntaje de Enfoque **no se obtiene solo por escribir código con la forma de una solución** (recorridos, condicionales, ciclos). Se obtiene por evidenciar que entendiste la lógica que el problema realmente exige.

| Lo que se observa | Puntos de Enfoque |
|---|---|
| Firma de función con `pass` o comentarios genéricos ("aquí iría el backtracking"), sin estructura de control real | 0% |
| Recorres la estructura (arreglo/tablero/grafo) con condicionales, pero **sin la lógica central que el problema exige** — por ejemplo, sin poda, sin memoization, sin criterio de selección greedy correcto — el recorrido existe, pero no resuelve el problema ni parcialmente | 0% |
| Al menos un elemento correcto de la lógica central está presente (ej. manejas el estado pero no podas correctamente, o memoizas pero con la clave equivocada) | 10–15% |
| La lógica central está presente y es mayormente correcta, con errores puntuales de ejecución (índices, condición de corte, caso base) | 20–25% |
| Enfoque completo y correcto, aunque la implementación final falle en un detalle menor | 30% |

**En otras palabras:** recorrer un arreglo o un tablero con alguna condición dentro no es, por sí solo, evidencia de que resolviste el problema. Lo que se evalúa es si esa lógica aborda específicamente la estrategia algorítmica que el enunciado pide (backtracking con poda, memoization/tabulation, criterio greedy correcto, descomposición divide y vencerás, etc.), no solo si "toca" la estructura de datos.

## Cómo se evalúa la Implementación

La Implementación solo puede recibir puntaje si el Enfoque ya obtuvo al menos 10-15%. Si tu Enfoque es 0% (por ejemplo, una plantilla vacía o un recorrido sin lógica real), la Implementación también será 0%, porque no hay una base conceptual sobre la cual evaluar "qué tan bien está implementado".

## Typehints obligatorios

Si tu solución no incluye typehints, el problema **no puede superar el 85% del total**, sin importar qué tan correcta sea el resto de tu solución.

## Principio general que aplica en todos los problemas

- Si tu enfoque es correcto pero la implementación falla, puedes obtener hasta 30-40% del problema — nunca 0 — porque el enfoque ya demuestra comprensión real.
- Si tu código da el resultado correcto "por casualidad", sin un enfoque claro (por ejemplo, fuerza bruta cuando se pedía una solución eficiente con backtracking, greedy o programación dinámica, o una solución que no generaliza a otros casos), no recibirás el 100% del problema aunque el resultado final coincida con lo esperado.
