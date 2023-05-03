# with - manager kontekstu - zamknięcie pliku

""" with open("names.txt", "r") as read_file:
    for line in read_file.read().splitlines():
        print(line) """
        
""" new_name = "Luke"
with open("names.txt", "a") as write_file:
    write_file.write(new_name) """
    
new_name = "Grzegorz"
with open("names.txt", "w") as write_file:
    write_file.write(new_name)