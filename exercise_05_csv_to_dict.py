# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    result = []
    header = None

    try:
        file = open(filename, "r")
        try:
            for line in file:
                clean_line = line.strip()
                if header is None:
                    if clean_line != "":
                        header = clean_line.split(",")
                        i = 0
                        while i < len(header):
                            header[i] = header[i].strip()
                            i += 1
                else:
                    if clean_line != "":
                        values = clean_line.split(",")
                        i = 0
                        while i < len(values):
                            values[i] = values[i].strip()
                            i += 1

                        row = {}
                        i = 0
                        while i < len(header):
                            key = header[i]
                            value = values[i]
                            if key == "age":
                                row[key] = int(value)
                            else:
                                row[key] = value
                            i += 1
                        result.append(row)
        finally:
            file.close()
    except FileNotFoundError:
        raise

    return result
