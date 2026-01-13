import pandas as pd

def test_setup():
    print("--- Verificando Entorno ---")
    print(f"Versión de Pandas: {pd.__version__}")
    print("¡Todo listo para empezar a trabajar con datos!")

if __name__ == "__main__":
    test_setup()