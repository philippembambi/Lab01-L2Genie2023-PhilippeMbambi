import operator

class Decipher:

    _BLOC         =   list()            # Longueur de la clé
    _PERMUTED_KEY = dict()             # clé de permutation
    _PI_PERMUTE   =   list()            # Fonction de permutation
    _PI_PERMUTED_VALUES = list()        # Valeur de permutation
    _PI = list()
    _Go        =   list()
    _Go_PERMUTATION        =   list()
    _Do        =   list()
    _G1        =   list()
    _G2        =   list()
    _G1_PERMUTATION        =   list()
    _D1        =   list()
    _D2        =   list()
    _C         =   list()

    def __init__(self, Bloc:int, PI:int) -> None:
        self._PI_PERMUTE       =    PI
        self._BLOC             =   Bloc

    def splitBloc(self) -> None:
        self._G2 = self._C[:4]
        self._D2 = self._C[4:]
        
        print("Le bloc C est maintenant divisé en 2 blocks :")
        print("G2' = ", *self._G2)
        print("D2' = ", *self._D2)
        print("\n")