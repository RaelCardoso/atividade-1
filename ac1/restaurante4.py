def calcular_conta_e_gorjeta(valor_despesa):
    gorjeta = valor_despesa * 0.1
    valor_total_conta = valor_despesa + gorjeta
    return valor_total_conta, gorjeta
