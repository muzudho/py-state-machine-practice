from lesson14.keywords import (
    A,
    E_A,
    E_AN,
    E_IS,
    E_OVER,
    E_PEN,
    E_PIN,
    E_THAT,
    E_THIS,
    E_WAS,
    INIT,
    IS,
    PEN,
    THIS,
)

transition_conf = {
    INIT: {
        E_OVER: [INIT],
        E_THAT: [INIT],
        E_THIS: [INIT, THIS],
        THIS: {
            E_OVER: [INIT],
            E_WAS: [INIT],
            E_IS: [INIT, THIS, IS],
            IS: {
                E_OVER: [INIT],
                E_AN: [INIT],
                E_A: [INIT, THIS, IS, A],
                A: {
                    E_OVER: [INIT],
                    E_PIN: [INIT],
                    E_PEN: [PEN],
                },
            },
        },
    },
    PEN: {
        E_OVER: None,
    },
}
