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

rey_blanco = PiezaEspecial(

    blanco,
    "reyB",
    {"x": 7, "y": 4},
    {
        "frente": {"x": -1, "y": 0},

        "atras": {"x": 1, "y": 0},

        "derecha": {"x": 0, "y": 1},

        "izquierda": {"x": 0, "y": -1},

        "diagDD": {"x": 1, "y": 1},

        "diagDU": {"x": -1, "y": 1},

        "diagIU": {"x": -1, "y": -1},

        "diagID": {"x": 1, "y": -1}
    }
)

torre_blanca_derecha = PiezaEspecial(
    blanco,
    "torreB",
    {"x": 7, "y": 7},
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

torre_blanca_izquierda = PiezaEspecial(
    blanco,
    "torreBI",
    {"x": 7, "y": 0},
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

alfil_blanco_izquierdo = PiezaEspecial(
    blanco,
    "alfilIB",
    {"x": 7, "y": 2},
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


alfil_blanco_derecho = PiezaEspecial(
    blanco,
    "alfilB",
    {"x": 7, "y": 5},
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

caballo_blanco_izquierdo = PiezaBase(

    blanco,
    "caballoB",

    {"x": 7, "y": 1},

    {
        # pendiente de movimientos
    }

)

caballo_blanco_derecho = PiezaBase(

    blanco,
    "caballoB",

    {"x": 7, "y": 6},

    {
        # pendiente de movimientos
    }

)

# Realizando clase para movimientos
peon_uno_B = PiezaEspecial(

    blanco,
    "peonUB",
    {"x": 6, "y": 0},

    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_dos_B = PiezaEspecial(

    blanco,
    "peonDB",
    {"x": 6, "y": 1},

    {
        "frente":
        {"x": -1, "y": 0},
    }

)

peon_tres_B = PiezaEspecial(
    blanco,
    "peonTB",
    {"x": 6, "y": 2},

    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_cuatro_B = PiezaEspecial(

    blanco,
    "peonCB",

    {"x": 6, "y": 3},
    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_cinco_B = PiezaEspecial(
    blanco,
    "peonCiB",
    {"x": 6, "y": 4},

    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_seis_B = PiezaEspecial(

    blanco,
    "peonSB",
    {"x": 6, "y": 5},

    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_siete_B = PiezaEspecial(
    blanco,
    "peonSiB",

    {"x": 6, "y": 6},

    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_ocho_B = PiezaEspecial(

    blanco,
    "peonOB",
    {"x": 6, "y": 7},

    {
        "frente":
        {"x": -1, "y": 0},
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

torre_negro_izquierda = PiezaEspecial(
    negro,
    "torreN",
    {"x": 0, "y": 0},
    {
        "frente":
        {"x": 0, "y": -1},

        "atras":
        {"x": -1, "y": 0},

        "izquierda":
        {"x": 0, "y": -1},

        "derecha":
        {"x": 0, "y": 1},
    }
)

peon_uno_N = PiezaEspecial(

    negro,
    "peonUN",

    {"x": 1, "y": 0},
    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_dos_N = PiezaEspecial(

    negro,
    "peonDN",

    {"x": 1, "y": 1},
    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_tres_N = PiezaEspecial(

    negro,
    "peonTN",

    {"x": 1, "y": 2},
    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_cuatro_N = PiezaEspecial(

    negro,
    "peonCN",

    {"x": 1, "y": 3},
    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_cinco_N = PiezaEspecial(

    negro,
    "peonCiN",

    {"x": 1, "y": 4},
    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_seis_N = PiezaEspecial(

    negro,
    "peonSN",

    {"x": 1, "y": 5},
    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_siete_N = PiezaEspecial(

    negro,
    "peonSiN",

    {"x": 1, "y": 6},
    {
        "frente":
        {"x": -1, "y": 0},
    }
)

peon_ocho_N = PiezaEspecial(

    negro,
    "peonON",

    {"x": 1, "y": 7},
    {
        "frente":
        {"x": -1, "y": 0},
    }
)
