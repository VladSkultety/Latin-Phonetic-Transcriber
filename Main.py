#coding: utf-8 -*-

LatinText = open("LatinText.txt", "r")

InternalText = LatinText.read()

MyList = [

#Phontic changes
('Ae','Ay'),
('ae','ay'),
('Oe','Oy'),
('oe','oy'),
('Ē','Ey'),
('ē','ey'),
('V','W'),
('v','w'),
('C','K'),
('c','k'),
('Qu','Kw'),
('qu','kw')
]

for k,v in MyList:
    InternalText = InternalText.replace(k, v)

LatinText.close()

#Write LatinText.txt file with phonetically transcribed Latin.
#Need to close and open LatinText again.

WriteFile = open("LatinText.txt", "w")
WriteFile.write(InternalText)
WriteFile.close()
