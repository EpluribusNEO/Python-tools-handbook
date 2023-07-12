import subprocess


def ip_to_dec(a,b,c,d):
    return a*pow(256,3) + b*pow(256,2) + c*pow(256,1) + d*pow(256,0)

def ip_dec_to_tetrads(numb: int) -> str:
    bin_numb_arr = '{0:032b}'.format(numb)
    octets_bit = ['0'*8, '0'*8, '0'*8, '0'*8]
    octets_dec = [0,0,0,0]

    octets_bit[0] = bin_numb_arr[0:8]
    octets_bit[1] = bin_numb_arr[8:16]
    octets_bit[2] = bin_numb_arr[16:24]
    octets_bit[3] = bin_numb_arr[24:33]

    octets_dec[0] = int(octets_bit[0], 2)
    octets_dec[1] = int(octets_bit[1], 2)
    octets_dec[2] = int(octets_bit[2], 2)
    octets_dec[3] = int(octets_bit[3], 2)

    return "{0}.{1}.{2}.{3}".format(octets_dec[0], octets_dec[1], octets_dec[2], octets_dec[3])


def show_wifi_network():
    result = subprocess.check_output(["netsh", "wlan", "show", "network"])
    result = result.decode("ascii", errors="ignore")
    result = result.replace("\r", "")
    ls = result.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    print(ssids)


if __name__ == "__main__":
    print("This is the file of the plug-in library (module). \nShould not be used as the main")
