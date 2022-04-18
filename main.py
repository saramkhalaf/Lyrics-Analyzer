#this project is to count how many times a word appears in a sony lyrics

#this variable stores our song lyrics
text="""Here comes the sun
Here comes the sun, and I say
It's all right

Little darling
It's been a long, cold lonely winter
Little darling
It feels like years since it's been here

Here comes the sun
Here comes the sun, and I say
It's all right

Little darling
The smiles returning to the faces
Little darling
It seems like years since it's been here

Here comes the sun
Here comes the sun, and I say
It's all right

Sun, sun, sun, here it comes
Sun, sun, sun, here it comes
Sun, sun, sun, here it comes
Sun, sun, sun, here it comes
Sun, sun, sun, here it comes"""
#this line prints the length of characters , or how many characters are in the lyrics
#print(len(text))
#if we want to know how many words there are in the text we use split
#print(text.split())
#print(len(text.split()))

word_count={}

#to count we automatically know we can use a for loop that loops through the split words not characters in the text, so for every word in the text or lyrics we want to find out how many times is it there?
#for word in text.split():
#we can store the number of times the word is in the a text as a int value in a dictionary, and have the key be the text, in a for loop we can assign each word as a key in the dictionary, cause lets say we have 100 words in the lyrics, so we assign each one as a key and then provide one as its value to say this has only shown up once 
  #for each word in the text, variable text, or text.split to identify as word not character, we are adding the word as a key in the dictionary we created word_count
  #simple terms: for every word in the text.split we are assigning it with a value 1, the way we assign each word with a 1 is by creating a dictionary, assigning each key in the dictionary as a word, and then assigning it with an integer1
  #word_count[word]=1
  #this tells only assigns each key in the dictionary as 1, but we want it to print out how many times each word or key is present
  #if statement can help us detect when each word is present by going through the list and if it detects a word again it adds one, else if it doesnt it just moves on
#for word in text.split():
  #we would like to pass every word in the text as a key in the dictionary and assign it a value 1, word_count[word]=1 this just tells us a:1, b:1, C:1, but if the word exists twice in the word_count, then we add more than one to it so the for loop goes to the first word in the text, if it is in the word count or exists again somewhere it adds one, in this case for word in text.split list, is the word in the word_count? no because word_count is an empty dictionary ok so it goes to else statement add the word as a key and assign 1 to it, it does that for a, b and c
  #for loop goes through first item in the text.split list, goes to the first if statement, does a exist in the word_count? no it doesnt so goes to the else statement, since it is not in the word_count, since the word_count is an empty dictionary we give it a key pass it in the dictionary and assign it a value of 1
  #for loop goes through second item b, does b exist in the word_count? no , so pass it as a key parameter in the dictionary and assign 1 to it
  #for loop goes through third item, c does c exist in the word_count? no, so pass it as a key parameter to the word_count dictionary and assign 1 to it. 
  #now our dictionary at this point has {a:1,b:1,c:1} but the for loop is not done yet it must go on!
  #now for loop is at the fourth item a , is a in the word_count? yes it is and it has a value 1, so simply just add to the existing value word_count[word]=+1, =word_count[word]+1, this means the value of the word_count[word]=x which is x in this case is being added one to it, word_count[word]+=word_count[word]+1
for word in text.lower().split():
  if word in word_count:
    word_count[word]+=1
  else:
    word_count[word]=1
print(word_count)
