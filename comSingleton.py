class CalculadoraEstacionamento:
    __instance = None

    @staticmethod
    def get_instance():
        if not CalculadoraEstacionamento.__instance:
            CalculadoraEstacionamento()
        return CalculadoraEstacionamento.__instance

    def __init__(self):
        if CalculadoraEstacionamento.__instance:
            raise Exception("Sou um Singleton, saia daqui!")
        else:
            CalculadoraEstacionamento.__instance = self

    def calcular_preco(self, hora):
        if hora > 10 * 24:
            return 240  # 10 dias
        elif hora > 12:
            return 24 
        else:
            return hora * 2 

calculadora = CalculadoraEstacionamento.get_instance()

tempo = int(input("Digite o tempo de estacionamento (em horas): "))
price = calculadora.calcular_preco(tempo)
print(f"O preço do estacionamento para {tempo} horas é: R${price:.2f}")
