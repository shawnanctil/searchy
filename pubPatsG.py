#!/usr/bin/env python

#Import relevant libraries, in this case the Google functions and classes from the pattern.web library, as well as the datetime library.

from datetime import date
from pattern.web import Google

# Define which engine I will be using and input the license key allowing me to grab results directly from Google's search results. This API key is restricted to my IP address and allows 200 free queries per day.
# Then define the 'today' string to ensure results can be time stamped.

engine = Google(license = '', throttle=0.5) #ENTER KEY
today = date.today()

#Create the index of keywords from whatever lexicon. 

with open('dKwordsApp.txt', 'r') as key:
    global kwords 
    kwords = [line.strip() for line in key]

#Main loop. First it specifies the number of times the loop will be executed. In this case the length of the kwords list.  # Second, it opens a document based on which keyword in the kwords list it's currently searching, writes results to it, separates each result with a new line, and then closes the file to preserve CPU memory.     #Third, it moves the index forward, proceding to the new item in the index. 

for i in range(len(kwords)):  # modify variable
    f = open(kwords[i] + 'DkApp_google.txt',"w") # modify variable
    f.write('Search results compiled on ' + str(today) + ':\n\n')
    for result in engine.search(kwords[i], count=10, cached=False): # modify variable
        f.write(str(result))
        f.write('\n\n')
        f.close
    i += 1