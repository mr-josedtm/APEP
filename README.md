# Filosofía:

* Un executor tiene un puton de entrada paretizable que define el input inicial y los flows a ejecutar
* Cada flow se ejecuta de forma independiente y paralelizable pero únicamente si ha acabado el anterior. Esto quiere decir que si un step tiene como salida un conjunto de resultados, el siguiente step podrá ser paralelizable
* El callback de un flow no puede dar lugar a una bifurcación, simplemente finalizará o revertirá aquellos cambios que procedan
* Idealmente, las operaciones pipeline serán idempotentes para garantizar la asincronía (si en un futuro se orquesta con una cola)
* Se asume que el conjunto de campos del output en el step X-1 es igual o mayor al número de campos necesar en el input del step X. Además se asume que se llaman igual
    * Que los Inputs tengan alguna forma de informar de los valores que esperan
    * Que si se quieren mapear objetos con nombres distintos se pueda con un mapper
* La salida de un step siempre será un metadata y una **lista de resultados** si el número de resultados es mayor que uno, el orquestador paralelizará las ejecuciones del siguiente step siempre que sea posible
    * Idealmente el hecho de que se paralelice o se haga secuencial sería parametrizable
* Si se produce un irrecuperable debe pararse la ejecución del step y finalizar devolviendo un objeto ApepOutput con información del error en el campo `error_result`


* El builder crea el flow previa validación de todo lo que flow necesita
* Cada flow se hace responsable de validar y mappear el input a su objeto interno, así como de validar que existen parámetros y variables de entorno




Apep es el ejecutor
Una pipeline es una ApepPipeline
Un flow es un dag
Todas las interfaces pueden tener un método get_dict o get_object que permita inferir el mapper



### NOTAS

Se opta por una estrategia de interfaces aunque se ha valorado la opción de objetos contenedores tipo:

```python
@dataclass
class ApepSucess:
    """ Class to store success result of an ApepFlow execution """
    result: object
```


