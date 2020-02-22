#Main Function
def main():
    tmp= input("Give Me the File path: ") #Waiting for user input
    file=open(tmp,"r")
    words = file.read().split() #split the file into words
    for i in range(len(words)):
        print("The Word:",words[i]," is a:",GoodOrBad(words[i].strip()))
        


#Function that counts all bad letters and returns if the word is a good or a bad one
def GoodOrBad(string):
    total_letters = len(string)
    list = split(string.lower())
    total_f = list.count("f")  
    total_c = list.count("c")
    total_k = list.count("k")
    total_r = list.count("r")
    total_bad = total_c + total_f + total_k +total_r
    if total_bad > total_letters-total_bad:
        return "Bad Word"
    else:
        return "Good Word"

#Function to generate an array with all word's available letters 
def split(word): 
    return [char for char in word]  


#Run the main Function
main()
