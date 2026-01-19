import pandas as pd
import numpy as np

def optimal_bins(data: pd.Series) -> int:
    """
    Calcula el número óptimo de bins usando la regla de Freedman-Diaconis para histogramas.
    Args: data (pd.Series): Serie de datos para la que se desea calcular el número óptimo de bins.
    Returns: int: Número óptimo de bins.
    """

    q25, q75 = np.percentile(data, [25, 75])  # Cálculo del rango intercuartílico (IQR)
    iqr = q75 - q25
    bin_width = 2 * iqr / (len(data) ** (1/3))  # Ancho de cada bin
    bins = int((data.max() - data.min()) / bin_width) if bin_width > 0 else 10  # Número de bins

    return bins

variable_name_map = {
    "escuela": "Instituto del estudiante",
    "sexo": "Sexo del estudiante",
    "edad": "Edad del estudiante",
    "entorno": "Tipo de zona en la que vive el estudiante",
    "TamFam": "Tamaño de la familia (número de miembros)",
    "EstPadres": "Convivencia de los padres",
    "Medu": "Nivel educativo de la madre",
    "Pedu": "Nivel educativo del padre",
    'PMedu': 'Promedio del nivel educativo de los padres',
    "Mtrab": "Trabajo de la madre",
    "Ptrab": "Trabajo del padre",
    "razon": "Razón para elegir este instituto",
    "tutor": "Tutor legal",
    "TiempoViaje": "Tiempo de viaje hasta la escuela",
    "TiempoEstudio": "Tiempo de estudio semanal",
    "suspensos": "Número de suspensos en el curso anterior",
    "apoyo": "Apoyo educativo del centro",
    "ApFam": "Apoyo educativo familiar",
    "academia": "Academia o clases particulares",
    "extras": "Actividades extraescolares",
    "enfermeria": "Ha acudido a la enfermería durante el curso",
    "EstSup": "Intención de cursar estudios superiores",
    "internet": "Acceso a internet en casa",
    "pareja": "Tiene pareja sentimental",
    "RelFam": "Calidad de las relaciones familiares",
    "TiempoLib": "Tiempo libre después de clase",
    "SalAm": "Frecuencia con la que sale con amigos",
    "AlcSem": "Consumo de alcohol entre semana",
    "AlcFin": "Consumo de alcohol en fines de semana",
    "Alc": "Consumo de alcohol en general",
    "salud": "Estado de salud",
    "faltas": "Número de faltas",
    "asignatura": "Asignatura",
    "T1": "Nota del primer trimestre",
    "T2": "Nota del segundo trimestre",
    "T3": "Nota final"
}


categories_map = {
    # 1. Instituto (escuela)
    'escuela': {
        'BG': 'Beatriz Galindo',
        'IC': 'Instituto Cervantes'
    },
    # 2. Sexo
    'sexo': {
        'M': 'Masculino',
        'F': 'Femenino'
    },
    # 4. Entorno
    'entorno': {
        'U': 'Urbana',
        'R': 'Rural'
    },
    # 6. Estado de los padres
    'EstPadres': {
        'J': 'Juntos',
        'S': 'Separados'
    },
    # 7. & 8. Nivel educativo (Madre/Padre)
    'Medu': {
        0: 'No tiene nivel constatado',
        1: 'Primaria',
        2: 'Secundaria',
        3: 'Graduado',
        4: 'Máster y/o Doctorado'
    },
    'Pedu': {
        0: 'No tiene nivel constatado',
        1: 'Primaria',
        2: 'Secundaria',
        3: 'Graduado',
        4: 'Máster y/o Doctorado'
    },
    # 13. Tiempo de viaje
    'TiempoViaje': {
        1: '<15mins',
        2: '15-30mins',
        3: '30mins-1h',
        4: '>1h'
    },
    # 14. Tiempo de estudio semanal
    'TiempoEstudio': {
        1: '<2h',
        2: '2-5h',
        3: '5-10h',
        4: '>10h'
    },
    # 15. Número de suspensos en el curso anterior
    'suspensos': {
        0: '0 suspensos',
        1: '1 suspenso',
        2: '2 suspensos',
        3: '3 suspensos',
        4: 'Más de 4 suspensos'
    },
    # 24. RelFam: calidad de relaciones familiares
    'RelFam': {
        1: 'Mala relación familiar',
        2: 'Algo conflictiva',
        3: 'Neutra',
        4: 'Buena relación',
        5: 'Excelente relación'
    },
    # 25. Tiempo libre
    'TiempoLib': {
        1: 'Poco tiempo libre',
        2: 'Algo de tiempo libre',
        3: 'Tiempo libre moderado',
        4: 'Bastante tiempo libre',
        5: 'Mucho tiempo libre'
    },
    # 26. Salir con amigos
    'SalAm': {
        1: 'Rara vez',
        2: 'Ocasionalmente',
        3: 'Varias veces por semana',
        4: 'Con mucha frecuencia',
        5: 'Todos los días'
    },
    # 27 & 28. Alcohol entre semana / fines de semana
    'AlcSem': {
        1: 'Nada o muy poco',
        2: 'Bajo consumo',
        3: 'Moderado',
        4: 'Frecuente',
        5: 'Alto consumo'
    },
    'AlcFin': {
        1: 'Nada o muy poco',
        2: 'Bajo consumo',
        3: 'Moderado',
        4: 'Frecuente',
        5: 'Alto consumo'
    },
    # 29. salud
    'salud': {
        1: 'Mala',
        2: 'Regular',
        3: 'Aceptable',
        4: 'Buena',
        5: 'Excelente'
    },
    # 31. Asignatura
    'asignatura': {
        'M': 'Matemáticas',
        'L': 'Lengua y Literatura'
    }
}
