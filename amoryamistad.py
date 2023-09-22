nombre = input("Ingresa tu nombre ")

print("¡Hola!", nombre)
print("¡HOY ES EL DÍA! Ya que no tienes planes en la noche, tus amig@s te invitaron a una fiesta y te contaron que tu crush va a ir, exacto al fin podrás tener la oportunidad de acercarte y poder hablarle, pero ante todo debes ir a disfrutar junto a tus amigos")

print("¿Vas o te quedas? Decide:")

decision = input("¿VOY O ME QUEDO?: ")
   
if decision == "VOY":
    print("Genial, es bueno divertirse de vez en cuando con amigos :)")
    
else:
    print("¿Por qué ir? Mejor en casa, cenar, Netflix y dormir, ¡SOL@! nuevamente :(")

print("¿Pides carro o vas en transmilenio? Decide:")

transporte = input("¿CARRO O TM?: ")

if transporte == "TM":
    print("Llegas a tiempo, ves que tus parceros están bailando")

else:
    print("¡OUGH! Llegas a la fiesta pero gastaste todo en el carro, dejaste el resto del efectivo en casa y te quedaste sin dinero para la vaca, así que no entras")


print("Llegas a tiempo, ves que tus parceros están bailando")

print("¿Bailas o te sientas? Decide:")

baile = input("BAILO O ME SIENTO: ")

if baile == "BAILO":
    print("¡Uff que flow! Mientras la das toda en la pista ves a tu crush sentad@ y te está observando")

else:
    print("¡ABURRIIIDOOO! Tu crush está frente a tí, pero bailando con otro. ;(")

print("¿Invitas a bailar a tu crush? Decide:")

invitacion = input("¿SÍ O NO?: ")

if invitacion == "SÍ":
    print("Valentía, eso es lo que corre por tu sangre. Te acepta la pieza (una salsita bien rosa y romántica)")

else:
    print("Vaya riesgos tomas, es increíble, ahora eres la única persona en la fiesta sin pareja de baile")

print("¿Cómo bailas, te luces o te diviertes? Decide:")

forma_de_bailar = input("¿BAILO O ME DIVIERTO?: ")

if forma_de_bailar == "ME DIVIERTO":
    print("Bailaste increíble, además hiciste disfrutar del baile a tu crush e incluso le sacaste risas. Después de un par de canciones más se sientan y empiezan una buena conversación")

else:
    print("Que engreid@ te viste, claro que te robaste el show, pero perdiste de vista disfrutar el baile junto a tu crush, se acabó la canción y se  sentó, te dejo sol@")

input("¿Hablas de tí o le preguntas sobre ella? Decide:")

conversacion = input("¿PREGUNTAR O HABLAR?: ")

if conversacion == "PREGUNTO":
    print("Que buen escucha eres. Tu crush te contó cosas de su vida y de sus gustos, ahora te gusta mucho más, tiene una personalidad que te vuelve loc@")

else:
    print("Hablas de tí, empiezas a hablar mucho, solo de tí, te excedes, tu crush se aburre y se retira, te viste algo egocentric@")

print("Alguien más invita a tu crush a bailar, ¿Cómo actuas? Decide:")

toxicidad = input("¿SERIEDAD O TRANQUI?: ")

if toxicidad == "TRANQUI":
    print("Luego de bailar con la otra persona, tu crush te vuelve a buscar para seguir charlando. Tienen un gran feeling y se divierten el resto de la fiesta junto a tus amigos")

else:
    print("Celos@, tu crush no es de tu pertenencia, en toda la noche no se te vuelve a acercar en toda la noche")

input("Es hora de despedirse, acompañas al carro a tu crush, ¿Cómo te despides? Decide:")

despedida = input("¿BESO O ABRAZO?: ")

if despedida == "ABRAZO":
    print("Bien, tu crush te dice: Eres muy chimba, muy cool, una persona genial, este es mi número para que volvamos a hablar, me caíste muy bien.")

else:
    print("¡OYEE! vas muy rápido, tu crush rechaza el beso y se retira sin más")


print("Un momento, la persona del carro baja y besa a tu crush, no puede ser tiene pareja  :o")

print("Que desilusión, ¿qué harás ahora, beber por la pena o celebrar? Decide:")

decision_final = input("¿BEBER O CELEBRAR?: ")

if decision_final == "CELEBRAR":
    print("Te vas con tus parcer@s a tu casa para cerrar la noche con broche de oro; rien, juegan, comen y ven el amanecer")

else:
    print("Qué duro, es entendible tú decisión, pero pierdes, el objetivo era disfrutar con tus amigos, no sufrir por tu ex")


print("¡Felicidades! Lo lograste, cumpliste el objetivo, a pesar de la desilusión amorosa, disfrutaste con tus amigos, allos siempre estuviero ahí ¿No?")

input("¿BUEN FINAL NO?")