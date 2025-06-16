from personagem import Personagem, CartaAumento, CartaRoubo, CartaAtordoamento, CartaDano, CartaCura

heroi = Personagem("Herói")
carta1 = CartaAumento("Ataque", 20, "Carta que aumenta o Ataque", 3, 5) # O número "3" é o número do tipo da carta. Por exemplo, o número do ataque é 3, porque é o "self.tipo == 3", e o número "5" é a quantidade que vai aumentar do ataque.
print(f"Ataque do Herói: {heroi.ataque}.")
carta1.usar_carta(personagem = heroi)
print(f"Ataque do Herói: {heroi.ataque}.")

carta2 = CartaAumento("Defesa", 20, "Carta que aumenta a Defesa", 2, 5)
print(f"Defesa do Herói: {heroi.defesa}.")
carta2.usar_carta(personagem = heroi)
print(f"Defesa do Herói: {heroi.defesa}.")

carta3 = CartaAumento("Vida Máxima", 30, "Carta que aumenta a Vida Máxima", 1, 10)
print(f"Vida Máxima do Herói: {heroi.vida_atual}.")
carta3.usar_carta(personagem = heroi)
print(f"Vida Máxima do Herói: {heroi.vida_atual}.")

carta4 = CartaAumento("Energia Máxima", 30, "Carta que aumenta a Energia Máxima", 4, 5)
print(f"Energia Máxima: {heroi.energia}")
carta4.usar_carta(personagem = heroi)
print(f"Energia Máxima: {heroi.energia}")

carta5 = CartaRoubo("Carta Roubo", 30, "Carta que rouba uma carta aleatória do adversário")

carta6 = CartaAtordoamento("Carta de Atordoamento", 10, "Carta que zera a energia do adversário", 0)

carta7 = CartaDano("Carta de Dano", 20, "Carta que dá dano no adversário", 10)

carta8 = CartaCura("Carta de Cura", 20, "Carta que cura a vida", 10)