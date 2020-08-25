# sem instanciar os objetos logo preciso dizer quias são os valores em cada operação
# o init não pode ser vazio logo precisa colocar o pass
class Calculadora:
    def __init__(self):
        pass
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
