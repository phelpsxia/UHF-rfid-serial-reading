#pip3 install pyserial
import serial

def max_count(lt):
    d = {}
    max_key = None
    for i in lt:
        if i not in d:
            count = lt.count(i)
            d[i] = count
            if count > d.get(max_key, 0):
                max_key = i
   
    return max_key

def readtag(port): #port:"/dev/ttyUSB0"
    ser=serial.Serial(port, 9600)
    ser.bytesize = 8
    ser.parity = 'N'
    ser.stopbits = 1
    ser.timeout = 0.5
    print (ser.name)
    count = 0
    r = [0,0,0,0,0]

    while True:
        data = ser.readline() 
        if data != b'':  #sample aa0014008e1000010100 e2000016740601060830c9ac 7c ,  e2000016740601060830c9ac is valid part
            d = str(data.hex())
            #print("length", len(d))
            if len(d) == 46:
                index = d.find("e20000")
                result = d[index:index+24]
                print("tagID:",result)
                r[count] = result
                count = count + 1
                if count == 5:
                    result = max_count(r)
                    print(result)

                    return result
        

if __name__ == "__main__":
    readtag("/dev/ttyUSB0")