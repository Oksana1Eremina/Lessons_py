"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

MULT = 50
COMISSION_PERCENT = 0.015
MIN_COMISSION = 30
MAX_COMISSION = 600
EXTRA_COMISSION_PERCENT = 0.03
EXTRA_COMISSION_FREQUENCY = 3
RICH_COMISSION_PERCENT = 0.1
RICH_COMISSION_THRESHOLD = 5_000_000

def add_cash_after_extra_comission(cash, count_tr):
    if (count_tr > 0) and (count_tr % EXTRA_COMISSION_FREQUENCY == 0):
        cash *= (1 - EXTRA_COMISSION_PERCENT)
    return cash

def give_cash_with_extra_comission(cash, count_tr):
    if (count_tr > 0) and (count_tr % EXTRA_COMISSION_FREQUENCY == 0):
        cash *= (1 + EXTRA_COMISSION_PERCENT)
    return cash

def get_rich_tax(balance):
    if balance > RICH_COMISSION_THRESHOLD:
        print("Balance {} more then {}. I am deducting rich tax at the moment.".format(balance, RICH_COMISSION_THRESHOLD))
        balance *= (1 - RICH_COMISSION_PERCENT)
        print("Current balance: {}".format(balance))
    return balance

def check_cash(cash):
    if cash % MULT != 0:
        print("Error! Cash must be divided into 50.")
        exit()

def add_cash(balance, cash, count_tr):
    balance = get_rich_tax(balance)
    check_cash(cash)
    return balance + add_cash_after_extra_comission(cash, count_tr)

def get_comission(cash):
    comission = cash * COMISSION_PERCENT
    if comission < MIN_COMISSION:
        comission = MIN_COMISSION
    elif comission > MAX_COMISSION:
        comission = MAX_COMISSION
    return comission


def give_cash(balance, cash, count_tr):
    balance = get_rich_tax(balance)
    check_cash(cash)
    cash = give_cash_with_extra_comission(cash, count_tr) + get_comission(cash)
    if cash > balance:
        print("Error! Not enough money.")
        exit()
    return balance - cash

def quit():
    print("Quit.")
    exit()

def print_balance(balance):
    print('Balance: {}'.format(balance))

def main():
    balance = 0
    count_tr = 0
    while True:
        print_balance(balance)
        type = input("Enter type of operation: ")
        if type == "quit":
            quit()
        elif type == "add":
            cash = input("Enter cash to add: ")
            cash = int(cash)
            balance = add_cash(balance, cash, count_tr)
        elif type == "give":
            cash = input("Enter cash to give: ")
            cash = int(cash)
            balance = give_cash(balance, cash, count_tr)
        count_tr += 1

if __name__ == '__main__':
    main()