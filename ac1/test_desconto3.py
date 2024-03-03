import pytest
from desconto3 import calcular_valor_promocional

def test_calculo_valor_promocional():
    
    valor_original_1 = 500.00
    desconto_1 = 50.00
    valor_promocional_esperado_1 = 450.00

    valor_promocional_calculado_1 = calcular_valor_promocional(valor_original_1, desconto_1)

    assert valor_promocional_calculado_1 == pytest.approx(valor_promocional_esperado_1, abs=1e-2)

    
    valor_original_2 = 10500.00
    desconto_2 = 500.00
    valor_promocional_esperado_2 = 10000.00

    valor_promocional_calculado_2 = calcular_valor_promocional(valor_original_2, desconto_2)

    assert valor_promocional_calculado_2 == pytest.approx(valor_promocional_esperado_2, abs=1e-2)

    # Terceiro teste
    valor_original_3 = 90.00
    desconto_3 = 0.80
    valor_promocional_esperado_3 = 89.20

    valor_promocional_calculado_3 = calcular_valor_promocional(valor_original_3, desconto_3)

    assert valor_promocional_calculado_3 == pytest.approx(valor_promocional_esperado_3, abs=1e-2)