# Definición operativa de clases — TF Módulo 5

**Cursante:** MAGALI POUPARD
**Variante:** A 
**AOI (área de estudio):** área no urbanizada del ejido municipal de Paso de la Patria, Corrientes **Superficie aprox. (ha):** 10.706 ha
**CRS:** EPSG:5347 - POSGAR 2007 / Argentina 5
**Fecha:** 2026/10/04

Completar **antes** de entrenar. Sin este documento la matriz de confusión no tiene interpretación posible: no se sabría qué se estaba distinguiendo.

Esquema propio, simplificado, orientado a la gestión ambiental rural del NEA. Toma como referencia conceptual los principios de clasificación de cobertura del *Land Cover Classification System* de la FAO (Di Gregorio & Jansen, 2005), pero **no reproduce sus categorías**: es una adaptación del cursante y así debe declararse.

---

## 1. Pregunta de gestión (una frase)

Dónde se ubican y cuál es la superficie de los bosques nativos, y sus categorías, dentro del ejido municipal de Paso de la Patria, Corrientes

**¿Qué decisión administrativa o de manejo depende de la respuesta?**

La actualización del OTBN, dentro del ejido de Paso de la Patria, y las restricciones a la urbanización en correspondencia con las áreas de bosques nativos de categorías 1 y 2 identificadas.

## 2. Clases a usar

Marcar las que aplican. **Cada clase marcada necesita al menos 4 polígonos de ROI**, porque el estimador de superficie exige muestras de validación en todas las clases mapeadas.

| Código | Clase | ¿Usamos? | Criterio operativo en nuestro AOI (con umbral explícito) |
| :---: | :--- | :---: | :--- |
| 1 | Agua / cuerpos de agua /humedal| SI |superficie cubierta por agua libre, en las dos ventanas.
| 2 | Bosque / cubierta leñosa densa | SI |superficie mínima de 0,5 ha de ocupación continua, 3 m de altura mínima y 20 % de cobertura de copas mínima.(criterio para definición de BN conforme Resolución COFEMA 230/12)|
| 3 | Sabana / mosaico árbol–pastizal | SI |Matriz herbácea con árboles o palmeras nativos dispersos, con cobertura de copas entre 5 % y menos de 20 %, en una superficie continua de al menos 0,5 ha (ref.: "otras tierras forestales", Inventario Nacional de Bosques Nativos; superficie mínima igual a la MMU)|
| 4 | Pastizal / herbáceas | SI |Vegetación herbácea con cobertura de copas arbóreas menor al 5 %, en una superficie continua de al menos 0,5 ha (superficie mínima igual a la MMU). |
| 5 | Cultivo / uso agrícola | NO | | NO APLICA
| 6 | Suelo desnudo / escasa vegetación | NO| |NO APLICA
| 7 | Humedal | SI |superficie cubierta por agua libre o con vegetación, en una de las dos ventanas.
| 8 | Urbanizado |SI | Superficie contínua de 0.50 ha o más, con presencia de construcciones, casas y caminos, en al menos el 30% de la superficie |

*El código del campo `clase` de los ROI debe coincidir con esta tabla.*

**Ejemplo de criterio operativo con umbral:** «Bosque: cobertura arbórea continua mayor al 60 % en un radio de 20 m, altura estimada superior a 5 m.» Sin el umbral, el criterio no es operativo.

---

## 3. Parámetros mínimos

| Parámetro | Valor | Justificación breve |
| :--- | :--- | :--- |
| MMU (*Minimum Mapping Unit*, unidad mínima cartografiable) | 0.5 ha | es el umbral mínimo para los bosques nativos conforme definición de la Resolución del COFEMA 230/12, complementaria a la Ley de OTBN) |
| Ventana temporal 1 |2025-12-01  /2026-02-01 | |
| Ventana temporal 2 (recomendada) |2026-05-01 /2026-08-01 | |
| Índices | NDVI ☐ NDMI ☐ dNDVI ☐ otro: ______ | |

**Si trabajan con una sola ventana**, escriban aquí por qué y qué clases quedan potencialmente confundidas:

_______________________________________________________________________

---

## 4. Confusores esperados

¿Qué coberturas distintas pueden parecerse a las de interés? (forestaciones, cultivos perennes, pasturas implantadas, suelos compactados, salitrales…)

_______________________________________________________________________

---

## 5. Limitación principal (una línea)

_______________________________________________________________________

---

### Referencia

Di Gregorio, A., & Jansen, L. J. M. (2005). *Land Cover Classification System (LCCS): Classification concepts and user manual* (Software version 2). Organización de las Naciones Unidas para la Alimentación y la Agricultura.
