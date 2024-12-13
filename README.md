# ToDoApp-Python-MySQL
Este proyecto es una aplicación en Python que permita a los usuarios gestionar sus tareas diarias, almacenando los datos por medio de bases de datos

## Instalación

1. **Instalación de Dependencias**

   Asegúrate de tener un entorno virtual y de instalar todas las dependencias necesarias. Puedes crear un entorno virtual con:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

2. **Interfaz Grafica**

   Asegúrate de tener instalada la interfaz grafica que necesita este programa para su ejecución:

   ```bash
   pip install PyQt5
   ```

3. **Conexión a la base de datos**

   Para interactuar con una base de datos MySQL, necesitarás un conector:

   ```bash
   pip install mysql-connector-python
   ```

   ```bash
   pip install SQLAlchemy
   ```

   

## Exigencias del Programa

1. **Agregar Tareas:** 

   ​	Permitir al usuario agregar nuevas tareas con un titulo y una descripción.

2. **Listar Tareas:** 

   ​	Mostrar todas las tareas agregadas con su estado (pendiente o completada).

3. **Marcar Tareas como Completadas:**  

   ​	Permitir al usuario marcar una tarea como completada.

4. **Eliminar Tareas:** 

   ​	Permitir al usuario eliminar tareas completadas.

5. **Guardar y Cargar Tareas:** 

   ​	Puede exportar las tareas en un archivo e importarlas desde el mismo archivo.

6. **Interfaz:** 

   ​	Puedes crear una interfaz grafica o realizarlo por medio de línea de comandos.
