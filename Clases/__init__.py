try:  
    from Clases.Insercion_dicotonomica import (
        ordenar, 
        ordenar_lista_vacia
        )

    from Clases.Ordenacion_topologica import (
        ordenacion_burbuja
    )

    from Clases.Explorar import (
        segmentos,
        explorar
    )
except ImportError:
    #Como no usamos estas clases, podemos saltarnoslas mediante una exepcion para que compile
    print ("ImportError inesperado en __init__.py")
    pass