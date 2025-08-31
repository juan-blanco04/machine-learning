def pedir_si_no(pregunta):
    """Pide repetidamente hasta que el usuario responda 's' o 'n' (acepta 'si'/'no')."""
    while True:
        r = input(pregunta + " (s/n): ").strip().lower()
        if r in ("s", "si", "sí"):
            return "s"
        if r in ("n", "no"):
            return "n"
        print("Por favor responde 's' (sí) o 'n' (no).")

#--------------------------------------------  RAMAS PRINCIPALES --------------------------------------------#
def rama_abstracto():
    """Rama para conceptos abstractos e intangibles"""
    print("\n--- CATEGORÍA: ABSTRACTOS/INTANGIBLES ---")
    
    r = pedir_si_no("Q3: ¿Está relacionado con emociones o sentimientos?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es una emoción positiva?")
        if r == "s":
            print("EMOCIONES POSITIVAS: alegría, amor, felicidad, esperanza, entusiasmo, gratitud")
        else:
            print("EMOCIONES NEGATIVAS: tristeza, miedo, enojo, ansiedad, celos, vergüenza")
        return
    
    r = pedir_si_no("Q3: ¿Es un concepto matemático o numérico?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es un número específico?")
        if r == "s":
            print("NÚMEROS: enteros, decimales, fracciones, números primos, π, e")
        else:
            print("CONCEPTOS MATEMÁTICOS: álgebra, geometría, cálculo, estadística, probabilidad")
        return
    
    r = pedir_si_no("Q3: ¿Es una idea filosófica o concepto abstracto?")
    if r == "s":
        print("CONCEPTOS FILOSÓFICOS: verdad, justicia, libertad, moral, ética, existencia")
        return
    
    r = pedir_si_no("Q3: ¿Está relacionado con el tiempo?")
    if r == "s":
        print("CONCEPTOS TEMPORALES: tiempo, eternidad, momento, pasado, presente, futuro")
        return
    
    r = pedir_si_no("Q3: ¿Es un concepto espiritual o religioso?")
    if r == "s":
        print("CONCEPTOS ESPIRITUALES: alma, fe, dios, karma, nirvana, reencarnación")
        return
    
    print("CONCEPTO ABSTRACTO NO ESPECIFICADO: idea, pensamiento, concepto intangible")

def rama_seres_vivos():
    """Rama para seres vivos"""
    print("\n--- CATEGORÍA: SERES VIVOS ---")
    
    r = pedir_si_no("Q3: ¿Es un animal?")
    if r == "s":
        animales()
        return
    
    r = pedir_si_no("Q3: ¿Es una planta?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Tiene flores?")
        if r == "s":
            print("PLANTAS CON FLORES: rosas, girasoles, orquídeas, árboles frutales")
        else:
            print("PLANTAS SIN FLORES: helechos, musgos, coníferas, algas")
        return
    
    r = pedir_si_no("Q3: ¿Es un hongo?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es comestible?")
        if r == "s":
            print("HONGOS COMESTIBLES: champiñones, setas, levaduras")
        else:
            print("HONGOS NO COMESTIBLES: mohos, hongos venenosos, parásitos")
        return
    
    r = pedir_si_no("Q3: ¿Es un microorganismo?")
    if r == "s":
        print("MICROORGANISMOS: bacterias, virus, protozoos, amebas")
        return
    
    print("SER VIVO NO CLASIFICADO")

def rama_lugares():
    """Rama para lugares y construcciones"""
    print("\n--- CATEGORÍA: LUGARES/CONSTRUCCIONES ---")
    
    r = pedir_si_no("Q3: ¿Es un lugar natural?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Contiene agua?")
        if r == "s":
            print("LUGARES NATURALES ACUÁTICOS: ríos, lagos, océanos, playas, cascadas")
        else:
            print("LUGARES NATURALES TERRESTRES: montañas, desiertos, bosques, valles, cavernas")
        return
    
    r = pedir_si_no("Q3: ¿Es una construcción humana?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es para habitar?")
        if r == "s":
            print("CONSTRUCCIONES HABITACIONALES: casas, edificios, apartamentos, chozas")
        else:
            r = pedir_si_no("Q5: ¿Es para transporte?")
            if r == "s":
                print("INFRAESTRUCTURA DE TRANSPORTE: puentes, carreteras, aeropuertos, estaciones")
            else:
                print("CONSTRUCCIONES PÚBLICAS: hospitales, escuelas, museos, templos")
        return
    
    r = pedir_si_no("Q3: ¿Es una división geopolítica?")
    if r == "s":
        print("DIVISIONES GEOGRÁFICAS: países, ciudades, estados, pueblos, continentes")
        return
    
    print("LUGAR NO CLASIFICADO")

def rama_persona():
    """Rama para personas y personajes"""
    print("\n--- CATEGORÍA: PERSONAS/PERSONAJES ---")
    
    r = pedir_si_no("Q3: ¿Es una persona real?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es famosa o histórica?")
        if r == "s":
            print("PERSONAS FAMOSAS/HISTÓRICAS: científicos, artistas, líderes, deportistas")
        else:
            print("PERSONAS COMUNES: familiares, amigos, conocidos, personas anónimas")
        return
    
    r = pedir_si_no("Q3: ¿Es un personaje ficticio?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es de literatura?")
        if r == "s":
            print("PERSONAJES LITERARIOS: de novelas, cuentos, poesía, comics")
        else:
            print("PERSONAJES DE MEDIOS: de cine, TV, videojuegos, animación")
        return
    
    print("PERSONA/PERSONAJE NO CLASIFICADO")

def rama_fenomeno():
    """Rama COMPLETA para fenómenos y energías"""
    print("\n--- CATEGORÍA: FENÓMENOS/ENERGÍA ---")
    
    # PRIMER NIVEL: Clasificación general
    r = pedir_si_no("Q3: ¿Es un FENÓMENO NATURAL observable?")
    if r == "s":
        # FENÓMENOS NATURALES
        r = pedir_si_no("Q4: ¿Está relacionado con la ATMÓSFERA o CLIMA?")
        if r == "s":
            # FENÓMENOS METEOROLÓGICOS
            r = pedir_si_no("Q5: ¿Involucra AGUA o PRECIPITACIÓN?")
            if r == "s":
                r = pedir_si_no("Q6: ¿Es en estado LÍQUIDO?")
                if r == "s":
                    print("PRECIPITACIÓN LÍQUIDA: lluvia, llovizna, rocío, garúa")
                else:
                    r = pedir_si_no("Q6: ¿Es en estado SÓLIDO?")
                    if r == "s":
                        print("PRECIPITACIÓN SÓLIDA: nieve, granizo, aguanieve, cellisca")
                    else:
                        print("FENÓMENOS HÚMEDOS: humedad, condensación, evaporación")
            else:
                r = pedir_si_no("Q5: ¿Involucra VIENTO o AIRE?")
                if r == "s":
                    r = pedir_si_no("Q6: ¿Es de ALTA INTENSIDAD?")
                    if r == "s":
                        print("FENÓMENOS EÓLICOS INTENSOS: huracán, tornado, tifón, ciclón")
                    else:
                        print("FENÓMENOS EÓLICOS: viento, brisa, ventisca, ráfaga")
                else:
                    r = pedir_si_no("Q5: ¿Involucra TEMPERATURA?")
                    if r == "s":
                        print("FENÓMENOS TÉRMICOS: calor, frío, ola de calor, helada")
                    else:
                        r = pedir_si_no("Q5: ¿Involucra ELECTRICIDAD ATMOSFÉRICA?")
                        if r == "s":
                            print("FENÓMENOS ELÉCTRICOS: rayo, relámpago, trueno, tormenta eléctrica")
                        else:
                            r = pedir_si_no("Q5: ¿Involucra OPTICA ATMOSFÉRICA?")
                            if r == "s":
                                print("FENÓMENOS ÓPTICOS: arcoíris, halo, espejismo, parhelio")
                            else:
                                print("FENÓMENOS ATMOSFÉRICOS: presión atmosférica, frente climático")
            return
        
        r = pedir_si_no("Q4: ¿Es un FENÓMENO GEOLÓGICO?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Involucra MOVIMIENTO TERRESTRE?")
            if r == "s":
                print("FENÓMENOS SÍSMICOS: terremoto, temblor, tsunami, maremoto")
            else:
                r = pedir_si_no("Q5: ¿Involucra ACTIVIDAD VOLCÁNICA?")
                if r == "s":
                    print("FENÓMENOS VOLCÁNICOS: erupción, lava, ceniza, fumarola")
                else:
                    r = pedir_si_no("Q5: ¿Involucra EROSIÓN?")
                    if r == "s":
                        print("FENÓMENOS DE EROSIÓN: deslizamiento, avalancha, derrumbe")
                    else:
                        print("FENÓMENOS GEOLÓGICOS: formación de montañas, deriva continental")
            return
        
        r = pedir_si_no("Q4: ¿Es un FENÓMENO ASTRONÓMICO?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Involucra CUERPOS CELESTES?")
            if r == "s":
                print("FENÓMENOS ASTRONÓMICOS: eclipse, lluvia de estrellas, conjunción, oposición")
            else:
                r = pedir_si_no("Q5: ¿Es un FENÓMENO LUMINOSO?")
                if r == "s":
                    print("FENÓMENOS LUMINOSOS: aurora boreal, luz zodiacal, supernova")
                else:
                    print("FENÓMENOS ESPACIALES: agujero negro, nebulosa, galaxia")
            return
        
        r = pedir_si_no("Q4: ¿Es un FENÓMENO HIDROLÓGICO?")
        if r == "s":
            print("FENÓMENOS HIDROLÓGICOS: marea, corriente, ola, inundación, sequía")
            return
        
        r = pedir_si_no("Q4: ¿Es un FENÓMENO BIOLÓGICO?")
        if r == "s":
            print("FENÓMENOS BIOLÓGICOS: fotosíntesis, migración, hibernación, eclosión")
            return
        
        print("FENÓMENO NATURAL NO ESPECIFICADO")
        return
    
    # SEGUNDO NIVEL: ENERGÍAS
    r = pedir_si_no("Q3: ¿Es una FORMA DE ENERGÍA?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es energía TÉRMICA?")
        if r == "s":
            print("ENERGÍA TÉRMICA: calor, temperatura, combustión, conducción")
            return
        
        r = pedir_si_no("Q4: ¿Es energía ELÉCTRICA/MAGNÉTICA?")
        if r == "s":
            print("ENERGÍA ELÉCTRICA/MAGNÉTICA: electricidad, magnetismo, corriente, campo electromagnético")
            return
        
        r = pedir_si_no("Q4: ¿Es energía LUMINOSA/RADIANTE?")
        if r == "s":
            print("ENERGÍA RADIANTE: luz, radiación, espectro electromagnético, fotones")
            return
        
        r = pedir_si_no("Q4: ¿Es energía SONORA?")
        if r == "s":
            print("ENERGÍA SONORA: sonido, onda sonora, eco, resonancia")
            return
        
        r = pedir_si_no("Q4: ¿Es energía MECÁNICA?")
        if r == "s":
            print("ENERGÍA MECÁNICA: movimiento, fuerza, trabajo, potencia")
            return
        
        r = pedir_si_no("Q4: ¿Es energía QUÍMICA/NUCLEAR?")
        if r == "s":
            print("ENERGÍA QUÍMICA/NUCLEAR: reacción química, fisión, fusión, radiactividad")
            return
        
        print("ENERGÍA NO ESPECIFICADA")
        return
    
    # TERCER NIVEL: FENÓMENOS FÍSICOS
    r = pedir_si_no("Q3: ¿Es un FENÓMENO FÍSICO fundamental?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Está relacionado con FUERZAS?")
        if r == "s":
            print("FUERZAS FUNDAMENTALES: gravedad, electromagnetismo, fuerza nuclear")
            return
        
        r = pedir_si_no("Q4: ¿Está relacionado con MOVIMIENTO?")
        if r == "s":
            print("FENÓMENOS DE MOVIMIENTO: inercia, aceleración, fricción, momentum")
            return
        
        r = pedir_si_no("Q4: ¿Está relacionado con MATERIA?")
        if r == "s":
            print("FENÓMENOS DE LA MATERIA: estados de la materia, cambio de fase, densidad")
            return
        
        print("FENÓMENO FÍSICO NO ESPECIFICADO")
        return
    
    # CUARTO NIVEL: FENÓMENOS QUÍMICOS
    r = pedir_si_no("Q3: ¿Es un FENÓMENO QUÍMICO?")
    if r == "s":
        print("FENÓMENOS QUÍMICOS: reacción, oxidación, combustión, fermentación")
        return
    
    # QUINTO NIVEL: FENÓMENOS HUMANOS
    r = pedir_si_no("Q3: ¿Es un FENÓMENO SOCIAL o HUMANO?")
    if r == "s":
        print("FENÓMENOS SOCIALES: globalización, migración, revolución, tendencia")
        return
    
    print("FENÓMENO/ENERGÍA NO CLASIFICADO")

def rama_objeto():
    """Rama para objetos inanimados"""
    print("\n--- CATEGORÍA: OBJETOS INANIMADOS ---")
    
    r = pedir_si_no("Q3: ¿Es NATURAL (no fabricado)?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es MINERAL?")
        if r == "s":
            print("OBJETOS MINERALES: rocas, cristales, gemas, metales, minerales")
        else:
            r = pedir_si_no("Q4: ¿Es de origen VEGETAL?")
            if r == "s":
                print("OBJETOS VEGETALES: madera, frutas, semillas, flores, hojas")
            else:
                print("OBJETOS ANIMALES: huesos, conchas, cuernos, pieles, plumas")
        return
    
    r = pedir_si_no("Q3: ¿Es ARTIFICIAL (fabricado)?")
    if r == "s":
        r = pedir_si_no("Q4: ¿Es HERRAMIENTA o UTENSILIO?")
        if r == "s":
            print("HERRAMIENTAS: martillo, destornillador, cuchillo, llave, pinza")
        else:
            r = pedir_si_no("Q4: ¿Es DISPOSITIVO ELECTRÓNICO?")
            if r == "s":
                print("ELECTRÓNICOS: teléfono, computadora, televisor, radio, tablet")
            else:
                r = pedir_si_no("Q4: ¿Es MUEBLE?")
                if r == "s":
                    print("MUEBLES: silla, mesa, cama, armario, estante")
                else:
                    r = pedir_si_no("Q4: ¿Es VEHÍCULO?")
                    if r == "s":
                        print("VEHÍCULOS: auto, bicicleta, avión, barco, tren")
                    else:
                        print("OBJETOS ARTIFICIALES: ropa, juguetes, libros, instrumentos")
        return
    
    print("OBJETO NO CLASIFICADO")

#------------------------------------------- SUB-RAMAS PRINCIPALES ------------------------------------------#
def animales():
    """Sub-rama para animales"""
    print("\n--- SUBCATEGORÍA: ANIMALES ---")
    
    r = pedir_si_no("Q4: ¿Es DOMÉSTICO?")
    if r == "s":
        r = pedir_si_no("Q5: ¿Es MAMÍFERO?")
        if r == "s":
            r = pedir_si_no("Q6: ¿Es PEQUEÑO?")
            if r == "s":
                r = pedir_si_no("Q7: ¿Hace CHILLIDOS?")
                if r == "s":
                    print("ROEDORES DOMÉSTICOS: hámster, ratón, gerbo, cobaya")
                else:
                    print("MAMÍFEROS PEQUEÑOS: conejo, hurón, erizo")
            else:
                r = pedir_si_no("Q6: ¿LADRA o MAÚLLA?")
                if r == "s":
                    print("MASCOTAS COMUNES: perro, gato")
                else:
                    r = pedir_si_no("Q7: ¿Es de GRANJA?")
                    if r == "s":
                        r = pedir_si_no("Q8: ¿Produce LANA?")
                        if r == "s":
                            print("ANIMALES DE LANAR: oveja, alpaca, llama")
                        else:
                            print("ANIMALES LECHEROS: vaca, cabra, búfala")
                    else:
                        r = pedir_si_no("Q7: ¿RELINCHA?")
                        if r == "s":
                            print("EQUINOS: caballo, pony, burro, mula")
                        else:
                            print("ANIMALES DE CORRAL: cerdo, pavo, gallina")
            return
        
        r = pedir_si_no("Q5: ¿Es AVE?")
        if r == "s":
            r = pedir_si_no("Q6: ¿CANTA?")
            if r == "s":
                print("AVES CANORAS: canario, periquito, jilguero, diamante")
            else:
                print("AVES DE CORRAL: gallina, pato, ganso, pavo")
            return
        
        r = pedir_si_no("Q5: ¿Es ACUÁTICO?")
        if r == "s":
            print("ANIMALES ACUÁTICOS DOMÉSTICOS: peces, tortugas acuáticas")
            return
        
        r = pedir_si_no("Q5: ¿Es REPTIL/ANFIBIO?")
        if r == "s":
            print("REPTILES/ANFIBIOS DOMÉSTICOS: tortugas, iguanas, ranas, salamandras")
            return
        
        print("ANIMAL DOMÉSTICO NO ESPECIFICADO")
        return
    
    else:
        # Animales salvajes
        r = pedir_si_no("Q4: ¿Es MAMÍFERO?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Es CARNÍVORO?")
            if r == "s":
                r = pedir_si_no("Q6: ¿Es GRANDE?")
                if r == "s":
                    print("GRANDES DEPREDADORES: león, tigre, oso, lobo, pantera")
                else:
                    print("PEQUEÑOS DEPREDADORS: zorro, lince, hurón, comadreja")
            else:
                r = pedir_si_no("Q5: ¿Es HERBÍVORO?")
                if r == "s":
                    r = pedir_si_no("Q6: ¿Es MUY GRANDE?")
                    if r == "s":
                        print("GRANDES HERBÍVOROS: elefante, jirafa, rinoceronte, hipopótamo")
                    else:
                        print("HERBÍVOROS MEDIANOS: ciervo, cebra, antílope, caballo salvaje")
                else:
                    print("OMNÍVOROS: oso, mapache, cerdo salvaje, mono")
            return
        
        r = pedir_si_no("Q4: ¿Es AVE?")
        if r == "s":
            r = pedir_si_no("Q5: ¿Es RAPAZ?")
            if r == "s":
                print("AVES RAPACES: águila, halcón, búho, buitre, cernícalo")
            else:
                r = pedir_si_no("Q5: ¿Es ACUÁTICA?")
                if r == "s":
                    print("AVES ACUÁTICAS: pato, cisne, gaviota, pelícano, pingüino")
                else:
                    print("AVES TERRESTRES: paloma, gorrión, cuervo, colibrí, gallina salvaje")
            return
        
        r = pedir_si_no("Q4: ¿Es REPTIL?")
        if r == "s":
            print("REPTILES: serpientes, lagartos, cocodrilos, tortugas, tuátaras")
            return
        
        r = pedir_si_no("Q4: ¿Es PEZ?")
        if r == "s":
            print("PECES: tiburón, atún, salmón, pez payaso, anguila")
            return
        
        r = pedir_si_no("Q4: ¿Es INSECTO/ARÁCNIDO?")
        if r == "s":
            print("ARTRÓPODOS: mariposa, abeja, araña, escorpión, cangrejo")
            return
        
        print("ANIMAL SALVAJE NO ESPECIFICADO")

def main():
    print("Piensa en lo que sea y lo adivinaré en (hasta) 20 preguntas.\nResponde solo 's' o 'n'.\n")

    # ESTRUCTURA CORREGIDA - Primera pregunta mejorada
    r = pedir_si_no("Q1: ¿Es algo FÍSICO que puedes percibir con los sentidos?")
    
    if r == "s":
        # Es físico - ahora preguntamos qué tipo de cosa física
        r = pedir_si_no("Q2: ¿Es un SER VIVO?")
        if r == "s":
            rama_seres_vivos()
            return
            
        r = pedir_si_no("Q2: ¿Es un LUGAR o CONSTRUCCIÓN?")
        if r == "s":
            rama_lugares()
            return
            
        r = pedir_si_no("Q2: ¿Es una PERSONA o PERSONAJE?")
        if r == "s":
            rama_persona()
            return

        r = pedir_si_no("Q2: ¿Es un FENÓMENO FÍSICO observable?")
        if r == "s":
            rama_fenomeno()
            return
            
        r = pedir_si_no("Q2: ¿Es un OBJETO INANIMADO?")
        if r == "s":
            rama_objeto()
            return
            
        print("No se pudo clasificar el concepto físico")
        
    else:
        # No es físico - debe ser abstracto o concepto intangible
        r = pedir_si_no("Q2: ¿Es un CONCEPTO ABSTRACTO o INTANGIBLE?")
        if r == "s":
            rama_abstracto()
            return
            
        print("No se pudo clasificar el concepto no físico")

if __name__ == "__main__":
    main()