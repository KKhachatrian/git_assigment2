def desyatcovuy_to_bit(number) :
    result = bin(int(number))
    return result

def bit_to_desyatkovuy(number):
    bit = number
    try:
        result = int(bit, 2)
        return result
    except ValueError:
        return None

def hexadecimal_to_desyatkovuy(number):
    hex = number
    try:
        result = int(hex, 2)
        return result
    except ValueError:
        return None

def bit_to_hexadecimal(number):
    bit = number
    try:
        result = hex(int(bit, 2))
        return result
    except ValueError:
        return None

def desyatkovuy_to_hex(number):
    result = hex(int(number))
    return result

def convertaciya():
    while True:
        number = input("Введіть число:")

        if number.startswith("0b"):
            system = input("В яку систему числення хочете перевести(hex,decimal):")
            if system == "hex":
                hexadecimal = bit_to_hexadecimal(number)
                if number is not None:
                    changed_number = print(f"Число у  шістнадцятковом вигляді: {hexadecimal}")
                else:
                    changed_number = print("Введено неправильно двійкове число.")
            elif system == "decimal":
                desyatkove = bit_to_desyatkovuy(number)
                if number is not None:
                    changed_number = print(f"Число у десятковому вигляді: {desyatkove}")
                else:
                    changed_number = print("Введено неправильно двійкове число.")

        elif number.startswith("0x"):
            system = input("В яку систему числення хочете перевести(bit,decimal):")
            if system == "bit":
                bit = desyatcovuy_to_bit(hexadecimal_to_desyatkovuy(number))
                if number is not None:
                    changed_number = print(f"Число у двійковому вигляді: {bit}")
                else:
                    changed_number = print("Введено неправильно шістнадцяткове число.")
            elif system == "decimal":
                desyatkove = hexadecimal_to_desyatkovuy(number)
                if number is not None:
                    changed_number = print(f"Число у десятковому вигляді: {desyatkove}")
                else:
                    changed_number = print("Введено неправильно шістнадцяткове число.")

        else:
            try:
                desyatkove = int(number)
                system = input("В яку систему числення хочете перевести(bit,hex):")
                if system == "hex":
                    hexadecimal = desyatkovuy_to_hex()
                    changed_number = print(f"Число у шістнадцятковом вигляді: {hexadecimal}")
                elif system == "bit":
                    bit = desyatcovuy_to_bit(number)
                    changed_number = print(f"Число у двійковому вигляді: {bit}")
            except ValueError:
                changed_number = print("Введено неправильно десяткове число.")

        repeat = input("Перевести ще якесь число? (так/ні): ").strip().lower()
        if repeat == 'ні':
            print("Робота завершена.")
            break


convertaciya()
