print("Mutithreadin even odd....")
import threading


def even(no):
    for i in range(1, no):
        if ((i % 2) == 0):
            print ("even",i)


def odd(no):
    for i in range(1, no):
        if ((i % 2) != 0):
            print ("odd",i)


def main():
    no = 10
    thread1 = threading.Thread(target=even, args=(no,))
    thread2 = threading.Thread(target=odd, args=(no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
