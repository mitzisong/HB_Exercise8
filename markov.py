#!/usr/bin/env python

import sys
import random
import twitter
import os



def tweet_text(ourtext):
    twitter_api_key = os.environ.get("TWITTER_API_KEY")
    twitter_api_secret = os.environ.get("TWITTER_API_SECRET")
    twitter_access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
    twitter_access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
    api = twitter.Api(consumer_key=twitter_api_key, consumer_secret=twitter_api_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_token_secret)

    status = api.PostUpdate(ourtext)
    print status.text

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
markov chains."""

    # create our empty dictionary
    dictionary = {}

    split_words = corpus.split()
    # print split_words
   
    for i in range(len(split_words)-2):
        if dictionary.get((split_words[i], split_words[i+1])):
            dictionary[(split_words[i], split_words[i+1])].append(split_words[i+2]) # append list with split_words[i+2]
        else:
            dictionary[(split_words[i], split_words[i+1])] = [split_words[i+2]]

#    print dictionary
    return dictionary


# ---------- this is all intact from the sample
#
def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
based off an original text."""
    keylist = chains.keys()
    first_tuple = random.choice(keylist)
    # could try the below by accessing first_tuple[0] and first_tuple[1]

    # create variables "word1" and "word2" and set them to the two words from the tuple
    word1, word2 = first_tuple # might need parentheses
    
    # we can also reference the first and second words by their index numbers in the tuple:
#    print first_tuple[0]
#    print first_tuple[1]

    # build the list: the first two items are the first tuple

    # create an "output_list" that starts with the first two words from above

    output_list = [word1, word2]
#    print output_list

    # here is our loop 

    for i in range(20):   # <- set max of 20 so that the list doesn't get too long

        # get our "next word" as a random choice from the value list from our tuple
        # (the tuple is written here as "chains[(word1, word2)]")
        next_word = random.choice(chains[(word1, word2)])

        # copy word2 over to word1, and next_word over to word2, to form our next tuple
        word1, word2 = word2, next_word

        # print word1
        # print word2
        # print next_word

        # add next_word to the end of our output_list
        output_list.append(next_word)

        # print output_list

    # once we have our list, we can create the string by combining the list
    # and separating each word with a space
    output_string = " ".join(output_list)
    
    # this changes the first character of our string (output_string[0])
    # to an upper case. 
#    output_string = output_string[0].upper() + output_string[1:]
    output_string_punctuated = output_string + "."

#    print output_string
    return output_string_punctuated

# join outside of for loop

# return "Here's some random text."

def main():
    args = sys.argv

    # Change this to read input_text from a file
    f = open('blender.txt', 'r')
      #read the file into another copy
    input_text = f.read()
      #close original file
    f.close()
    
    input_text = input_text.lower()
    
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    tweet_text(random_text)
    #print random_text

if __name__ == "__main__":
    main()