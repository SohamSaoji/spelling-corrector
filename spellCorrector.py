# Spelling Correction program in python using textblob

#pip install textblob
from textblob import TextBlob 

s = TextBlob("Helllo verryy goood codee")

correct_spell = str(s.correct())

print(correct_spell)