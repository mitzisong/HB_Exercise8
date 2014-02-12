#!/usr/bin/env python

import sys
import random

  #read the file
f = open('blender.txt', 'r')
  #read the file into another copy 
sourcefile = f.read()
  #close original file
f.close()

#------------------------------
#  The story, so far.. 
# 
# 1. read the file (done)
# 2. copy the file into a single string/variable )done)
# 3. close the file (done)
# 4. split the string into words (done)
# 5. identify the number of words in the new list (done)
# 6. crawl through the list and pair:
#     word 1 + word 2
#        if this doesn't exist as a tuple already, add it, with the third word as a value
#        if this does exist as a tuple already, append the next word to the value list

#def make_chains(corpus):
dictionary = {}

def make_chains():
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    split_words = sourcefile.split()
    # print split_words
    

   
    for i in range(len(split_words)-2):
        if dictionary.get((split_words[i], split_words[i+1])):
            dictionary[(split_words[i], split_words[i+1])].append(split_words[i+2]) # append list with split_words[i+2]
        else:
            dictionary[(split_words[i], split_words[i+1])] = [split_words[i+2]]

    print dictionary
#    for word in split_lines:
make_chains()

# ---------- this is all intact from the sample 
#
def make_text(chains):
   """Takes a dictionary of markov chains and returns random text
  based off an original text."""

# for i in xrange(maxwords):
#     newword = random.choice(table[(w1, w2)])
#     if newword == nonword: sys.exit()
#     print newword;
#     w1, w2 = w2, newword

# for i in range(len(dictionary)):
#     keylist = dictionary.keys()
#     next_word = random.choice(keylist)
#     print next_word

#     for (word1, word2) in dictionary


    # word1, word2 = word2, next_word

    # print word1
    # print word2
    # print next_word


#    return "Here's some random text."

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = "Some text"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()


