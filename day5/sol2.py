# Part 1 of day 5 of advent of code
#
# Finding Collisions
# Tyler Stuessi

from hashlib import md5

def find_collisions(door_id, password_len):
    code = ["-1"] * 8
    index = 0
    ctr = 0
    while ctr < password_len:
        x = md5((door_id + str(index)).encode("ascii")).digest().hex()
        if x.startswith("00000"):
            if x[5].isdigit() and int(x[5]) < len(code) and code[int(x[5])] == "-1":
                code[int(x[5])] = x[6]
                ctr += 1
        index += 1

    return code

if __name__ == "__main__":
    print(find_collisions("abbhdwsy", 8))

