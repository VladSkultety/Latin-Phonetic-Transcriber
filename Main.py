#coding: utf-8 -*-

LatinText = open("LatinText.txt", "r")

InternalText = LatinText.read()

MyList = [

#Prep

(';',',') #changing all ';' to ','.

#Phontic changes

#Greek loan words
,('Ch','Kʰ'),('ch','kʰ') #transliteration of Greek 'χ'
,('Th','Tʰ'),('th','tʰ') #transliteration of Greek 'θ'
,('Ph','Pʰ'),('ph','pʰ') #transliteration of Greek 'φ'
,('Rh','R̥'),('rh','r̥') #transliteration of Greek 'ῥ'
,('Z','Zː'),('z','zː') #transliteration of Greek 'ζ'
,('Yi','Öi'),('yi','öi') #transliteration of the Greek diphthong 'υι'

#Pronunciation of Greek loanwords by educated speakers of Latin

,('Y','Ö'),('y','ö') #Hungarian 'ö'
,('Ȳ','Ű'),('ȳ','ű') #Hungarian 'ű'

#General pronunciation rules majuscule, minuscule

#Diphtongs
,('Ae','Ay'),('ae','ay')
,('Uā','wā'),('uā','wā')
,('Oe','Oy'),('oe','oy')
,('Vu','Wɔ'),('vu','wɔ')

#Glides
,('Qu','Kʷ'),('qu','kʷ')
,('Quu','Kʷɔ'),('quu','kʷɔ') #as pronounce by educated speakers

#Misc
,('V','ʷ'),('v','ʷ')
,('C','K'),('c','k')
,('X','Ks'),('x','ks')

#Full phonetic transcript of vowels
#conversion of a,e,i,o,u to their corresponding qualities when long and short
#'|' used to distinguish capital 'ɪ' from capital 'I'

#short majuscule, minuscule
,('A','A'),('a','a') #Slovak 'a' (both 'a' exactly the same)
,('E','Ɛ'),('e','ɛ') #French 'è'
,('I','|'),('i','ɪ') #Hungarian 'i' (both 'ɪ' and 'i' almost the same)
,('O','Ɔ'),('o','ɔ') #Russian 'o' as in сухой
,('U','Ʊ'),('u','ʊ') #Hungarian 'u' (both 'u' and 'ʊ' almost the same)
#long majuscule, minuscule
,('Ā','Aː'),('ā','aː') #Slovak 'a' (both 'a' exactly the same)
,('Ē','Éːy'),('ē','éːy') #French 'é'
,('Ī','Iː'),('ī','iː') #Slovak 'i'(both 'ɪ' and 'i' almost the same)
,('Ō','Oː'),('ō','oː') #Slovak 'o'
,('Ū','Uː'),('ū','uː') #Slovak 'u' (both 'u' and 'ʊ' almost the same)

#Nasalization
#All nasal vowels pronounced as 'aːéːyiːoːuː' after nasalization regardless of
#wheather they are written short or long in the orginal Latin text.
#Ex.: 'ūm = ũː' but also 'um = ũː'

#'m' at the end of words

#(before space, fullstop, comma)
#'ẽ' is actually 'é' + tilde, but there is not such character so 'ẽ' was used.
#short
,('am ','ãː '),('am.','ãː.'),('am,','ãː,')
,('ɛm ','ẽyː '),('ɛm.','ẽyː.'),('ɛm,','ẽyː,')
,('ɪm ','ĩː '),('ɪm.','ĩː.'),('ɪm,','ĩː,')
,('ɔm ','õː '),('ɔm.','õː.'),('ɔm,','õː,')
,('ʊm ','ũː '),('ʊm.','ũː.'),('ʊm,','ũː,')
#long
,('aːm ','ãː '),('aːm.','ãː.'),('aːm.','ãː.')
,('éːym ','ẽyː '),('éːym.','ẽyː.'),('éːym.','ẽyː.')
,('iːm ','ĩː '),('iːm.','ĩː.'),('iːm.','ĩː.')
,('oːm ','õː '),('oːm.','õː.'),('oːm.','õː.')
,('uːm ','ũː '),('uːm.','ũː.'),('uːm.','ũː.')

#Nasalization of 'm/n' before 's' and 'f'.

#'N/n'
#any vowel, long or short, followed by 'n' + 's' and 'n' + 'f'

#short minuscule
,('ans','ãːs'),('anf','ãːf')
,('ɛns','ẽyːs'),('ɛnf','ẽyːf')
,('ɪns','ĩːs'),('ɪnf','ĩːf')
,('ɔns','õːs'),('ɔnf','õːf')
,('ʊns','ũːs'),('ʊnf','ũːf')
#long minuscule
,('aːns','ãːs'),('aːnf','ãːf')
,('éːyns','ẽyːs'),('éːynf','ẽyːf')
,('iːns','ĩːs'),('iːnf','ĩːf')
,('oːns','õːs'),('oːnf','õːf')
,('uːns','ũːs'),('uːnf','ũːf')
#short majuscule
,('Ans','Ãːs'),('Anf','Ãːf')
,('Ɛns','Ẽyːs'),('Ɛnf','ẽyːf')
,('|ns','Ĩːs'),('|nf','Ĩːf')
,('Ɔns','Õːs'),('Ɔnf','Õːf')
,('Ʊns','ũːs'),('Ʊnf','ũːf')
#long majuscule
,('Aːns','Ãːs'),('Aːnf','Ãːf')
,('Éːyns','Ẽyːs'),('Éːynf','ẽyːf')
,('Iːns','Ĩːs'),('Iːnf','Ĩːf')
,('Oːns','Õːs'),('Oːnf','Õːf')
,('Uːns','Ũːs'),('Uːnf','Ũːf')

#'M/m'
#any vowel, long or short followed by 'm' + 's' and 'm' + 'f'

#short minuscule
,('ams','ãːs'),('amf','ãːf')
,('ɛms','ẽyːs'),('ɛmf','ẽyːf')
,('ɪms','ĩːs'),('ɪmf','ĩːf')
,('ɔms','õːs'),('ɔmf','õːf')
,('ʊms','ũːs'),('ʊmf','ũːf')
#long minuscule
,('aːms','ãːs'),('aːmf','ãːf')
,('éːyms','ẽyːs'),('éːymf','ẽyːf')
,('iːms','ĩːs'),('iːmf','ĩːf')
,('oːms','õːs'),('oːmf','õːf')
,('uːms','ũːs'),('uːmf','ũːf')
#short majuscule
,('Ams','Ãːs'),('Amf','Ãːf')
,('Ɛms','Ẽyːs'),('Ɛmf','ẽyːf')
,('|ms','Ĩːs'),('|mf','Ĩːf')
,('Ɔms','Õːs'),('Ɔmf','Õːf')
,('Ʊms','ũːs'),('Ʊmf','ũːf')
#long majuscule
,('Aːms','Ãːs'),('Aːmf','Ãːf')
,('Éːyms','Ẽyːs'),('Éːymf','ẽyːf')
,('Iːms','Ĩːs'),('Iːmf','Ĩːf')
,('Oːms','Õːs'),('Oːmf','Õːf')
,('Uːms','Ũːs'),('Uːmf','Ũːf')


#Diphtong cleanup
,('ɪa','ia')

#Due to extreme similarity, decided to: ɪ > i; ʊ > u
#For better reading, decided to: ɛ > è; ē > é
#This section of the code can be muted in case more of an IPA feel is desired.

,('Ɛ','È'),('ɛ','è')
,('|','I'),('ɪ','i')
,('Ʊ','U'),('ʊ','u')

]

for k,v in MyList:
    InternalText = InternalText.replace(k, v)

LatinText.close()

#Write LatinText.txt file with phonetically transcribed Latin.
#Need to close and open LatinText again.

WriteFile = open("LatinText.txt", "w")
WriteFile.write(InternalText)
WriteFile.close()
