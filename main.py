
are_you_coding_in_repl = True
Folder_Where_Dictionaries_AreSaved = 'D:\\Personal\\Karthik Personal\\AEC\\Homework\\Session 9\\Files\\Dictionaries\\'

def is_word_in_dictionary(word = ''):
    if word is None:
        return (False,'No word provided')
    elif word == "–":
        return ( False, "Not a word")
    elif isinstance(word, str) == False:
        return (False,'Not a string')
    elif len(word) == 0:
        return (False,'Empty string')
    elif word.isalpha() == False:
        return (False,'String with non-alphabets')
    else:
        word = word.lower()
        starting_letter = word[0]
        if(are_you_coding_in_repl):
            dictionary_file_name = starting_letter + '.xml'
        else:
            dictionary_file_name = Folder_Where_Dictionaries_AreSaved + starting_letter + '.xml'
        word = starting_letter.upper() + word[1:]
        with open(dictionary_file_name) as f:
            if '<ent>' + word + '</ent>' in f.read():
                return (True,word + ' is in dictionary')
        return (False, word + ' is not in dictionary')




#2
word="history"
l=len(word)

wordarr = []
Allwordarr = []

ctr=1
for c1 in range (0, l):
  #print( word[c], " ")
  for c2 in range (0, l):
    if (word[c1]!=word[c2]):
     word2= word[c1] + word[c2]
     #print( ctr, word2)
     ctr=ctr+1
     wordarr.append(word2)
     Allwordarr.append(word2) 

print ("total 2 Letter Word Count is ", len(wordarr) )


wordarr = []
ctr=1
for c1 in range (0,l):
  for c2 in range (0,l):
    for c3 in range (0,l):
      if(word[c1] != word[c2] and word[c1] != word[c3] and word[c2] != word[c3]):
        word3 = word[c1] + word[c2] + word[c3]
        #print(ctr, word3)
        ctr=ctr+1
        wordarr.append(word3)
        Allwordarr.append(word3) 

print ("total 3 Letter Word Count is ", len(wordarr) )


wordarr = []
ctr=0
for c1 in range (0,l):
  for c2 in range (0,l):
    for c3 in range (0,l):
      for c4 in range (0,l):
        if(word[c1] != word[c2] and word[c1] != word[c3] and word[c1] != word[c4] and word[c2] != word[c3] and word[c2] != word[c4] and word[c3] != word[c4]):
          word4 = word[c1] + word[c2] + word[c3] + word[c4]
          ctr=ctr+1
          wordarr.append(word4)
          Allwordarr.append(word4) 

print ("total 4 Letter Word Count is ", len(wordarr) )

wordarr = []
ctr=0
for c1 in range (0,l):
  for c2 in range (0,l):
    for c3 in range (0,l):
      for c4 in range (0,l):
        for c5 in range (0,l):
          word5 = word[c1] + word[c2] + word[c3]+ word[c4] + word[c5]
          if(word[c1] != word[c2] and word[c1] != word[c3] and word[c1] != word[c4]and word[c1] != word[c5] and word[c2] != word[c3] and word[c2] != word[c4] and word[c2] != word[c5] and word[c3] != word[c4] and word[c3] != word[c5] and word[c4] != word[c5]):
            #print (ctr, word5)
            ctr = ctr + 1
            wordarr.append(word5)
            Allwordarr.append(word5) 

print ("total 5 Letter Word Count is ", len(wordarr) )


wordarr = []
ctr=0
for c1 in range (0,l):
  for c2 in range (0,l):
    for c3 in range (0,l):
      for c4 in range (0,l):
        for c5 in range (0,l):
          for c6 in range (0,l):
              word6 = word[c1] + word[c2] + word[c3]+ word[c4] + word[c5]+ word[c6] + word[c6]
              if(word[c1] != word[c2] and word[c1] != word[c3] and word[c1] != word[c4]and word[c1] != word[c5] and word[c1] != word[c6] and word[c2] != word[c3] and word[c2] != word[c4] and word[c2] != word[c5] and word[c2] != word[c6] and word[c3] != word[c4] and word[c3] != word[c5] and word[c3] != word[c6] and word[c4] != word[c5] and word[c4] != word[c6] and word[c5] != word[c6]):
                #print (ctr, word7)
                wordarr.append(word6)
                Allwordarr.append (word6)
                ctr = ctr + 1

print ("total 6 Letter Word Count is ", len(wordarr) )


wordarr = []
ctr=0
for c1 in range (0,l):
  for c2 in range (0,l):
    for c3 in range (0,l):
      for c4 in range (0,l):
        for c5 in range (0,l):
          for c6 in range (0,l):
            for c7 in range (0,l):
              word7 = word[c1] + word[c2] + word[c3]+ word[c4] + word[c5]+ word[c6] + word[c7]
              if(word[c1] != word[c2] and word[c1] != word[c3] and word[c1] != word[c4]and word[c1] != word[c5] and word[c1] != word[c6] and word[c1] != word[c7] and word[c2] != word[c3] and word[c2] != word[c4] and word[c2] != word[c5] and word[c2] != word[c6] and word[c2] != word[c7] and word[c3] != word[c4] and word[c3] != word[c5] and word[c3] != word[c6] and word[c3] != word[c7] and word[c4] != word[c5] and word[c4] != word[c6] and word[c4] != word[c7] and word[c5] != word[c6] and word[c5] != word[c7] and word[c6] != word[c7]):
                #print (ctr, word7)
                wordarr.append(word7)
                Allwordarr.append( word7)
                ctr = ctr + 1


print ("total 7 Letter Word Count is ", len(wordarr) )

# now look for meaningfull word count in the all array 

MeaningfullWordarr = [] 

for wrd in Allwordarr:
  (is_word_meaningful, error_message) = is_word_in_dictionary(wrd)
  if ( is_word_meaningful  ):
     MeaningfullWordarr.append( wrd )
     print (wrd)


print ( "total count of meaningfull words is : " , len( MeaningfullWordarr) ) 
#it takes a long time to execute


exit()



lincoln_speech = ''

Folder_Where_SpeechTexts_AreSaved = 'D:\\Personal\\Karthik Personal\\AEC\\Homework\\Session 9\\Files\\Speeches\\'

if(are_you_coding_in_repl):
    lincoln_speech_filename = 'Abraham Lincoln - The Gettysburg Address.txt'
else:
    lincoln_speech_filename = Folder_Where_SpeechTexts_AreSaved +'Abraham Lincoln - The Gettysburg Address.txt'

with open(lincoln_speech_filename) as f:
    lincoln_speech = f.read()

mlk_speech = ''

if(are_you_coding_in_repl):
    mlk_speech_filename = 'Martin Luther King Jr. - I Have a Dream.txt'
else:
    mlk_speech_filename = Folder_Where_SpeechTexts_AreSaved + 'Martin Luther King Jr. - I Have a Dream.txt'

with open(mlk_speech_filename) as f:
    mlk_speech = f.read()
    
#print(lincoln_speech)
#print(mlk_speech)


def MeaningfulWordCount( sentence = ''):
   
  sarr = []
  sarr =  sentence.split(" ")

  num_of_dictionary_words=0  
  for wrd in sarr:
    #wrd = wrd.replace( ".", "" ) # dots are an issue to check
    (is_word_meaningful, error_message) = is_word_in_dictionary(wrd)
    if ( is_word_meaningful  ):
      num_of_dictionary_words=num_of_dictionary_words+1
      #print(num_of_dictionary_words, " -", wrd)
    
  return(num_of_dictionary_words)


print ( "Lincon speech : ", MeaningfulWordCount( lincoln_speech), " meaningful words" )

print("Martin Luther King Jr. speech :", MeaningfulWordCount(mlk_speech), "words")