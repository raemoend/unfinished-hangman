import himself
import os
import random
import itertools

def clear():
    if os.name == nt:
        os.system('cls')
    else:
        os.system('clear')

wordListString = "account act addition adjustment advertisement agreement air amount amusement animal answer apparatus approval argument art attack attempt attention attraction authority back balance base behavior belief birth bit bite blood blow body brass bread breath brother building burn burst business butter canvas care cause chalk chance change cloth coal color comfort committee company comparison competition condition connection control cook copper copy cork cotton cough country cover crack credit crime crush cry current curve damage danger daughter day death debt decision degree design desire destruction detail development digestion direction discovery discussion disease disgust distance distribution division doubt drink driving dust earth edge education effect end error event example exchange existence expansion experience expert fact fall family father fear feeling fiction field fight fire flame flight flower fold food force form friend front fruit glass gold government grain grass grip group growth guide harbor harmony hate hearing heat help history hole hope hour humor ice idea impulse increase industry ink insect instrument insurance interest invention iron jelly join journey judge jump kick kiss knowledge land language laugh law lead learning leather letter level lift light limit linen liquid list look loss love machine man manager mark market mass meal measure meat meeting memory metal middle milk mind mine minute mist money month morning mother motion mountain move music name nation need news night noise note number observation offer oil operation opinion order organisation ornament owner page pain paint paper part paste payment peace person place plant play pleasure point poison polish porter position powder power price print process produce profit property prose protest pull punishment purpose push quality question rain range rate ray reaction reading reason record regret relation religion representative request respect rest reward rhythm rice river road roll room rub rule run salt sand scale science sea seat secretary selection self sense servant sex shade shake shame shock side sign silk silver sister size sky sleep slip slope smash smell smile smoke sneeze snow soap society son song sort sound soup space stage start statement steam steel step stitch stone stop story stretch structure substance sugar suggestion summer support surprise swim system talk taste tax teaching tendency test theory thing thought thunder time tin top touch trade transport trick trouble turn twist unit use value verse vessel view voice walk war wash waste water wave wax way weather week weight wind wine winter woman wood wool word work wound writing year"
wordList = str.split(wordListString)

word = random.choice(wordList)

alphabetString = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabetStringCaps = str.capitalize(alphabetString)
alphabet = str.split(alphabetString)
alphabetCaps = str.split(alphabetStringCaps)

letterAmount = 0

for letter in alphabet:
    letterCount = str.count(word, letter)
    letterAmount = letterAmount + letterCount


letterBlanksList = list(itertools.repeat("_", letterAmount))     
blankSeperator = ""
letterBlanks = blankSeperator.join(letterBlanksList)

incorrectLetterList = []
incorrectSeperator = ", "

def letterVerify(prompt):
    try:
        inp = input(prompt)
        verify = str.count(inp)
        if (verify > 1) or (verify < 1):
            print("Please enter one character.")
            
        if inp not in alphabet or alphabetCaps:
            print("Please enter a letter from the English alphabet.")

        else:
            return inp
                
    except:
        print("Please enter a letter from the English alphabet.")


        
def letterCheck(letter, word):
    lowLetter = str.lower(letter)
    if lowLetter in word:
        findLetter = str.find(lowLetter, word)
        capLetter = str.capitalize(lowLetter)
        blankRemove = letterBlanksList[findLetter]
        letterBlanksList.remove(blankRemove)
        letterInt = findLetter + 1
        letterBlanksList.append(letterInt, capLetter)
        letterBlanks = blankSeperator.join(letterBlanksList)

    else:
        capLetter = str.capitalize(lowLetter)
        incorrectLetterList.append(capLetter)


while True:

    if "_" not in letterBlanksList:
        print("Congratulations! You've figured out the word and saved the hangman's life!")
        break

    elif (len(incorrectLetterList) == 0):
        himself.Hangman.noose(letterBlanks)
        inpLetter = letterVerify("Enter a letter you think is in this word. ")
        letterCheck(inpLetter, word)
        clear()

    elif (len(incorrectLetterList) == 1):
        himself.Hangman.plusHead(letterBlanks)
        print(str.format("Incorrect Letters: {}", incorrectLetterList))
        inpLetter = letterVerify("Enter a letter you think is in this word. ")
        letterCheck(inpLetter, word)
        clear()

    elif (len(incorrectLetterList) == 2):
        himself.Hangman.plusTorso(letterBlanks)
        print(str.format("Incorrect Letters: {}", incorrectLetterList))
        inpLetter = letterVerify("Enter a letter you think is in this word. ")
        letterCheck(inpLetter, word)
        clear()

    elif (len(incorrectLetterList) == 3):
        himself.Hangman.plusLeftArm(letterBlanks)
        print(str.format("Incorrect Letters: {}", incorrectLetterList))
        inpLetter = letterVerify("Enter a letter you think is in this word. ")
        letterCheck(inpLetter, word)
        clear()

    elif (len(incorrectLetterList) == 4):
        himself.Hangman.plusRightArm(letterBlanks)
        print(str.format("Incorrect Letters: {}", incorrectLetterList))
        inpLetter = letterVerify("Enter a letter you think is in this word. ")
        letterCheck(inpLetter, word)
        clear()

    elif (len(incorrectLetterList) == 5):
        himself.Hangman.plusLeftLeg(letterBlanks)
        print(str.format("Incorrect Letters: {}", incorrectLetterList))
        inpLetter = letterVerify("Enter a letter you think is in this word. ")
        letterCheck(inpLetter, word)
        clear()

    elif (len(incorrectLetterList) == 6):
        himself.Hangman.plusRightLeg(letterBlanks)
        print(str.format("Incorrect Letters: {}", incorrectLetterList))
        print(str.format("Game over! The word was {}. Rest in peace hangman :(", word))
