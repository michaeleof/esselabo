from web3 import Web3

def cprint(text, color='white', attrs=[]):
    """
    Prints text in color to the console.

    Args:
        text (str): The text to print.
        color (str): The color of the text.
        attrs (list): A list of attributes to apply to the text.
    """
    colors = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
    }
    attributes = {
        'bold': '1',
        'underline': '4',
        'blink': '5',
        'reverse': '7',
        'concealed': '8',
    }
    color_code = colors.get(color, '37')
    attr_codes = [attributes.get(attr, '0') for attr in attrs]
    print(f'\033[{";".join(attr_codes)};{color_code}m{text}\033[0m')

w3 = Web3(Web3.HTTPProvider('https://www.example.com = '0x43852e61161c1c73c458f467909827824704241c154c35373f38437201a551c9'
cprint(f'\n>>> stake LP | https://www.example.com ', 'green')
