from __future__ import annotations
from cartas import Carta

class Personagem:  
    def __init__(self, nome):
        # Atributos
        self.nome =  nome
        self.vida_maxima = 100
        self.vida_atual = 100
        self.ataque = 30
        self.defesa = 40
        self.cartas = []
        self.energia = 100
        self.energia_maxima = 100
        
    # Sortear cartas
        
    # Método Atacar
    def atacar(self, inimigo: Personagem, heroi: Personagem):
        dano = heroi.ataque
        dano = max(0,dano) # Pro dano não ser negativo
        inimigo.vida_atual -= dano
        print(f"{heroi.nome} atacou {inimigo.nome} causando {dano} de dano!")
 
    # Método Usar Carta 
    def usar_carta(personagem: Personagem, inimigo: Personagem, indice: int):
        # Verifica se o número digitado pelo jogador é válido
        if indice < 1 or indice > len(personagem.cartas):
           print(f"Carta Inválida.")
           return
       
        carta = personagem.cartas[indice - 1]
        
        # Reduz a energia a cada carta usada
        if personagem.energia < carta.energia_gasta:
            print(f"{personagem.nome} não tem energia suficiente para usar {carta.nome}.")
            return
        
        # Cada vez que usa uma carta, a energia do personagem diminui de acordo com a carta
        personagem.energia -= carta.energia_gasta
        print(f"{personagem.nome} usou a carta {carta.nome}")
        
        # Remove a carta após o uso
        personagem.cartas.pop(indice -1)
        print(f"A carta {carta.nome} foi descartada do deck. \n")
        
    # Método Comprar Carta    
    def comprar_carta(self, personagem: Personagem, nova_carta: Carta):
        personagem.cartas.append(nova_carta)
        print(f"{personagem.nome} comprou a carta: {nova_carta.nome}")
    
    # Método Levar Dano
    def levar_dano(self, personagem: Personagem, dano: int):
        dano_real = max(0, dano - (personagem.defesa // 10)) # A defesa reduz o dano
        personagem.vida_atual -= dano_real
        personagem.vida_atual = max(0, personagem.vida_atual) # Pro dano não ser negativo
        print(f"{personagem.nome} levou {dano.real} de dano! Vida atual: {personagem.vida_atual}")
        
    
    # Método Ver Cartas
    def ver_cartas(self, personagem: Personagem):
        print(f"Cartas de {personagem.nome}:")
        if not personagem.cartas:
            print("Nenhuma carta no momento.")
        else:
            for i, carta in enumerate(personagem.cartas, 1):
                print(f"{i}. {carta.nome} - Custa {carta.energia_gasta} de energia\n {carta.descricao}")   
    
    # Método Curar-se                    
    def curar_se(self, personagem: Personagem, quantidade: int):
        vida_antes = personagem.vida_atual
        personagem.vida_atual = min(personagem.vida_atual + quantidade, personagem.vida_maxima)
        cura_real = personagem.vida_atual - vida_antes
        print(f"{personagem.nome} recuperou {cura_real} de vida! Vida atual: {personagem.vida_atual}")