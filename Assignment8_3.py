print("Mutithreadin evenlist oddlist....")
import threading


def evenlist(no):
    ans=0
    #print (len(no))
    for i in range(0,int(len(no))):
        if((int(no[i])%2)==0):
            #print ("even",no[i])
            ans=ans+int(no[i])
    print ("even",ans)

def oddlist(no):
    #print (no)
    ans=0
    for i in range(0, int(len(no))):
        if (int(no[i]) % 2) != 0:
            #print ("even", no[i])
            ans = ans + int(no[i])
    print ("odd",ans)


def main():
    inputlist=list();
    no = list(input("Enter elements"))
    thread1 = threading.Thread(target=evenlist, args=(no,))
    thread2 = threading.Thread(target=oddlist, args=(no,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
