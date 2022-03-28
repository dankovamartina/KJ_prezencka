def is_natural_number(number):
    """
    overuje, zda je zadane cislo cele cislo
    :param number: cislom ktere chceme proverit
    :return: (bool) True / cislo je cele, False / cislo neni cele
    """

    if isinstance(number, int) == True and number > 0:
        return True
    else:
        return False

def is_even_number(number):
    """
    proveri, zda je cislo sude nebo liche
    :param number: cislo ktere proverujeme
    :return: (bool) True = sude, False = liche
    """

    if number % 2 == 0:
        return True
    else:
        return False

def main ():
    my_number = 7
    print(f"{my_number} je prirozene: {is_natural_number(my_number)}")
    print (f"{my_number} je sude {is_even_number(my_number)}")


if __name__ == "__main__":
    main()