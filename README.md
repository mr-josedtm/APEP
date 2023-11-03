
![APEP](doc/apep-logo.png)

# Filosofía:

> 📝 **_TODO_**:
> * Todos los resultados del step N-1 deben procesarse y finalizar en el step N antes de lanzar ninguna ejecución del step N+1. Solo se lanzarán aquellos que finalicen OK.
> * ¿Ejecuciones priorizadas? La salida de un step va parametrizada para priorizarlas y hasta que no estén terminadas todas las de orden X-1 no se lanzan las de orden X
>   * Cualquier operación de orden X se podrá realizar en paralelo con una operación del mismo orden
> * Al finalizar todas la ejecuciones de un step paralelizado, se reagrupan y se ordenan

* La función del orquestador es:
    1. Leer los datos de arranque
    2. Lanzar el primer flujo, que puede producir 0 o N resultados.
    3. Lanzar iterativamente el siguiente flujo, paralelizando aquellos flujos cuya salida anterior haya tenido más de un resultado

* Cada flow se ejecuta de forma independiente y paralelizable pero únicamente si ha acabado el anterior. Esto quiere decir que si un step tiene como salida un conjunto de resultados, el siguiente step podrá ser paralelizable
* Cada flow se hace responsable de validar y mappear el input a su objeto interno, así como de validar que existen parámetros y variables de entorno
* El callback de un flow no puede dar lugar a una bifurcación, simplemente finalizará o revertirá aquellos cambios que procedan
* Idealmente, las operaciones pipeline serán idempotentes para garantizar la asincronía (si en un futuro se orquesta con una cola)
* Se asume que el conjunto de campos del output en el step X-1 es igual o mayor al número de campos necesar en el input del step X. Además se asume que se llaman igual o se proporciona un mapper para adaptar la entrada
* La salida de un step siempre será un metadata y una **lista de resultados** si el número de resultados es mayor que uno, el orquestador paralelizará las ejecuciones del siguiente step siempre que sea posible
    * Idealmente el hecho de que se paralelice o se haga secuencial sería parametrizable
* Si se produce un error irrecuperable debe pararse la ejecución del step y finalizar devolviendo un objeto ApepOutput con información del error en el campo `error_result`


# Clases

## ApepParams:
Almacena aquellos valores que van a ser recibidos por **todos** los flujos orquestados. Aunque todos los flujos reciben un `ApepParams` ninguno lo devuelve, es el orquestador el que mantiene el objeto y lo inyecta en cada flujo que arranca. Este objeto no debe mutar a lo largo de la ejecución.

## ApepUtils:
Conjuto de utilidades para minimizar el acoplamiento entre flujos:
* `input_to_dto` : recibe el contrato objetivo, un `ApepInput` y una **instancia** del DTO necesario y devuelve dicho DTO inicializado

## ApepInput:
Encapsula la entrada de un flujo
* `__init__` : acepta un objeto sin ningún tipo de restricción y opcionalmente un mapeador
* `__post_init__` : si se ha indicado un mapper, se mapea el objeto recibido, si no, el objeto recibido se usa como data
* `get_data_fields` : devuelve una lista de las claves **de primer nivel** que contiene el diccionario
* `get_field` : recive una `key` y devuelve el valor asociado

## ApepFieldDef:
Define los posibles grados de necesidad de cada campo del contrato de un flujo:
```py
from enum import Enum

class ApepFieldDef(Enum):
    """ Enum to indicate the ApepInput data definition
        REQUIRED: the field must be present and not null
        NULLABLE: the field must be present and could be null
        OPTIONAL: the field could be present and could be null
    """
    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"
    NULLABLE = "NULLABLE"
```

## ApepFieldType:
Define los tipos de datos válidos para las claves del contrato de un flujo:

```py
from enum import Enum

class ApepFieldType(Enum):
    """ Enum to indicate the ApepField type """
    STRING = str
    INTEGER = int
    FLOAT = float
    # ...
```
## ApepStatus
Define el estado en que se encuentra la ejecución del flujo:
* `OK`: el flujo ha finalizado de forma correcta
* `KO`: el flujo ha finalizado de forma incorrecta
* `RUNNING`: el flujo se está ejecutando
* `CALLBACK_EXC`: el flujo ha finalizado con una ejecución del su función callback

> Nota: Dado que el callback no puede producir una salida útil ni servir para realizar una bifurcación. La ejecución del callback siempre finalizará con estado `CALLBACK_EXC`

## ApepMetadata
Almacena los metadatos de la ejecución de un flujo. Su uso principal es monitorizar la ejecución de dicho flujo. Entre otros campos contiene el `status: ApepStatus`

## ApepOutput
Encapsula el resultado de una ejecución. Entre otros campos, contiene:
* `result: List[object]`: lista de resultados generados, todos ellos deben ser del mismo tipo. El resultado puede contener 0 a N objetos
* `metadata: ApepMetadata`: metadatos asociados a la ejecución del flujo 

# Interfaces

## ApepFlow [Iface]:
Definie el flujo a ejecutar.
* Recibe los `ApepParams` necesarios para ejecutar el flujo y el `ApepInput`
* `execute` : ejecuta el flujo. Al empezar definiremos en el metadato `ApepStatus.RUNNING` y los valores válidos al finalizar son `ApepStatus.OK` o `ApepStatus.KO`
* `callback` : ejecuta una acción de cierre, normalmente en caso de que el flujo haya terminado con estado `KO`. El **único estado válido** con el que puede finalizar un callback es `ApepStatus.CALLBACK_EXC` en caso de querer ampliar información sobre la finalización de la ejecución utilizar el resto de campos del metadato.

## ApepBuilder [Iface]:
Define el builder que construirá el flujo a ejecutar.

* Recibe un `ApepParams` y un `ApepInput` para construir el flujo
* `get_input_contract` : devuelve el contrato que deben cumplir los datos encapsulados en el `ApepInput`. Se trata de un diccionario donde la clave es la clave requerida y el valor asociado es una tupla que especifica si el campo es requerido y el tipo. Ej:
* `check_required_envs` : valida si existen todas las variables de entorno necesarias para la ejecución del flujo
* `build_flow` : devuelve el flujo construido. Todos tendrán un formato muy parecido ya que aprovechando la utilidad `input_to_dto`, la inicialización es muy sencilla. Se mantiene este método para facilitar acciones previas a la contrucción del flujo pero que queden implementadas dentro del mismo.

**EJEMPLO:**
```py
class SumBuilder(ApepFlowBuilder):

    def get_input_contract() -> Dict:
        return {"sumando_uno": (fd.REQUIRED, ft.INTEGER), "sumando_dos":  (fd.REQUIRED, ft.INTEGER)}

    @classmethod
    def build_flow(cls, apep_input: ApepInput, params: ApepParams) -> ApepFlow:
        sum_dto = input_to_dto(cls.get_input_contract(), apep_input, SumDto())
        return SumFlow(params, sum_dto)
```



