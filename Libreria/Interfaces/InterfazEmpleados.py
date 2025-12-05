from typing import Optional
from Interfaces.InterfazBase import InterfazBase
from Modelo.Empleado import Empleado

class InterfazEmpleados(InterfazBase):
    def __init__(self):
        """
        Inicializa la interfaz específica para gestionar empleados
        """
        super().__init__("JSON/Empleados.json", Empleado, "empleado")
    
    def solicitar_datos_entidad(self, cedula_actual: Optional[int] = None) -> Optional[Empleado]:
        """
        Este método será responsable de solicitar los datos de un empleado con validación.

        Args:
            cedula_actual (Optional[int]): La cédula actual del empleado (para actualizaciones)

        Returns:
            Optional[Empleado]: Una instancia de Empleado con los datos ingresados o None si hubo error
        """
        # Obtener cédula
        if cedula_actual is None:
            cedula = self.obtener_codigo()
            if cedula is None:
                return None
                
            # Verificar duplicados al agregar
            if self.gestor.buscar_por_codigo(cedula):
                print(f"[ADVERTENCIA] La cédula {cedula} ya existe. No se puede agregar un empleado duplicado.")
                return None
        else:
            # Para actualización, la cédula no se puede cambiar
            cedula = cedula_actual
        
        # Solicitar resto de datos
        if cedula_actual is None:
            # Agregando nuevo empleado
            nombre = input("Nombre completo: ")
            correo = input("Correo electrónico: ")
            sede = input("Sede: ")
            cargo = input("Cargo: ")
        else:
            # Actualizando empleado existente
            empleado_actual = self.gestor.buscar_por_codigo(cedula)
            nombre = input(f"Nombre [{empleado_actual.nombre}]: ") or empleado_actual.nombre
            correo = input(f"Correo [{empleado_actual.correo}]: ") or empleado_actual.correo
            sede = input(f"Sede [{empleado_actual.sede}]: ") or empleado_actual.sede
            cargo = input(f"Cargo [{empleado_actual.cargo}]: ") or empleado_actual.cargo
        
        # Validar que todos los campos estén completos
        if not all([nombre, correo, sede, cargo]):
            print("[ERROR] Todos los campos son obligatorios.")
            return None
    
        # Validar formato de correo básico
        if '@' not in correo or '.' not in correo:
            print("[ERROR] El correo debe tener un formato válido.")
            return None
               
        return Empleado(cedula, nombre, correo, sede, cargo)
    
    def get_campos_busqueda(self) -> dict:
        """
        Este método retorna un diccionario con los campos de búsqueda disponibles para empleados
        
        Returns:
            dict: Diccionario con formato {opcion: nombre_campo}
        """
        return {
            '1': 'cedula',
            '2': 'nombre',
            '3': 'correo',
            '4': 'sede',
            '5': 'cargo'
        }