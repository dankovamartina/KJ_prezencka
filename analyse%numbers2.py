def is_whole_number(number):
    """
    overuje, zda je zadane cislo cele cislo
    :param number: cislom ktere chceme proverit
    :return: (bool) True / cislo je cele, False / cislo neni cele
    """

    bool = isinstance(number, int)
    return bool

def main ():
    my_number = 7
    print(f"{my_number} je cele: {is_whole_number(my_number)}")


if __name__ == "__main__":
    main()