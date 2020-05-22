STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


#remove punctuation
#normalize all words to lowercase
#remove "stop words" -- words used so frequently they are ignored
#go through the file word by word and keep a count of how often each word is used
#"""Read in `file` and print out the frequency of words in that file."""




def remove_punctuation(text):
    punct = "!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~"
    words_to_keep = ''
    
    for character in text:
        if not character in punct:
            words_to_keep += (character)
            
    return words_to_keep
          
def remove_stop_words(string, words_to_remove):
    words_to_count = []
    for word in string: 
        if word != words_to_remove:
            words_to_count.append(word)
            return(words_to_count)

def count_words(list):
    word_count = dict()
    for word in list:
            if word in list:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    word_count = {key: value for key, value in word_count.items() if value >=6}
    return word_count            
    

        
        
        


def print_word_freq(file):
     
     file = open(file)
     text = file.read()
     text = text.lower()
     words_to_keep = remove_punctuation(text)
     words_to_count = remove_stop_words(words_to_keep, STOP_WORDS)
     word_count = count_words(words_to_count)
     print(word_count)
     

     file.close

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


