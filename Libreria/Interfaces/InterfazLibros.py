from typing import Optional
from Interfaces.InterfazBase import InterfazBase
from Modelo.Libro import Libro

class InterfazLibros(InterfazBase):
    def __init__(self):
        """
        Inicializa la interfaz específica para gestionar libros
        """
        super().__init__("JSON/Libros.json", Libro, "libro")
    
    def solicitar_datos_entidad(self, codigo_actual: Optional[int] = None) -> Optional[Libro]:
        """
        Este método será responsable de solicitar los datos de un libro con validación.

        Args:
            codigo_actual (Optional[int]): El código actual del libro (para actualizaciones)

        Returns:
            Optional[Libro]: Una instancia de Libro con los datos ingresados o None si hubo error
        """
        # Obtener código
        if codigo_actual is None:
            codigo = self.obtener_codigo()
            if codigo is None:
                return None
                
            # Verificar duplicados al agregar
            if self.gestor.buscar_por_codigo(codigo):
                print(f"[ADVERTENCIA] El código {codigo} ya existe. No se puede agregar un libro duplicado.")
                return None
        else:
            # Para actualización, el código no se puede cambiar
            codigo = codigo_actual
        
        # Solicitar resto de datos
        if codigo_actual is None:
            # Agregando nuevo libro
            titulo = input("Título del libro: ")
            
            # Validar año de publicación
            try:
                fecha_publicacion = int(input("Año de publicación: "))
                if fecha_publicacion <= 0:
                    print("[ERROR] El año de publicación debe ser un número positivo.")
                    return None
            except ValueError:
                print("[ERROR] El año de publicación debe ser un número entero.")
                return None
            
            # Validar género
            genero = input("Género del libro: ")
            if not genero:
                print("[ERROR] El género es obligatorio.")
                return None
        else:
            # Actualizando libro existente
            libro_actual = self.gestor.buscar_por_codigo(codigo)
            titulo = input(f"Título [{libro_actual.titulo}]: ") or libro_actual.titulo
            
            # Validar año de publicación
            fecha_input = input(f"Año de publicación [{libro_actual.fecha_publicacion}]: ")
            if fecha_input:
                try:
                    fecha_publicacion = int(fecha_input)
                    if fecha_publicacion <= 0:
                        print("[ERROR] El año de publicación debe ser un número positivo.")
                        return None
                except ValueError:
                    print("[ERROR] El año de publicación debe ser un número entero.")
                    return None
            else:
                fecha_publicacion = libro_actual.fecha_publicacion
            
            # Validar género
            genero_input = input(f"Género [{libro_actual.genero}]: ")
            if genero_input:
                genero = genero_input
            else:
                genero = libro_actual.genero
        
        # Validar que todos los campos estén completos
        if not titulo:
            print("[ERROR] El título es obligatorio.")
            return None
            
        return Libro(codigo, titulo, genero, fecha_publicacion)
    
    def get_campos_busqueda(self) -> dict:
        """
        Este método retorna un diccionario con los campos de búsqueda disponibles para libros
        
        Returns:
            dict: Diccionario con formato {opcion: nombre_campo}
        """
        return {
            '1': 'codigo',
            '2': 'titulo',
            '3': 'fecha_publicacion',
            '4': 'genero'
        }