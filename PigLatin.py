def pigTranslator(pigConsonantSuffix , pigVowelSuffix , originalWord):
    if len(originalWord) > 0 and originalWord.isalpha():
        vowelChecker = originalWord[0].lower()
        if(vowelChecker == "a" or vowelChecker == "e" or vowelChecker == "i" or vowelChecker == "o" or vowelChecker == "u"):    
            translatedWord = originalWord +  pigVowelSuffix
            return translatedWord
        else:
            firstLetter = originalWord[0]
            translatedWord = originalWord + firstLetter + pigConsonantSuffix
            translatedWord= translatedWord[1:len(translatedWord)]
            return translatedWord
    return False


def main():
    pigConsonantSuffix = "ay"
    pigVowelSuffix = "way"
    translateSentence = []
    originalSentence = raw_input("Enter a sentence to translate into Pig Latin:")
    translateSentence = originalSentence.split()
    for counter in range(0 , len(translateSentence)):
        print pigTranslator(pigConsonantSuffix , pigVowelSuffix , translateSentence[counter]),     
    return True

if __name__ == "__main__":
    main()
