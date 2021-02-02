#coding: utf-8 -*-

LatinText = open("LatinText.txt", "r")

InternalText = LatinText.read()

MyList = [

('Αυ','Αφ'),]

for k,v in MyList:
    InternalText = InternalText.replace(k, v)

LatinText.close()

#Write LatinText.txt file with phonetically transcribed Latin. 
#Need to close and open LatinText again.

WriteFile = open("LatinText.txt", "w")
WriteFile.write(InternalText)
WriteFile.close()
