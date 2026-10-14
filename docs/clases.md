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

Dónde se ubican y cuál es la superficie de los bosques nativos, dentro del ejido municipal de Paso de la Patria, Corrientes

**¿Qué decisión administrativa o de manejo depende de la respuesta?**

La actualización del OTBN, dentro del ejido de Paso de la Patria, y las restricciones a la urbanización en correspondencia con las áreas de bosques nativos identificadas.

## 2. Clases a usar

Marcar las que aplican. **Cada clase marcada necesita al menos 4 polígonos de ROI**, porque el estimador de superficie exige muestras de validación en todas las clases mapeadas.

| Código | Clase | ¿Usamos? | Criterio operativo en nuestro AOI (con umbral explícito) |
| :---: | :--- | :---: | :--- |
| 1 | Humedal/ cuerpos de agua | SI |Superficie cubierta por agua, libre o entre vegetación, en al menos una de las dos ventanas, en una superficie continua de al menos 0,5 ha (superficie mínima igual a la MMU)|
| 2 | Bosque nativo | SI |superficie mínima de 0,5 ha de ocupación continua, 3 m de altura mínima y 20 % de cobertura de copas mínima.(criterio para definición de BN conforme Resolución COFEMA 230/12; superficie mínima igual a la MMU)|
| 3 | Sabana / pastizal | SI | Matriz herbácea con árboles o palmeras nativos dispersos, con cobertura de copas menor al 20 %, en una superficie continua de al menos 0,5 ha (superficie mínima igual a la MMU)|
| 4 | Urbanizado | SI | Superficie contínua de 0.50 ha o más, con presencia de construcciones, casas y caminos, en al menos el 30% de la superficie (superficie mínima igual a la MMU)| 
| 5 | Cultivo / uso agrícola | NO | | NO APLICA
| 6 | Suelo desnudo / escasa vegetación | NO| |NO APLICA

*El código del campo `clase` de los ROI debe coincidir con esta tabla.*

**Ejemplo de criterio operativo con umbral:** «Bosque: cobertura arbórea continua mayor al 60 % en un radio de 20 m, altura estimada superior a 5 m.» Sin el umbral, el criterio no es operativo.

---

## 3. Parámetros mínimos

| Parámetro | Valor | Justificación breve |
| :--- | :--- | :--- |
| MMU (*Minimum Mapping Unit*, unidad mínima cartografiable) | 0.5 ha | es el umbral mínimo para los bosques nativos conforme definición de la Resolución del COFEMA 230/12, complementaria a la Ley de OTBN)|
| Ventana temporal 1 | 2026-01-01 / 2026-04-01 | se elige período representativo del verano en la región |
| Ventana temporal 2 (recomendada) | 2026-06-01 / 2026-09-01 |se elige período representativo del invierno en la región |
| Índices | NDVI ☒ NDMI ☒ dNDVI ☒ otro: ______ | NDVI: separa vegetación de agua y suelo desnudo, y distingue niveles de verdor. NDMI: aporta el contenido de humedad de la vegetación, que diferencia la vegetación boscosa del pastizal. dNDVI: mide el cambio de verdor entre verano e invierno (contraste fenológico), principal rasgo para separar bosque nativo de vegetación no boscosa. | 

**Si trabajan con una sola ventana**, escriban aquí por qué y qué clases quedan potencialmente confundidas:

_______________________________________________________________________

---

## 4. Confusores esperados

¿Qué coberturas distintas pueden parecerse a las de interés? (forestaciones, cultivos perennes, pasturas implantadas, suelos compactados, salitrales…)

- **Arbustales densos de menos de 3 m → Bosque nativo.** con alta cobertura pueden confundirse con bosque
- **Formaciones cercanas al 20 % de cobertura de copas → Bosque nativo o Sabana / pastizal.** A 10 m de resolución, árboles dispersos y pasto se mezclan en el mismo píxel; el umbral se aplica al etiquetar las muestras y es esperable confusión en ese límite.
- **Esteros con vegetación que no se inundaron en ninguna ventana → Sabana / pastizal.** El criterio de humedal depende del nivel del agua en las fechas elegidas; en este caso no fue prioritario elegir ventanas conocidas con altos niveles de agua, ya que se prioriza identificar los bosques.
- **Cultivos y lotes arados → Sabana / pastizal o Urbanizado.** No tienen clase propia: con vegetación se parecen al pastizal; arados o recién cosechados, al suelo expuesto de áreas urbanizadas.
- **Viviendas dispersas con jardines o arboleda (quintas, casas de fin de semana) → Sabana / pastizal o Bosque nativo.** Con menos de 30 % de construcciones, o con mucha arboleda, quedan fuera de Urbanizado.
- **Caminos de tierra → Urbanizado o eliminados por la MMU.** Son angostos; la mayoría desaparece con el tamizado y el resto puede confundirse con construcciones._____________________________________________________

---

## 5. Limitación principal (una línea)

La limitación principal consiste en la dificultad para estimar la altura de las copas , el mapa no mide altura ni distingue árboles de arbustos: la separación entre bosque nativo y sabana / pastizal cerca del umbral del 20 % de cobertura, dependen de la fotointerpretación de las muestras y deben verificarse en terreno.__

---

### Referencia

Di Gregorio, A., & Jansen, L. J. M. (2005). *Land Cover Classification System (LCCS): Classification concepts and user manual* (Software version 2). Organización de las Naciones Unidas para la Alimentación y la Agricultura.
