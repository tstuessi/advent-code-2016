# Part 1 of day 5 of advent of code
#
# Finding Collisions
# Tyler Stuessi

from hashlib import md5

def find_collisions(door_id, password_len):
    code = ""
    index = 0
    while len(code) < password_len:
        x = md5((door_id + str(index)).encode("ascii")).digest().hex()
        if x.startswith("00000"):
            code += x[5]
        index += 1

    return code

if __name__ == "__main__":
    print(find_collisions("abbhdwsy", 8))

