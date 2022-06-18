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

"""
Piezas Negras
---------------------------------------------------------------------
"""

reyNegro = PiezaBase(
    negro,
    "reyN",
    {"x": 0, "y": 4},
    {
        "frente": {
            "x": 1,
            "y": 0
        },
        "atras": {
            "x": -1,
            "y": 0
        },
        "derecha": {
            "x": 0,
            "y": -1
        },
        "izquierda": {
            "x": 0,
            "y": 1
        },
        "diagDD": {
            "x": -1,
            "y": 1,
        },
        "diagDU": {
            "x": 1,
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

torre_negra_derecha = PiezaEspecial(
    negro,
    "torreN",
    {"x": 0, "y": 7},
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

torre_negra_izquierda = PiezaEspecial(
    negro,
    "torreN",
    {"x": 0, "y": 0},
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

alfil_negro_izquierda = PiezaEspecial(
    negro,
    "alfilN",
    {"x": 0, "y": 2},
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

alfil_negro_derecha = PiezaEspecial(
    negro,
    "alfilN",
    {"x": 0, "y": 5},
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

caballo_negro_izquierda = PiezaBase(
    negro,
    "caballoN",
    {"x": 0, "y": 1},
    {


    }
)

caballo_negro_derecha = PiezaBase(
    negro,
    "caballoN",
    {"x": 0, "y": 6},
    {


    }
)

reina_negro = PiezaEspecial(
    negro,
    "reinaN",
    {"x": 0, "y": 3},
    {


    }
)