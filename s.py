import random
import math

class Individuo:
    def __init__(self, genes=None, grupo_hermanos=None):
        if genes is None:
            # Crear genes aleatorios entre 0 y 9
            self.genes = [random.randint(0, 9) for _ in range(20)]
        else:
            self.genes = genes.copy()
        self.padre = None
        self.madre = None
        self.grupo_hermanos = grupo_hermanos  # Para marcar hermanos de la generación inicial
    
    def fitness(self):
        """Calcula el fitness como la suma de todos los genes"""
        return sum(self.genes)
    
    def es_perfecto(self):
        """Verifica si todos los genes son 9"""
        return all(gen == 9 for gen in self.genes)
    
    def mutar(self, probabilidad=0.1):
        """Aplica mutación a un gen aleatorio con la probabilidad dada"""
        if random.random() < probabilidad:
            # Seleccionar un gen aleatorio para mutar
            gen_aleatorio = random.randint(0, 19)  # Índice de 0 a 19
            self.genes[gen_aleatorio] = random.randint(1, 9)
    
    def __str__(self):
        return f"Genes: {self.genes}, Fitness: {self.fitness()}"

def crear_poblacion_inicial(tamaño=100):
    """Crea la población inicial con individuos aleatorios marcados como hermanos"""
    poblacion = []
    
    # Marcar hermanos: 1,2 hermanos; 3,4 hermanos; 5,6 hermanos, etc.
    for i in range(tamaño):
        grupo_hermanos = (i // 2) + 1  # 1,2 -> grupo 1; 3,4 -> grupo 2, etc.
        individuo = Individuo(grupo_hermanos=grupo_hermanos)
        poblacion.append(individuo)
    
    return poblacion

def reproducir(padre, madre):
    """Crea dos hijos a partir de dos padres"""
    hijo1_genes = []
    hijo2_genes = []
    
    for i in range(20):
        # Calcular promedio de los genes de los padres
        promedio = (padre.genes[i] + madre.genes[i]) / 2
        
        # Asignar valores alto y bajo aleatoriamente
        valor_alto = math.ceil(promedio)
        valor_bajo = math.floor(promedio)
        
        # Decidir aleatoriamente quién recibe qué valor
        if random.random() < 0.5:
            hijo1_genes.append(valor_alto)
            hijo2_genes.append(valor_bajo)
        else:
            hijo1_genes.append(valor_bajo)
            hijo2_genes.append(valor_alto)
    
    # Crear los hijos
    hijo1 = Individuo(hijo1_genes)
    hijo2 = Individuo(hijo2_genes)
    
    # Establecer parentesco
    hijo1.padre = padre
    hijo1.madre = madre
    hijo2.padre = padre
    hijo2.madre = madre
    
    # Los hijos no tienen grupo_hermanos (solo la generación inicial)
    hijo1.grupo_hermanos = None
    hijo2.grupo_hermanos = None
    
    return hijo1, hijo2

def son_hermanos(ind1, ind2):
    """Verifica si dos individuos son hermanos"""
    # Hermanos de la generación inicial (mismo grupo_hermanos)
    if ind1.grupo_hermanos is not None and ind2.grupo_hermanos is not None:
        return ind1.grupo_hermanos == ind2.grupo_hermanos
    
    # Hermanos de generaciones posteriores (mismos padres)
    return (ind1.padre is not None and ind2.padre is not None and
            ind1.madre is not None and ind2.madre is not None and
            ind1.padre == ind2.padre and ind1.madre == ind2.madre)

def seleccionar_parejas(poblacion):
    """Selecciona 50 parejas aleatorias que no sean hermanos"""
    parejas = []
    individuos_disponibles = poblacion.copy()
    random.shuffle(individuos_disponibles)
    
    intentos = 0
    max_intentos = 1000
    
    while len(parejas) < 50 and len(individuos_disponibles) >= 2 and intentos < max_intentos:
        # Tomar los dos primeros individuos disponibles
        ind1 = individuos_disponibles.pop(0)
        
        # Buscar una pareja válida (no hermano)
        pareja_encontrada = False
        for i, ind2 in enumerate(individuos_disponibles):
            if not son_hermanos(ind1, ind2):
                parejas.append((ind1, ind2))
                individuos_disponibles.pop(i)
                pareja_encontrada = True
                break
        
        # Si no se encontró pareja válida, devolver ind1 a la lista
        if not pareja_encontrada:
            individuos_disponibles.append(ind1)
        
        intentos += 1
    
    # Si no se pudieron formar 50 parejas, completar con las disponibles
    while len(parejas) < 50 and len(individuos_disponibles) >= 2:
        ind1 = individuos_disponibles.pop(0)
        ind2 = individuos_disponibles.pop(0)
        parejas.append((ind1, ind2))
    
    return parejas

def nueva_generacion(poblacion):
    """Crea una nueva generación a partir de la población actual"""
    parejas = seleccionar_parejas(poblacion)
    nueva_poblacion = []
    
    for padre, madre in parejas:
        hijo1, hijo2 = reproducir(padre, madre)
        
        # Aplicar mutación
        hijo1.mutar()
        hijo2.mutar()
        
        nueva_poblacion.extend([hijo1, hijo2])
    
    return nueva_poblacion

def imprimir_estadisticas(poblacion, generacion, mejor_historico=None, generacion_mejor_historico=None):
    """Imprime estadísticas de la generación"""
    fitness_valores = [ind.fitness() for ind in poblacion]
    mejor_individuo = max(poblacion, key=lambda x: x.fitness())
    
    print(f"\n=== GENERACIÓN {generacion} ===")
    print(f"Población: {len(poblacion)} individuos")
    print(f"Fitness promedio: {sum(fitness_valores) / len(fitness_valores):.2f}")
    print(f"Fitness máximo: {max(fitness_valores)}")
    print(f"Fitness mínimo: {min(fitness_valores)}")
    print(f"Mejor individuo actual: {mejor_individuo}")
    
    # Mostrar el mejor individuo histórico
    if mejor_historico is not None:
        print(f"🏆 MEJOR HISTÓRICO: {mejor_historico} (Generación {generacion_mejor_historico})")
        if mejor_historico.fitness() == mejor_individuo.fitness() and generacion_mejor_historico == generacion:
            print("   ✨ ¡NUEVO RÉCORD EN ESTA GENERACIÓN! ✨")
    
    # Mostrar algunos individuos de muestra
    print(f"\nMuestra de individuos:")
    for i in range(min(5, len(poblacion))):
        individuo = poblacion[i]
        if individuo.grupo_hermanos is not None:
            print(f"  {i+1}: {individuo} (Grupo hermanos: {individuo.grupo_hermanos})")
        else:
            print(f"  {i+1}: {individuo}")
    
    # Si es la generación inicial, mostrar la estructura de hermanos
    if generacion == 0:
        print(f"\nEstructura de hermanos en generación inicial:")
        grupos = {}
        for i, individuo in enumerate(poblacion):
            if individuo.grupo_hermanos not in grupos:
                grupos[individuo.grupo_hermanos] = []
            grupos[individuo.grupo_hermanos].append(i+1)
        
        # Mostrar primeros 10 grupos como ejemplo
        for grupo in sorted(grupos.keys())[:10]:
            print(f"  Grupo {grupo}: Individuos {grupos[grupo]}")
        if len(grupos) > 10:
            print(f"  ... y {len(grupos) - 10} grupos más")

def algoritmo_genetico():
    """Ejecuta el algoritmo genético hasta encontrar el ser perfecto"""
    print("🧬 INICIANDO ALGORITMO GENÉTICO 🧬")
    print("Objetivo: Encontrar un individuo con todos los genes en 9")
    print("\n📊 ¿Qué es FITNESS?")
    print("- Fitness = suma de todos los genes del individuo")
    print("- Fitness máximo posible = 180 (20 genes × 9)")
    print("- Fitness mínimo posible = 0 (20 genes × 0)")
    print("- Mayor fitness = mejor individuo")
    print("\nParámetros:")
    print("- 20 genes por individuo (valores 0-9)")
    print("- 100 individuos por generación")
    print("- Generación inicial: hermanos marcados (1,2), (3,4), (5,6)...")
    print("- 50 parejas, 2 hijos por pareja")
    print("- 10% probabilidad de mutación (1 gen aleatorio por individuo)")
    print("- Sin reproducción entre hermanos")
    print("- SOLO TERMINA al encontrar ser perfecto (fitness = 180)")
    print("- 🏆 Seguimiento del mejor individuo histórico")
    print("="*60)
    
    # Crear población inicial
    poblacion = crear_poblacion_inicial(100)
    generacion = 0
    
    # Variables para rastrear el mejor individuo histórico
    mejor_historico = max(poblacion, key=lambda x: x.fitness())
    generacion_mejor_historico = 0
    
    # Mostrar generación inicial
    imprimir_estadisticas(poblacion, generacion, mejor_historico, generacion_mejor_historico)
    
    # Buscar el ser perfecto - BUCLE INFINITO HASTA ENCONTRARLO
    while True:
        # Verificar si hay algún individuo perfecto
        ser_perfecto = None
        for individuo in poblacion:
            if individuo.es_perfecto():
                ser_perfecto = individuo
                break
        
        # SI SE ENCUENTRA EL SER PERFECTO, TERMINAR EL PROGRAMA
        if ser_perfecto:
            print(f"\n🎉🎉🎉 ¡SER PERFECTO ENCONTRADO EN LA GENERACIÓN {generacion}! 🎉🎉🎉")
            print(f"Genes: {ser_perfecto.genes}")
            print(f"Fitness: {ser_perfecto.fitness()} / 180 (PERFECTO)")
            print(f"🏆 El mejor histórico fue superado en la generación {generacion}")
            print("🧬 EVOLUCIÓN COMPLETADA - OBJETIVO ALCANZADO 🧬")
            return  # TERMINAR EL PROGRAMA AQUÍ
        
        # Crear nueva generación
        generacion += 1
        poblacion = nueva_generacion(poblacion)
        
        # Verificar si hay un nuevo mejor individuo histórico
        mejor_actual = max(poblacion, key=lambda x: x.fitness())
        if mejor_actual.fitness() > mejor_historico.fitness():
            mejor_historico = mejor_actual
            generacion_mejor_historico = generacion
        
        # Imprimir estadísticas cada 10 generaciones o si es una de las primeras
        if generacion <= 5 or generacion % 10 == 0:
            imprimir_estadisticas(poblacion, generacion, mejor_historico, generacion_mejor_historico)
            print(f"⏳ Continuando búsqueda... Generación {generacion}")
    
    # Esta línea nunca debería ejecutarse
    print("❌ ERROR: El bucle terminó inesperadamente")

# Ejecutar el algoritmo
if __name__ == "__main__":
    algoritmo_genetico()