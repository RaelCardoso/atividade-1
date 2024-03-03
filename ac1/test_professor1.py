import pytest
from professor1 import calcular_salario_liquido

def test_calculo_salario_liquido():

    valor_hora_aula_1 = 6.25
    num_aulas_dadas_1 = 160
    percentual_desconto_inss_1 = 1.3
    salario_1 = 987

    salario_liquido_1 = calcular_salario_liquido(valor_hora_aula_1,num_aulas_dadas_1, percentual_desconto_inss_1, percentual_desconto_inss_1, salario_1)

    assert salario_liquido_1 == pytest.approx(987.0, abs=1e-2)


    valor_hora_aula_2 = 20.5
    num_aulas_dadas_2 = 240
    percentual_desconto_inss_2 = 1.7
    salario_2 = 4836.36

    salario_liquido_2 = calcular_salario_liquido(valor_hora_aula_2,num_aulas_dadas_2, percentual_desconto_inss_2, percentual_desconto_inss_2, salario_2)

    assert salario_liquido_2 == pytest.approx(4836.36, abs=1e-2)


    valor_hora_aula_3 = 13.9
    num_aulas_dadas_3 = 200
    percentual_desconto_inss_3 = 6.48
    salario_3 = 2599.86

    salario_liquido_3 = calcular_salario_liquido(valor_hora_aula_3,num_aulas_dadas_3, percentual_desconto_inss_3, percentual_desconto_inss_3, salario_3)

    assert salario_liquido_3 == pytest.approx(4836.36, abs=1e-2)