from network_tools import ip_to_dec, ip_dec_to_tetrads
from network_tools import show_wifi_network

def help():
    print(f"Options:\n 0: help\n 1: IP to decemal format"+
          "\n 2: IP in decemal format to octets" +
          "\n 3: show Wi-Fi networks" +
          "\n99: to exit")

if __name__ == '__main__':
    help()
    while(True):
        option = int(input(":>"))
        if(option == 0):
            help()
        elif (option == 1):
            print("Convert IP-addres to decimal format.")
            print("Enter Ip-addres: First.Second.Third.Fourth:")
            a = int(input("First:> "))
            b = int(input("Second:> "))
            c = int(input("Third:> "))
            d = int(input("Fourth:> "))
            ipdec = ip_to_dec(a, b, c, d)
            print("{0}.{1}.{2}.{3}  --> {4}".format(a, b, c, d, ipdec))
        elif (option == 2):
            numb = int(input("enter IP in decemal format :>"))
            print("{0} --> {1}".format(numb, ip_dec_to_tetrads(numb)))
        elif (option == 3):
            show_wifi_network()
        elif (option == 99):
            break
        else:
            print("!_[WARNING]: wrong command!\n!_[INFO]: Use command '0' to show hints.")

    print("end of line")	
