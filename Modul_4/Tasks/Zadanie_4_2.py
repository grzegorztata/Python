def palindrom(word):
  '''
  Do zadania dodano:
   - Input do wprowadzania słowa przez użytkownika
   - funkcję lower() do konwertowania liter w słowie na małe litery
   - slicing do odwracania słowa
   - weryfikacja czy słowo nie jest zbyt krótkie
  Jeszcze nie działa:
   - Palindromy dla zdań
  '''
  word = word.lower()
  return word == word[::-1]

word = input("Wprowadź słowo aby sprawdzić czy jest palindromem: ")

if len(word) < 2:
  print("Słowo jest zbyt krótkie. Wprowadź minimum 2 znaki")
else:
  if palindrom(word):
    print("Jest palindromem")
  else:
    print("Nie jest palindromem")
