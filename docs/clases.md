# Definición operativa de clases — TF Módulo 5

**Cursante:** MAGALI POUPARD
**Variante:** A 
**AOI (área de estudio):** área no urbanizada del ejido municipal de Paso de la Patria, Corrientes **Superficie aprox. (ha):** 10.764 ha
**CRS:** EPSG:5347 - POSGAR 2007 / Argentina 5
**Fecha:** 2026/10/04 

Completar **antes** de entrenar. Sin este documento la matriz de confusión no tiene interpretación posible: no se sabría qué se estaba distinguiendo.

Esquema propio, simplificado, orientado a la gestión ambiental rural del NEA. Toma como referencia conceptual los principios de clasificación de cobertura del *Land Cover Classification System* de la FAO (Di Gregorio & Jansen, 2005), pero **no reproduce sus categorías**: es una adaptación del cursante y así debe declararse.

---

## 1. Pregunta de gestión (una frase)

¿Dónde se ubican y cuál es la superficie de los bosques nativos, dentro del ejido municipal de Paso de la Patria, Corrientes?

**¿Qué decisión administrativa o de manejo depende de la respuesta?**

La actualización del OTBN dentro del ejido de Paso de la Patria y la definición de restricciones a la urbanización sobre las áreas de bosque nativo identificadas. El mapa es la base sobre la que luego se asignan las categorías de conservación, aplicando los criterios de sustentabilidad ambiental de la Ley 26.331; el mapa por sí solo no asigna categorías.

## 2. Clases a usar

Marcar las que aplican. **Cada clase marcada necesita al menos 4 polígonos de ROI**, porque el estimador de superficie exige muestras de validación en todas las clases mapeadas.

| Código | Clase | ¿Usamos? | Criterio operativo en nuestro AOI (con umbral explícito) |
| :---: | :--- | :---: | :--- |
| 1 | Humedales y cuerpos de agua | Sí | Superficie cubierta por agua, libre o entre vegetación, en al menos una de las dos ventanas, en una superficie continua de al menos 0,5 ha (superficie mínima igual a la MMU). |
| 2 | Bosque nativo | Sí | Formación arbórea natural de especies nativas (incluye palmares; excluye forestaciones) con cobertura de copas ≥ 20 %, altura ≥ 3 m y superficie continua ≥ 0,5 ha (Res. COFEMA 230/12, Pauta 1.2; superficie mínima igual a la MMU). |
| 3 | Sabana / pastizal | Sí | Vegetación herbácea natural, con o sin árboles o palmeras nativos dispersos, con cobertura de copas menor al 20 % (por debajo del umbral de bosque de la Res. COFEMA 230/12), en una superficie continua de al menos 0,5 ha (superficie mínima igual a la MMU). |
| 4 | Urbanizado | Sí | Superficie continua de al menos 0,5 ha con construcciones, viviendas y caminos que ocupan al menos el 30 % de la superficie (superficie mínima igual a la MMU). |
| 5 | Cultivo / uso agrícola | No | No aplica. |
| 6 | Suelo desnudo / escasa vegetación | No | No aplica. |

*El código del campo `clase` de los ROI debe coincidir con esta tabla.*

**Ejemplo de criterio operativo con umbral:** «Bosque: cobertura arbórea continua mayor al 60 % en un radio de 20 m, altura estimada superior a 5 m.» Sin el umbral, el criterio no es operativo.

---

## 3. Parámetros mínimos

| Parámetro | Valor | Justificación breve |
| :--- | :--- | :--- |
| MMU (*Minimum Mapping Unit*, unidad mínima cartografiable) | 0,5 ha | Superficie mínima de bosque nativo según la Res. COFEMA 230/12 (Pauta 1.2), complementaria de la Ley 26.331. Se aplica a todas las clases. |
| Ventana temporal 1 | 2026-01-01 / 2026-04-01 | Verano: máximo verdor de todas las coberturas vegetales. |
| Ventana temporal 2 (recomendada) | 2026-06-01 / 2026-09-01 | Invierno: pastizales se secan; el bosque nativo conserva el follaje. |
| Índices | NDVI ☒ NDMI ☒ dNDVI ☒ otro: — | NDVI: separa vegetación de agua y suelo, y distingue niveles de verdor. NDMI: aporta el contenido de humedad de la vegetación, que diferencia la vegetación boscosa del pastizal seco. dNDVI: mide el cambio de verdor entre verano e invierno (contraste fenológico), principal rasgo para separar bosque nativo de vegetación no boscosa. |

**Si trabajan con una sola ventana**, escriban aquí por qué y qué clases quedan potencialmente confundidas: No aplica: se trabaja con dos ventanas
______________________________

---

## 4. Confusores esperados

¿Qué coberturas distintas pueden parecerse a las de interés? (forestaciones, cultivos perennes, pasturas implantadas, suelos compactados, salitrales…)

- **Arbustales densos de menos de 3 m → Bosque nativo.** con alta cobertura pueden confundirse con bosque, Sentinel-2 no mide altura, y la Res. COFEMA 230/12 excluye los arbustales puros.
- **Formaciones cercanas al 20 % de cobertura de copas → Bosque nativo o Sabana / pastizal.** A 10 m de resolución, árboles dispersos y pasto se mezclan en el mismo píxel; el umbral se aplica al etiquetar las muestras y es esperable confusión en ese límite.
- **Esteros con vegetación que no se inundaron en ninguna ventana → Sabana / pastizal.** El criterio de humedal depende del nivel del agua en las fechas elegidas; en este caso no fue prioritario elegir ventanas conocidas con altos niveles de agua, ya que se prioriza identificar los bosques.
- **Cultivos y lotes arados → Sabana / pastizal o Urbanizado.** No tienen clase propia: con vegetación se parecen al pastizal; arados o recién cosechados, al suelo expuesto de áreas urbanizadas.
- **Viviendas dispersas con jardines o arboleda (quintas, casas de fin de semana) → Sabana / pastizal o Bosque nativo.** Con menos de 30 % de construcciones, o con mucha arboleda, quedan fuera de Urbanizado.
- **Caminos de tierra → Urbanizado o eliminados por la MMU.** Son angostos; la mayoría desaparece con el tamizado y el resto puede confundirse con construcciones._____________________________________________________


## 5. Limitación principal (una línea)

El mapa no mide altura ni distingue árboles de arbustos: la separación entre bosque nativo y sabana / pastizal cerca del umbral del 20 % de cobertura depende de la fotointerpretación de las muestras y debe verificarse en terreno.



### Referencias

Consejo Federal de Medio Ambiente. (2012). *Resolución N.º 230/2012: Pautas para la consideración, identificación y mapeo de los bosques nativos en el Ordenamiento Territorial de Bosques Nativos*. https://www.mendoza.gov.ar/wp-content/uploads/sites/33/2023/05/Res-230-2012-COFEMA.pdf

Convención relativa a los Humedales de Importancia Internacional especialmente como Hábitat de Aves Acuáticas [Convención de Ramsar], 2 de febrero de 1971, art. 1.1.     Ley 23.919 de 1991. Aprueba la Convención en Argentina.

Di Gregorio, A., & Jansen, L. J. M. (2005). *Land Cover Classification System (LCCS): Classification concepts and user manual* (Software version 2). Organización de las Naciones Unidas para la Alimentación y la Agricultura.
