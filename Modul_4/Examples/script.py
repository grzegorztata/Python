def shopping(items, payment='card', shop='local'):
  result = ""
  result = result + "Ide na zakupy do %s.\n" % shop
  result = result + "Kupię następujące rzeczy: \n"
  for item in items:
    result = result + " - %s.\n" % item
  result = result + "By zapłacić używam %s." % payment
  return result

if __name__ == "__main__":
  items_text = input("Proszę podaj produkty rozdzielone przecinkiem: ")
  items = items_text.split(',')
  shopping_result = shopping(items)
  print(shopping_result)