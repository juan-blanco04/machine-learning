import random
import time

# Definimos una clase para el individuo
class Individuo:
    def __init__(self, genes=None, grupo_hermanos=None):
        if genes is None:
            # Crear genes aleatorios entre 1 y 9
            self.genes = [random.randint(1, 9) for _ in range(20)]
        else:
            self.genes = genes.copy()
        self.padre = None
        self.madre = None
        self.grupo_hermanos = grupo_hermanos  # Para marcar hermanos de la generación inicial

    def calificacion(self):
        """Calcula la calificación como la suma de todos los genes"""
        return sum(self.genes)

    def es_perfecto(self):
        """Verifica si todos los genes son 9"""
        return all(gen == 9 for gen in self.genes)

    def mutar(self, probabilidad=0.15):
        """Aplica mutación a un gen aleatorio con la probabilidad dada"""
        if random.random() < probabilidad:
            # Seleccionar un gen aleatorio para mutar
            gen_aleatorio = random.randint(0, 19)  # Índice de 0 a 19
            self.genes[gen_aleatorio] = random.randint(1, 9)

# Función para generar la población inicial
def crear_parejas(num_parejas=50):
    parejas = []
    for i in range(num_parejas):
        grupo_hermanos = (i // 2) + 1  # 1,2 -> grupo 1; 3,4 -> grupo 2, etc.
        madre = Individuo(grupo_hermanos=grupo_hermanos)
        padre = Individuo(grupo_hermanos=grupo_hermanos)
        pareja = (madre, padre)
        parejas.append(pareja)
    return parejas

# Función para crear hijos de una pareja, promediando los genes
def crear_hijos_por_promedio(pareja):
    madre, padre = pareja
    hijos = []
    for _ in range(2):  # Cada pareja tiene 2 hijos
        hijo_genes = []
        for i in range(20):  # Para cada gen de los padres
            promedio = (madre.genes[i] + padre.genes[i]) / 2
            # Redondeamos el promedio
            if promedio % 1 == 0.5:
                hijo_genes.append([int(promedio), int(promedio) + 1][random.choice([0, 1])])  # Redondeo aleatorio
            else:
                hijo_genes.append(round(promedio))
        
        hijo = Individuo(hijo_genes)
        hijo.mutar()  # Manteniendo la mutación al 15% como en el código original
        hijos.append(hijo)

        # Establecer el parentesco
        hijo.padre = padre
        hijo.madre = madre
        hijo.grupo_hermanos = None  # Los hijos no tienen grupo de hermanos
    
    return hijos

# Función para seleccionar parejas aleatorias
def seleccionar_parejas_aleatorias(poblacion):
    """Selecciona aleatoriamente 50 parejas"""
    parejas = []
    while len(parejas) < 50:
        # Selección aleatoria de 2 individuos (padres)
        madre, padre = random.sample(poblacion, 2)
        parejas.append((madre, padre))
    return parejas

# Función para simular varias generaciones
def evolucionar(parejas, generaciones=1000):
    mejor_individuo = None
    mejor_calificacion = 0
    tiempo_inicio = time.time()  # Comienza el temporizador
    
    generacion = 0
    while True:
        generacion += 1
        nueva_generacion = []
        for pareja in parejas:
            hijos = crear_hijos_por_promedio(pareja)
            nueva_generacion.extend(hijos)
        
        # Aquí seleccionamos solo a los hijos, no a los padres
        mejor_individuo_generacion = max(nueva_generacion, key=lambda x: x.calificacion())
        mejor_calificacion_generacion = mejor_individuo_generacion.calificacion()

        # Imprimir el mejor individuo de toda la generación (solo los hijos) con el número de generación
        print(f"Generación {generacion}: Mejor individuo -> Calificación: {mejor_calificacion_generacion}, Genes: {mejor_individuo_generacion.genes}")
        
        # Verificar si el mejor individuo de la generación supera al mejor histórico
        if mejor_calificacion_generacion > mejor_calificacion:
            mejor_calificacion = mejor_calificacion_generacion
            mejor_individuo = mejor_individuo_generacion
        
        # Si algún individuo tiene calificación perfecta, terminamos
        if mejor_individuo.es_perfecto():  # Verificamos si todos los genes son 9
            tiempo_final = time.time()  # Termina el temporizador
            tiempo_total = tiempo_final - tiempo_inicio  # Calcula el tiempo total
            print(f"Generación {generacion} encontró un individuo perfecto!")
            print(f"Tiempo total: {tiempo_total:.2f} segundos")
            break
    
    return mejor_individuo

# Ejecutar el programa
parejas_iniciales = crear_parejas()
mejor_individuo = evolucionar(parejas_iniciales)

# Resultado final
if mejor_individuo:
    print("Mejor individuo encontrado:")
    print(f"Calificación total: {mejor_individuo.calificacion()}")
    print(f"Genes: {mejor_individuo.genes}")
else:
    print("No se encontró un individuo perfecto.")
