# Análisis y Diseño de Algoritmos (ADA)

Bienvenido/a al repositorio del curso. Aquí vas a encontrar todo el material que usamos en clase: teoría, ejercicios, talleres, simulacros y material de apoyo de semestres anteriores.

## Cómo está organizado

Las carpetas numeradas (`01_...` a `06_...`) son el curso en sí, **en el orden real del semestre**. Dentro de cada una vas a encontrar notebooks con distintos prefijos:

| Prefijo | Qué es |
|---|---|
| `teoria_*.ipynb` | Guion de clase: la explicación conceptual, con ejemplos ya resueltos. Es el material que usamos en vivo. |
| `ejercicios_*.ipynb` | Problemas para que resuelvas tú. El enunciado, las pistas y los ejemplos están completos; las celdas de código están vacías (`# Tu código aquí`) a propósito. |
| `taller_*.ipynb` | Ejercicios guiados para trabajar en clase, mismo criterio que `ejercicios_*`. |
| `simulacro_*.ipynb` | Simulacros de examen para practicar antes de un parcial. |

## Temario

1. [`01_analisis_asintotico/`](01_analisis_asintotico/) — Notación Big-O, análisis de complejidad temporal y espacial, medición práctica de rendimiento.
2. [`02_fuerza_bruta/`](02_fuerza_bruta/) — Estrategia de fuerza bruta, generación de permutaciones y combinaciones.
3. [`03_greedy/`](03_greedy/) — Algoritmos voraces, criterios de ordenamiento, colas de prioridad (heaps).
4. [`04_backtracking/`](04_backtracking/) — Recursión, árboles de espacio de estados, poda (pruning).
5. [`05_dividir_y_conquistar/`](05_dividir_y_conquistar/) — Descomposición y combinación, árboles de recurrencia, Teorema Maestro.
6. [`06_programacion_dinamica/`](06_programacion_dinamica/) — Memoization (top-down), tabulation (bottom-up), optimización de estados.

El cronograma completo, semana a semana, con los hitos evaluativos de cada bloque, está en [`00_curso/cronograma.md`](00_curso/cronograma.md).

## Otras carpetas

- [`00_curso/`](00_curso/) — Información general del curso (metodología, evaluación, comunicación), el cronograma y el reto diagnóstico inicial.
- [`proyecto_final/`](proyecto_final/) — Enunciado y rúbrica del proyecto final del semestre.
- [`material_de_apoyo/`](material_de_apoyo/) — Parciales y simulacros reales de semestres anteriores, organizados por tema, más una carpeta `examenes_generales/` para finales, recuperaciones y supletorios que combinan varios temas. Útil para practicar, pero no revela necesariamente el formato exacto del próximo parcial.

## Cómo usar los notebooks de ejercicios

1. Ábrelo y lee el enunciado completo (incluye pistas y ejemplos de entrada/salida).
2. Completa las celdas marcadas con `# Tu código aquí`.
3. Corre las celdas de prueba que ya vienen en el notebook para validar tu solución.
4. Si te trabas, revisa el notebook de `teoria_*` del mismo tema — normalmente ahí está el concepto que necesitas.

## Herramientas

Puedes trabajar en el lenguaje que prefieras (C++, Java, Python...); el foco del curso son los conceptos, no la sintaxis. Los notebooks de este repositorio están en Python porque es el lenguaje que usamos en clase para las explicaciones.
