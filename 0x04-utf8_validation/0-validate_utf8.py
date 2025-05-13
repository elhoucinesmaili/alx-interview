#!/usr/bin/python3
"""
Validation UTF-8
"""

def validUTF8(data):
    """
    data : liste d'entiers représentant des octets
    Retourne : True si les données représentent une
    encodage UTF-8 valide, sinon False
    """
    byte_count = 0  # Nombre d'octets restants à valider pour un caractère multioctets

    for i in data:
        if byte_count == 0:
            # Déterminer le nombre d'octets dans le caractère UTF-8 en cours
            if i >> 5 == 0b110:
                byte_count = 1  # Caractère sur 2 octets
            elif i >> 4 == 0b1110:
                byte_count = 2  # Caractère sur 3 octets
            elif i >> 3 == 0b11110:
                byte_count = 3  # Caractère sur 4 octets
            elif i >> 7 == 0b1:
                return False  # Caractère invalide (octet de départ incorrect)
        else:
            # Vérifier que l'octet suivant commence par '10'
            if i >> 6 != 0b10:
                return False
            byte_count -= 1

    return byte_count == 0  # Retourne True uniquement si tous_
