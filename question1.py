# QUESTION 1
def afficher_combinaisons_binaires(n: int, str: str = ""):
  # Cas de base : si n est égal à zéro, on n'a plus rien à faire
  if n == 0:
    print(str)
    return
  
  # Sinon, on affiche la combinaison binaire courante et on appelle récursivement la fonction
  # en diminuant n de 1
  str0 = str + "0"
  afficher_combinaisons_binaires(n - 1, str0)
  str1 = str + "1"
  afficher_combinaisons_binaires(n - 1, str1)

afficher_combinaisons_binaires(512)
