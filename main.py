from KeyGenerator import *
from Encrypt import *

# Algorithme de la Génération des clés

print("*****************************************")
print("______________Algorithme de génération de clé______________")
print("\n")

# Iniialisation
KEY = list()
KEY = (0, 1, 1, 0, 1, 1, 0, 1)
H_PERMUTE = list()
H_PERMUTE = (6, 5, 2, 7, 4, 1, 3, 0)

# Etape 1 : Entrée (la clé de permutation)
feistelCipher = KeyGenerator(KEY, H_PERMUTE)

# Etape 2 : Appliquer la fonction de permutation
feistelCipher.applyPermutation()

# Etape 3 : Diviser en 2 blocs de 4 bits k = k1' || k2'
feistelCipher.splitKey()

# Etape 4 : K1 = k1' + k2' et K2 = K2' ET K1
feistelCipher.applyKey1Operator()
feistelCipher.applyKey2Operator()

# Etape 5 : Décalage à gauche de K1
feistelCipher.leftShift()
feistelCipher.leftRight()

# Etape 6 : Sortie
feistelCipher.outputKeys() 
print("*****************************************")
print("\n")

print("______________Algorithme de Chiffrement______________")
print("\n")

# Algorithme de Chiffrement
# Iniialisation
BLOC = list()
BLOC = (0, 1, 1, 0, 1, 1, 1, 0)
PI = list()
PI = (4, 6, 0, 2, 7, 3, 1, 5)
P = (2, 0, 1, 3)

# Etape 1 : Entrée (le bloc N de 8 bits)
encrypt = Encrypt(BLOC, PI)

# Etape 2 : Appliquer la fonction de permutation
encrypt.applyBlocPermutation()

# Etape 3 : Diviser N en deux blocs de 4 bits : N = Go || Do
encrypt.splitBloc()

# Etape 4 : #Premier Round, calculer : D1 = P(Do) XOR k1
encrypt.calculateD1(P) # Calculer la permutation de Go
encrypt.calculateFirstRound(feistelCipher.getK1()) # Calculer la valeur de D1

# Etape 5 : Deuxième Round Calculer la valeur de D2
print("\n")
print("Deuxième Round")
encrypt.calculateSecondRound(P, feistelCipher.getK2()) 

# Etape 6 Concatenation : C = G2 || D2
print("\n")
encrypt.concatenate()

# Etape 7 Inverse de PI
print("\n")
encrypt.inverse_PI_permutation(PI)
