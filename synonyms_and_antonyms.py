def wordmeaning(w):
    import nltk
    from nltk.corpus import wordnet
    x=wordnet.synsets(w)
    print(x[0].definition())
##    for syn in wordnet.synsets(w):
##        for l in syn.lemmas():
##            synonyms.append(l.name())
##            if l.antonyms():
##                antonyms.append(l.antonyms()[0].name())
##      
##    print('synonyms:',set(synonyms))
##    print('antonyms:',set(antonyms))
import random
from nltk.corpus import words
word_list = words.words()
# prints 236736
global i
for i in range(20):
    
    wordm=random.choice(word_list)
    
    try:
        syn(wordm)
        break
    except IndexError:
        continue
    print(wordm)
        
##from nltk.corpus import wordnet 
##syns = wordnet.synsets("bostrychid")
##print("Defination of the said word:")
##print(syns[0].definition())
##print("\nExamples of the word in use::")
##print(syns[0].examples())    
