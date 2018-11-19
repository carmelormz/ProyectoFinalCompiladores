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



## **CREACION DE FIGURA**
## **MODIFICAR UNA FIGURA**
## **EJECUTAR CODIGO**
