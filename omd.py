def step2_umbrella() -> str:
    """
    Returns a string describing the action of the duck-muralist when she
    takes an umbrella.

    Returns:
        str: A string indicating that the duck-muralist 🦆 took an umbrella ☂.
    """
    return 'Утка-маляр 🦆 взяла зонтик ☂'


def step2_no_umbrella() -> str:
    """
    Returns a string describing the action of the duck-muralist when she
    does not take an umbrella.

    Returns:
        str: A string indicating that the duck-muralist 🦆 did not take an
             umbrella ☂ :(
    """
    return 'Утка-маляр 🦆 не взяла зонтик ☂ :('


def step1() -> str:
    """
    Implements the first step of the duck-muralist's story.

    The function displays a prompt asking the user if the duck-muralist
    should take an umbrella or not.
    It validates the user's input and returns the appropriate action based
    on the choice.

    Returns:
        str: A string describing the action taken by the duck-muralist based
        on the user's choice.
    """
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
