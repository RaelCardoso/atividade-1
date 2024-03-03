def calcular_salario_liquido(valor_hora_aula, num_aulas_dadas, percentual_desconto_inss, salario):
    salario_bruto = valor_hora_aula * num_aulas_dadas
    desconto_inss = salario_bruto * (percentual_desconto_inss / 100)
    salario_liquido = salario_bruto - desconto_inss
    return salario_liquido