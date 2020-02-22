import os
import json

#Main Function
def main():
    tmp= input("Give me targets username: ") #Waiting for user input
    CreateUserFile(tmp)
    jsonfile = ReadJson(tmp+"/"+tmp+".json")
    MostCommentsUser(jsonfile,tmp)

#Function to generate an array with all word's available letters 
def CreateUserFile(username): 
    os.system("python app.py --comments -m 100 "+ username)

#Read the json and returns it so python be able to read it
def ReadJson(filepath): 
    try:
        file = open(filepath).read()
    except FileNotFoundError as identifier:
        print("The user not found or account is private")
        exit()
    file = open(filepath).read()
    information = json.loads(file)
    return information

def MostCommentsUser(jsonfile,profilename):
    #Creating a hashmap  user:commentsInt
    map={}
    #Search into Json file for all post and scan all coments
    for i in jsonfile["GraphImages"]:
        for z in i["comments"]["data"]:
            author = z["owner"]["username"]
            if author in map.keys():
                map[author] += 1
            else:
                map[author] = 1
    #Scan the hashmap to find the user with most comments!  
    most_comments = 0     
    del map[profilename]     #removes the profile owner from the map
    for key in map:
        if map[key] > most_comments:
            most_comments_author = key
            most_comments = map[key]
    print("The user with most comments is:",most_comments_author,"With",most_comments,"comments!")



#Run the main Function
main()
