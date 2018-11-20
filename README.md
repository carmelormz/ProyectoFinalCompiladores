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
void funcion3() {
  int variable;
  variable = 1;
  print(variable);
  return;
}
```
## **LLAMADA A FUNCIONES**
Para llamar a una función en FYG solamente hay que escribir el nombre de la función y asignarle los parámetros necesarios para la ejecución de la función. 

**Ejemplo**:

```python
#Llamada a funcion con parametros

main() { 
  int i;
  i = 2;
  
  #Se llama a funcion1(), se manda como parametro la variable i
  funcion1(i);  
  
  return;
}
```

Cuando la función tiene un valor de retorno, su llamada se puede igualar a una variable, para que esta almacene el valor de retorno.

**Ejemplo**:

```python
#Llamada a funcion con parametros

main() { 
  int i;
  
  #Se llama a funcion2(), no recibe parametros
  i = funcion2();
  
  return;
}
```

## **USO DE CICLOS**

En el lenguaje FYG existe el estatuto de ciclo *repeat*, el cual realiza un bloque de código un numero finito de veces hasta que se cumpla la condicion establecida en el parámetro de la función.

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

La salida gráfica de FYG se concentra en una figura principal, que es la encargada de dibujar cada figura o realizar cada instrucción gráfica que el código el dicte. Esta figura se puede mover hacia diferentes direcciones, habilitar/inhabilitar el pincel de dibujo, entre otras. Las funciones habilitadas para la figura principal son las siguientes:

- **Forward**: Movimiento de la figura principal hacia enfrente, siguiendo la orientación que tenga. Se utiliza la función ***forward(dist)***. Recibe como parámetro la distancia a mover hacia adelante. 

**Ejemplo**:

```python
# Movimiento de la figura principal, 10 hacia adelante
forward(10);
```

- **Backward**: Movimiento de la figura principal hacia atras, siguiendo la orientación que tenga. Se utiliza la función ***backward(dist)***. Recibe como parámetro la distancia a mover hacia atras.

**Ejemplo**:

```python
# Movimiento de la figura principal, 10 hacia atras
backwards(10);
```
- **Left**: Movimiento de la figura completa hacia la izquierda basada en la actual orientación, no afecta orientación. Se utiliza la función ***left(dist)***. Recibe como parámetro la distancia a moverse a la izquierda.

**Ejemplo**:

```python
# Movimiento de la figura principal hacia la izquierda, 10 en distancia.
left(10);
```


- **Right**: Movimiento de la figura completa hacia la derecha basada en la actual orientación, no afecta orientación. Se utiliza la función ***right(dist)***. Recibe como parámetro la distancia a moverse a la derecha.

**Ejemplo**:

```python
#Movimiento de la figura principal hacia la derecha, 10 en distancia
right(10);
```

- **Turn**: Cambio de orientación de la figura hacia la derecha, según un ángulo dado por el usuario como parámetro. Se utiliza la función ***turn(angle)***.

**Ejemplo**:

```python
# Rotar la figura principal 90 angulos a la derecha.
turn(90);
```

- **Up**: Levanta el pincel de dibujo, la figura principal deja de dibujar. No recibe ningún parámetro. Se utiliza la función ***up()***.

**Ejemplo**:

```python
# Cancelar que la figura dibuje.
up();
```

- **Down**: Baja el pincel de dibujo, la figura principal puede dibujar. No recibe ningún parámetro. Se utiliza la función ***down()***.

**Ejemplo**:

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
  - **Circulo**: Se se utiliza la función ***circle(size)***, la cual recibe como parametro el tamaño de radio.
  
  **Ejemplo:**
  
  ```python
  # Circulo con 10 de radio.
  circle(10);
  ```
    
  - **Triangulo**: Para dibujar un triangulo en FYG se utiliza la función ***triangle(size)***, que recibe como parámetro el tamaño del triangulo deseado.
  
  **Ejemplo:**
  
  ```python
  # Triangulo de tamaño 5
  triangle(5);
  ```
    
  - **Cuadrado**: Para dibujar un cuadrado en FYG se utiliza la función ***square(size)***, la cual recibe como parametro tamaño de los lados del cuadrado.
  
  **Ejemplo:**
  
  ```python
  #Cuadrado con tamaño 10 de cada lado.
  square(10);
  ```
  - **N-gon:** N-gon es una figura de n-lados determinados por el usuario. Esta función puede crear figuras de cualquier número de lados. Para hacer uso de esta función, se necesita utilizar la función ***ngon(#_sides, size)*** de FYG, la cual recibe de parámetros dos parametros: el primero es el número de lados de la figura, el segundo el tamaño de la figura.
  
  **Ejemplo:**
  
  ```python
  # N-gon de 6 lados, con un tamaño de 10
  ngon(6,10);
  ```
  
  - **Arco**: Para dibujar un arco se utiliza la función ***arc(size)***, la cual recibe como parámetro el tamaño del arco.
  
   **Ejemplo:**
   
   ```python
   # Arco de tamaño 15
   arc(15);
   ```
   
## **MODIFICAR UNA FIGURA GEOMETRICA Y PINCEL DE DIBUJO**

Al momento de crear una figura geométrica, predeterminadamente se crean vacías. Dado esto, FYG incluye varias funciones predeterminadas para modificar las figuras geométricas al momento de estarse creando (Una vez creadas ya no se pueden modificar). Las funciones disponibles para la modificación de las figuras son:

- **Size**: El ancho del pincel de dibujo se modifica. Se utiliza la función ***size(size)***. Recibe como parametro el tamaño del pincel.

**Ejemplo**:

```python
# Modifica el tamaño de dibujo del pincel
size(10);
```

- **Color**: Modifica el color de dibujo del pincel y de rellenado al utilizar ***fill()***. Se utiliza la función ***color(r,g,b)***. Recibe como parametros el color deseado en RGB.

**Ejemplo**:

```python
# Cambio de color a AZUL(34,113,179)
color(34,113,179);
```

- **Fill**: Rellena la figura del color que este determinado para el dibujo. Se utiliza la función ***fill()***. No recibe parámetros.

**Ejemplo**:

```python
#Rellenar circulo de color rojo
color(255,35,1);
circle(50).fill();
```

- **Rotate**: Rota la figura creada una cierta cantidad de ángulo. Se utiliza la función ***rotate(angle)***. Recibe como parámetro la cantidad de angulos que se quiere rotar la figura hacia la derecha.

**Ejemplo**:

```python
# Rotar triangulo 35 grados.
triangle(10).rotate(35);
```

- **Stretch**: Estira la figura una cierta cantidad determinada por el usuario. Se utiliza la función ***stretch(dist)***. Recibe como parámetro la distancia que se quiere estirar.

**Ejemplo**:

```python
# Estirar un circulo, una dist de 10.
circle(50). stretch(10);
```

## MODIFICAR/CAMBIAR FONDO DE LA SALIDA GRAFICA

El lenguaje de FYG permite al usuario cambiar las características del fondo de la salida gráfica. El usuario puede cambiar la altura, ancho y color del fondo, ó poner una imagen deseada de fondo. Para realizar estas acciones, se necesita ingresa el siguiente código al programa FYG:

- **Modificar características ventana de salida gráfica**: Cambiar la altura, anchura y color del fondo de la ventana.

**Ejemplo**:

```python
canvas {
  widht: 500;
  height: 500;
  background 0,0,0
}
```

El código anterior define la ventana emergente con un tamaño de 500x500 y un color de fondo Negro. Este bloque de código se debe poner la principio del programa, antes del main().

- **Definir Imagen de Fondo**: Se define una imagen personalizada de fondo para la ventana emergente.

**Ejemplo**:
```python
import "image.jpg";
```

El código anterior define la imagen "image.jpg" como el fondo de la ventana emergente.

**NOTA**: No se pueden utilizar ambas funcionalidades al mismo tiempo en el programa: O se cambia las características de la ventana emergente ó se define una imagen personalizada como fondo.

## **EJECUTAR CODIGO**

Para ejecutar el programa FYG, realice los siguientes pasos:
1. Bajar el proyecto de FYG
2. Dentro de la carpeta del proyecto, crear un nuevo archivo .txt y escribir el código en el lenguaje de FYG, deseado a ejecutar por el compilador.
3. En la terminal de la computadora, posicionarse en el directorio del proyecto, donde se encuentran los archivos de Python (.py) y su archivo de texto en el lenguaje de FYG creado. 
4. Ejecutar ```python MaquinaVirtual.py NOMBRE_ARCHIVO.txt``` donde el NOMBRE_ARCHIVO.txt es el nombre de su archivo con el código en FYG.
