fonte = open("Fonte.txt", "r")
line_count = 0
char_count = 0
word_count = 0
space_count = 0


for x in fonte:
    line_count += 1
    char_count += len(x)
    words = x.split()
    word_count += len(words)
    space_count += len(words) - 1
    print(words)
