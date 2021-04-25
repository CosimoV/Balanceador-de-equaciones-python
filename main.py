from equation import Equation
from time import sleep


def run_balance():
    """
    Runs the chemical equation balance algorithm
    """
    print('=================================================')
    print('Introduce ecuacion quimica con elementos dentro de \nparentesis seguido por numero de atomos:')
    print('Ejemplo: (H)2 + (O)2 = (H)2(O)1')
    user_input = input('>>> ')
    try:
        equation = Equation(user_input)
        print('Ecuacion balanceada: ' + equation.balance())
        sleep(3)
        run_balance()
    except IndexError:
        print('Input invalido...')
        sleep(3)
        run_balance()

run_balance()