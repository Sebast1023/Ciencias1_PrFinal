from Modelo.Base import Base

class Empleado(Base):
    def __init__(self, cedula: int, nombre: str, correo: str, cargo: str, sede: str):
        """
        Constructor para crear una nueva instancia de empleado.

        Args:
            cedula (int): La cédula única de identificación del empleado.
            nombre (str): El nombre completo del empleado.
            correo (str): La dirección de correo electrónico del empleado.
            cargo (str): El cargo o puesto que ocupa el empleado en la empresa.
            sede (str): La sede o ubicación de trabajo del empleado.
        """
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.cargo = cargo
        self.sede = sede

    def get_codigo(self) -> int:
        """
        Retorna la cédula única de identificación del empleado.

        Returns:
            int: Cédula del empleado.
        """
        return self.cedula

    def to_dict(self):
        """
        Convierte la instancia de empleado a un diccionario.

        Returns:
            dict: Un diccionario con todos los atributos del empleado.
        """
        return {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "correo": self.correo,
            "cargo": self.cargo,
            "sede": self.sede
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Crea una instancia de `Empleado` a partir de un diccionario.

        Args:
            data (dict): Un diccionario con los datos del empleado.

        Returns:
            Empleado: Una nueva instancia de `Empleado`.
        """
        return Empleado(
            data["cedula"],
            data["nombre"],
            data["correo"],
            data["cargo"],
            data["sede"]
        )

    def __str__(self):
        """
        Proporciona una representación en cadena de texto de la instancia de empleado.

        Returns:
            str: Una cadena con todos los datos del empleado.
        """
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}, Correo: {self.correo}, Cargo: {self.cargo}, Sede: {self.sede}"
