import scanner
import mgolparser
fonte = open("Fonte.txt", "r")

token_list = scanner.scanner(fonte.read())

print("-------------------------")
print("LISTA DE TOKENS")
print("-------------------------")
for token in token_list:
    print(token)
