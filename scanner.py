import DFA
dfa0 = DFA.dfa0

symbol_table = {
    'inicio': 'inicio',
    'varinicio': 'varinicio',
    'varfim': 'varfim',
    'escreva': 'escreva',
    'leia': 'leia',
    'se': 'se',
    'entao': 'entao',
    'fimse': 'fimse',
    'fim': 'fim',
    'inteiro': 'inteiro',
    'lit': 'lit',
    'real': 'real',
}

error_table = {
    0: 'Caminho nao reconhecido',
    19: 'Numeral incorreto',
    20: 'Numeral incorreto',
    21: 'Numeral incorreto',
    4: 'Literal incorreto',
    7: 'Comentário incorreto'
}


def scanner(content):
    line_count = 0
    char_count = 0
    word_count = 0
    space_count = 0

    pointer = 0
    current_line = 1
    current_column = 1
    current_state = 0
    lexeme = ""
    token_list = []
    for x in content:
        line_count += 1
        char_count += len(x)
        words = x.split()
        word_count += len(words)
        space_count += len(words) - 1

    while (pointer < char_count):
        if content[pointer] not in dfa0.getAlphabet():
            print("Erro lexico na linha ", current_line,
                  "e coluna ", current_column, " caractere invalido: ", content[pointer])
            pointer += 1
            current_state = 0
            lexeme = ""
        else:
            transition_table = dfa0.getDelta()
            final_states = dfa0.getFinalStates()
            try:
                transition = transition_table[(
                    current_state, content[pointer])]
            except:
                transition = "None"

            if transition == "None" and current_state in final_states:
                tokenClass = dfa0.find_token_state(current_state)
                finalStateType = dfa0.find_token_type(current_state)
                if tokenClass != 'id':
                    output = "Lexema: " + str(lexeme) + "\tToken: " + \
                        str(tokenClass) + "\tTipo: " + str(finalStateType)
                    print(output)
                    token_list.insert(pointer, [tokenClass, lexeme,
                                      finalStateType, current_line, current_column])

                else:
                    if (lexeme in symbol_table):
                        output = "Lexema: " + str(lexeme) + "\tToken: " + \
                            str(lexeme) + \
                            "\tTipo: " + str(symbol_table[lexeme])
                        print(output)
                        token_list.insert(pointer, [tokenClass, lexeme,
                                          finalStateType, current_line, current_column])

                    else:
                        output = "Lexema: " + str(lexeme) + "\tToken: " + \
                            str(tokenClass) + "\tTipo: " + str(finalStateType)
                        print(output)
                        token_list.insert(pointer, [tokenClass, lexeme,
                                          finalStateType, current_line, current_column])

                        symbol_table[lexeme] = None

                current_state = 0
                lexeme = ""

            elif transition == "None" and current_state not in final_states:
                print(error_table[current_state], "na linha", current_line,
                      "e coluna", current_column)
                current_state = 0
                pointer += 1
                current_column += 1
                lexeme = ""

            elif (current_state == 4 or current_state == 10) and pointer == (char_count - 1):
                print(error_table[current_state])
                print(" Na linha ", current_line,
                      "e coluna ", current_column)
                pointer += 1

            else:
                if current_state == 0 and (content[pointer] == "\n" or content[pointer] == "\t" or content[pointer] == " "):
                    if content[pointer] == "\n":
                        current_line += 1
                        current_column = 1
                else:
                    lexeme += content[pointer]
                current_state = transition
                pointer += 1
                current_column += 1
    token_list.insert(char_count, ["EOF", None, None, current_line, 0])
