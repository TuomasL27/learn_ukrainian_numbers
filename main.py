import random

ukr = ["Нуль", "Один", "Два", "Три", "Чостири", "П'ять", "Шість", "Сім", "Вісім", "Дев'ять", "Десять"]
eng = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]


def main():
    results = []
    while 1:
        print(
            f"\033[1;36mWhat is \033[1;31m{ukr[(x := random.randint(0, len(ukr) - 1))].lower()}\033[1;36m in english?")
        usr = input("\033[1;31m> \033[1;32m")
        if usr.lower() == eng[x] or usr.lower() == str(x):
            results.append(1)
            print(f"\033[1;32mCorrect \033[1;36m| Your accuracy is {sum(results) / len(results) * 100}")
        else:
            results.append(0)
            print(f"\033[0;31mIncorrect \033[1;36m| Your accuracy is {sum(results) / len(results) * 100}")


if __name__ == "__main__":
    main()

