"""Variables predictoras: pocas y justificadas.

NDVI  = Normalized Difference Vegetation Index (indice de vegetacion de diferencia normalizada)
NDMI  = Normalized Difference Moisture Index  (indice de humedad de diferencia normalizada)
"""
from __future__ import annotations

import numpy as np

from . import config

BANDAS_REQUERIDAS = ("B2", "B3", "B4", "B8", "B11")


def _dn_a_indice(arr: np.ndarray) -> np.ndarray:
    """Prepara un DN de data/raw para los indices, sin escribir el archivo.

    El 0 del GeoTIFF queda como NaN. Al resto se le resta config.S2_DN_OFFSET.
    Lo que queda por debajo de config.S2_REFLECTANCIA_MIN se lleva a ese piso.
    """
    x = np.array(arr, dtype="float32", copy=True)
    sin_dato = x == 0
    x -= np.float32(config.S2_DN_OFFSET)
    x[sin_dato] = np.nan
    piso = np.float32(config.S2_REFLECTANCIA_MIN)
    negativos = np.isfinite(x) & (x < piso)
    x[negativos] = piso
    return x


def _norm_diff(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    den = (a + b).astype("float32")
    out = np.full(den.shape, np.nan, dtype="float32")
    np.divide(a - b, den, out=out, where=den != 0)
    return out


def ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    return _norm_diff(_dn_a_indice(nir), _dn_a_indice(red))


def ndmi(nir: np.ndarray, swir: np.ndarray) -> np.ndarray:
    return _norm_diff(_dn_a_indice(nir), _dn_a_indice(swir))


def features_ventana(bands: dict[str, np.ndarray], sufijo: str = ""):
    """Devuelve (arreglo apilado, nombres) para una ventana temporal.

    NDMI usa B11 (SWIR1). B12 no entra: no esta justificado en docs/clases.md.
    Las bandas del arreglo ya tienen restado S2_DN_OFFSET. Los indices reciben
    el DN original: ndvi y ndmi aplican el mismo desplazamiento una sola vez.
    """
    faltan = [k for k in BANDAS_REQUERIDAS if k not in bands]
    if faltan:
        raise KeyError(f"Faltan bandas requeridas: {faltan}")

    capas = [_dn_a_indice(bands[b]) for b in ("B2", "B3", "B4", "B8")]
    nombres = [f"B2{sufijo}", f"B3{sufijo}", f"B4{sufijo}", f"B8{sufijo}"]

    v = ndvi(bands["B8"], bands["B4"])
    capas.append(v)
    nombres.append(f"NDVI{sufijo}")

    capas.append(ndmi(bands["B8"], bands["B11"]))
    nombres.append(f"NDMI{sufijo}")

    return np.stack(capas, axis=0), nombres


def combinar_ventanas(bands_v1, bands_v2=None):
    """Apila las variables de una o dos ventanas.

    Con dos ventanas agrega ademas dNDVI = NDVI_v2 - NDVI_v1, que es la variable
    de contraste fenologico (Variante A) o de cambio (Variante B).
    """
    feat, nombres = features_ventana(bands_v1, "_v1")
    if bands_v2 is None:
        return feat, nombres, False

    feat2, nombres2 = features_ventana(bands_v2, "_v2")
    d = (ndvi(bands_v2["B8"], bands_v2["B4"]) - ndvi(bands_v1["B8"], bands_v1["B4"])).astype("float32")
    feat = np.concatenate([feat, feat2, d[None, ...]], axis=0)
    nombres = nombres + nombres2 + ["dNDVI"]
    return feat, nombres, True
