import canbangpthh as cb
#fhand=input("Nhap link file cua ban:")
fhand=r"C:\Users\SNC\Desktop\CODE\Python Code\pthh12.txt"
f=open(fhand,"r",encoding="utf-8")
line=f.read().split("\n")
for i in range(len(line)):
    if len(line[i])!=0:
        line[i]=line[i].replace(" ","")
        print("%40s%s%s"%(line[i],"     ---->     ",cb.canbang(line[i])))
