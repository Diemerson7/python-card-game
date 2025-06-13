class Personagem:  
    def __init__(self, nome):
        # Atributos
        self.nome =  nome
        self.vida_maxima = 100
        self.vida = 100
        self.ataque = 70
        self.defesa = 50
        self.cartas = []
        self.energia = 10

class Carta:
    def __init__(self, nome, energia_gasta, descricao):
        # Atributos
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao

    # Métodos
    def usar_carta(self):
        pass
    
class CartaAumento(Carta):
    # O "init" é o construtor
    def __init__(self, nome, energia_gasta, descricao, tipo, pontos_aumentados):
        super().__init__(nome, energia_gasta, descricao)
        self.tipo = tipo
        self.pontos_aumentados = pontos_aumentados
    
    def usar_carta(self, personagem):
        if self.tipo == 1: 
            personagem.vida_maxima = self.pontos_aumentados + personagem.vida_maxima
            print(f"{self.nome} usou a carta de Aumento de Vida Máxima.")
            return
        
        if self.tipo == 2:
            personagem.defesa = self.pontos_aumentados + personagem.defesa
            print(f"{self.nome} usou a carta de Aumento de Defesa.")
            return
        
        if self.tipo == 3:
            personagem.ataque = self.pontos_aumentados + personagem.ataque
            print(f"{self.nome} Usou a carta de Aumento de Ataque.")
            return
        
        if self.tipo == 4:
            personagem.energia_maxima = self.pontos_aumentados + personagem.energia_maxima
            print(f"{self.nome} Usou a carta de Aumento de Energia Máxima.")
            return
        
class CartaRoubo(Carta):
    def __init__(self, nome, energia_gasta, descricao):
        super().__init__(nome, energia_gasta, descricao)