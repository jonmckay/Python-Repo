'''
Created on Apr 19, 2017

@author: jmckay
'''
def rgb_hex():
    invalid_msg = 'Invalid value entered'
    red = int(raw_input('Enter a value for red: '))
    if red < 0 or red > 255:
        print invalid_msg
        return
    green = int(raw_input('Enter a value for green: '))
    if green < 0 or green > 255:
        print invalid_msg
        return
    blue = int(raw_input('Enter a value for blue: '))
    if blue < 0 or blue > 255:
        print invalid_msg
        return
    val = (red << 16) + (green << 8) + blue
    value = hex(val).upper()
    print value[2:]

def hex_rgb():
    hex_val = raw_input('Enter a hexadecimal value: ')
    if len(hex_val) != 6:
        print 'Invalid hex value entered'
        return
    else:
        hex_val = int(hex_val, 16)
        two_hex_digits = 2 ** 8
        blue = hex_val % two_hex_digits
        hex_val << 8
        green = hex_val % two_hex_digits
        hex_val << 8
        red = hex_val % two_hex_digits
        print '%s%s%s' % (red, green, blue)

def convert():
    while(True):
        option = raw_input('Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ')
        if option == '1':
            print 'RGB to Hex...'
            rgb_hex()
        elif option == '2':
            print 'Hex to RGB...'
            hex_rgb()
        elif option == 'X' or option == 'x':
            break
        else:
            print 'Error'
      
convert()