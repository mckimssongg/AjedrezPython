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
    { "x": 7, "y": 4 },
    {
        "frente": { "x": -1, "y": 0},

        "atras": { "x": 1, "y": 0 },

        "derecha": { "x": 0, "y": 1},

        "izquierda": { "x": 0, "y": -1 },

        "diagDD": { "x": 1, "y": 1},

        "diagDU": { "x": -1, "y": 1},

        "diagIU": { "x": -1, "y": -1},

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
    "torreB",
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
    "alfilB",
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
        #pendiente de movimientos
    }

)

caballo_blanco_derecho = PiezaBase( 

    blanco,
    "caballoB",

    {"x": 7, "y": 6},

    {
        #pendiente de movimientos
    }

)

#Realizando clase para movimientos
peon_uno_B = PiezaBase(

    blanco,
    "peonB",
    {"x": 6, "y": 0},

    {
        #pendiente de movimientos
    }
)

peon_dos_B = PiezaBase(

    blanco,
    "peonB",
    {"x": 6, "y": 1},

    {
        #pendiente de movimientos
    }

)

peon_tres_B = PiezaBase(
    blanco,
    "peonB",
    {"x": 6, "y": 2},

{
    #pendiente de movimientos
}
)

peon_cuatro_B = PiezaBase(

    blanco,
    "peonB",

    {"x": 6, "y": 3},
    {
        #pendiente de movimientos
    }
)

peon_cinco_B = PiezaBase(
    blanco,
    "peonB",
    {"x": 6, "y": 4},

    {
        #pendiente de movimientos
    }
)

peon_seis_B = PiezaBase(

    blanco,
    "peonB",
    {"x": 6, "y": 5},

    {
        #pendiente de movimientos
    }
)

peon_siete_B = PiezaBase(
    blanco,
    "peonB",
    {"x": 6, "y": 6},

    {
        #pendiente de movimientos
    }
)

peon_ocho_B = PiezaBase(

    blanco,
    "peonB",
    {"x": 6, "y": 7},

    {
        #pendiente de movimientos
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