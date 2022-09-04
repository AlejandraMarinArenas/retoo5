#descripción del tetris
#existe un jugador
#existen fichas de varias formas
#existe un puntaje
#existen niveles





class Fichas:
    def __init__(self,forma):
        self.forma = []
        

    def ubicacion_ficha(self,hacia_derecha,hacia_izquierda):
        self.hacia_derecha = hacia_derecha
        self.hacia_izquierda = hacia_izquierda

    def rotar(self,rotar_derecha,rotar_izquierda,rotar_arriba,rotar_abajo):
        self.rotar_derecha = rotar_derecha
        self.rotar_izquierda = rotar_izquierda
        self.rotar_arriba = rotar_arriba
        self.rotar_abajo = rotar_abajo

class Nivel:
    def __init__(self,numero_nivel,nivel_jugador):
        self.numero_nivel = numero_nivel
        self.numero_jugador = nivel_jugador

    def recompensa_por_subir_nivel(self,sube_puntaje):
        self.sube_puntaje = sube_puntaje


class Jugador:
    def __init__(self,nombre,id,nivel):
        self.nombre = str
        self.id = id
        self.nivel = nivel



class Puntaje:
    def __init__(self,agregar_100_por_fila_llena,disminucion_por_saturacion):
        self.agregar_100_por_fila_llena = agregar_100_por_fila_llena
        self.disminucion_por_saturacion = disminucion_por_saturacion


class Dificultad:
    def __init__(self,muy_facil,facil,medio,dificil):
        self.muy_facil = muy_facil
        self.facil = facil
        self.medio = medio
        self.dificil = dificil 



jugador1=Jugador("Juan",8712,14)
jugador2=Jugador("Camila",6745,23)
jugador3=Jugador("Eliza",5634,34)
jugador4=Jugador("Simón",1287,10)


print(jugador1.nivel)





























