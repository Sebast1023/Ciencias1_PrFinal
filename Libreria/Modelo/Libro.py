from Modelo.Base import Base

class Libro(Base):
    def __init__(self, codigo: int, titulo: str, autor: str, fecha_publicacion: int, genero: str):
        """
        Constructor de la clase Libro.
        
        Args:
            codigo (int): Código único del libro (clave primaria).
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            fecha_publicacion (int): Año de publicación del libro.
            genero (str): Género del libro (por ejemplo, "Ficción", "No Ficción").
        """
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.genero = genero
    
    def __str__(self):
        """
        Representación del libro como cadena de texto.
        """
        return f"Código: {self.codigo}, Título: {self.titulo}, Autor: {self.autor}, Año de publicación: {self.fecha_publicacion}, Género: {self.genero}"
    
    def get_codigo(self) -> int:
        """
        Retorna el código único del libro.
        """
        return self.codigo
    
    def to_dict(self):
        """
        Convierte el libro a un diccionario para ser guardado como JSON.
        
        Returns:
            dict: Diccionario con los datos del libro.
        """
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "autor": self.autor,
            "fecha_publicacion": self.fecha_publicacion,
            "genero": self.genero
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """
        Crea un libro a partir de un diccionario.
        
        Args:
            data (dict): Diccionario con los datos del libro.
        
        Returns:
            Libro: Una nueva instancia del libro.
        """
        return cls(
            data["codigo"],
            data["titulo"],
            data["autor"],
            data["fecha_publicacion"],
            data["genero"]
        )