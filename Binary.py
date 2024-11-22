def desyatcovuy_to_bit(number) :
    result = bin(int(number))
    return result

def bit_to_desyatkovuy(number):
    bit = number
    try:
        result=int(bit, 2)
        return result
    except ValueError:
        return None

def convertaciya():
    while True:
        number = input("Введіть число:")

        if number.startswith("0b"):
            desyatkove = bit_to_desyatkovuy(number)
            if number is not None:
                changed_number = print(f"Число у десятковому вигляді: {desyatkove}")
            else:
                changed_number = print("Введено неправильно двійкове число.")

        else:
            try:
                desyatkove = int(number)
                bit = desyatcovuy_to_bit(number)
                changed_number = print(f"Число у двійковому вигляді: {bit}")
            except ValueError:
                changed_number = print("Введено неправильно десяткове число.")

        repeat = input("Перевести ще якесь число? (так/ні): ").strip().lower()
        if repeat == 'ні':
            print("Робота завершена.")
            break

convertaciya()
