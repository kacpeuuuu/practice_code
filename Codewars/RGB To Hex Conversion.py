"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
Examples (input --> output):

255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""

numbers_in_hex = {
        0:"0",
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"A",
        11:"B",
        12:"C",
        13:"D",
        14:"E",
        15:"F"
    }

def dec_to_hex(x):
    final_str = ""
    if x > 255:
        x = 255
    elif x < 0:
        x = 0

    while x != 0:
        number = x % 16
        final_str += str(numbers_in_hex[number])
        x = x // 16


    final_str = final_str[::-1]
    print(final_str)
    
    return final_str.rjust(2, '0')

def rgb(r,g,b):
    return dec_to_hex(r) + dec_to_hex(g) + dec_to_hex(b)

print(rgb(1,2,3))