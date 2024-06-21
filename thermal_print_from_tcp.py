# DEBUGGING NOTES
# start pc
# run dirver installer -> "modify" or "remove" then install again
# in VS code, change python interpreter ctrl+shift+p, then select interpreter in C/python39
# need to find port address/name of printer, use serial.tools to search
# instead of usb, use Serial to define printer


from escpos.printer import Serial
from serial.tools import list_ports
import socket
from datetime import datetime

def printme(mytext):
    max_char_per_line = 48

    try:
        p.text("hello")
    except Exception as E:
        print (E)

if __name__ == "__main__":
    for port in list_ports.comports():
        if "USB" in port.hwid:
            print(f"Name: {port.name}")
            print(f"Description: {port.description}")
            print(f"Location: {port.location}")
            print(f"Product: {port.product}")
            print(f"Manufacturer: {port.manufacturer}")
            print(f"ID: {port.pid}")
            if port.description.startswith("Prolific"):
                printerName = port.name
                print("setting printer...")

try:
    p = Serial(devfile=printerName,
            baudrate=9600,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1.00,
            dsrdtr=True)
    print("printer set %s" % p.paper_status)
    p.text("ALQUIMIA " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "\n")

except Exception as E:
    print(E)



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
#print (sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print(client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received %s' % data)
            if data:
                max_char_per_line = 48

                dataReceived = float(str.split(data.decode("utf-8"))[0])
                val = int(dataReceived / 5)
                
                #print(val)
                textToPrint = ("_" * val) + "\n"
                
                print(textToPrint)
                p.text(textToPrint)
                
            else:
                print('no more data from')
                break
            
    finally:
        # Clean up the connection
        connection.close()
        p.close()
