print ("welcome to judson's project")

mediatype = input("what is your media type")
title = input("what is the title of media?")
description = input ("type a quick description of your media")
genre = input("what is the genre of media?")
releaseyear = input("what year was it released?")
rating = input("give a quick rating out of ten of your media")



new_list = [mediatype,description,genre,releaseyear,rating]
print (new_list) 

if mediatype == "movies":
    movies.append(new_list)
    
if mediatype == "videogames":
    videogames.append(new_list)
    
if mediatype == "books":
    books.append(new_list)
    
if mediatype == "music":
    music.append(new_list)
    
print ("thank you for using my program")
