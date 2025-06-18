import random
from personagem import Personagem


class Carta:
    def __init__(self, nome, energia_gasta, descricao):
        # Atributos
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao
    
class CartaAumento(Carta):
    # O "init" é o construtor
    def __init__(self, nome, energia_gasta, descricao, tipo, pontos_aumentados):
        super().__init__(nome, energia_gasta, descricao)
        # Atributos
        self.tipo = tipo
        self.pontos_aumentados = pontos_aumentados
    
    # Métodos
    def usar_carta(self, personagem):
        if self.tipo == 1: 
            personagem.vida_maxima = self.pontos_aumentados + personagem.vida_maxima
            print(f"{self.nome} Usou a carta de Aumento de Vida Máxima.")
            return
        
        if self.tipo == 2:
            personagem.defesa = self.pontos_aumentados + personagem.defesa
            print(f"{self.nome} Usou a carta de Aumento de Defesa.")
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
        
    def usar_carta(self, vitima: Personagem, ladrao: Personagem):
        sorteio_carta_roubada = random.randint(0, len(vitima.cartas)-1) 
        carta_roubada = vitima.cartas.pop(sorteio_carta_roubada) # Rouba a carta da Vítima
        ladrao.cartas.append(carta_roubada) # Carta da Vítima vem para mim
        return  
        
    
class CartaAtordoamento(Carta):
    def __init__(self, nome, energia_gasta, descricao):
        super().__init__(nome, energia_gasta, descricao)
        
    def usar_carta(self, vitima: Personagem):
        vitima.energia = 0
        return
        
    
class CartaDano(Carta):
    def __init__(self, nome, energia_gasta, descricao, pontos_de_dano):
        super().__init__(nome, energia_gasta, descricao)
        self.pontos_de_dano = pontos_de_dano

    def usar_carta(self, inimigo: Personagem, causador: Personagem):
        inimigo.vida_atual -= causador.ataque - inimigo.defesa
        
        
class CartaCura(Carta):
    def __init__(self, nome, energia_gasta, descricao, pontos_de_vida_curado):
        super().__init__(nome, energia_gasta, descricao)
        self.pontos_de_vida_curado = pontos_de_vida_curado
        
    def usar_carta(self, beneficiario: Personagem):
        beneficiario.vida_atual += beneficiario.vida_maxima * 0.30  # Cura 30% da vida máxima
           