def draw(canX,canY,char,data):
    itr=0
    data=list(data)
    for i in range(canY):
        for j in range(canX):
            if data[itr]=="1":
                print(char,end="")
            else:
                print(" ",end="")
            itr=itr+1
        print("")
widths=[5,3,9]
heights=[8,4,8]
datas=["0111001010011100010011111001000101010001","101000101010","001000010011000110000000000100000010010000001011000101010111001100000010"]
names=["Man","Smiley","Eating"]

while True:
    print("Which piece would you like to view? (There are"    ,len(datas),"pieces) ")
    piece=int(input())
    piece=piece-1
    print("")
    draw(widths[piece],heights[piece],"#",datas[piece])
    print(names[piece])
    print("")
