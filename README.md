# Proyecto de Aprendizaje Automático
Pablo Berástegui Magallón (202311460)
Ingeniería Matemática e Inteligencia Artificial
Universidad Pontificia Comillas

### Ficheros principales del proyecto

- **notebooks/**: Contiene los cuadernos Jupyter (`.ipynb`) utilizados para el análisis y desarrollo del proyecto. Cada cuaderno está documentado y corresponde a una etapa específica del flujo de trabajo:
    - `exploration.ipynb`: Limpieza, preparación y visualización de los datos.
    - `models.ipynb`: Implementación y evaluación de todos los modelos.
    - `test_prep.ipynb`: Preparación de los datos de test para su predicción
- **data/**: Carpeta con los conjuntos de datos utilizados, tanto en bruto como procesados.
- **src/**: Código fuente con funciones auxiliares y scripts reutilizables.
    - `utils.py`: contiene una función hecha para visualizar mejor y unos diccionarios de mapeo


## Descripción general

Este proyecto aborda la predicción de la nota final (`T3`) de estudiantes de secundaria a partir de variables sociodemográficas, académicas y de comportamiento. Se han aplicado técnicas de aprendizaje supervisado y no supervisado, utilizando dos enfoques:

- **Modelo (i)**: incluye todas las variables disponibles, incluidas `T1` y `T2` (notas previas).
- **Modelo (ii)**: excluye `T1` y `T2`, con el objetivo de anticipar el rendimiento antes de que el estudiante haya sido evaluado.

**Nota**: se ha optado por emplear los códigos de scickit-learn por sencillez, coherencia sintáctica y eficiencia computacional.