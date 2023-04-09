class ProntuarioMedico:
    def __init__(self, nome, idade, peso, altura, historico_medico):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.historico_medico = historico_medico
    
    def mostrar_prontuario(self):
        print("Prontuário de", self.nome)
        print("Idade:", self.idade)
        print("Peso:", self.peso)
        print("Altura:", self.altura)
        print("Histórico médico:")
        for item in self.historico_medico:
            print("-", item)

    def adicionar_item_historico(self, item):
        self.historico_medico.append(item)
