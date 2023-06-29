def calcular_preco_estacionamento(tempo_estacionado):
    preco_hora = 2
    preco_diaria = 24
    preco_mensalidade = 240

    if tempo_estacionado <= 0:
        return 0
    
    if tempo_estacionado <= 12:
        return tempo_estacionado * preco_hora
    elif tempo_estacionado <= 240: # Dez dias
        dias = tempo_estacionado // 24
        horas = tempo_estacionado % 24
        if horas > 12:
            dias += 1
        return dias * preco_diaria
    else:
        meses = tempo_estacionado // (24 * 30)
        dias_restantes = tempo_estacionado % (24 * 30)
        if dias_restantes > 10 * 24:
            meses += 1
        return meses * preco_mensalidade

tempo = int(input("Digite o tempo de estacionamento (em horas): "))
preco = calcular_preco_estacionamento(tempo)
print(f"O preço do estacionamento é: R$ {preco}")
