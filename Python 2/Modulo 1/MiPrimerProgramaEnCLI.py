"""Archivo de práctica con código de relleno para CLI."""

from datetime import datetime


def saludar(nombre: str) -> str:
    return f"Hola, {nombre}. Bienvenido a tu primer programa en CLI."


def sumar_lista(numeros: list[int]) -> int:
    total = 0
    for n in numeros:
        total += n
    return total


def generar_reporte() -> dict:
    datos = {
        "usuario": "Aldri",
        "fecha": datetime.now().isoformat(timespec="seconds"),
        "items": ["python", "cli", "github", "git"],
        "activo": True,
    }
    return datos


def imprimir_menu() -> None:
    print("=" * 40)
    print("        MI PRIMER PROGRAMA EN CLI")
    print("=" * 40)
    print("1) Saludar")
    print("2) Sumar lista de ejemplo")
    print("3) Ver reporte")
    print("4) Salir")


def ejecutar_demo() -> None:
    print(saludar("Mundo"))
    ejemplo = [10, 20, 30, 40, 50]
    print(f"Suma de {ejemplo}: {sumar_lista(ejemplo)}")
    print("Reporte:")
    for clave, valor in generar_reporte().items():
        print(f"- {clave}: {valor}")


if __name__ == "__main__":
    imprimir_menu()
    ejecutar_demo()
