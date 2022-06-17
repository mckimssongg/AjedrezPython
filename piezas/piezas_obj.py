from piezas.modelos_piezas import Jugador, PiezaBase, PiezaEspecial

blanco = Jugador('blanco')
negro = Jugador('negro')

reina_blanca = PiezaEspecial(
    blanco,
    "reinaB",
    {
        "x": 7,
        "y": 3
    },
    {
        "frente": {
            "x": -1,
            "y": 0
        },
        "atras": {
            "x": 1,
            "y": 0
        },
        "derecha": {
            "x": 0,
            "y": 1
        },
        "izquierda": {
            "x": 0,
            "y": -1
        },
        "esq_1": {
            "x": 1,
            "y": 1,
        },
        "esq_2": {
            "x": -1,
            "y": 1,
        },
        "esq_3": {
            "x": -1,
            "y": -1,
        },
        "esq_4": {
            "x": 1,
            "y": -1,
        }
    }
)
