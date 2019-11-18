print("Mutithreading ===>thread scheduling....")
import threading
import sched

no = 50


def counter(fun, lock):
    fun(lock)


def order(lock):
    # global no
    # no = int(input("Enter number"))
    lock.acquire()
    for i in range(1, no + 1):
        print("ordered", i)
    lock.release()


def reverse(lock):
    global no
    # no = int(input("Enter number rev"))
    lock.acquire()
    while no > 0:
        print("reverse", no)
        no = no - 1
    lock.release()


def main():
    lock = threading.Lock()
    thread1 = threading.Thread(target=counter, args=(order, lock,))
    thread2 = threading.Thread(target=counter, args=(reverse, lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
