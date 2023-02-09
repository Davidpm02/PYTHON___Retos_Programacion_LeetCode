#You are given two string arrays words1 and words2.

#A string b is a subset of string a if every letter in b occurs in a including multiplicity.

#For example, "wrr" is a subset of "warrior" but is not a subset of "world".
#A string a from words1 is universal if for every string b in words2, b is a subset of a.

#Return an array of all the universal strings in words1. You may return the answer in any order.

#Example:
#Input: words1 = ["amazon","apple","facebook","google","leetcode"],words2 = ["e","o"]
#Output: ["facebook","google","leetcode"]


def comprobarPalabras(lista1,lista2):
    """Funcion parametrizada que retorna una lista cuyos elementos dependen de los argumentos de los parametros.
    
       Parametros
           - lista1 : array que contiene una serie de strings.
           - lista2 : array compuesto de strings, que pueden formar o no parte de los string del parametro 'lista1'.
    
    """
    
    
    palabrasCoincidentes = []
    
    for palabra in lista1:
        for letra in lista2:
            if letra not in palabra:
                break
            elif letra in palabra:
                if letra == lista2[-1]:
                    if letra in palabra:
                        palabrasCoincidentes.append(palabra)
                    else:
                        break
                else:
                    continue
    else:                
        return palabrasCoincidentes
                
                
        


if __name__ == '__main__':
    lista1 = ["amazon","apple","facebook","google","leetcode"]
    lista2 = ["e","o"]
    print(comprobarPalabras(lista1,lista2))