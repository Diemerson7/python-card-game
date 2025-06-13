from personagem import Personagem, CartaAumento

heroi = Personagem("Herói")
carta1 = CartaAumento("Herói", 20, "Carta que aumenta o Ataque", 3, 5)
print(f"Ataque do Herói: {heroi.ataque}.")
carta1.usar_carta(personagem = heroi)
print(f"Ataque do Herói: {heroi.ataque}.")

carta2 = CartaAumento("Herói", 30, "Carta que aumenta a Defesa", )