import time
import serial
import struct
ser = serial.Serial(
   port     = '/dev/ttyUSB0',
   baudrate = 115200,
   parity   = serial.PARITY_EVEN,
   stopbits = serial.STOPBITS_ONE,
   bytesize = serial.EIGHTBITS,
   timeout  = 2
)
while True:

   data = ser.readline()
   print("Rasberry's receiving:",data)
   data1 = bytes.hex(data)
   offset = 6
   i = offset + 1
   j = 0
   k = 0
   data2 = tuple()
   b = tuple()
   while(j < len(data1)+1):
       data2 = data2 + (data1[j:(j+2)],)
       j = j + 2
   print(data2)
   if data2[k] == (''):
       k = k + 1
       print("du lieu trong")
####################################################
   else:
       while i < (len(data2) - 5):
           data_temp = data2[(i+2):(i+4)] + data2[i:(i+2)]
           reversed_data = ' '.join(data_temp)
           byte_array = bytes.fromhex(reversed_data)
           a = struct.unpack('!f',byte_array)
           b = b + (a,)

#
   print(b)


   class paper:
       loaipaper = "Voltage"
       def __init__(seft,params, b, unit):
           seft.params = params
           seft.b = b
           seft.unit = unit
       i = i + 4
Voltage_A = paper("Voltage ", b[1], "V")
Voltage_B = paper("Voltage ", b[2], "V")
Voltage_C = paper("Voltage ", b[3], "V")
Voltage_D = paper("Voltage ", b[4], "V")
# print("Dien ap A la {}.".format(Dien_ap_A.__class__.typepaper))
print("Voltage A is {}with value = {} {} ".format(Voltage_A.name, Voltage_A.b, Voltage_A.unit))
print("Voltage B is {}with value = {} {} ".format(Voltage_B.name, Voltage_B.b, Voltage_B.unit))
print("Voltage C is {}with value = {} {} ".format(Voltage_C.name, Voltage_C.b, Voltage_C.unit))
print("Voltage D is {}with value = {} {} ".format(Voltage_D.name, Voltage_D.b, Voltage_D.unit))