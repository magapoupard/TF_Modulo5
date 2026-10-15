# Registro de decisiones metodológicas — TF Módulo 5

**Cursante:** MAGALI POUPARD. **Repositorio:** https://github.com/magapoupard/TF_Modulo5

Regla: cada decisión lleva **fecha**, **decisión**, **fundamento** y **alternativa descartada** (si aplica). Referencias en APA 7.ª.

Este archivo es la diferencia entre un método documentado y una sucesión de ajustes. Si un producto cartográfico llega a un expediente administrativo, es lo primero que se pide.

---

## Plantilla de entrada

### AAAA-MM-DD — Título corto

* **Etapa:** (caso-AOI / clases / evidencia / muestreo / implementación / validación / cierre)
* **Decisión:** 
* **Fundamento:** 
* **Alternativa descartada:**  
* **Evidencia / archivo:**  
* **Responsable (humano):**

---

## 1\. Caso, AOI y techo de cómputo

### 2026-10-01 — Variante A y problema de gestión

* **Etapa:** caso-AOI
* **Decisión:** Variante A (clasificación de coberturas).
* **Decisión de gestión que depende del mapa:** Actualización del OTBN dentro del Ejido Municipal de Paso de la Patria, Corrientes, como insumo para delimitar áreas no urbanizables en el ámbito de la administración municipal.
* **Fundamento:** La pregunta es de estado: dónde se encuentran los bosques nativos del ejido y qué superficie ocupan en la actualidad. Esa información es la base para zonificar el bosque a escala municipal en concordancia con el OTBN provincial y para restringir la urbanización sobre él. El mapa no asigna categorías de conservación: estas se definen en un paso posterior, aplicando los criterios de sustentabilidad ambiental de la Ley 26.331.
* **Alternativa descartada:** Variante B (monitoreo de cambio), porque el objetivo no es cuantificar pérdida entre dos fechas sino caracterizar la situación actual.
* **Responsable (humano):** MAGALI POUPARD

### 2026-10-01 — Delimitación del AOI (*Area of Interest*)

* **Etapa:** caso-AOI
* **Extensión aproximada (ha):** 10.764 ha.  
* **¿Respeta el techo 5.000–20.000 ha?** Sí 
* **Fundamento del AOI:** Se determinó un polígono correspondiente al área no urbanizada, o con asentamientos muy dispersos, porque es donde se encuentran los bosques nativos y donde se definirán las áreas no urbanizables.
* **Alternativa descartada:**  Tomar todo el ejido municipal de Paso de la Patria, porque el área consolidada no contiene bosque nativo relevante para el ordenamiento y para restringir la urbanización.
* **Evidencia / archivo:** data/raw/aoi.geojson (CRS:EPSG:5347 - POSGAR 2007 / Argentina 5)
* **Responsable (humano):** MAGALI POUPARD
---
### 2026-10-13 — Sistema de referencia

* **Etapa:** caso-AOI
* **Decisión:** EPSG:5347 (POSGAR 2007 / Argentina faja 5) para todo el proyecto: AOI, muestras e imágenes (`CRS = "EPSG:5347"` en src/config.py).
* **Fundamento:** Sistema métrico y oficial para la provincia de Corrientes, compatible con la cartografía oficial del OTBN. El pipeline exige un sistema métrico único para todo el proyecto.
* **Alternativa descartada:** UTM 21 Sur (EPSG:32721), se descartó por preferencia y familiaridad con el sistema elegido.
* **Evidencia / archivo:** src/config.py; data/raw/aoi.geojson; data/raw/rois.geojson
* **Responsable (humano):** MAGALI POUPARD

### 2026-10-13 — Ajuste de AOI

 * **Ajuste AOI:**  Se corrigió el límite norte del polígono; la superficie pasó de aprox. 10.706 ha a 10.764 ha (calculada en QGIS )
 * **Fundamento:** Incorporar zona donde en el mapa actual de OTBN, identifica área de bosque nativo, y afinar mejor el límite del área urbanizada.
 * **Responsable (humano):** MAGALI POUPARD


## 2\. Clases y umbrales

### 2026-10-01 — Esquema de clases

* **Decisión:** Esquema de 4 clases: 1 humedales y cuerpos de agua, 2 bosque nativo, 3 sabana / pastizal, 4 urbanizado. (vincular a `docs/clases.md`)  
* **MMU** (*Minimum Mapping Unit*): 0.5 ha — **¿se aplicó el tamizado?** sí (APLICAR_MMU = True en src/config.py)
* **Fundamento:** El umbral de bosque nativo (cobertura de copas ≥ 20 %, altura ≥ 3 m, superficie ≥ 0,5 ha.) y la MMU siguen la Res. COFEMA 230/12 (Pauta 1.2), para que el mapa sea coherente con la definición legal de bosque nativo que rige el OTBN. Estos umbrales son compatibles con el LCCS de la FAO (árboles de 3 m o más con fisonomía arbórea y cobertura abierta o cerrada; Di Gregorio & Jansen, 2005, §3.4.1). Para humedales / cuerpos de agua, se adopta la definición amplia de humedal de la Convención de Ramsar (1971, art. 1.1; Ley 23.919), que incluye cuerpos de agua permanentes y temporales.
* **Alternativa descartada:** Se descartó desagregar Sabana y Pastizal, ya que  para el objeto del mapa (identificar bosques nativos) no resulta relevante; separar cuerpos de agua permanente y humedal por lo fundamentado arriba y porque  ambas clases debieran corresponderse a zonas no urbanizables a efectos de la normativa municipal; se descartaron las clases suelo de cultivo y suelo desnudo por no contar con muestras suficientes en el AOI.
* **Evidencia / archivo:** docs/clases.md; src/config.py
* **Responsable (humano):** MAGALI POUPARD
---

## 3\. Evidencia

### 2026-10-13 — Ventanas temporales

* **Ventana 1:** 2026-01-01 / 2026-04-01 (verano).
* **Ventana 2:** 2026-06-01 / 2026-09-01 (invierno).
* **Fundamento fenológico de la elección:** Se eligen estaciones contrastantes del mismo ciclo anual. En verano todas las coberturas vegetales presentan alto verdor (bosque, sabana y pastizal tienen comportamientos espectrales similares). En invierno, a diferencia de los pastizales, el bosque nativo conserva mayormente el follaje. 
* **Alternativa descartada:** Una sola ventana (análisis mono-fecha), porque no permite separar con confiabilidad bosque de sabana / pastizal, que se distinguen por su fenología.
* **Evidencia / archivo:** src/config.py (`VENTANAS`); docs/clases.md
* **Responsable (humano):** MAGALI POUPARD

### 2026-10-14 — Sentinel-2 L2A (ESA) vía STAC

* **Etapa:** evidencia
* **Fuente:** STAC (*SpatioTemporal Asset Catalog*) de Planetary Computer, colección `sentinel-2-l2a`. Script `python -m src.download_s2_stac`.
* **Escenas por ventana y nubosidad:** Ventana 1 (2026-01-01 / 2026-04-01): 22 escenas, tile T21JUK, nubosidad entre 0,002 % y 12,9 %. Ventana 2 (2026-06-01 / 2026-09-01): 12 escenas, tile T21JUK, nubosidad entre 0,005 % y 18,2 %. Umbral aplicado: `MAX_CLOUD = 20` (escenas con nubosidad menor a ese valor).
* **Composición:** mediana de cada ventana.
* **Archivos:** `data/raw/stack_s2_v1.tif` y `data/raw/stack_s2_v2.tif`. Seis bandas en el orden B2, B3, B4, B8, B11, B12; CRS EPSG:5347; píxel de 10 m; extensión del recuadro del AOI (2089 × 1290).
* **Índices:** NDVI, NDMI y dNDVI, declarados en `docs/clases.md`. Este bloque no los calculó.
* **Observación:** Durante la descarga, la verificación de seguridad de la conexión falló en esta computadora. El asistente la desactivó solo para esa descarga para poder completarla. Los datos se verificaron visualmente en QGIS.
* **Responsable (humano):** MAGALI POUPARD

### 2026-10-14 — Predictores

* **Etapa:** implementación
* **Decisión:** Por ventana: B2, B3, B4, B8, NDVI y NDMI. Con las dos ventanas se agrega dNDVI = NDVI de la ventana 2 menos NDVI de la ventana 1. NDVI = (B8 − B4) / (B8 + B4). NDMI = (B8 − B11) / (B8 + B11). Si el denominador es 0, el píxel queda como NaN.
* **Fundamento:** Son los índices declarados en `docs/clases.md`. NDVI separa vegetación de agua y suelo. NDMI aporta humedad para diferenciar bosque de pastizal seco. dNDVI es el contraste fenológico entre invierno y verano.
* **Alternativa descartada:** Agregar otros índices espectrales sin una justificación específica para separar las clases del AOI.
* **Evidencia / archivo:** `src/features.py`
* **Responsable (humano):** MAGALI POUPARD

### 2026-10-14 — Desplazamiento del DN de Sentinel-2 L2A

* **Etapa:** implementación
* **Decisión:** `S2_DN_OFFSET = 1000` en `src/config.py`. Antes de NDVI, NDMI y dNDVI se resta 1000 a cada banda. Un DN igual a 0 queda como NaN. Los GeoTIFF de `data/raw` no se modifican.
* **Fundamento:** Las 34 escenas usadas tienen `s2:processing_baseline` 05.11 (8 escenas, ventana de verano) o 05.12 (26 escenas). Desde la línea 04.00, la ESA define `BOA_ADD_OFFSET = -1000`: el archivo guarda el número digital más 1000. El factor 10000 de la reflectancia se cancela en el cociente y no se aplica.
* **Alternativa descartada:** Calcular los índices con el número digital sin restar el desplazamiento.
* **Evidencia / archivo:** `src/config.py`; `src/features.py`
* **Responsable (humano):** MAGALI POUPARD

### 2026-10-14 — Piso de reflectancia en cero

* **Etapa:** implementación
* **Decisión:** `S2_REFLECTANCIA_MIN = 0`. Después de restar el desplazamiento, todo valor de banda negativo se lleva a 0 antes de NDVI, NDMI y dNDVI. El DN 0 del archivo sigue siendo NaN.
* **Fundamento:** La reflectancia de superficie no puede ser negativa. Un DN entre 1 y 999 queda negativo al restar 1000.
* **Alternativa descartada:** Calcular los índices con valores de banda negativos, que dan resultados fuera del intervalo de −1 a 1.
* **Evidencia / archivo:** `src/config.py`; `src/features.py`
* **Responsable (humano):** MAGALI POUPARD

### 2026-10-14 — Random Forest con índices corregidos

* **Etapa:** implementación
* **Decisión:** Se volvió a entrenar el Random Forest (200 árboles, `class_weight="balanced_subsample"`, semilla 42) con el desplazamiento de 1000 y el piso de reflectancia en 0. La MMU de 0,5 ha se aplicó. Dentro del AOI se removieron 146.043 píxeles por parches menores a 50 píxeles.
* **Superficie por conteo de píxeles dentro del AOI:** clase 1, 798,16 ha; clase 2, 2.061,53 ha; clase 3, 5.709,57 ha; clase 4, 738,90 ha; no cartografiado (`-1`), 1.461,43 ha. No es la superficie ajustada por error.
* **Evidencia / archivo:** `data/processed/mapa_prediccion.tif`; `outputs/resumen_TF_2026-10-14.json`
* **Responsable (humano):** MAGALI POUPARD

---

## 4\. Muestreo y validación

### \_\_\_\_-**\-** — Diseño del muestreo

* **ROI por clase (entrenamiento / validación):**  
* **Independencia:** distancia mínima / fallback documentado  
* **ROI descartados por proximidad:**  
* **Píxeles de validación por polígono:**  
* **Limitación asumida:**

---

## 5\. Implementación asistida por IA

### 2026-10-14 — Bloques asistidos

* **Etapa:** implementación
* **Herramienta / modelo:**   Cursor, con el modelo Grok 4.7, para el trabajo sobre el código. Claude (Anthropic) para orientación metodológica, búsqueda de normativa y bibliografía.
* **Bloques en que intervino la IA:**  - 2026-10-14 — Bloque 1, verificación de AOI y variante (Cursor): recalculó la superficie desde la geometría (10.769,6 ha planimétrica vs. 10.764,4 ha en QGIS), confirmó la variante A y las ventanas, y detectó un error de sintaxis en src/config.py (corregido)
- 2026-10-14 — Bloque 2, revisión de ventanas temporales (Cursor): confirmó que el contraste verano–invierno sirve para separar bosque nativo de sabana / pastizal y señaló sus límites (umbral del 20 %, altura, inundaciones breves, cultivos y forestaciones). Se decide mantener las ventanas. A partir de esta revisión, se incorporó a docs/clases.md el confusor de forestaciones.
- 2026-10-14 — Bloque 3, descarga de Sentinel-2 L2A por STAC (Cursor): instaló las dependencias, ejecutó src/download_s2_stac.py con las ventanas predefinidas y redactó la entrada de la sección 3 (revisada y aceptada). Desactivó, solo para esa descarga, la verificación de certificados de la conexión, que fallaba en esta computadora. Verificación: composiciones revisadas en QGIS sobre el AOI; cubren el área y muestran el contraste esperado entre verano e invierno.
- 2026-10-14 — Bloque 4, revisión src/ingest.py según PIPELINE (Cursor): El archivo ya cumplía lo indicado, no fue necesario modificarlo y no se tocaron los datos de data/raw. Informó que se leen correctamente el AOI, los 29 polígonos de muestra (6 de humedales, 7 de bosque nativo, 11 de sabana / pastizal y 5 de urbanizado) y las dos imágenes, todos en EPSG:5347.
- 2026-10-14 —Bloque 5 (índices): Le pedí a Cursor calcular NDVI, NDMI y dNDVI. Según su respuesta, se generaron 13 capas. Le pregunté por los píxeles con valor 0 y respondió que son muy pocos dentro del AOI.
- 2026-10-14 — Corrección del bloque 5: Al revisar los rangos de los índices con asistencia de Claude, el NDVI máximo de verano (0,69) resultó más bajo de lo esperable. Le consulté a Cursor, que confirmó que las 34 escenas tienen línea de procesamiento 05.11 o 05.12 y que el desplazamiento de 1000 no se restaba. Le pedí restarlo antes de calcular los índices. Según su respuesta, al restar quedaban valores negativos, sobre todo en agua fuera del AOI, que hacían salir los índices de −1 a 1; le pedí llevarlos a 0. No se modificaron los datos originales. El mapa y el resumen del bloque 6 provisorio quedaron incluidos por error en el commit del bloque 5; se reemplazan al volver a ejecutar el bloque 6
- 2026-10-14 — Bloque 6 (modelo y MMU, repetido): Le pedí a Cursor volver a ejecutar el modelo con los índices corregidos y los parámetros de config.py. Según su respuesta, dentro del AOI quedaron 100 píxeles sin dato, que el modelo no clasifica, y la MMU dejó sin clase 1.460 ha (14 % del AOI). Las superficies por conteo de píxeles quedan para ajustar en el bloque 7.
- 2026-10-15 —Bloque 7 (matriz y superficie ajustada): Le pedí a Cursor calcular la matriz de confusión y la superficie ajustada por error. Según su respuesta, la exactitud global es 0,80 (45 píxeles en 9 polígonos de validación) y el bosque nativo ajustado es 1.874 ha (IC 95 %: 1.507–2.241 ha). Claude verificó las cuentas con la fórmula de Olofsson et al. (2014) y coinciden.
* **Decisiones humanas no delegadas:** Elección de la variante y del AOI; esquema de clases y umbrales; MMU; sistema de referencia; ventanas temporales; digitalización y etiquetado de las muestras; interpretación de los resultados. 
* **Verificación aplicada sobre las salidas:** Superficie del AOI contrastada con el cálculo de QGIS y con una verificación independiente; corrección de config.py revisada antes de aceptarla.
* **Responsable (humano):** MAGALI POUPARD

---

## 6\. Validación y superficie

### 2026-10-15 — Resultados

* **OA** (*overall accuracy*, exactitud global): 0,80 (36/45 píxeles de validación).
* **Exactitud del usuario y del productor por clase:** Usuario: clase 1 = 1,00 (4/4); clase 2 = 0,91 (10/11); clase 3 = 0,79 (15/19); clase 4 = 0,64 (7/11). Productor: clase 1 = 0,40 (4/10); clase 2 = 1,00 (10/10); clase 3 = 1,00 (15/15); clase 4 = 0,70 (7/10). Matriz con filas = mapa y columnas = referencia: [[4, 0, 0, 0], [1, 10, 0, 0], [1, 0, 15, 3], [4, 0, 0, 7]].
* **Superficie ajustada por clase (ha) + IC 95 %:** Dentro del área mapeada del AOI (9.308,16 ha; el no cartografiado no entra en los pesos). Clase 1: 1.554,8 ha (826,5–2.283,0). Clase 2: 1.874,1 ha (1.506,8–2.241,4). Clase 3: 4.507,6 ha (3.432,2–5.582,9). Clase 4: 1.371,7 ha (385,0–2.358,4).
* **Superficie por conteo de píxeles (ha):** Clase 1: 798,16. Clase 2: 2.061,53. Clase 3: 5.709,57. Clase 4: 738,90. No cartografiado: 1.461,43, fuera del estimador.
* **Diferencia entre ambas y su interpretación:** El ajuste sube humedales y urbanizado, y baja bosque y sabana / pastizal. De 10 píxeles de referencia de humedal, 6 quedaron en otra clase del mapa (1 en bosque, 1 en sabana / pastizal y 4 en urbanizado). De 10 píxeles de referencia de urbanizado, 3 quedaron en sabana / pastizal, que es la clase con más peso en el mapa. Para el bosque nativo, el conteo de píxeles (2.061,5 ha) queda por encima de la superficie ajustada (1.874,1 ha): el mapa tiende a sobreestimar levemente el bosque.
* **Lo que el mapa NO afirma:** No asigna categorías de conservación del OTBN. No mide altura ni distingue árboles de arbustos. No informa superficie del 13,6 % del AOI que quedó sin clase por la MMU (1.461,43 ha). No valida forestaciones: ningún polígono de la capa roi se dibujó sobre plantaciones. Los intervalos tratan como independientes 45 píxeles de solo 9 polígonos (5 por polígono). La clase 1 del mapa solo tiene 4 píxeles de validación. 
* **Evidencia / archivo:** `outputs/resumen_TF_2026-10-15.json`
* **Responsable (humano):** MAGALI POUPARD

---

## 7\. Cierre

### \_\_\_\_-**\-** — Listo para entrega

* Checklist de `REGLAS_AGENTE.md` §7 revisado: sí / no  
* Limitaciones del resumen incorporadas al informe: sí / no  
* Pendientes: