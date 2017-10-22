import struct

in_file = "helloWorld.bin" #add your source file here
out_file = "helloWorld.csv" #add your target file here

block_len = 512     #Block length
lines_per_block = 7
line_len = 68       #Length of each data row
h = 8               #Length of line header 
col_per_line = 16   #No. of columns or data elements on each line
fmt = 'i'           #Datatype
data_size = struct.calcsize(fmt)
lines = 1

with open(in_file, "rb") as binary_file:
    print("Converting file..")
    f = open(out_file, 'a')
    binary_file.seek(0,2)
    fsize = binary_file.tell()
    print("File size is: %d" %(fsize))
    blocks = fsize/block_len
    print("Blocks to process : %d" %(blocks))
    for x in range(int(blocks)):    
        for y in range(lines_per_block):
            binary_file.seek((y*line_len)+(x*block_len)+h) #Go to beginning of each line, skip header
            for z in range(col_per_line):
                data_tup = struct.unpack(fmt, binary_file.read(data_size))
                data = str(data_tup[0])
                f.write(data)
                if z < col_per_line - 1:
                    f.write(",")
            f.write("\n")
            lines = lines + 1
    print("Ready, total rows: %d" %(lines))
    print("Total recording time @100hz in hours: %f" % (((lines/100)/60)/60))
    f.close()
