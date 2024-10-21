from planilla import consumo_planilla


def test_consumo_planilla():
    assert consumo_planilla(1000, 900, 0.1) == 4.0  # 100 kW, debería aplicar tarifa de dignidad
    assert consumo_planilla(1300, 1000, 0.1) == 30.0  # 300 kW, debería usar tarifa normal
    assert consumo_planilla(1130, 1000, 0.1) == 5.2  # 130 kW, justo en el límite de tarifa de dignidad
    assert consumo_planilla(1000, 1000, 0.1) == 0.0  # Sin consumo
    assert consumo_planilla(1050.5, 1000, 0.1) == 2.02  # Consumo con decimales
    assert consumo_planilla(1200, 1000, 0.03) == 6.0  # Tarifa menor que la de dignidad, debería usar la normal
    print("Pruebas de consumo de planilla pasadas con éxito.")


if __name__ == '__main__':
    test_consumo_planilla()
