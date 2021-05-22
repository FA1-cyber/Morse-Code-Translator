import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import itertools
from itertools import groupby
from scipy.io import wavfile

def morse_to_text(message): 
    full_text = '' 
    one_letter = '' 
    for letter in message: 
        if (letter != ' '): 
            i = 0  
            one_letter += letter 
        else: 
            i += 1
            if i == 2 : #DOUBLE SPACE MEANS SPACE BETWEEN WORDS
                full_text += ' '
            else:  #SINGLE SPACE MEANS SPACE BETWEEN LETTERS
                full_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(one_letter)] 
                one_letter = '' 
    return full_text 
  
  MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
  
filepath = 'dd.wav'
data, sr = librosa.load(filepath)
plt.figure()
librosa.display.waveplot(data, sr=sr)
plt.title('MORSE FILE')

non_zero_list = [list(g) for k, g in groupby(data, lambda x: x != 0) if k]
morse = []
for i in range(len(non_zero_list)):
    morse.append(len(non_zero_list[i]))
threshold = np.mean(morse)



#IF THE VALUE IS BIGGER THAN THE MEAN (THRESHOLD) THEN IT IS A DASH, IF NOT IT IS A DOT
for i in range(len(morse)):
    if morse[i]>threshold:
        morse[i] = "-"
    elif morse[i]<threshold:
        morse[i] = "."
print(morse)


space_list = [list(g) for k, g in groupby(data, lambda x: x == 0) if k]
morse_empty = []
for i in range(len(space_list)):
    morse_empty.append(len(space_list[i]))

empty_threshold = np.mean(morse_empty)
print(empty_threshold)
for i in range(len(morse_empty)):
    if morse_empty[i]>5000:
        morse_empty[i] = "+"
    elif morse_empty[i]>empty_threshold:
        #print(morse_empty[i])
        morse_empty[i] = "="
        #print(morse_empty[i])
    else:
        #print(morse_empty[i])
        morse_empty[i] = ","
        
        
# print(morse_empty)

space_indices = []
for i in range(len(morse_empty)):
    if morse_empty[i] == "=":
        space_indices.append(i)
    elif morse_empty[i] == "+":
        space_indices.append(i)
        space_indices.append(i)

increment = len(space_indices)
while increment>0:
    space_indices[increment-1]+=increment
    increment-=1
for i in range(len(space_indices)):
    morse.insert(space_indices[i]," ")
    
morse.append(' ')
message = "".join(morse)
print("THIS IS THE MESSAGE IN MORSE: ",message)


result = morse_to_text(message) 

print(result)
