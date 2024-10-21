import random
from sistema_riego import simular_riego


def test_sistema_riego():
    random.seed(42)

    assert simular_riego() == "OK"

    print("Todas las pruebas pasaron exitosamente.")


if __name__ == "__main__":
    test_sistema_riego()
