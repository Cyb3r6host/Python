
def main():
    tmp= input("Give Me the File path: ") #Waiting for user input
    file=open(tmp,"r+")
    words = file.read().split() #split the file
    newlist = []
    for word in words:
        newlist.append(AyMaker(word.strip()))
    result = ' '.join(newlist)
    print(result)
    file.seek(0)
    file.write(result)
    file.close

        


#Function that removes the first letter and re-add it to the and with ay
def AyMaker(string):
    if len(string)>3:
        string = string[1:]+string[0:1]+"ay"
        return string
    else:
        return string



#Run the main Function
main()
