import random
  
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, aposta,values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * aposta
            winnings_lines.append(line +1)

    return winnings, winnings_lines
            

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in  enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposito():
    while True:
        quantia = input("Quanto você quer depositar? $")
        if quantia.isdigit():
            quantia = int(quantia)
            if quantia > 0:
                break
            else:
                print("Quantia deve ser maior que 0 ")
        else:
            print("Por favor insira um número ")
    return quantia

def get_number_lines():
    while True:
        lines = input("digite o número de linhas para apostar(1-" + str(MAX_LINES) +"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Coloque um número válido de linhas: ")
        else:
            print("Por favor insira um número ")
    return lines

def get_bet():
    while True:
        quantia = input("Quanto você quer apostar em cada linha ? $")
        if quantia.isdigit():
            quantia = int(quantia)
            if MIN_BET<= quantia <= MAX_BET:
                break
            else:
                print(f"Quantia deve ser entre ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Por favor insira um número ")
    return quantia

def spin(saldo):
    lines = get_number_lines()
    while True:
        aposta = get_bet() 
        total_bet = aposta * lines

        if total_bet > saldo:
            print(f"Você não tem o suficiente para apostar essa quantia, seu saldo atual é ${saldo}")
        else:
            break

    print(f"Você está apostando ${aposta} em {lines} linhas. Total apostado igual a: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, aposta, symbol_value)
    print(f"Você  ganhou ${winnings}. ")
    print(f"Você  ganhou na linha: ", *winnings_lines)
    return winnings - total_bet


def main():
    saldo = deposito()
    while True:
        print(f"Saldo atual ${saldo}")
        resposta = input("Aperte enter para jogar (s para sair).")
        if resposta == "s":
            break
        saldo += spin(saldo)

        print(f"Você saiu com ${saldo}")



main()

