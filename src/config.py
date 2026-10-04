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
CURSANTE = ""                 # apellido y nombre
AOI_NOMBRE = ""               # nombre del area de estudio

# ---------------------------------------------------------------------------
# 2. Marco espacial
# ---------------------------------------------------------------------------
CRS = "EPSG:32721"            # UTM metrico; 32721 = 21S. Ajustar al AOI.
PIXEL_M = 10.0                # Sentinel-2
MMU_HA = 0.5                  # Minimum Mapping Unit (unidad minima cartografiable)
APLICAR_MMU = True            # si True, los parches < MMU se marcan como no cartografiados

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
VENTANAS: list[tuple[str, str]] = []
# Ejemplo: [("2026-01-01", "2026-03-15"), ("2026-07-01", "2026-09-15")]

MAX_CLOUD = 20                # % de nubosidad maxima por escena
COMPOSITE = "median"          # composicion dentro de cada ventana: "median" | "mean"

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
