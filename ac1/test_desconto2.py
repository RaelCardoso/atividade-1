import pytest
from desconto2 import calcular_desconto

def test_calculo_desconto():
    
    valor_produto_1 = 100
    novo_valor_esperado_1 = 91.00
    desconto_esperado_1 = 9.00

    novo_valor_calculado_1, desconto_calculado_1 = calcular_desconto(valor_produto_1)

    assert novo_valor_calculado_1 == pytest.approx(novo_valor_esperado_1, abs=1e-2)
    assert desconto_calculado_1 == pytest.approx(desconto_esperado_1, abs=1e-2)

    
    valor_produto_2 = 1500
    novo_valor_esperado_2 = 1365.00
    desconto_esperado_2 = 135.00

    novo_valor_calculado_2, desconto_calculado_2 = calcular_desconto(valor_produto_2)

    assert novo_valor_calculado_2 == pytest.approx(novo_valor_esperado_2, abs=1e-2)
    assert desconto_calculado_2 == pytest.approx(desconto_esperado_2, abs=1e-2)

    
    valor_produto_3 = 60000
    novo_valor_esperado_3 = 54600.00
    desconto_esperado_3 = 5400.00

    novo_valor_calculado_3, desconto_calculado_3 = calcular_desconto(valor_produto_3)

    assert novo_valor_calculado_3 == pytest.approx(novo_valor_esperado_3, abs=1e-2)
    assert desconto_calculado_3 == pytest.approx(desconto_esperado_3, abs=1e-2)