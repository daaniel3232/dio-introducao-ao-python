# como não vai inicializar nada não é necessário usar o método "__init__"

class Calculadora:
    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


calculador = Calculadora()
print(calculador.soma(10, 2))
print(calculador.subtracao(5, 3))
print(calculador.divisao(100, 2))
print(calculador.multiplicacao(10, 5))
