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
        "diagDD": {
            "x": 1,
            "y": 1,
        },
        "diagDU": {
            "x": -1,
            "y": 1,
        },
        "diagIU": {
            "x": -1,
            "y": -1,
        },
        "diagID": {
            "x": 1,
            "y": -1,
        }
    }
)

torre_blanca = PiezaEspecial(
    blanco,
    "torreB",
    {"x": 1, "y": 7},
    {
        "frente":
        {"x": -1, "y": 0},

        "atras":
        {"x": 1, "y": 0},

        "izquierda":
        {"x": 0, "y": -1},

        "derecha":
        {"x": 0, "y": 1},
    },
)

torre_blanca0 = PiezaEspecial(
    blanco,
    "torreB",
    {"x": 2, "y": 0},
    {
        "frente":
        {"x": -1, "y": 0},

        "atras":
        {"x": 1, "y": 0},

        "izquierda":
        {"x": 0, "y": -1},

        "derecha":
        {"x": 0, "y": 1},
    },
)

alfil_blanco0 = PiezaEspecial(
    blanco,
    "alfilB",
    {"x": 3, "y": 2},
  
        "diagDD":
        {"x": 1, "y": 1},

        "diagDU":
        {"x": -1, "y": 1},

        "diagIU":
        {"x": -1, "y": -1},

        "diagID":
        {"x": 1, "y": -1},
    }
)


alfil_blanco = PiezaEspecial(
    blanco,
    "alfilB",
    {"x": 4, "y": 5},
    {
        "diagDD":
        {"x": 1, "y": 1},

        "diagDU":
        {"x": -1, "y": 1},

        "diagIU":
        {"x": -1, "y": -1},

        "diagID":
        {"x": 1, "y": -1},
    }
)
