import re


def palindrome(l: list):
    
    size = len(l) - 1
    for i in range(len(l) // 2):
        if l[i] != l[size - i]:
            return False

    return True


def main():
    nb = 0
    for i in range(int(input())):
        entry = input()
        if not palindrome(re.findall(r"[0-9]", entry)):
            continue
        if not palindrome(re.findall(r"[a-z]", entry)):
            continue
        elif not palindrome(re.findall(r"[A-Z]", entry)):
            continue
        nb += 1

    return nb
    # print(nb)


if __name__ == "__main__":
    main()
