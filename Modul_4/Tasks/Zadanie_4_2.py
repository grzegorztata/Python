def palindrom(sentence):
  '''
  Do zadania dodano:
   - Input do wprowadzania słowa przez użytkownika
   - funkcję lower() do konwertowania liter w słowie na małe litery
   - slicing do odwracania słowa
   - weryfikacja czy słowo nie jest zbyt krótkie
  Poprawiono:
   - Palindromy dla zdań
  '''
#  word = word.lower()
#  return word == word[::-1]
  sentence = ''.join(single_char for single_char in sentence if single_char.isalnum()).lower()
  return sentence == sentence[::-1]  

word = input("Wprowadź słowo aby sprawdzić czy jest palindromem: ")

if len(word) < 2:
  print("Słowo jest zbyt krótkie. Wprowadź minimum 2 znaki")
else:
  if palindrom(word):
    print("Jest palindromem")
  else:
    print("Nie jest palindromem")
