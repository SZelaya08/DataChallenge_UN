# Data Challenge PRO HUN 2026 — Equipo Insignia

Análisis del flujo de pacientes de urgencias del Hospital Universidad del Norte
(Universidad del Norte + Fundación Hospital Universidad del Norte). El objetivo
es comprender, predecir y optimizar el flujo de pacientes, encontrar cuellos de
botella y proponer acciones factibles para reducir demoras.

**Equipo:** Kryss Taliana Caro Támara · Santiago José Faroy Zelaya Ríos · Leia Valentina Patiño Lara

> **Confidencialidad.** Este repositorio **no contiene datos del hospital**:
> ni filas de pacientes, ni extractos, ni el caché de Power BI, ni resultados
> numéricos de los modelos. Los términos del reto (§6 y §13) prohíben subirlos.
> Revisa la sección *Antes de cada commit*.

## Estructura

| Ruta | Contenido |
|---|---|
| `Hun_Insignia.pbip` | Abre el dashboard en Power BI Desktop (formato proyecto). |
| `Hun_Insignia.Report/` | Páginas, visuales y tema del informe (texto, sin datos). |
| `Hun_Insignia.SemanticModel/` | Modelo semántico en TMDL: tablas, medidas DAX, relaciones. |
| `HUN_Insignia_tema_color.json` | Tema de colores del dashboard (Diseño → Importar tema). |
| `modelos/01_prediccion_demanda.ipynb` | Modelo 1: predicción de demanda horaria de urgencias. |
| `modelos/02_prediccion_duracion.ipynb` | Modelo 2: duración de los episodios de urgencias. |
| `herramientas/limpiar_notebook.py` | Filtro que quita las salidas de los notebooks al hacer commit. |
| `requirements.txt` | Dependencias de Python. |

Carpetas que existen en cada computador pero **no** se suben: `resultados/`,
`modelos/resultados/`, `.venv/` y cualquier `.csv`, `.joblib` o `.pbix`.

## Cómo reproducirlo

1. **Acceso a datos.** Conéctate a la VPN del reto y carga las tablas en tu
   PostgreSQL local: base `hun_analitica`, esquema `urgencias`
   (`demanda_horaria`, `episodios`). Las credenciales nunca van en el código:
   los notebooks las piden con `getpass` al ejecutarse.
2. **Entorno de Python (3.14).**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Notebooks.** Ejecuta en orden `01_prediccion_demanda` y luego
   `02_prediccion_duracion`. Las salidas se guardan en `modelos/resultados/`
   y `resultados/`, que quedan solo en tu computador.
4. **Dashboard.** Abre `Hun_Insignia.pbip` en Power BI Desktop y pulsa
   **Inicio → Actualizar**. Se conecta a `localhost:5432/hun_analitica`
   en modo Importar.

## Dashboard (provisional)

| Página | Pregunta que responde |
|---|---|
| 1. Resumen | ¿Cuántos episodios hay y cuánto duran? Demanda mes a mes. |
| 2. Cuándo | ¿A qué hora y qué días se concentra la demanda? (promedio y P90) |
| 3. Episodios | ¿Qué queda registrado en cada episodio? Estancias > 24 h / > 48 h. |
| 4. Modelo (reportado) | Métricas e importancias del modelo 1 **reportadas, sin verificar**. |
| 5. Pendientes | Predicciones, simulación y optimización por construir. |

Las medidas están en la carpeta de visualización *Dashboard provisional* del
modelo. La duración es el tiempo documentado del episodio (permanencia), no el
tiempo de espera.

## Notebooks: configuración obligatoria (una vez por clon)

Las salidas de los notebooks pueden mostrar filas de la base. El archivo
`.gitattributes` hace que git las quite automáticamente al hacer commit, pero
cada integrante tiene que activar el filtro en su clon:

```powershell
git config filter.limpiar-notebook.clean "python herramientas/limpiar_notebook.py"
git config filter.limpiar-notebook.required true
```

Con `required true`, si el filtro falla el commit se detiene en vez de subir
el notebook con salidas. Tu archivo local conserva sus salidas.

## Antes de cada commit

- `git status` no debe mostrar ningún `.csv`, `.joblib`, `.pbix` ni `cache.abf`.
- Nada de contraseñas, IPs de la VPN ni cadenas de conexión con usuario real.
- Si dudas si algo es confidencial, no lo subas y pregúntale al equipo.
