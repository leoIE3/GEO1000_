# GEO1000 - Assignment 2
# Authors: Leonardo Melo	
# Studentnumbers: 4690923

import string

def sentence_value(sentence):
	sentence=sentence.lower()
	sentence=sentence.translate(None, string.punctuation)
	return sentence

def rds(value):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    sumo=0    
    for char2 in value:
    	i=1
    	for char1 in alphabet:
            if char2.isspace() or char2.isdigit():
          		i=0
           	 	break
     	    elif char2==char1:
       	     	break 
            i+=1
        sumo+=i
    B=sum([int(char) for char in str(sumo)])
    return B
	
if __name__ == "__main__":
	print "The reduced digit sum is: %d" %(rds(sentence_value("geomatics is fun!")))


