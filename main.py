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
for word in text.lower().split():
  if word in word_count:
    word_count[word]+=1
  else:
    word_count[word]=1
print(word_count)
