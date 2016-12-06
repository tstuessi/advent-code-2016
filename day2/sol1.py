# Part 1 on day 2 on advent of code
#
# Tyler Stuessi

def get_bathroom_code(rows, columns):
    # get input

    code = ""

    keypaths = []
    try:
        while True:
            raw = input()
            keypaths.append(raw)
    except EOFError:
        pass

    num = 5
    for path in keypaths:
        for c in path:
            if c == "L" and num % columns != 1:
                num -= 1
            elif c == "U" and (num-1) // columns != 0:
                num -= columns
            elif c == "D" and (num-1) // columns != rows - 1:
                num += columns
            elif c == "R" and num % columns != 0:
                num += 1
        code += str(num)

    return code


if __name__ == "__main__":
    print(get_bathroom_code(3, 3))
