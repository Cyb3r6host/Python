tmp= input("Give Me the File path: ") #Waiting for user input
file=open(tmp,"r")

Vowels = ['a', 'e', 'i', 'o', 'u'] #List of all english Vowels 

#Reading the file and sort the words by length 
words = file.read().split()  
words.sort(key = len)
words.reverse()


#Function that removes all vowels and reverses the string
def RevVowelRemove(string):
    string = string[::-1]
    for letter in string:
        if letter in Vowels:
            string = string.replace(letter, '')
    return string


#Run the function for the 5 first longest words
for i in range(5):
    print(RevVowelRemove(words[i].strip()))
