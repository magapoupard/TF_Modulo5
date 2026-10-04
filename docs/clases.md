# Definición operativa de clases — TF Módulo 5

**Cursante:** ________________
**Variante:** A / B
**AOI (área de estudio):** ________________   **Superficie aprox. (ha):** ________
**CRS:** ________________
**Fecha:** ________________

Completar **antes** de entrenar. Sin este documento la matriz de confusión no tiene interpretación posible: no se sabría qué se estaba distinguiendo.

Esquema propio, simplificado, orientado a la gestión ambiental rural del NEA. Toma como referencia conceptual los principios de clasificación de cobertura del *Land Cover Classification System* de la FAO (Di Gregorio & Jansen, 2005), pero **no reproduce sus categorías**: es una adaptación del cursante y así debe declararse.

---

## 1. Pregunta de gestión (una frase)

_______________________________________________________________________

**¿Qué decisión administrativa o de manejo depende de la respuesta?**

_______________________________________________________________________

---

## 2. Clases a usar

Marcar las que aplican. **Cada clase marcada necesita al menos 4 polígonos de ROI**, porque el estimador de superficie exige muestras de validación en todas las clases mapeadas.

| Código | Clase | ¿Usamos? | Criterio operativo en nuestro AOI (con umbral explícito) |
| :---: | :--- | :---: | :--- |
| 1 | Agua / cuerpos de agua | ☐ | |
| 2 | Bosque / cubierta leñosa densa | ☐ | |
| 3 | Sabana / mosaico árbol–pastizal | ☐ | |
| 4 | Pastizal / herbáceas | ☐ | |
| 5 | Cultivo / uso agrícola | ☐ | |
| 6 | Suelo desnudo / escasa vegetación | ☐ | |
| 7 | Otra (especificar): ____________ | ☐ | |

*El código del campo `clase` de los ROI debe coincidir con esta tabla.*

**Ejemplo de criterio operativo con umbral:** «Bosque: cobertura arbórea continua mayor al 60 % en un radio de 20 m, altura estimada superior a 5 m.» Sin el umbral, el criterio no es operativo.

---

## 3. Parámetros mínimos

| Parámetro | Valor | Justificación breve |
| :--- | :--- | :--- |
| MMU (*Minimum Mapping Unit*, unidad mínima cartografiable) | ______ ha | |
| Ventana temporal 1 | ______ / ______ | |
| Ventana temporal 2 (recomendada) | ______ / ______ | |
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
