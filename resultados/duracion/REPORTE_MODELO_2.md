# REPORTE MODELO 2 — Duración documentada de episodios

## A. Estado de ejecución

| Elemento | Estado |
|---|---|
| Notebook creado | Sí: `modelos/02_prediccion_duracion.ipynb` |
| Celdas de código ejecutadas | 11 |
| Celdas pendientes | 0; el bloque de modelos se ejecutó y fue omitido por la puerta metodológica |
| Fuente ejecutada | csv_local |
| Diagnóstico y sensibilidad | Ejecutados |
| Modelos predictivos | NO EJECUTADOS: `permitir_modelado = False` |
| Artefactos de modelo | NO GENERADOS |
| Errores encontrados | La conexión PostgreSQL sin contraseña fue rechazada; el diagnóstico ejecutado usa el respaldo local explícito. |

## B. Calidad de datos

| Indicador | Valor |
|---|---:|
| Total de episodios | 801440 |
| Nulos totales | 0 |
| Duraciones negativas | 0 |
| Duraciones cero | 378697 |
| Duraciones positivas | 422743 |
| Episodios > 24 h | 78126 |
| Episodios > 48 h | 55188 |
| Episodios > 7 días | 15153 |
| Duplicados de `episode_id` | 0 |
| `episode_end < episode_start` | 0 |
| Inconsistencias duración-fechas | 509 |
| Proporción positiva | 0.527479 |
| Período observado | 2023-01-01 00:21:55 a 2026-07-17 18:57:09 |

## C. Estadísticas de duración

| Estadística | Todos | Positivos |
|---|---:|---:|
| Media (min) | 818.910 | 1552.496 |
| Mediana (min) | 2.467 | 282.850 |
| P75 (min) | 335.583 | 858.358 |
| P90 (min) | 1372.073 | 4112.143 |
| P95 (min) | 4358.134 | 7691.382 |
| P99 (min) | 14856.100 | 20650.838 |
| Máximo (min) | 1684217.246 | 1684217.246 |
| Proporción cero | 0.472521 | NO APLICA |

## D. Sensibilidad

| Umbral | Episodios | Proporción cero | Mediana (min) | P90 (min) | Proporción >24 h |
|---:|---:|---:|---:|---:|---:|
| 24 | 801440 | 0.472521 | 2.467 | 1372.073 | 0.097482 |
| 48 | 797095 | 0.474066 | 2.433 | 1418.160 | 0.099254 |

Los conjuntos de 24 y 48 horas se analizaron por separado; no se combinaron.

## E. Viabilidad predictiva

| Pregunta | Resultado |
|---|---|
| ¿Se habilitó el modelado? | No |
| Razón | No existe confirmación hospitalaria de que la duración reconstruida sea estancia, espera o atención clínica real. |
| Predictores candidatos de inicio | Componentes de calendario derivados de `episode_start`, sujetos a validación. |
| Riesgo principal | Data leakage por usar campos acumulados o el desenlace final. |

## F. Resultados de modelos

NO CALCULADO. Los modelos fueron preparados como código opcional, pero no se entrenaron ni se reportan métricas.

## G. Recomendación

Solicitar aclaración y validación con el hospital antes de modelar. Confirmar el significado operacional de la reconstrucción de 24 horas, definir el momento de predicción y verificar qué variables están disponibles en ese momento. Después, realizar una validación cronológica y prospectiva; si la variable no representa un objetivo operacional, cambiar la pregunta predictiva.
