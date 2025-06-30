"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    
    # Importar las librerías necesarias
    import pandas as pd
    import os

    # Paso 1: Leer el archivo CSV con separador punto y coma
    datos = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")

    # Paso 2: Eliminar filas con datos faltantes (valores NaN)
    datos = datos.dropna()
    
    # Paso 3: Normalizar columnas de texto - convertir a minúsculas
    datos["sexo"] = datos["sexo"].str.lower()
    datos["tipo_de_emprendimiento"] = datos["tipo_de_emprendimiento"].str.lower()

    # Paso 4: Limpiar y normalizar la columna 'idea_negocio'
    # - Convertir a minúsculas
    # - Reemplazar guiones bajos por espacios
    # - Reemplazar guiones por espacios
    # - Eliminar espacios al inicio y final
    datos["idea_negocio"] = (
        datos["idea_negocio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
        .str.strip()
    )

    # Paso 5: Limpiar y normalizar la columna 'barrio'
    # - Convertir a minúsculas
    # - Reemplazar guiones bajos por espacios
    # - Reemplazar guiones por espacios
    datos["barrio"] = (
        datos["barrio"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    # Paso 6: Definir función para normalizar fechas
    # Convierte fechas del formato YYYY/MM/DD al formato DD/MM/YYYY
    def normalizar_fechas(fecha):
        # Dividir la fecha por el separador "/"
        partes = fecha.split("/")
        # Si el primer elemento tiene 4 dígitos (año), reorganizar la fecha
        if len(partes[0]) == 4:
            return f"{partes[2]}/{partes[1]}/{partes[0]}"
        return fecha

    # Paso 7: Aplicar la normalización de fechas a la columna correspondiente
    datos["fecha_de_beneficio"] = datos["fecha_de_beneficio"].apply(normalizar_fechas)

    # Paso 8: Limpiar y convertir la columna 'monto_del_credito' a números
    # - Eliminar espacios en blanco
    # - Eliminar el símbolo de pesos "$"
    # - Eliminar comas separadoras de miles
    # - Convertir a tipo float (número decimal)
    datos["monto_del_credito"] = (
        datos["monto_del_credito"]
        .str.replace(" ", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # Paso 9: Limpiar y normalizar la columna 'línea_credito'
    # - Convertir a minúsculas
    # - Reemplazar guiones bajos por espacios
    # - Reemplazar guiones por espacios
    datos["línea_credito"] = (
        datos["línea_credito"]
        .str.lower()
        .str.replace("_", " ", regex=False)
        .str.replace("-", " ", regex=False)
    )

    # Paso 10: Definir las columnas que se usarán para identificar duplicados
    columnas_unicas = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "comuna_ciudadano",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito"
    ]
   
    # Paso 11: Eliminar registros duplicados basándose en las columnas especificadas
    datos = datos.drop_duplicates(subset=columnas_unicas)

    # Paso 12: Crear el directorio de salida si no existe
    os.makedirs(os.path.dirname("files/output/solicitudes_de_credito.csv"), exist_ok=True)
   
    # Paso 13: Guardar el archivo limpio en la carpeta de salida
    # Usar separador punto y coma y no incluir el índice
    datos.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

pregunta_01()
