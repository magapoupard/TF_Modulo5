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

### 2026-10-13 — Sentinel-2 L2A (ESA) y fuente

* **Fuente:** STAC (*SpatioTemporal Asset Catalog*) / Copernicus Data Space / GEE / paquete del docente  
* **Escenas por ventana y nubosidad:**  
* **Composición:** mediana / media  
* **Índices:** NDVI, NDMI, dNDVI, otros:

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
* **Decisiones humanas no delegadas:** Elección de la variante y del AOI; esquema de clases y umbrales; MMU; sistema de referencia; ventanas temporales; digitalización y etiquetado de las muestras; interpretación de los resultados. 
* **Verificación aplicada sobre las salidas:** Superficie del AOI contrastada con el cálculo de QGIS y con una verificación independiente; corrección de config.py revisada antes de aceptarla.
* **Responsable (humano):** MAGALI POUPARD

---

## 6\. Validación y superficie

### \_\_\_\_-**\-** — Resultados

* **OA** (*overall accuracy*, exactitud global):  
* **Exactitud del usuario y del productor por clase:**  
* **Superficie ajustada por clase (ha) \+ IC 95 %:**  
* **Superficie por conteo de píxeles (ha):**  
* **Diferencia entre ambas y su interpretación:**  
* **Lo que el mapa NO afirma:**

---

## 7\. Cierre

### \_\_\_\_-**\-** — Listo para entrega

* Checklist de `REGLAS_AGENTE.md` §7 revisado: sí / no  
* Limitaciones del resumen incorporadas al informe: sí / no  
* Pendientes: