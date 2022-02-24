###
# Kim Kaufman
# This program counts the number of occurences for each word in a sentence that is obtained from user input

def main():
    
    print("Word count program \n")
    
    user_sentence = input("Please enter a sentence: ")
    
    #removes all punctuation
    user_sentence = user_sentence.replace(",", "")
    user_sentence = user_sentence.replace(":", "")
    user_sentence = user_sentence.replace("!", "")
    user_sentence = user_sentence.replace(";", "")
    user_sentence = user_sentence.replace(".", "")
    user_sentence = user_sentence.replace("'", "")
    user_sentence = user_sentence.replace("?", "")
    user_sentence = user_sentence.replace('"', '')
    
    user_sentence = user_sentence.lower()
    
    #converts string into list
    sentence = user_sentence.split(" ")
    
    word_count = {}
    
    #adds words from sentence as keys into the word_count dictionary and adds 1 to the value for each occurence
    for word in sentence:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    print()
    print("Word Count: ")
            
    for key, value in word_count.items():   #prints each key, value pair on a separate line        
        print(f"{key}: {value}")                
        
      
            
      
        
main()
