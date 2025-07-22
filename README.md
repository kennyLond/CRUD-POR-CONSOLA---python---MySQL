# Sistema de Gestión de Cursos en Consola (Python + MySQL)

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar cursos (listar, registrar, actualizar y eliminar) con persistencia en una base de datos MySQL. El sistema está estructurado de manera modular y aplica principios básicos de programación orientada a objetos.

---

## Funcionalidades

- Listar cursos disponibles
- Registrar nuevos cursos
- Actualizar información de un curso existente
- Eliminar cursos
- Validación de opciones ingresadas
- Gestión de errores controlados

---

##  Tecnologías Utilizadas

- **Python 3**
- **MySQL**
- **MySQL Workbench**
- **Conector MySQL para Python (`mysql-connector-python`)**

---

## Estructura del Proyecto

```
proyecto_cursos/
│
├── assets/
│    └── img/             # Imágenes de evidencia  
├── BD/
│   └── conexion.py      # Contiene la clase DAO para la conexión y operaciones en la base de datos
│
├──  funciones.py            # Funciones auxiliares (mostrar lista, pedir datos, etc.)
│
└──  principal.py          # Archivo principal con el menú y lógica de ejecución

```

---

##  Base de Datos

### Nombre de la base de datos: `universidad`

### Tabla: `cursos`

```sql
CREATE TABLE cursos (
  codigo VARCHAR(6) PRIMARY KEY,
  nombre VARCHAR(50),
  credito INT(2)
);
```

### Ejemplo de datos insertados:

```sql
INSERT INTO cursos (codigo, nombre, credito) VALUES 
('000001', 'Introducción a la informática', 2),
('000002', 'Bases de Datos', 2),
('000003', 'Programación Python', 1);
```

---

##  Evidencia 

### Menú principal
![Menú principal](https://github.com/kennyLond/CRUD-POR-CONSOLA---python---MySQL/blob/main/assets/img/001MEN%C3%9A.png?raw=true)

### Lista de Cursos
![Lista de Cursos](https://github.com/kennyLond/CRUD-POR-CONSOLA---python---MySQL/blob/main/assets/img/002_listar.png?raw=true)

### Registro de Cursos
![Registro de Cursos](https://github.com/kennyLond/CRUD-POR-CONSOLA---python---MySQL/blob/main/assets/img/003_registrar.png?raw=true)

### Lista de curso agregado
![Lista de curso agregado](https://github.com/kennyLond/CRUD-POR-CONSOLA---python---MySQL/blob/main/assets/img/004_listar_registro.png?raw=true)

### Eliminar Curso
![Eliminar Curso](https://github.com/kennyLond/CRUD-POR-CONSOLA---python---MySQL/blob/main/assets/img/005_eliminar.png?raw=true)

### Lista de Curso actualizado 
![Lista de Curso actualizado ](https://github.com/kennyLond/CRUD-POR-CONSOLA---python---MySQL/blob/main/assets/img/006_listar_eliminado.png?raw=true)


---

## Comentarios del código

Todo el código está correctamente **comentarizado** para facilitar su lectura, aprendizaje y mantenimiento. Se incluye manejo de errores y separación por responsabilidades (DAO, lógica del menú, funciones auxiliares).

---

## Requisitos para ejecutar

1. Tener instalado **Python 3**
2. Instalar el conector MySQL:
   ```
   pip install mysql-connector-python
   ```
3. Tener una base de datos MySQL en ejecución
4. Configurar los datos de conexión en `BD/conexion.py`

---

##  Ejecución

Ejecutar el programa principal desde consola:

```bash
python principal.py
```

---

## ✍️ Autor

Kenny Orlando Londoño Torrado  
[GitHub](https://github.com/kennyLond)
