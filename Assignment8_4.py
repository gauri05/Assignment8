print("Accept string display no. of small,capital and digit....")
import threading


def small(str):
    cnt = 0
    for i in range(0, len(str)):
        #print("letter", str[i])
        if ((str[i]>='a')&(str[i]<='z')):
        #if 65 < ord(str[i]) & (90 > ord(str[i])):
            cnt += 1
    print("Small letter count==>", cnt)


def capital(str):
    cnt = 0
    for i in range(0, len(str)):
        #print("letter", str[i])
        if ((str[i]>='A')&(str[i]<='Z')):
            cnt += 1
    print("Capital letter count==>", cnt)


def digit(str):
    cnt = 0
    for i in range(0, len(str)):
        #print("letter", str[i])
        if(str[i].isdigit()):
            #print(str[i])
            cnt += 1
    print("Digit letter count==>", cnt)


def main():
    str = input("Enter String")
    thread1 = threading.Thread(target=small, args=(str,))
    thread2 = threading.Thread(target=capital, args=(str,))
    thread3 = threading.Thread(target=digit, args=(str,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    main()
