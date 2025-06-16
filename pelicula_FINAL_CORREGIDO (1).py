class ContenidoAudiovisual:
    def __init__(self,titulo,duracion,genero):
        self.titulo = titulo
        self.duracion = duracion  #en minutos
        self.genero = genero
        self.premios = 0

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Duración: {self.duracion} min")
        print(f"Género: {self.genero}")
        print(f"Premios: {self.premios}")

    def añadir_premio(self):
        self.premios += 1



class Pelicula(ContenidoAudiovisual):
    """Clase que representa una película con un director."""

    def __init__(self, titulo, duracion, genero, director):
        super().__init__(titulo, duracion, genero)
        self.director = director

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Director: {self.director}")

    def to_dict(self):
        return {
            "tipo": "Pelicula",
            "titulo": self.titulo,
            "duracion": self.duracion,
            "genero": self.genero,
            "premios": self.premios,
            "director": self.director
        }


class Serie(ContenidoAudiovisual):
    def __init__(self, titulo, duracion, genero, temporadas):
        super().__init__(titulo, duracion, genero)
        self.temporadas = temporadas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Temporadas: {self.temporadas}")

    def to_dict(self):
        return{
            "tipo": "Serie",
            "titulo": self.titulo,
            "duracion": self.duracion,
            "genero": self.genero,
            "premios": self.premios,
            "temporadas": self.temporadas

        }

class Documental(ContenidoAudiovisual):
    def __init__(self, titulo, duracion, genero, tema):
        super().__init__(titulo, duracion, genero)
        self.tema = tema

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tema: {self.tema}")

    def to_dict(self):
        return {
            "tipo": "Documental",
            "titulo": self.titulo,
            "duracion": self.duracion,
            "genero": self.genero,
            "premios": self.premios,
            "tema": self.tema

        }

class Cortometraje(ContenidoAudiovisual):
    def __init__(self, titulo, duracion, genero, festival):
        super().__init__(titulo, duracion, genero)
        self.festival = festival

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Festival: {self.festival}")
    def to_dict(self):
        return {
            "tipo": "Cortometraje",
            "titulo": self.titulo,
            "duracion": self.duracion,
            "genero": self.genero,
            "premios": self.premios,
            "festival": self.festival

        }
    
