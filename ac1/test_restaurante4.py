import pytest
from restaurante4 import calcular_conta_e_gorjeta

def test_calcular_conta_e_gorjeta():
    # Teste 1
    valor_despesa_1 = 75.00
    total_conta_esperado_1 = 82.50
    gorjeta_esperada_1 = 7.50

    total_conta_calculado_1, gorjeta_calculada_1 = calcular_conta_e_gorjeta(valor_despesa_1)

    assert total_conta_calculado_1 == pytest.approx(total_conta_esperado_1, abs=1e-2)
    assert gorjeta_calculada_1 == pytest.approx(gorjeta_esperada_1, abs=1e-2)

    # Teste 2
    valor_despesa_2 = 125.00
    total_conta_esperado_2 = 137.50
    gorjeta_esperada_2 = 12.50

    total_conta_calculado_2, gorjeta_calculada_2 = calcular_conta_e_gorjeta(valor_despesa_2)

    assert total_conta_calculado_2 == pytest.approx(total_conta_esperado_2, abs=1e-2)
    assert gorjeta_calculada_2 == pytest.approx(gorjeta_esperada_2, abs=1e-2)

    # Teste 3
    valor_despesa_3 = 350.87
    total_conta_esperado_3 = 385.96
    gorjeta_esperada_3 = 35.09

    total_conta_calculado_3, gorjeta_calculada_3 = calcular_conta_e_gorjeta(valor_despesa_3)

    assert total_conta_calculado_3 == pytest.approx(total_conta_esperado_3, abs=1e-2)
    assert gorjeta_calculada_3 == pytest.approx(gorjeta_esperada_3, abs=1e-2)