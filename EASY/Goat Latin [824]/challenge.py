"""
DESCRIPTION:

You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

    If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
        For example, the word "apple" becomes "applema".
    If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
        For example, the word "goat" becomes "oatgma".
    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
        For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.

Return the final sentence representing the conversion from sentence to Goat Latin.

 

Example 1:

Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:

Input: sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

 

Constraints:

    1 <= sentence.length <= 150
    sentence consists of English letters and spaces.
    sentence has no leading or trailing spaces.
    All the words in sentence are separated by a single space.

"""

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        """
        Traduce una cadena recibida como parámetro al lenguaje
        Goat Latin.

        Para la transformación a este lenguaje, se siguen todas
        normas y requerimientos del mismo.

        params:
            sentence (str)
        
        returns:
            str
        """

        # Lista de palabras contenidas en la cadena "sentence".
        words_in_sentence = sentence.split()

        # Recorro la lista y actualizo cada palabra según las normas
        # del lenguaje Goat Latin.
        for idx, word in enumerate(words_in_sentence):
            if word.lower().startswith(("a", "e", "i", "o", "u")):
                word = word + "ma" + "a"*(idx + 1)
            else:
                first_letter_on_word = word[0]
                word_without_beginning = word[1:]
                word = word_without_beginning + first_letter_on_word + "ma" + "a"*(idx + 1)
            
            # Actualizo la palabra en iteración al lenguaje 'Goat Latin'
            words_in_sentence[idx] = word

        return " ".join(words_in_sentence)