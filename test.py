import DFA

dfa0 = DFA.dfa0
transition_table = dfa0.getDelta()

reserved_words = {
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

reserved_words['teste'] = 'oi!!'
print(reserved_words)
""" string = "Oi meu nome e heitor"

print(string.split()) """
