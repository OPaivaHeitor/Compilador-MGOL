import scanner
fonte = open("Fonte.txt", "r")
token_list = scanner.scanner(fonte.read())

goto_table = [
    [1, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, 3, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None],
    [None, None, 18, None, None, None, None, 19, None, 20,
        None, None, 21, 27, None, None, 22, None, 29, None],
    [None, None, None, 5, 6, None, 8, None, None, None, None,
        None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, 12, 6, None, 8, None, None, None, None,
        None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 13, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 17, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, 31, None, None, None, None, 19, None, 20,
        None, None, 21, 27, None, None, 22, 29, None, None],
    [None, None, 32, None, None, None, None, 19, None, 20,
        None, None, 21, 27, None, None, 22, 29, None, None],
    [None, None, 33, None, None, None, None, 19, None, 20,
        None, None, 21, 27, None, None, 22, 29, None, None],
    [None, None, 34, None, None, None, None, 19, None, 20,
        None, None, 21, 27, None, None, 22, 29, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, 45, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, 51, None, 53,
        None, None, 54, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, 73, None, 75,
        None, None, 76, 27, None, None, None, None, None, 72],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        38, 40, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, 42, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, 53,
        None, None, 54, None, None, None, None, None, 52, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, 51, None, 53,
        None, None, 54, None, None, None, None, None, 56, None],
    [None, None, None, None, None, None, None, 51, None, 53,
        None, None, 54, None, None, None, None, None, 59, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, 66, None, None, None, 63, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, 68, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, 66, None, None, None, 70, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, 73, None, 75,
        None, None, 76, 27, None, None, None, None, None, 74],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, 73, None, 75,
        None, None, 76, 27, None, None, None, None, None, 78],
    [None, None, None, None, None, None, None, 73, None, 75,
        None, None, 76, 27, None, None, None, None, None, 80],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None],
]

action_table = [
    [None, 'S2', None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    ['ACC', None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, 'S4', None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'S25', None, None, None, None, 'S24', 'S26', None,
        None, None, None, None, None, 'S28', None, None, 'S30', None, None, None],
    [None, None, None, 'S7', None, None, None, 'S9', 'S10', 'S11', None, None,
        None, None, None, None, None, None, None, None, None, None, None, None, None],
    ['R3', None, None, None, None, 'R3', None, None, None, None, 'R3', 'R3', None,
        None, None, None, None, None, 'R3', None, None, 'R3', None, None, None],
    [None, None, None, 'S7', None, None, None, 'S9', 'S10', 'S11', None, None,
        None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'S79', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'S14', None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'R9', None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'R10', None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'R11', None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    ['R4', None, None, None, None, 'R4', None, None, None, None, 'R4', 'R4', None,
        None, None, None, None, None, 'R4', None, None, 'R4', None, None, None],
    [None, None, None, None, 'S15', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'R8', None, 'S16', None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, 'R6', None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'S14', None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'R7', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    ['R2', None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'S25', None, None, None, None, 'S24', 'S26', None,
        None, None, None, None, None, 'S28', None, None, 'S30', None, None, None],
    [None, None, None, None, None, 'S25', None, None, None, None, 'S24', 'S26', None,
        None, None, None, None, None, 'S28', None, None, 'S30', None, None, None],
    [None, None, None, None, None, 'S25', None, None, None, None, 'S24', 'S26', None,
        None, None, None, None, None, 'S28', None, None, 'S30', None, None, None],
    [None, None, None, None, None, 'S25', None, None, None, None, 'S24', 'S26', None,
        None, None, None, None, None, 'S28', None, None, 'S30', None, None, None],
    ['R39', None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'S35', None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, 'S37', None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'S49', None, None, None, None, None, None, 'S47',
        'S48', None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, 'S55', None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, 'S60', None, None, None, None, None],
    [None, None, None, None, None, 'S25', None, None, None, None, 'S24', 'S26', None,
        None, None, None, None, None, 'S28', None, None, None, None, 'S77', None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, 'S69', None, None, None, None, None],
    ['R12', None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    ['R18', None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    ['R24', None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    ['R32', None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'S36', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'R13', None, None, None, None, 'R13', 'R13', None,
        None, None, None, None, None, 'R13', None, None, 'R13', None, None, None],
    [None, None, None, None, None, 'S43', None, None, None, None, None, None, None,
        'S44', None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'S39', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'R19', None, None, None, None, 'R19', 'R19', None,
        None, None, None, None, None, 'R19', None, 'R19', 'R19', None, None, None],
    [None, None, None, None, 'R21', None, None, None, None, None, None, None, None,
        None, None, None, 'S41', None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'S43', None, None, None, None, None, None, None,
        'S44', None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'R20', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'R22', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'R23', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'S46', 'S49', None, None, None, None, None, None, 'S47',
        'S48', None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'R14', None, None, None, None, 'R14', 'R14', None,
        None, None, None, None, None, 'R14', None, None, 'R14', None, None, None],
    [None, None, None, None, 'R15', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'R16', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'R17', None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 'R25', None, None, None, None, 'R25', 'R25', None,
        None, None, None, None, None, 'R25', None, None, 'R25', None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, 'S55', None, None, None, None],
    [None, None, None, None, None, 'R28', None, None, None, None, 'R28', 'R28', None,
        None, None, None, None, None, 'R28', None, None, 'R28', None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, 'S55', None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, 'S55', None, None, None, None],
    [None, None, None, None, None, 'R31', None, None, None, None, 'R31', 'R31', None,
        None, None, None, None, None, 'R31', None, None, 'R31', None, None, None],
    [None, None, None, None, None, 'R29', None, None, None, None, 'R29', 'R29', None,
        None, None, None, None, None, 'R29', None, None, 'R29', None, None, None],
    [None, None, None, None, None, 'R30', None, None, None, None, 'R30', 'R30', None,
        None, None, None, None, None, 'R30', None, None, 'R30', None, None, None],
    [None, None, None, None, None, 'S61', None, None, None, None, None, None, None,
        'S62', None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 'R22', None, None, None, None, None, None, None, None,
        None, None, None, 'R22', 'R22', None, None, None, None, None, None, None],
    [None, None, None, None, 'R23', None, None, None, None, None, None, None, None,
        None, None, None, 'R23', 'R23', None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, 'S64', None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, 'S65'],
    [None, None, None, None, None, 'R26', None, None, None, None, 'R26', 'R26', None,
        None, None, None, None, None, 'R26', None, 'R26', None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, 'S67', None, None, None, None, None, None, None],
    [None, None, None, None, None, 'S61', None, None, None, None, None, None, None,
        'S62', None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, 'R27', None, None],
    [None, None, None, None, None, 'S61', None, None, None, None, None, None, None,
        'S62', None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, 'S71', None, None],
    [None, None, None, None, None, 'R34', None, None, None, None, 'R34', 'R34',
        None, None, None, None, None, None, 'R34', None, None, None, None, None, None],
    [None, None, None, None, None, 'R33', None, None, None, None, 'R33', 'R33', None,
        None, None, None, None, None, 'R33', None, None, 'R33', None, None, None],
    [None, None, None, None, None, 'S25', None, None, None, None, 'S24', 'S26',
        None, None, None, None, None, None, None, None, None, None, None, 'S77', None],
    [None, None, None, None, None, 'R35', None, None, None, None, 'R35', 'R35', None,
        None, None, None, None, None, 'R35', None, None, 'R35', None, None, None],
    [None, None, None, None, None, 'S25', None, None, None, None, 'S24', 'S26',
        None, None, None, None, None, None, None, None, None, None, None, 'S77', None],
    [None, None, None, None, None, 'S25', None, None, None, None, 'S24', 'S26',
        None, None, None, None, None, None, None, None, None, None, None, 'S77', None],
    [None, None, None, None, None, 'R38', None, None, None, None, 'R38', 'R38', None,
        None, None, None, None, None, 'R38', None, None, 'R38', None, None, None],
    ['R5', None, None, None, None, 'R5', None, None, None, None, 'R5', 'R5', None,
        None, None, None, None, None, 'R5', None, None, 'R5', None, None, None],
]

actions_dictionary = {
    '$': 0,
    'inicio': 1,
    'varinicio': 2,
    'varfim': 3,
    'pt_v': 4,
    'id': 5,
    'vir': 6,
    'inteiro': 7,
    'real': 8,
    'literal': 9,
    'leia': 10,
    'escreva': 11,
    'lit': 12,
    'num': 13,
    'atr': 14,
    'rcb': 15,
    'opm': 16,
    'opr': 17,
    'se': 18,
    'ab_p': 19,
    'fimse': 20,
    'repita': 21,
    'fc_p': 22,
    'fimrepita': 23,
}

goto_dictionary = {
    'P': 0,
    'V': 1,
    'A': 2,
    'LV': 3,
    'D': 4,
    'L': 5,
    'TIPO': 6,
    'ES': 7,
    'ARG': 8,
    'CMD': 9,
    'LD': 10,
    'OPRD': 11,
    'COND': 12,
    'CAB': 13,
    'CD': 14,
    'EXP_R': 15,
    'R': 16,
    'CABR': 17,
    'CP': 18,
    'CPR': 19,
}

grammar = {
    2: [3, 'P'],
    3: [2, 'V'],
    4: [2, 'LV'],
    5: [2, 'LV'],
    6: [3, 'D'],
    7: [3, 'L'],
    8: [1, 'L'],
    9: [1, 'TIPO'],
    10: [1, 'TIPO'],
    11: [1, 'TIPO'],
    12: [2, 'A'],
    13: [3, 'ES'],
    14: [3, 'ES'],
    15: [1, 'ARG'],
    16: [1, 'ARG'],
    17: [1, 'ARG'],
    18: [2, 'A'],
    19: [4, 'CMD'],
    20: [3, 'LD'],
    21: [1, 'LD'],
    22: [1, 'OPRD'],
    23: [1, 'OPRD'],
    24: [2, 'A'],
    25: [2, 'COND'],
    26: [5, 'CAB'],
    27: [3, 'EXP_R'],
    28: [2, 'CP'],
    29: [2, 'CP'],
    30: [2, 'CP'],
    31: [1, 'CP'],
    32: [1, 'A'],
    33: [2, 'R'],
    34: [4, 'CABR'],
    35: [2, 'CPR'],
    36: [2, 'CPR'],
    37: [2, 'CPR'],
    38: [1, 'CPR'],
    39: [1, 'A']
}

reductions = {
    2: 'P -> inicio V A',
    3: 'V -> varincio LV',
    4: 'LV -> D LV',
    5: 'LV -> varfim pt_v',
    6: 'D -> TIPO L pt_v',
    7: 'L -> id vir L',
    8: 'L -> id',
    9: 'TIPO -> inteiro',
    10: 'TIPO -> real',
    11: 'TIPO -> literal',
    12: 'A -> ES A',
    13: 'ES -> leia id pt_v',
    14: 'ES -> escreva ARG pt_v',
    15: 'ARG -> lit',
    16: 'ARG -> num',
    17: 'ARG -> id',
    18: 'A -> CMD A',
    19: 'CMD -> id atr LD pt_v',
    20: 'LD -> OPRD opm OPRD',
    21: 'LD -> OPRD',
    22: 'OPRD -> id',
    23: 'OPRD -> num',
    24: 'A -> COND A',
    25: 'COND -> CAB CP',
    26: 'CAB -> se ab_p EXP_R fc_p então',
    27: 'EXP_R -> OPRD opr OPRD',
    28: 'CP -> ES CP',
    29: 'CP -> CMD CP',
    30: 'CP -> COND CP',
    31: 'CP -> fimse',
    32: 'A -> RA',
    33: 'R -> CABR CPR',
    34: 'CABR -> repita ab_p EXP_R fc_p',
    35: 'CPR -> ES CPR',
    36: 'CPR -> CMD CPR',
    37: 'CPR -> COND CPR',
    38: 'CPR -> fimrepita',
    39: 'A -> fim'
}


def find_error(actTableStateNumber):
    actTableLine = action_table[actTableStateNumber]
    reduction_flag = 0
    expected_inputs = []
    resulting_actions = []
    for i in range(len(actTableLine)):
        if actTableLine[i] != None:
            resulting_actions.append(actTableLine[i])
            for action in actions_dictionary:
                if actions_dictionary[action] == i:
                    expected_inputs.append(action)
    for action in resulting_actions:
        if action[0] == 'R':
            reduction_flag = 1
    return expected_inputs, resulting_actions, reduction_flag


def parser(token_list, error_routine):
    if error_routine != 0 and error_routine != 1:
        print("Favor inserir um dos seguintes valores para a rotina de erro:\n0 - Panico\n1 - Insercao de Token")
        return 0

    global pilha_semantica, atributos, verificador

    ponteiro = 0
    a = token_list[ponteiro]
    token = a[0]
    pilha = 0

    while (True):
        # Seja s o estado ao topo da pilha
        s = int(pilha[0])
        # Verifica qual a coluna do token na tabela e busca a ação a ser feita na action_table
        coluna = actions_dictionary[token]
        tipo_action = action_table[s][coluna]
        print("COLUNA: ", coluna)
        print("TIPO_ACTION: ", tipo_action)
        if (tipo_action[0] == 'S'):
            pilha.insert(0, int(tipo_action[1:]))
            t = int(pilha[0])

            if (token != 'pt_v'):
                atributos = [token, a[1], a[2], a[3], a[4]]
                pilha_semantica.insert(0, atributos)
                pilha_semantica.insert(0, token)

            ponteiro += 1
            a = token_list[ponteiro]
        elif (tipo_action[0] == 'R'):
            reduz = int(tipo_action[1:])
            if (reduz in grammar):
                lado_direito = grammar.get(reduz)
                numero = lado_direito[0]
                nonterminal = lado_direito[1]

            for i in range(numero):
                pilha.pop(0)

            t = int(pilha[0])

            # Busca a transição do não terminal
            goto_type = goto_table[t][goto_dictionary[nonterminal]]

            # Empilha o valor encontrado na tabela e imprime a redução
            pilha.insert(0, int(goto_type))
            # print("Redução: ", reductions[reduz])
            # print(pilha_semantica[1])

        # Verificação se a ação na tabela de transição é um estado de aceitação com base no valor do topo da pilha
        # Aqui, a análise deve terminar
        elif (tipo_action == 'ACC'):
            print("----------------------------------------")
            print("Análise sintática concluída com sucesso!")
            print("----------------------------------------")
            break
        else:
            # Situação de erro
            print("----------------------------------------")
            expected_inputs, resulting_actions, reduction_flag = find_error(s)
            verificador = False
            print("Erro sintatico, entradas esperadas: ", expected_inputs)
            print("----------------------------------------")

        # Rotinas de erro

        # PÂNICO
        if error_routine == 0:
            while (True):
                ponteiro += 1
                a = token_list[ponteiro]
                token = a[0]
                if (token == 'pt_v' or token == 'fc_p' or token == 'id' or token == 'fim' or token == 'fimse'):
                    pilha.pop(0)
                    break

        # POR INSERÇÃO DE TOKEN
        elif error_routine == 1:
            token = expected_inputs[0]
            ponteiro -= 1
            a = token_list[ponteiro]


print(token_list[0])
