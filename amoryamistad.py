class Juego_Amor_y_Amistad:
    def __init__(self):
        self.nombre = input("Ingresa tu nombre ")
    
    def personajes(self):
        self.persona_no_agradable
        self.crush

    def inicio(self):
        print("¡Holaaaaaa!", self.nombre, "Hoy junto a tu personaje serás nuevamente una persona jóven, enamoradiza, con muchos amigos y ganas de fiesta")
        print("La única regla que tendrás es escribir tus decisiones en MAYÚSCULA")
        print("Así que, ¡Comencemos el juego!")
        print("¡HOY ES EL DÍA! Ya que no tienes planes en la noche, tus amig@s te invitaron a una fiesta y te contaron que tu crush va a ir, exacto al fin podrás tener la oportunidad de acercarte y poder hablarle, pero ante todo debes ir a disfrutar junto a tus amigos")
        self.crush = input("Será que al fin podrás atreverte a hablarle a ")
    def parte1(self):
        print("Tu amigo Sebas te hace videollamada, el ya se encuentra reunido en su casa con Nathalia, Tomás, Santiago y laura, quieren saber si finalmente irás")
        print("Sebas pregunta:", "Hey", self.nombre, "¿Vas a la fiesta o te quedas en casa?")
        print("Decide:")

        "VOY" == True
        while True:
            asistencia = input("¿VOY O ME QUEDO?: ")
            if asistencia == "VOY":
                print("Genial, es bueno divertirse de vez en cuando con amigos :)")
                break
            elif asistencia == "ME QUEDO":
                print("¿Por qué ir? Mejor en casa, cenar, Netflix y dormir, ¡SOL@! nuevamente :(")
                return
            else:
                print("Sebas:")
                print("¿Qué? No no no, responde lo que te preguntamos, se concreto, di VOY O ME QUEDO")
            
    def parte2(self):
        print("Sebas te pregunta, parce", self.nombre, "¿vas a ir en transmi con nosotros o vas irte en carro?")
        print("¿Pides carro o vas en transmilenio con tus amigos? Decide:")

        transporte = input("¿CARRO O TM?: ")

        if transporte == "TM":
            print("Te encuentras con todos tus parceros y parceras en la casa de Sebas")
            print("Perfectoooo, llegan cuando la fiesta está más buena")

        else:
            print("¡OUGH! Llegas a la fiesta pero gastaste todo en el carro, dejaste el resto del efectivo en casa y te quedaste sin dinero para la vaca, así que no entras")


    def parte3(self):
        print("Tus amigos se van a la pista a bailar")
        print("¿Vas a bailar con ellos o te sientas? Decide:")

        baile = input("BAILO O ME SIENTO: ")

        if baile == "BAILO":
            print("¡Uff que flow! Todos te quieren seguir el paso")
            print("Mientras la das toda en la pista ves a", self.crush, ",sentad@ y te está observando")

        else:
            print("¡ABURRIIIDOOO! Tu crush está frente a tí, pero bailando con otro. ;(")

    def parte4(self):
        print("Tu amiga Nath te dice:")
        print("Oyeee,", self.nombre, "acercatele, deberías invitar a", self.crush, "a bailar, es la oportunidad perfecta para empezar")
        print("¿Invitas a bailar a", self.crush, "? Decide:")

        invitacion = input("¿SÍ O NO?: ")

        if invitacion == "SI":
            print("Valentía, eso es lo que corre por tu sangre. Te acepta la pieza (una salsita bien rosa y romántica)")

        else:
            print("Vaya riesgos tomas, es increíble, ahora eres la única persona en la fiesta sin pareja de baile")

    def parte5(self):
        print("¿Cómo bailarás, de qué forma quieres que te perciba", self.crush, ", quieres impresionar o te diviertes? Decide:")

        forma_de_bailar = input("¿IMPRESIONO O ME DIVIERTO?: ")

        if forma_de_bailar == "ME DIVIERTO":
            print("Bailaste increíble, hiciste disfrutar del baile a", self.crush, ", e incluso le sacaste risas. Después de un par de canciones más se sientan y empiezan una buena conversación")

        else:
            print("Que engreid@ te viste, claro que te robaste el show, pero perdiste de vista disfrutar el baile junto a", self.crush, ", se acabó la canción y se  sentó, te dejo sol@")

    def parte6(self):
        print("Empiezan a hablar más profundo con", self.crush)
        print("¿Hablas de tí o le preguntas sobre su vida?")

        conversacion = input("¿PREGUNTO O HABLO?: ")

        if conversacion == "PREGUNTO":
            print("Que buen escucha eres", self.crush, ", te contó cosas de su vida y de sus gustos, ahora te gusta mucho más, tiene una personalidad que te vuelve loc@")

        else:
            print("Hablas de tí, empiezas a hablar mucho, solo de tí, te excedes,", self.crush, "se aburre y se retira, te viste algo egocentric@")

    def parte7(self):

        self.persona_no_agradable = input ("No te habías percatado pero Laura te muestra quién está en la fiesta, esa persona, aunque no le has hecho nada te hace la vida cuadritos, es: ")
        
        print("Ohh no,", self.crush, "está mirando a", self.persona_no_agradable, "Ahora se está acercando")
        print("Carajo", self.persona_no_agradable, "invita a tu crush a bailar, esto te disgustó un poco ¿Actúas con molestia o tranquilidad?")
        
        toxicidad = input("¿SERIEDAD O TRANQUI?: ")

        if toxicidad == "TRANQUI":
            print("Te molestó bastante, es claro que no te agrada", self.persona_no_agradable,", sin embargo mantuviste la calma y actuaste con madurez")
            print("Luego de bailar con", self.persona_no_agradable, self.crush, "te vuelve a buscar, no parece haberle gustado bailar con esa persona, así que se sienta a tu lado para seguir charlando. Tienen un gran feeling y se divierten el resto de la fiesta")

        else:
            print("Celos@, tu crush no es de tu pertenencia, en toda la noche no se te vuelve a acercar en toda la noche")

    def parte7_8(self):
        print("Tus amigos te buscan para bailar")
        print("Prefieres estár a solas con", self.crush, "o unir a", self.crush, "al parche")
        
        union = input("¿A SOLAS O CON AMIGOS? ")

        if union == "CON AMIGOS":
            print("Tomás se te acerca y te felicita por no dejarlos a un lado a pesar de estár con la persona que te gusta, esto aumenta la confianza en la relación con tus amigos")
        else:
            print("Es incríble, alejaste a tus amigos por estár enamorado de una extraña, ahora cómo regresas a casa si te emborrachas")

    def parte8(self):
        print("Es hora de despedirse")
        print("Acompañas al carro a", self.crush, "¿Cómo te despides?")
        print("Mueres por besar a", self.crush, "Sin embargo no sabes cómo lo pueda tomar, son suficientes riesgos por esta noche o es mejor pedir disculpas que permiso")

        despedida = input("¿BESO O ABRAZO?: ")

        if despedida == "ABRAZO":
            print("Bien,", self.crush, "te dice: ")
            print("Eres muy chimba, muy cool, una persona genial, este es mi número para que volvamos a hablar, me caíste muy bien.")

        else:
            print("¡OYEE! vas muy rápido,", self.crush, "te rechaza el beso y se retira sin más")

    def final(self):
        print("Un momento, la persona del carro baja y besa a", self.crush, "no puede ser tiene pareja  :o")

        print("Que desilusión, ¿qué harás ahora, beber por la pena o celebrar? Decide:")

        decision_final = input("¿BEBER O CELEBRAR?: ")

        if decision_final == "CELEBRAR":
            print("Te vas con tus parcer@s a tu casa para cerrar la noche con broche de oro; rien, juegan, comen y ven el amanecer")

        else:
            print("Qué duro, es entendible tú decisión, pero pierdes, el objetivo era disfrutar con tus amigos, no sufrir por", self.crush)


        print("¡Felicidades! Lo lograste, cumpliste el objetivo, a pesar de la desilusión amorosa, disfrutaste con tus amigos, al fin y al cabo el objetivo era disfrutar con ellos")

        input("¿BUEN FINAL NO? ")

if __name__ == "__main__":
    juego = Juego_Amor_y_Amistad() 
    juego.inicio()
    juego.parte1()
    juego.parte2()
    juego.parte3()
    juego.parte4()
    juego.parte5()
    juego.parte6()
    juego.parte7()
    juego.parte7_8()
    juego.parte8()
    juego.final()