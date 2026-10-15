"""Parametros del Trabajo Final. Todo umbral del proyecto vive aqui.

Regla del modulo: ningun valor numerico decidido por el analista puede estar
escrito dentro de otro script. Si aparece un numero nuevo, viene a este archivo
y se justifica en docs/decisiones.md.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_INTERIM = ROOT / "data" / "interim"
DATA_PROCESSED = ROOT / "data" / "processed"
OUTPUTS = ROOT / "outputs"

# ---------------------------------------------------------------------------
# 1. Identificacion (completar)
# ---------------------------------------------------------------------------
CURSANTE = "MAGALI POUPARD"  
AOI_NOMBRE = "Área no urbanizada correspondiente al ejidomunicipal de Paso de la Patria"     

# ---------------------------------------------------------------------------
# 2. Marco espacial
# ---------------------------------------------------------------------------
CRS = "EPSG:5347"  # (POSGAR 2007 / Argentina faja 5)
PIXEL_M = 10.0     # Sentinel-2
MMU_HA = 0.5       # Minimum Mapping Unit (unidad minima cartografiable)
APLICAR_MMU = True       # si True, los parches < MMU se marcan como no cartografiados

# ---------------------------------------------------------------------------
# 3. Variante y clases
# ---------------------------------------------------------------------------
VARIANTE = "A"                # "A" coberturas | "B" cambio
BAND_NAMES = ["B2", "B3", "B4", "B8", "B11", "B12"]

# ---------------------------------------------------------------------------
# 4. Ventanas temporales  (completar: sin esto no se descarga nada)
# ---------------------------------------------------------------------------
# Cada ventana es (inicio, fin) en formato ISO. El modulo sostiene que la
# fenologia es el rasgo discriminante principal en sabanas y pastizales:
#   - 1 ventana  -> modo mono-fecha. Admitido, pero limita las clases separables.
#                   Debe declararse como limitacion en el resumen.
#   - 2 ventanas -> contraste fenologico (Variante A) o dos fechas (Variante B).
# Elegir estaciones contrastantes del MISMO ciclo hidrologico y del ano vigente.
VENTANAS: list[tuple[str, str]] = [("2026-01-01", "2026-04-01"), ("2026-06-01", "2026-09-01")]
# Ejemplo: [("2026-01-01", "2026-03-15"), ("2026-07-01", "2026-09-15")]

MAX_CLOUD = 20                # % de nubosidad maxima por escena
COMPOSITE = "median"          # composicion dentro de cada ventana: "median" | "mean"

# Desplazamiento del numero digital (DN) de Sentinel-2 L2A.
# Desde la linea de procesamiento 04.00, la ESA define BOA_ADD_OFFSET = -1000:
# el GeoTIFF guarda DN = reflectancia * 10000 + 1000, y el valor para los
# indices es DN - 1000. Las 34 escenas de este TF tienen s2:processing_baseline
# 05.11 o 05.12. features.py resta S2_DN_OFFSET; no reescribe data/raw.
# El factor 10000 se cancela en NDVI y NDMI, y no se aplica.
# Un DN igual a 0 en el archivo es sin dato: pasa a NaN antes de restar.
S2_DN_OFFSET = 1000
# Piso de la reflectancia despues de restar S2_DN_OFFSET. Un DN entre 1 y 999
# queda negativo; la reflectancia de superficie no puede ser negativa y se
# lleva a este piso antes de los indices. El DN 0 sigue siendo NaN.
S2_REFLECTANCIA_MIN = 0

# ---------------------------------------------------------------------------
# 5. Modelo
# ---------------------------------------------------------------------------
RANDOM_STATE = 42
N_TREES = 200

# ---------------------------------------------------------------------------
# 6. Muestreo y validacion
# ---------------------------------------------------------------------------
FRAC_VAL = 0.30               # proporcion de ROI reservados a validacion
MIN_DIST_VAL_M = 200.0        # distancia minima entre centroides train / val
MAX_PX_TRAIN_POR_ROI = 300    # tope de pixeles de entrenamiento por poligono
MAX_PX_VAL_POR_ROI = 5        # pixeles de validacion por poligono (pocos: dentro de un ROI estan autocorrelacionados)
Z_95 = 1.96                   # cuantil normal para intervalos del 95 %

# ---------------------------------------------------------------------------
# 7. Rutas de insumos
# ---------------------------------------------------------------------------
AOI_PATH = DATA_RAW / "aoi.geojson"
ROI_PATH = DATA_RAW / "rois.geojson"
STACK_PATH = DATA_RAW / "stack_s2_v1.tif"      # ventana 1
STACK_T2_PATH = DATA_RAW / "stack_s2_v2.tif"   # ventana 2 (opcional)

# ---------------------------------------------------------------------------
# 8. Fuente de imagenes
# ---------------------------------------------------------------------------
STAC_URL = "https://planetarycomputer.microsoft.com/api/stac/v1"
STAC_COLLECTION = "sentinel-2-l2a"             # Sentinel-2 L2A (ESA)
