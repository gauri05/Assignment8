print("Mutithreadin evenfactors oddfactors....")
import threading


def evenfactors(no):
    ans=0
    for i in range(1, no):
        if ((i % 2) == 0):
            ans=ans+i
    print ("evenfactors", ans)


def oddfactors(no):
    ans=0
    for i in range(1, no):
        if ((i % 2) != 0):
            ans = ans + i
    print ("oddfactors",ans)


def main():
    no = 10
    thread1 = threading.Thread(target=evenfactors, args=(no,))
    thread2 = threading.Thread(target=oddfactors, args=(no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    #print (thread1.status())
    #return thread1
    #if thread1
    print ("exit from main")


if __name__ == "__main__":
    main()
