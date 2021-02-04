# Classical Latin-Phonetic-Transcriber
A simple code phonetically transcribing Classical Latin into a reader-friendly text based on Classical Latin pronunciation rules.

It does this:

Input:

Gallia est omnis dīvīsa in partēs trēs, quārum ūnam incolunt Belgae, aliam Aquītānī, tertiam quī  ipsōrum linguā Celtae, nostrā Gallī appellantur.

Output:

Gallia est omnis dīwīsa in parteys treys, kwārum ūnam inkolunt Belgay, aliam Akwītānī, tertiam kwī  ipsōrum linguā Keltay, nostrā Gallī appellantur.

Will try to add stress markers in the future.

A work in progress.

Latin Pronunciation Rules

Consonants:

c/k	> [k]	  As 'k' in 'sky'. Found in Greek loanwords, representing the Greek 'κ'.
ch  >	[kʰ]	As 'ch' in 'chemistry', and aspirated. Transliteration of Greek χ.
g	  > [ɡ]	  As 'g' in 'good'.
gn  >	[gn]	As 'gn' in 'wingnut'.
i	  > [j]	  As 'y' in 'yard', only in some cases at the beginning of syllables.
      [jː]	As 'y y' in 'joy years', when between two vowels.
l   > [l]	  As 'l' in 'leave', when doubled as 'll' or positioned before 'i'.
      [ɫ]	  As 'll' in 'all', in all other positions.
n	  > [n]	  As 'n' in 'man'.
p   > [p]	  As 'p' in 'spy', never aspirated.
ph  > [pʰ]	As 'p' in party, always aspirated. Transliteration of Greek φ.
qu  > [kʷ]	As 'qu' in quiet/
quu	> [kʷɔ] Educated pronunciation.
      [ku]  Popular pronunciation.
r   > [r]	  As 'r' in Italian or Spanish.
rh  > [r̥]	 As 'r' in Turkish at the end of words. Transliteration of Greek 'ῥ'.
s   > [s]	  As 's' in 'say'.
t   > [t]	  As 't' in 'stay', never aspirated.
th  > [tʰ]	As 'th' in 'thyme', always aspirated. Transliteration of Greek 'θ'.
v   > [ʷ]	  As 'w' in wine, in some cases at the beginning of a syllable, or after g and s.
x   > [k͡s]	 As 'x' in 'axe', in some cases as 'gs' in 'eggs'.
z   > [zː]	As 'zz' in 'jazz'. Transliteration of Greek 'ζ'.

Vowels:

a   > [a]   As 'a' in Slovak. Similar to 'u' in 'cut' in English. Transliteration of Greek short 'α'.
ā   > [aː]  Same sound but long. Transliteration of Greek long 'α'.
            Both 'a' exactly the same sounds, differ only in length.

e   > [ɛ]   French 'è'. Transliteration of Greek 'ε'.
ē   > [eːy] French 'é', pronounced long and with a 'y'glide at the end. Similar to 'ey' in 'they'.
            Transliteration of Greek 'η', and 'ει' in some cases.
            This code transcribes them as 'è' and 'é' respectively.

i   > [ɪ]   As 'i' in 'sit'. Hungarian 'i'. Transliteration of short Greek 'ι'.
ī   > [iː]  As 'i' in 'machine'. Slovak 'i'. Transliteration of Greek long 'ι', and 'ει' in some cases.
            Both 'i' very similar. This code transcribes both as 'i'.

o   > [ɔ]   As the 'o' in British English words like 'sort, thought'. As the Russian 'o' in 'сухой'.
            Transliteration of Greek 'ο'.
ō   > [oː]  Similar to 'o' in 'holy'. Slovak 'o'. Transliteration of Greek 'ω', and 'ου' in some cases.

u   > [ʏ]   As 'u' in 'put'. Hungarian 'u'.
ū   > [yː]  As 'oo' in 'cool'. Slovak 'u'. Transliteration of Greek 'ου'.
            Both 'u' very similar. This code transcribes both as 'u'.

y   > [ʏ]   Hungarian 'ö' (Educated speakers). Slovak short 'u/i' (Popular pronunciation).
            Transliteration of Greek short 'υ'.
ȳ   > [yː]  Hungarian 'ű'. (Educated speakers). Slovak short 'u/i' (Popular pronunciation).
            Transliteration of Greek long 'υ'.

Diphthongs:

ae  > [ae̯]	As 'uy' in 'buy'. Transliteration of Greek 'αι'. This code transcribes the sound as 'ay'.
au  > [au̯]	As 'ou' in 'out'. Transliteration of Greek 'αυ'.
ei  > [ei̯]	As 'ey' in 'they'. Transliteration of Greek 'ει' in some cases.
eu  > [eu̯]	As 'eu' in Portuguese 'eu'. Transliteration of Greek 'ευ'.
oe  > [oe̯]	As 'oy' in 'boy'. Transliteration of Greek 'οι'.
ui  > [ui̯]	As 'uy' in Spanish 'muy', approximately to 'hooey'.
yi  > [ʏɪ̯]	As 'ű+j' in Hungarian. Transliteration of the Greek diphthong 'υι'.

Nasalization:

'm' at the end of words:

quārum    >   qwaːrũː
ūnam      >   uːnãː
aliam     >   aliãː

Any vowel followed by 'm/n', followed by 'f' or 's':

trāns       >   trãːs
īnstitūtīs  >   ĩːstituːtiːs

Accent:

(This code does not mark Latin accent. Hope to add the feature in the future).

Generally speaking, the accent tends to fall on the penultimate syllable in polysyllabic words:

1) Accent is never on the last syllable.
2) In disyllabic words, accent always on the penultimate syllable.
3) In tri- and more syllabic words:
  a) Accent on penultimate syllable if penultimate is heavy.
  b) Accent on antepenultimate (third from the end) if penultimate is light.

Note:

1) Light syllables:

a) Every short vowel followed by a single consonant: incolunt, initium

2) Heavy syllable if:

a) Every long syllable is heavy: grātiās, salvē, quaesō
b) Diphtong: aliam, proeliīs
c) short + double consonant: servat, portat, puella


Source:
https://en.wikipedia.org/wiki/Latin_phonology_and_orthography#Vowels
https://en.wikipedia.org/wiki/Help:IPA/Latin
https://txclassics.org/old/PronunciationGuide.pdf
