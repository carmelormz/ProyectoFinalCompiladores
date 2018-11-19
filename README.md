# FYG

## **DESCRIPCION**

FYG es un lenguaje de programación con salida gráfica, el cual se caracteriza por su facil creación y modificación de figuras. Su fácil sintaxis permite al usuario entender y comprender de manera rápida y fácil lo que se esta ejecutando en su código. FYG es un lenguaje de programación orientado a usuarios con ningúna o poca experencia en la programación, que busquen una herramienta adicional para aprender más sobre la lógica en instrucciones de programación. Con FYG, el usuario puede crear figuras como círculos, cuadrados, triangulos, y cualquier figura de n-lados. Así mismo, el usuario puede modificar su color y tamaño a su gusto, teniendo en sus manos un lenguaje muy flexible al usuario en lo que se quiere crear.

## **REQUERIMIENTOS**
- **Python 3.7**: https://www.python.org/
- **PLY**: https://www.dabeaz.com/ply/
- **NumPy**: http://www.numpy.org/

## **DECLARACION VARIABLES**

En el lenguaje FYG existen dos tipos de variables: *int* y *float*.
  - Las variables de tipo *int* son números enteros. Por ejemplo: 0, 1, 10, 500, 1000, etc.
  - Las variables de tipo *float* son números flotantes. Por ejemplo: 0.0, 1.5, 120.54, etc.
 
Para declarar una variable de alguno de estos dos tipos se sigue la siguiente sintaxis: TIPO(int | float) NOMBRE_VARIABLE;

**Ejemplo**:
```python
int variableEntera;
float variableFlotante;
```
Si se requieren declarar variables del mismo tipo, pueden ser declaradas seguidas, separando los nombres de cada una por medio de una coma, solamente definiendo su tipo una vez: TIPO(int | float) NOMBRE_VARIABLE_1, NOMBRE_VARIABLE_2, ... , NOMBRE_VARIABLE_N;

**Ejemplo:**
```python
int variableEntera1, variableEntera2, variableEntera3;
float variableFlotante1, variableFlotante2, variableFlotante3;
```

## **DECLARACION FUNCIONES**

En el lenguaje FYG se pueden crear funciones que el usuario requiera para su programa. Las funciones creadas por el usuario pueden tener tres tipos de valor de retorno: *void*, *int*, *float*. Así mismo, la función puede tener o no parametros para su funcionamiento, en caso de no tener parámetros, la declaración de parámetros se deja vacía. Las funciones siempre deben de terminar con el estatuto return, aunque no tenga valores de retorno.

La sintaxis para crear una función en FYF es la siguiente: TIPO (void | int | float) NOMBRE_FUNCION (TIPO(int | float) PARAMETRO_1, ... TIPO(int | float) PARAMETRO_N) { return; }

**Ejemplos:**
```python
# Declaracion de Funcion con Parametros
int funcion1(int parametro) {
  int variable;
  variable = parametro + 1;
  return parametro;
}
```

```python
# Declaracion de Funcion sin Parametros
int funcion2() {
  int variable;
  variable = 1;
  return variable;
}
```
```python
# Declaracion de Funcion sin Retorno
void funcion2() {
  int variable;
  variable = 1;
  print(variable);
  return;
}
```
## **LLAMADA A FUNCIONES**

## **USO DE CILCOS**

En el lenguaje FYG existe el estatuto de cilo *repeat*, el cual realiza un bloque de código un numero finito de veces hasta que se cumpla la condicion establecida en el parámetro de la función.

La sintaxis del estatuto *repeat* es la siguiente: REPEAT ( CONDICION) {}

**Ejemplo:**

```python
# Ejemplo REPEAT - Ciclo que corre 10 veces.
int x;
x = 10;
repeat(x > 0) {
  x = x - 1;
}
```

## **MOVIMIENTO FIGURA PRINCIPAL**

La salida gráfica de FYG se concentra en una figura principal, que es la encargada de dibujar cada figura o realizar cada instrucción gráfica que el código el dicte. Esta figura se pude mover hacia diferentes direcciones, habilitar/inhabilitar el pincel de dibujo, entre otras. Las funciones habilitadas para la figura principal son las siguientes:

- **Forward**: Movimiento de la figura principal hacia enfrente, siguiendo la orientación que tenga. Recibe como parámetro la distancia a mover hacia adelante.

**Ejemplo**:

```python
# Movimiento de la figura principal, 10 hacia adelante
forward(10);
```

- **Backward**: Movimiento de la figura principal hacia atras, siguiendo la orientación que tenga. Recibe como parámetro la distancia a mover hacia atras.

**Ejemplo**:

```python
# Movimiento de la figura principal, 10 hacia atras
backwards(10);
```
- **Left**: Movimiento de la figura completa hacia la izquierda basada en la actual orientación, no afecta orientación. Recibe como parámetro la distancia a moverse a la izquierda.

```python
# Movimiento de la figura principal hacia la izquierda, 10 en distancia.
left(10);
```


- **Right**: Movimiento de la figura completa hacia la derecha basada en la actual orientación, no afecta orientación. Recibe como parámetro la distancia a moverse a la derecha.

```python
#Movimiento de la figura principal hacia la derecha, 10 en distancia
right(10);
```

- **Turn**: Cambio de orientación de la figura hacia la derecha, según un ángulo dado por el usuario como parámetro. 

```python
# Rotar la figura principal 90 angulos a la derecha.
turn(90);
```

- **Up**: Levanta el pincel de dibujo, la figura principal deja de dibujar. No recibe ningún parámetro.

```python
# Cancelar que la figura dibuje.
up();
```

- **Down**: Baja el pincel de dibujo, la figura principal puede dibujar. No recibe ningún parámetro.

```python
# Habilitar que la figura dibuje.
down();
```


## **CREACION DE FIGURA GEOMETRICA**
El lenguaje FYG tiene la funcionalidad de crear diferentes figuras geométricas. Las figuras disponibles son: 
  - Circulo
  - Triangulo
  - Cuadrado
  - N-gon
  - Arco

Para crear alguna de estas figuras se tiene que utilizar las funciones predeterminadas del lenguaje para cada una de las figuras. Las funciones para cada figura son:
  - **Circulo**: Se se utiliza la función ***circle()***, la cual recibe como parametro el tamaño de radio.
  
  **Ejemplo:**
  
  ```python
  # Circulo con 10 de radio.
  circle(10);
  ```
    
  - **Triangulo**: Para dibujar un triangulo en FYG se utiliza la función ***triangle()***, que recibe como parámetro el tamaño del triangulo deseado.
  
  **Ejemplo:**
  
  ```python
  # Triangulo de tamaño 5
  triangle(5);
  ```
    
  - **Cuadrado**: Para dibujar un cuadrado en FYG se utiliza la función ***square()***, la cual recibe como parametro tamaño de los lados del cuadrado.
  
  **Ejemplo:**
  
  ```python
  #Cuadrado con tamaño 10 de cada lado.
  square(10);
  ```
  - **N-gon:** N-gon es una figura de n-lados determinados por el usuario. Esta función puede crear figuras de cualquier número de lados. Para hacer uso de esta función, se necesita utilizar la función ***ngon()*** de FYG, la cual recibe de parámetros dos parametros: el primero es el número de lados de la figura, el segundo el tamaño de la figura.
  
  **Ejemplo:**
  
  ```python
  # N-gon de 6 lados, con un tamaño de 10
  ngon(6,10);
  ```
  
  - **Arco**: Para dibujar un arco se utiliza la función ***arc()***, la cual recibe como parámetro el tamaño del arco.
  
   **Ejemplo:**
   
   ```python
   # Arco de tamaño 15
   arc(15);
   ```
   
## **MODIFICAR UNA FIGURA GEOMETRICA**
## **EJECUTAR CODIGO**
