# Registro de decisiones metodológicas — TF Módulo 5

**Cursante:** **MAGALI POUPARD**

Regla: cada decisión lleva **fecha**, **decisión**, **fundamento** y **alternativa descartada** (si aplica). Referencias en APA 7.ª.

Este archivo es la diferencia entre un método documentado y una sucesión de ajustes. Si un producto cartográfico llega a un expediente administrativo, es lo primero que se pide.

---

## Plantilla de entrada

### 2026-09-29 — Monitoreo Forestal con AI asistida en SIG

* **Etapa:** caso-AOI
* **Decisión:**  Variante A (clasificación de coberturas)
* **Fundamento:** la pregunta es de estado: dónde se encuentran los bosques nativos del ejido y qué superficie ocupan en la actualidad
* **Alternativa descartada:**  Variante B (monitoreo de cambio), porque el  objetivo no es cuantificar pérdida entre dos fechas sino caracterizar la situación actual.
* **Evidencia / archivo:**  data/raw/aoi.geojson (CRS: [EPSG:5347 - POSGAR 2007 / Argentina 5])
* **Responsable (humano):** MAGALI POUPARD

---

## 1\. Caso, AOI y techo de cómputo

### 2026-10-01-**\-** — Variante A y problema de gestión

* **Decisión:**  Variante A (clasificación de coberturas) 
* **Decisión de gestión que depende del mapa:** Actualización del OTBN dentro del Ejido Municipal de Paso de la Patria, Corrientes, como insumo para delimitar áreas no urbanizables en el ámbito de la administración municipal.
* **Fundamento:** se requiere indentificar los bosques nativos del ejido y qué superficie ocupan en la actualidad. Esa información es la base para zonificar el bosque a escala municipal en concordancia con el OTBN provincial y para restringir la urbanización sobre él.

### 2026-10-01-**\-** — Delimitación del AOI (*Area of Interest*)

* **Extensión aproximada (ha):** 10706 mil ha.  
* **¿Respeta el techo 5.000–20.000 ha?** sí 
* **Fundamento del AOI:** Se estableció el polígono correspondiente al area no urbanizada, o con asentamientos muy dispersos

---

## 2\. Clases y umbrales

### 2026-10-01-**\-** — Esquema de clases

* **Decisión:** se seleccionaron 4 clases, bosques nativos, urbanizado, sabana y humedales (vincular a `docs/clases.md`)  
* **MMU** (*Minimum Mapping Unit*): 0.5 ha — **¿se aplicó el tamizado?** sí / no  
* **Alternativa descartada:**

---

## 3\. Evidencia

### \_\_\_\_-**\-** — Ventanas temporales

* **Ventana 1:** \_\_\_\_\_\_ / \_\_\_\_\_\_  
* **Ventana 2:** \_\_\_\_\_\_ / \_\_\_\_\_\_  (si no hay segunda ventana, justificar)  
* **Fundamento fenológico de la elección:**

### \_\_\_\_-**\-** — Sentinel-2 L2A (ESA) y fuente

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

### \_\_\_\_-**\-** — Bloques asistidos

* **Herramienta / modelo:**  
* **Bloques en que intervino la IA:** (un bloque por vez)  
* **Decisiones humanas no delegadas:**  
* **Verificación aplicada sobre las salidas:**

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