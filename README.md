# Automatización de Pruebas con Selenium y Python - Your Store

## Descripción

Este proyecto de automatización de pruebas utiliza Selenium con Python para llevar a cabo diversas pruebas en la tienda en línea "Your Store"(https://opencart.abstracta.us/). Las pruebas incluyen el registro de nuevos usuarios, inicio de sesión, compras como usuario invitado y compras con una cuenta de usuario registrada.

## Requisitos

- Python 3
- Biblioteca Selenium
- WebDriver para el navegador (en este proyecto, se utilizó el controlador de Chrome)

## Configuración

Asegúrate de tener Python 3 instalado en tu sistema. Luego, instala la biblioteca de Selenium utilizando pip:
    
    pip install selenium
    
## Uso

Clona el repositorio:
   
```python
git clone https://github.com/paulamicaelaflorio/yourstore-automation-tests.git
```

Abre el proyecto en tu entorno de desarrollo.

Ejecuta las pruebas de acuerdo a tus necesidades. Por ejemplo:
```python
python yourstore-automation-tests.py
```
## Evidencia de Pruebas

Para mantener un registro organizado de los resultados de cada caso de prueba, en este proyecto se crea automáticamente una carpeta de evidencia para cada caso. Dentro de la carpeta del caso de prueba, se almacenan las evidencias relevantes, como capturas de pantalla, que se generan durante la ejecución del caso de prueba.



## Test Cases

1. Registro de Nuevo Usuario: 
Este caso de prueba verifica el proceso de registro de un nuevo usuario en la tienda en línea "Your Store".

2. Registro de Usuario Existente:
Este caso de prueba verifica el proceso de registro de un usuario que ya está registrado en la tienda.

3. Inicio de Sesión:
Este caso de prueba verifica el proceso de inicio de sesión en la tienda.

4. Inicio de Sesión con Usuario No Registrado:
Este caso de prueba verifica el inicio de sesión con un usuario que no está registrado en la tienda.

5. Compra como Invitado:
Este caso de prueba simula el proceso de compra de un producto como usuario invitado.

6. Compra con Usuario Registrado:
Este caso de prueba simula el proceso de compra de un producto con un usuario registrado.

## Funciones Creadas

En este proyecto, se crearon las siguientes funciones que facilitan la interacción con la página web y la ejecución de pruebas:

### `wait_and_click(driver, locator)`

Esta función espera hasta que el elemento especificado, identificado por `locator`, sea clickeable y luego lo selecciona. Es útil para garantizar que un elemento esté listo para interactuar antes de realizar una acción.

Ejemplo de uso:

```python
wait_and_click(driver, (By.CLASS_NAME, "caret"))
```

### `wait_and_send_keys(driver, locator, keys)`
La función wait_and_send_keys espera hasta que el elemento especificado, identificado por `locator`, sea visible y luego envía las teclas proporcionadas como entrada. Es útil para ingresar texto en campos de entrada y formularios.

Ejemplo de uso:

```python
wait_and_send_keys(driver, (By.ID, "input-payment-firstname"), "user_name")
```
