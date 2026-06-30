import json
import re


def procesar_proyectos(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as f:
            datos = json.load(f)

        for item in datos:

            match item.get("estado"):
                case "activo":
                    print(f"Proyecto {item['nombre']} está en ejecución.")
                case "pendiente":
                    print(f"Proyecto {item['nombre']} requiere atención.")
                case _:
                    print(f"Estado desconocido para {item['nombre']}")

            if not re.match(r"^[A-Z][a-z]+ [A-Z]$", item["nombre"]):
                print(
                    f"¡Aviso! El nombre '{item['nombre']}' no sigue el formato estándar."
                )

    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except json.JSONDecodeError:
        print("Error: El formato del JSON es inválido.")
    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    procesar_proyectos("src/fundamentos/datos.json")
