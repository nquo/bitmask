
import sys

input_filename = 'input.txt'
output_filename = 'output.txt'

def str2bit(value):
    value = int("0x{}".format(value), 16)
    return "{:032b}".format(value)

def find_index(data, counter=0):
    hex_str = "0x{}".format(data)
    found_positions = []
    value = int(hex_str, 16)
    bits = list("{:032b}".format(value))
    for bit in bits[::-1]:
        if int(bit) == 1:
            found_positions.append(counter)
        counter += 1
    print("{}\t{}".format(hex_str, found_positions))
    return counter

if __name__ == '__main__':
    orig_stdout = sys.stdout
    f = open(output_filename, "w+")
    try:
        sys.stdout = f
        with open(input_filename, 'r') as reader:
            file_content = reader.read()
            values = file_content.split()
            bitmasks = [index for index in values[::-1]]
            current_index = 0
            for bitmask in bitmasks:
                current_index = find_index(bitmask, current_index)

        sys.stdout = orig_stdout
    finally:
        f.close()
