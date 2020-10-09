from logic import *

if __name__ == '__main__':
    queue_a = Queue()
    queue_b = Queue()
    queue_c = Queue()

    while True:

        type = input("""Pobierz numer:
A - rejestracja pojazdów
B - prawa jazdy
C - dowody osobiste
""")
        clr()
        if type == 'A' or type == 'a':
            print('Twój numer to: A', queue_a.add_number())
            time.sleep(5)
        elif type == 'B' or type == 'b':
            print('Twój numer to: B', queue_b.add_number())
            time.sleep(5)
        elif type == 'C' or type == 'c':
            print('Twój numer to: C', queue_c.add_number())
            time.sleep(5)
        elif type == 'Quit' or type == 'quit':
            break
        elif type == 'haslo1':
            magic = input("""Z której kolejki chcesz skorzystać?:
A - rejestracja pojazdów
B - prawa jazdy
C - dowody osobiste
""")
            clr()
            if magic == 'A' or magic == 'a':
                print('Twój numer to: A', queue_a.add_number())
                time.sleep(5)
            if magic == 'B' or magic == 'b':
                print('Twój numer to: B', queue_b.add_number())
                time.sleep(5)
            if magic == 'C' or magic == 'c':
                print('Twój numer to: C', queue_c.add_number())
                time.sleep(5)

        else:
            print('Zły numer! Podaj jeszcze raz!')