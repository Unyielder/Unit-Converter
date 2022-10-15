from unit_converter import UnitConverter


def new_conversion() -> bool:
    while True:
        val = input('New conversion? (y/n) \n')
        if val.lower() == 'y':
            return True
        elif val.lower() == 'n':
            return False
        else:
            print("Sorry, I don't understand")


def console() -> None:
    while True:
        input_val = input('Enter input value and unit (ex: 10 ml) \n')
        output_unit = input('Enter desired conversion unit \n')
        num, unit = input_val.split(' ')

        converter = UnitConverter()
        converted_value = converter.convert(float(num), unit, output_unit)
        print('Converted value:', converted_value, output_unit)

        answer = new_conversion()
        if answer:
            continue
        else:
            break


if __name__ == '__main__':
    console()
