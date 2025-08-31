"""
    Practica 1: 20Q

    Integrantes del eqipo:
    - Agreda Iparraguirre Rodrigo Imanol
    - Pimentel Gonzalez Ricardo Antonio
    - Taboada Montiel Enrique
    
"""
print("Practica 1: 20Q")
print("Integrantes del equipo:")
print("Agreda Iparraguirre Rodrigo Imanol")
print("Pimentel Gonzalez Ricardo Antonio")
print("Taboada Montiel Enrique\n")

print("Piensa en algo, y yo tratare de adivinarlo con preguntas de si o no")

respuesta = input("Estas pensando en algo real?  (si/no): ").strip().lower()

if respuesta == "si":
    respuesta = input("¿Es un ser vivo? (si/no): ").strip().lower()
    
    if respuesta == "si":
        respuesta = input("¿Es un animal? (si/no): ").strip().lower()
            
        if respuesta == "si":
            respuesta = input("¿Es un vertebrado? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es un mamifero? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un animal doméstico? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("¿Es un animal de compañía común? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un perro o gato.")
                        else:
                            print("Pensaste en un conejo, hámster o pez de acuario.")
                    else:
                        respuesta = input("Pone huevos? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un ornitorrinco o equidna.")
                        else:
                            respuesta = input("¿Es un marsupial? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un canguro, koala o zarigüeya.")
                            else:
                                respuesta = input("¿Es un animal omnivoro? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un oso, cerdo.")
                                else:
                                    respuesta = input("¿Es un animal carnivoro? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en un león, tigre o lobo.")
                                    else:
                                        respuesta = input("¿Es un animal herbívoro? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            respuesta = input("¿Es un animal rumiante? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                print("Pensaste en una vaca, oveja o cabra.")
                                            else:
                                                print("Pensaste en un caballo, elefante o jirafa.")                                   
                else:
                    respuesta = input("¿Es un ave? (si/no): ").strip().lower()
                    if respuesta =="si":
                        respuesta = input("¿Es un ave domestica? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un canario, gallina o pato.")
                        else:
                            respuesta = input("¿Puede volar? (si/no): ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("¿Es nocturno? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un búho o lechuza.")
                                else:
                                    print("Pensaste en un águila, halcón o colibrí.")
                            else:
                                respuesta = input("¿Es un ave acuatica? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un pato, cisne o flamenco.")
                                else:
                                    print("Pensaste en un ave terrestre.")
                                    respuesta = input("¿Es de lo hemisferios polo norte o sur? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en un pinguino o albatros.")
                                    else:
                                        print("Pensaste en un avestruz o emú.")
                    else:
                        respuesta = input("¿Es un reptil? (si/no): ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("¿Es un reptil terrestre? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en una serpiente, lagartija o cocodrilo.")
                            else:
                                print("Pensaste en una tortuga o iguana.")
                        else:
                            respuesta = input("¿Es un anfibio? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en una rana o salamandra.")
                            else:
                                respuesta = input("¿Es un pez? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    respuesta = input("¿Es un pez de agua dulce? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en una trucha, carpa o bagre.")
                                    else:
                                        print("Pensaste en un pez de agua salada.")                    
                    
            else:
                respuesta = input("¿Es un invertebrado? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un insecto? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en una mariposa, abeja o escarabajo.")
                    else:
                        respuesta = input("¿Es un aracnido? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en una araña o escorpión.")
                        else:
                            respuesta = input("¿Es un molusco? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un caracol o pulpo.")
                            else:
                                respuesta = input("¿Es un crustaceo? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un cangrejo o langosta.")
                                else:
                                    respuesta = input("¿Es un Miriápodos (ciempiés y milpiés)? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en un ciempiés o milpiés.")
                                    else:
                                        respuesta = input("¿Tiene simetria radial, como una estrella ? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            print("Pensaste en una estrella de mar o erizo de mar.")
                                        else:
                                            respuesta = input("¿Es un gusano? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                print("Pensaste en una lombriz o gusano de seda.")
                                        
        else:                                
            respuesta = input("¿Es una planta? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Da frutos? (si/no): ").strip().lower()
                if respuesta == "si":
                    print("Pensaste en un árbol frutal o arbusto.")
                else:
                    respuesta = input("¿Es una planta de interior? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un cactus, helecho o palma.")
                    else:
                        respuesta = input("¿Es una planta de exterior? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un rosal, césped o arbusto ornamental.")
                        else:
                            respuesta = input("¿Es una planta acuática? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un loto, jacinto de agua o alga.")
                            else:
                                respuesta = input("¿Es una planta carnívora? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en una Venus atrapamoscas, planta cobra o planta araña.")
                                else:
                                    print("Pensaste en otro tipo de planta como un helecho, cactus o orquídea.")
            else:
                respuesta = input("¿Es una persona? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es un personaje histórico? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un rey, presidente o científico.")
                    else:
                        respuesta = input("¿Es un personaje famoso? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un actor, cantante o deportista.")
                        else:
                            respuesta = input("¿Es un profesionista? (si/no): ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("¿Es de area fisico-matematicas? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un ingeniero, matematico, arquitecto o fisico.")
                                else:
                                    respuesta = input("¿Es de area de la salud? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en un doctor, enfermera o paramedico, psicologo.")
                                    else:
                                        respuesta = input("¿Es de area de humanidades? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            print("Pensaste en un filosofo, escritor o historiador.")
                                        else:
                                            respuesta = input("¿Es de area de social-administrativa? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                print("Pensaste en un abogado, administrador o contador.")
                                            else:
                                                respuesta = input("¿Es de area de artes? (si/no): ").strip().lower()
                                                if respuesta == "si":
                                                    print("Pensaste en un pintor, escultor o músico.")
                                                else:
                                                    respuesta = input("¿Es de area de educacion? (si/no): ").strip().lower()
                                                    if respuesta == "si":
                                                        print("Pensaste en un profesor, pedagogo.")
                            else:
                                respuesta = input("¿Se dedica a un oficio? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un carpintero, plomero o electricista.")
                                else:
                                    print("Pensaste en un campesino, pescador o minero.")                                                
                else:
                    respuesta = input("¿Es un hongo? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un hongo comestible o venenoso.")
    else:
        respuesta = input("¿Es un objeto de la tierra? (si/no): ").strip().lower()
        if respuesta == "si":
            respuesta = input("¿Se encuentra solo en una casa? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Se usa en la cocina? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Se usa para cocinar? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un sartén, olla o microondas.")
                    else:
                        print("Pensaste en un cuchillo, tenedor o licuadora.")
                else:
                    respuesta = input("¿Es un electrodoméstico? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en una lavadora, refrigerador o televisor.")
                    else:
                         respuesta = input("¿Produce luz? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("¿Funciona con electricidad? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en una bombilla o lámpara.")
                        else:
                            print("Pensaste en una vela o antorcha.")
                    else:
                        respuesta = input("¿Es un mueble? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en una silla, mesa o sofá.")
                        else:
                            respuesta = input("¿Se usa para la limpieza? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en una escoba, trapeador o detergente.")
                            else:
                                respuesta = input("¿Se usa para la higiene personal? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en una toalla, cepillo de dientes o jabón.")
                                else:
                                    print("Pensaste en otro objeto del hogar como un cuadro, reloj o cortina.")
            else:
                respuesta = input("¿Es una herramienta? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Se usa en la construcción? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en un martillo, serrucho o taladro.")
                    else:
                        print("Pensaste en una llave inglesa o una pinza.")
                else:
                    respuesta = input("¿Es un medio de transporte? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("¿Es terrestre? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en un coche, motocicleta o bicicleta.")
                        else:
                            print("Pensaste en un barco o avión.")
                    else:
                        respuesta = input("¿Es un lugar público? (si/no): ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("¿Es un lugar educativo? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en una escuela, universidad o biblioteca.")
                            else:
                                respuesta = input("¿Es un lugar de salud? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un hospital, clínica o farmacia.")
                                else:
                                    respuesta = input("¿Es un lugar de entretenimiento? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en un cine, teatro o parque de diversiones.")
                                    else:
                                        respuesta = input("¿Es un lugar comercial? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            print("Pensaste en un centro comercial, supermercado o tienda.")
                                        else:
                                            print("Pensaste en otro tipo de lugar público como una plaza, parque o museo.")
                        else:
                            respuesta = input("¿Puede ser un medio de entretenimiento? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un dispositivo tecnológico como una computadora o consola.")
                            else:
                                respuesta = input("¿Es un objeto cultural? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    respuesta = input("¿Es una obra de arte? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en una pintura, escultura o fotografía famosa.")
                                    else:
                                        respuesta = input("¿Es un instrumento musical? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            print("Pensaste en un piano, guitarra o violín.")
                                        else:
                                            respuesta = input("¿Es un alimento o bebida típica? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                print("Pensaste en un plato típico o una bebida tradicional.")
                                            else:
                                                print("Pensaste en otro tipo de objeto cultural.")
                                else:
                                    respuesta = input("¿Es un elemento químico o compuesto? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        respuesta = input("¿Es un elemento de la tabla periódica? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            respuesta = input("¿Es un metal? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                print("Pensaste en oro, hierro o aluminio.")
                                            else:
                                                respuesta = input("¿Es un gas noble? (si/no): ").strip().lower()
                                                if respuesta == "si":
                                                    print("Pensaste en helio, neón o argón.")
                                                else:
                                                    print("Pensaste en otro tipo de elemento como carbono, oxígeno o hidrógeno.")
                                        else:
                                            respuesta = input("¿Es un compuesto orgánico? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                print("Pensaste en metano, etanol o glucosa.")
                                            else:
                                                print("Pensaste en un compuesto inorgánico como agua, sal o ácido sulfúrico.")
                                    else:
                                        respuesta = input("¿Es un evento histórico? (si/no): ").strip().lower()
                                        if respuesta == "si":
                                            respuesta = input("¿Ocurrió en el siglo XX? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                respuesta = input("¿Está relacionado con una guerra mundial? (si/no): ").strip().lower()
                                                if respuesta == "si":
                                                    print("Pensaste en la Primera o Segunda Guerra Mundial.")
                                                else:
                                                    respuesta = input("¿Es un evento político? (si/no): ").strip().lower()
                                                    if respuesta == "si":
                                                        print("Pensaste en una Revolución, la caída de un imperio o la independencia de algun pais.")
                                                    else:
                                                        print("Pensaste en el primer viaje a la Luna, un descubrimiento o invencion.")
                                            else:
                                                respuesta = input("¿Ocurrió antes del siglo XIX? (si/no): ").strip().lower()
                                                if respuesta == "si":
                                                    print("Pensaste en el descubrimiento de América, la Revolución Francesa o la caída del Imperio Romano.")
                                                else:
                                                    print("Pensaste en la Revolución Industrial, la Guerra Civil Estadounidense o la Primera Guerra Mundial.")
                                        else:
                                            respuesta = input("¿Es una obra de arte famosa? (si/no): ").strip().lower()
                                            if respuesta == "si":
                                                respuesta = input("¿Es una pintura? (si/no): ").strip().lower()
                                                if respuesta == "si":
                                                    respuesta = input("¿Es del Renacimiento? (si/no): ").strip().lower()
                                                    if respuesta == "si":
                                                        print("Pensaste en la Mona Lisa, La última cena o El nacimiento de Venus.")
                                                    else:
                                                        respuesta = input("¿Es del siglo XIX o XX? (si/no): ").strip().lower()
                                                        if respuesta == "si":
                                                            print("Pensaste en La noche estrellada, Los girasoles o El grito.")
                                                        else:
                                                            print("Pensaste en otra pintura famosa como Las meninas o La persistencia de la memoria.")
                                                else:
                                                    respuesta = input("¿Es una escultura? (si/no): ").strip().lower()
                                                    if respuesta == "si":
                                                        print("Pensaste en el David de Miguel Ángel, La Piedad o El pensador.")
                                                    else:
                                                        respuesta = input("¿Es una obra arquitectónica? (si/no): ").strip().lower()
                                                        if respuesta == "si":
                                                            print("Pensaste en la Torre Eiffel, el Taj Mahal o la Sagrada Familia.")
                                                        else:
                                                            print("Pensaste en otra forma de arte como una fotografía o instalación famosa.")
                                            else:
                                                respuesta = input("¿Es un género musical o instrumento? (si/no): ").strip().lower()
                                                if respuesta == "si":
                                                    respuesta = input("¿Es un género musical? (si/no): ").strip().lower()
                                                    if respuesta == "si":
                                                        respuesta = input("¿Es un género clásico o tradicional? (si/no): ").strip().lower()
                                                        if respuesta == "si":
                                                            print("Pensaste en música clásica, jazz o blues.")
                                                        else:
                                                            respuesta = input("¿Es un género popular moderno? (si/no): ").strip().lower()
                                                            if respuesta == "si":
                                                                print("Pensaste en rock, pop o hip-hop.")
                                                            else:
                                                                print("Pensaste en otro género musical como electrónica, reggae o country.")
                                                    else:
                                                        respuesta = input("¿Es un instrumento de cuerda? (si/no): ").strip().lower()
                                                        if respuesta == "si":
                                                            print("Pensaste en una guitarra, violín o piano.")
                                                        else:
                                                            respuesta = input("¿Es un instrumento de viento? (si/no): ").strip().lower()
                                                            if respuesta == "si":
                                                                print("Pensaste en una flauta, saxofón o trompeta.")
                                                            else:
                                                                respuesta = input("¿Es un instrumento de percusión? (si/no): ").strip().lower()
                                                                if respuesta == "si":
                                                                    print("Pensaste en una batería, tambor o xilófono.")
                                                                else:
                                                                    print("Pensaste en otro tipo de instrumento musical.")
                                                else:
                                                    respuesta = input("¿Es un deporte o evento deportivo? (si/no): ").strip().lower()
                                                    if respuesta == "si":
                                                        respuesta = input("¿Es un deporte de equipo? (si/no): ").strip().lower()
                                                        if respuesta == "si":
                                                            respuesta = input("¿Se juega con una pelota? (si/no): ").strip().lower()
                                                            if respuesta == "si":
                                                                print("Pensaste en fútbol, baloncesto o voleibol.")
                                                            else:
                                                                print("Pensaste en hockey, rugby o waterpolo.")
                                                        else:
                                                            respuesta = input("¿Es un deporte individual? (si/no): ").strip().lower()
                                                            if respuesta == "si":
                                                                respuesta = input("¿Es un deporte olímpico? (si/no): ").strip().lower()
                                                                if respuesta == "si":
                                                                    print("Pensaste en atletismo, natación o gimnasia.")
                                                                else:
                                                                    print("Pensaste en golf, tenis o boxeo.")
                                                            else:
                                                                respuesta = input("¿Es un evento deportivo? (si/no): ").strip().lower()
                                                                if respuesta == "si":
                                                                    print("Pensaste en los Juegos Olímpicos, la Copa Mundial de Fútbol o el Super Bowl.")
                                                                else:
                                                                    print("Pensaste en otro tipo de actividad deportiva o competición.")
                                                    else:
                                                        respuesta = input("¿Es un idioma o lenguaje? (si/no): ").strip().lower()
                                                        if respuesta == "si":
                                                            respuesta = input("¿Es un idioma hablado? (si/no): ").strip().lower()
                                                            if respuesta == "si":
                                                                respuesta = input("¿Es un idioma europeo? (si/no): ").strip().lower()
                                                                if respuesta == "si":
                                                                    print("Pensaste en inglés, español o francés.")
                                                                else:
                                                                    respuesta = input("¿Es un idioma asiático? (si/no): ").strip().lower()
                                                                    if respuesta == "si":
                                                                        print("Pensaste en chino, japonés o hindi.")
                                                                    else:
                                                                        print("Pensaste en árabe, swahili o otro idioma no europeo ni asiático.")
                                                            else:
                                                                respuesta = input("¿Es un lenguaje de programación? (si/no): ").strip().lower()
                                                                if respuesta == "si":
                                                                    print("Pensaste en Python, Java o JavaScript.")
                                                                else:
                                                                    respuesta = input("¿Es un lenguaje de señas? (si/no): ").strip().lower()
                                                                    if respuesta == "si":
                                                                        print("Pensaste en el lenguaje de señas americano, británico o internacional.")
                                                                    else:
                                                                        print("Pensaste en otro tipo de lenguaje o sistema de comunicación.")
                                                        else:
                                                            respuesta = input("¿Es una marca o producto comercial? (si/no): ").strip().lower()
                                                            if respuesta == "si":
                                                                respuesta = input("¿Es una marca de tecnología? (si/no): ").strip().lower()
                                                                if respuesta == "si":
                                                                    print("Pensaste en Apple, Microsoft o Google.")
                                                                else:
                                                                    respuesta = input("¿Estas pensando en ropa? (si/no): ").strip().lower()
                                                                    if respuesta == "si":
                                                                        respuesta = input("¿Es una marca de ropa? (si/no): ").strip().lower()
                                                                        if respuesta == "si":
                                                                            print("Pensaste en Nike, Adidas o Zara.")
                                                                        else:
                                                                            print("Pensaste en una prenda de vestir como camisa, pantalón o zapato.")
                                                                    else:
                                                                        respuesta = input("¿Es una marca de alimentos o bebidas? (si/no): ").strip().lower()
                                                                        if respuesta == "si":
                                                                            print("Pensaste en Coca-Cola, McDonald's o Nestlé.")
                                                                        else:
                                                                            print("Pensaste en otra marca o producto comercial.")
                                                            else:
                                                                respuesta = input("¿Es un alimento o bebida? (si/no): ").strip().lower()
                                                                if respuesta == "si":
                                                                    respuesta = input("¿Es un alimento? (si/no): ").strip().lower()
                                                                    if respuesta == "si":
                                                                        respuesta = input("¿Es un plato principal? (si/no): ").strip().lower()
                                                                        if respuesta == "si":
                                                                            print("Pensaste en pizza, hamburguesa o sushi.")
                                                                        else:
                                                                            respuesta = input("¿Es un postre? (si/no): ").strip().lower()
                                                                            if respuesta == "si":
                                                                                print("Pensaste en helado, pastel o chocolate.")
                                                                            else:
                                                                                print("Pensaste en otro tipo de alimento como fruta, verdura o snack.")
                                                                    else:
                                                                        respuesta = input("¿Es una bebida alcohólica? (si/no): ").strip().lower()
                                                                        if respuesta == "si":
                                                                            print("Pensaste en cerveza, vino o whisky.")
                                                                        else:
                                                                            respuesta = input("¿Es una bebida caliente? (si/no): ").strip().lower()
                                                                            if respuesta == "si":
                                                                                print("Pensaste en café, té o chocolate caliente.")
                                                                            else:
                                                                                print("Pensaste en agua, refresco o jugo.")
                                                                else:
                                                                    respuesta = input("¿Es una festividad o celebración? (si/no): ").strip().lower()
                                                                    if respuesta == "si":
                                                                        respuesta = input("¿Es una festividad religiosa? (si/no): ").strip().lower()
                                                                        if respuesta == "si":
                                                                            print("Pensaste en Navidad, Pascua o Ramadán.")
                                                                        else:
                                                                            respuesta = input("¿Es una celebración nacional? (si/no): ").strip().lower()
                                                                            if respuesta == "si":
                                                                                print("Pensaste en el Día de la Independencia, Año Nuevo o Día Nacional.")
                                                                            else:
                                                                                respuesta = input("¿Es una celebración internacional? (si/no): ").strip().lower()
                                                                                if respuesta == "si":
                                                                                    print("Pensaste en el Día de la Tierra, Día Internacional de la Mujer o Día Mundial de la Salud.")
                                                                                else:
                                                                                    print("Pensaste en otra festividad o celebración como Halloween, San Valentín o Carnaval.")
                                                                    else:
                                                                        respuesta = input("¿Es un invento o descubrimiento científico? (si/no): ").strip().lower()
                                                                        if respuesta == "si":
                                                                            respuesta = input("¿Es un invento tecnológico? (si/no): ").strip().lower()
                                                                            if respuesta == "si":
                                                                                respuesta = input("¿Es un dispositivo electrónico? (si/no): ").strip().lower()
                                                                                if respuesta == "si":
                                                                                    print("Pensaste en el teléfono, la computadora o el televisor.")
                                                                                else:
                                                                                    print("Pensaste en la rueda, la imprenta o el avión.")
                                                                            else:
                                                                                respuesta = input("¿Es un descubrimiento médico? (si/no): ").strip().lower()
                                                                                if respuesta == "si":
                                                                                    print("Pensaste en la penicilina, la vacuna o los rayos X.")
                                                                                else:
                                                                                    respuesta = input("¿Es un descubrimiento físico o químico? (si/no): ").strip().lower()
                                                                                    if respuesta == "si":
                                                                                        print("Pensaste en la teoría de la relatividad, la tabla periódica o la ley de la gravedad.")
                                                                                    else:
                                                                                        print("Pensaste en otro tipo de invento o descubrimiento científico.")
                                                                        else:
                                                                            print("Lo siento, no puedo adivinar en qué estás pensando.")
        else:
            respuesta = input("¿Es algo del espacio? (si/no): ").strip().lower()
            if respuesta == "si":
                respuesta = input("¿Es un planeta? (si/no): ").strip().lower()
                if respuesta == "si":
                    print("Pensaste en Marte, Júpiter o la Tierra.")
                else:
                    respuesta = input("¿Es una estrella? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en el Sol o Sirio.")
                    else:
                        respuesta = input("¿Es un satélite? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en la Luna o un satélite artificial.")
                        else:
                            respuesta = input("¿Es un asteroide? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un asteroide o cometa.")
                            else:
                                respuesta = input("¿Es un fenómeno astronómico? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un eclipse o lluvia de estrellas.")
            else:
                respuesta = input("¿Es un concepto? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es una emocion? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en amor, odio o tristeza.")
                    else:
                        respuesta = input("¿Es un valor? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en justicia, libertad o respeto.")
                        else:
                            respuesta = input("¿Es un fenómeno natural? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en un arcoíris, tormenta o terremoto.")
                            else:
                                respuesta = input("¿Es un concepto matemático? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en un número, operación o figura geométrica.")
                                else:
                                    respuesta = input("¿Es un concepto científico? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en una teoría, ley o experimento.")
                                    else:
                                        print("Pensaste en un concepto filosófico o abstracto.")
                    
else:
    respuesta = input("¿Es un concepto imaginario? (si/no): ").strip().lower()
    if respuesta == "si":
        respuesta = input("¿Es un personaje de ficción? (si/no): ").strip().lower()
        if respuesta == "si":
            respuesta = input("¿Es un superhéroe? (si/no): ").strip().lower()
            if respuesta == "si":
                print("Pensaste en Batman, Superman o Spider-Man.")
                if respuesta == "si":
                    print("Pensaste en Batman, Superman o Spider-Man.")
                else:
                    respuesta = input("¿Es un personaje de cuento de hadas? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en Cenicienta, Blancanieves o el Lobo Feroz.")
                    else:
                        respuesta = input("¿Es un personaje de una película o serie famosa? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en Harry Potter, Darth Vader o Sherlock Holmes.")
                        else:
                            print("Pensaste en otro tipo de personaje ficticio.")
            else:
                respuesta = input("¿Es una criatura mitologica? (si/no): ").strip().lower()
                if respuesta == "si":
                    respuesta = input("¿Es de la mitologia griega? (si/no): ").strip().lower()
                    if respuesta == "si":
                        respuesta = input("¿Es un dios o semidios? (si/no): ").strip().lower()
                        if respuesta == "si":
                            print("Pensaste en Zeus, Hades o Aquiles.")
                        else:
                            print("Pensaste en un centauro, minotauro o gorgona.")
                    else:
                        respuesta = input("¿Es de la mitologia nórdica? (si/no): ").strip().lower()
                        if respuesta == "si":
                            respuesta = input("¿Es un dios o gigante? (si/no): ").strip().lower()
                            if respuesta == "si":
                                print("Pensaste en Thor, Odín o Loki.")
                            else:
                                print("Pensaste en un elfo, enano o troll.")
                        else:
                            respuesta = input("¿Es de la mitologia egipcia? (si/no): ").strip().lower()
                            if respuesta == "si":
                                respuesta = input("¿Es un dios o faraón? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    print("Pensaste en Ra, Anubis o Cleopatra.")
                                else:
                                    print("Pensaste en un escarabajo, serpiente o esfinge.")
                            else:
                                respuesta = input("¿Es de la mitologia china? (si/no): ").strip().lower()
                                if respuesta == "si":
                                    respuesta = input("¿Es un dios o dragón? (si/no): ").strip().lower()
                                    if respuesta == "si":
                                        print("Pensaste en Buda, Shenlong o Hotei.")
                                    else:
                                        print("Pensaste en un qilin, fénix o jiangshi.")
                                else:
                                    print("Pensaste en un ser mitológico de otra cultura.")             
                else:
                    respuesta = input("¿Es un lugar imaginario? (si/no): ").strip().lower()
                    if respuesta == "si":
                        print("Pensaste en el Paraíso, el Infierno o la Atlántida.")
                    else:
                        print("Pensaste en un concepto abstracto imaginario.")
    else:
        respuesta = input("¿Es un mundo ficticio? (si/no): ").strip().lower()
        if respuesta == "si":
            respuesta = input("¿Es un mundo de fantasía? (si/no): ").strip().lower()
            if respuesta == "si":
                print("Pensaste en Narnia, Hogwarts o la Tierra Media.")
            else:
                print("Pensaste en un universo de ciencia ficción como Star Wars o Star Trek.")
        else:
            print("Pensaste en un concepto filosófico o abstracto como el tiempo o la conciencia.")

print("¡Juego terminado!")