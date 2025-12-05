---

# Gestor de Bases de Datos No Relacional con Árboles Autobalanceados

### Árboles AVL + Persistencia en JSON (Python)

Este proyecto implementa un sistema de gestión de **Libros** y **Empleados**, utilizando Árboles AVL para almacenar los datos de manera eficiente y archivos JSON como sistema de persistencia. Incluye operaciones CRUD completas, interfaces de consola y arquitectura modular basada en POO.

---

## Estructura del Proyecto

```
Proyecto/
│
├── Arboles/
│   ├── ArbolAVL.py
│   └── NodoAVL.py
│
├── BD/
│   └── GestorBD.py
│
├── Interfaces/
│   ├── InterfazBase.py
│   ├── InterfazEmpleados.py
│   └── InterfazLibros.py
│
├── Modelo/
│   ├── Base.py
│   ├── Empleado.py
│   └── Libro.py
│
├── JSON/
│   ├── Empleados.json
│   └── Libros.json
│
├── main.py
└── README.md
```

---

##  Tecnologías y Librerías Usadas

| Librería | Uso                                   |
| -------- | ------------------------------------- |
| `json`   | Cargar y guardar datos en JSON        |
| `os`     | Manejo de rutas y limpieza de consola |
| `typing` | Tipado (`Optional`, `Type`, `List`)   |
| `abc`    | Creación de clases abstractas         |

No requiere instalaciones adicionales.

---

## Árbol AVL

Los datos de cada entidad se almacenan en un **Árbol AVL**, lo que permite:

* Inserciones, búsquedas y eliminaciones en **O(log n)**
* Balance automático mediante:

  * Rotación izquierda
  * Rotación derecha
  * Rotación doble izquierda–derecha
  * Rotación doble derecha–izquierda
* Recorrido inorden para mostrar los elementos ordenados

El AVL utiliza el “código” de cada entidad como **clave primaria**.

---

## GestorBD – Persistencia en JSON

El componente `GestorBD` realiza:

* Carga del árbol AVL desde archivo JSON
* Guardado automático del árbol después de cada operación
* CRUD completo:

  * Agregar entidad
  * Eliminar entidad
  * Actualizar datos
  * Buscar por código

Garantiza que toda la información se conserve entre ejecuciones.

---

## Interfaz de Usuario en Consola

Cada tipo de entidad cuenta con su propia interfaz:

* `InterfazLibros`
* `InterfazEmpleados`

Basadas en `InterfazBase`, ofrecen:

* Agregar
* Buscar por código o por otros campos
* Actualizar
* Eliminar
* Mostrar datos en orden ascendente (inorden del AVL)

Permiten interacción intuitiva por consola.

---

## Entidades (Modelo)

### Empleado

* cédula
* nombre
* correo
* cargo
* sede

### Libro

* código
* título
* autor
* fecha de publicación
* género

Todas las entidades heredan de `Base` y deben implementar:

* `get_codigo()`
* `to_dict()`
* `from_dict()`
* `__str__()`

---

## Ejecución del Programa

Ejecuta el menú principal con:

```bash
python main.py
```

Aparecerá:

```
==============================
  SISTEMA DE GESTIÓN BIBLIORED
==============================
1. Gestionar Libros
2. Gestionar Empleados
3. Salir
```

---

## Cómo Extenderlo

Para crear una nueva entidad:

1. Crear clase en `/Modelo`
2. Crear interfaz en `/Interfaces`
3. Crear archivo JSON correspondiente
4. Añadirla al `MenuPrincipal`

El sistema está diseñado para ser escalable y modular.

---

## Notas

* Los archivos JSON se crean automáticamente si no existen.
* El sistema valida campos (duplicados, correos, tipos de datos, etc.).
* El AVL incluye mensajes internos para depuración (rotaciones y balanceos).

---

Si quieres, puedo generarte:
✔ versión resumida del README
✔ versión con imágenes y diagramas
✔ diagrama UML del proyecto

