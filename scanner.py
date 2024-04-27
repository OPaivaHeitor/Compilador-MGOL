import DFA
dfa0 = DFA.dfa0

symbol_table = {
    'inicio': None,
    'varinicio': None,
    'varfim': None,
    'escreva': None,
    'leia': None,
    'se': None,
    'entao': None,
    'fimse': None,
    'fim': None,
    'inteiro': None,
    'lit': None,
    'real': None,
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
            print("Erro léxico na linha ", current_line,
                  "e coluna ", current_column, " caractere inválido")
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
                tokenType = dfa0.find_token_state(current_state)
                finalStateType = dfa0.find_token_type(current_state)

                if tokenType != 'id':
                    output = "Lexema: " + lexeme + "\tToken: " + \
                        tokenType + "\tTipo: " + finalStateType

                    token_list.insert(pointer, tokenType, lexeme,
                                      finalStateType, current_line, current_column)

                else:
                    if (lexeme in symbol_table):
                        output = "Lexema: " + lexeme + "\tToken: " + \
                            lexeme + \
                            "\tTipo: " + symbol_table[lexeme]

                        token_list.insert(pointer, tokenType, lexeme,
                                          finalStateType, current_line, current_column)

                    else:
                        output = "Lexema: " + lexeme + "\tToken: " + \
                            tokenType + "\tTipo: " + finalStateType

                        token_list.insert(pointer, tokenType, lexeme,
                                          finalStateType, current_line, current_column)

                        symbol_table[lexeme] = None

                current_state = 0
                lexeme = ""

            else:
                if current_state == 0 and (content[pointer] == "\n" or content[pointer] == "\t" or content[pointer] == " "):
                    if content[pointer] == "\n":
                        current_line += 1
                        current_column = 1
                else:
                    lexeme += content[pointer]
                current_state = 0
                pointer += 1
                column += 1
