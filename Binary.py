import re
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

def arbitrary_to_desyatkovuy(number):
    match = re.match(r'([0-9A-Fa-f]+)x([2-9]|1[0-6])$', number)
    try:
        number_part = match.group(1)
        base = int(match.group(2))
        result = int(number_part,base)
        return result
    except ValueError:
        return None

def desyatkovuy_to_arbitrary(number, base):
    base = input("Введіть основу числа:")
    try:
        if base < 2 or base > 16:
            raise ValueError("Основа системи числення повинна бути в діапазоні від 2 до 16.")
        if number == 0:
            return "0"
        digits = "0123456789ABCDEF"
        result = ""
        while number > 0:
            result = digits[number % base] + result
            number //= base
        return result
    except ValueError:
        return None
    
def is_integer(number):
    try:
        int(number) 
        return True
    except ValueError:
        return False


def convertaciya():
    while True:
        number = input("Введіть число:")

        if number.startswith("0b"):
            system = input("В яку систему числення хочете перевести(hex,decimal,arbitrary):")
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
            elif system == "arbitrary":
                desyatkove = bit_to_desyatkovuy(number)
                arbitrary = desyatkovuy_to_arbitrary(desyatkove)
                if number is not None:
                    changed_number = print(f"Число у вигляді довільного числення: {arbitrary}")
                else:
                    changed_number = print("Введено неправильно двійкове число.")

        elif number.startswith("0x"):
            system = input("В яку систему числення хочете перевести(bit,decimal,arbitrary):")
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
            elif system == "arbitrary":
                desyatkove = hexadecimal_to_desyatkovuy(number)
                arbitrary = desyatkovuy_to_arbitrary(desyatkove)
                if number is not None:
                    changed_number = print(f"Число у вигляді довільного числення: {arbitrary}")
                else:
                    changed_number = print("Введено неправильно шістнадцяткове число.")

        checking_intenger = is_integer(number)
        if checking_intenger == True:
            try:
                desyatkove = int(number)
                system = input("В яку систему числення хочете перевести(bit,hex,arbitrary):")
                if system == "hex":
                    hexadecimal = desyatkovuy_to_hex(number)
                    changed_number = print(f"Число у шістнадцятковом вигляді: {hexadecimal}")
                elif system == "bit":
                    bit = desyatcovuy_to_bit(number)
                    changed_number = print(f"Число у двійковому вигляді: {bit}")
                elif system == "arbitrary":
                    arbitrary = desyatkovuy_to_arbitrary(desyatkove)
                    if number is not None:
                        changed_number = print(f"Число у вигляді довільного числення: {arbitrary}")
            except ValueError:
                changed_number = print("Введено неправильно десяткове число.")
        
        else:
            try:
                system = input("В яку систему числення хочете перевести(bit,hex,decimal):")
                desyatkove = arbitrary_to_desyatkovuy(number)
                if number is not None:
                    if system == "hex":
                        hexadecimal = desyatkovuy_to_hex(desyatkove)
                        changed_number = print(f"Число у шістнадцятковом  вигляді: {hexadecimal}")
                    elif system == "bit":
                        bit = desyatcovuy_to_bit(bit)
                        changed_number = print(f"Число у двійковому вигляді: {bit}")
                    elif system == "decimal":
                        changed_number = print(f"Число у десятковому вигляді: {desyatkove}")
            except ValueError:
                changed_number = print("Введено неправильно довільне число.")
    
                    
        repeat = input("Перевести ще якесь число? (так/ні): ").strip().lower()
        if repeat == 'ні':
            print("Робота завершена.")
            break


convertaciya()
