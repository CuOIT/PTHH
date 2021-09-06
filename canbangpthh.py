import re
import matran as mt
import numpy as np
def mahoa(chat):
    while ")" in chat:
        nhom=re.search("[(]([^()]+)[)]",chat)
        heso=re.findall("[)]([0-9]+)",chat)
        lnhom=list(chat)
        ma=lnhom[nhom.start()+1:nhom.end()-1]*int(heso[0])
        lnhom=lnhom[:nhom.start()]+ma+lnhom[nhom.end()+1:]
        chat="".join(lnhom)
    if chat[-1].isalpha():
        chat=chat+'1'
    a=re.search("[A-Z][a-z]*[A-Z]",chat)
    while a!=None:
        chat=chat[:a.end()-1]+'1'+chat[a.end()-1:]
        a=re.search("[A-Z][a-z]*[A-Z]",chat)
    nhom=re.findall("[A-Z][a-z]*",chat)
    heso=re.findall("[0-9]+",chat)
    chat=""
    for i in range(len(nhom)):
        chat=chat+nhom[i]*int(heso[i])
    return chat
def canbang(pthh):
    pthh=pthh.replace(" ","")
    nguyento=list(set(re.findall("[A-Z][a-z]*",pthh)))
    nguyento.sort(reverse=True)
    pthh=pthh.split("=")
    thamgia=pthh[0].split("+")
    sanpham=pthh[1].split("+")
    chat=thamgia.copy()+sanpham.copy()
    chatmahoa=[]
    for x in chat:
        x=mahoa(x)
        chatmahoa.append(x)
    matrix=[]
    for i in range(len(nguyento)):
        lst=[]
        for j in range(len(chat)):
            lst.append(chatmahoa[j].count(nguyento[i]))
            chatmahoa[j]=chatmahoa[j].replace(nguyento[i],"")
            if j>=len(thamgia):
                lst[j]*=-1
        lst.append(0)
        matrix.append(lst)
    lst=[]
    for i in range(len(chat)+1):
        if i==0 or i==(len(chat)) :
            lst.append(1)
        else: 
            lst.append(0)
    matrix.append(lst)
    bt=mt.bacthang(matrix)
    no=mt.giai(bt)
    kq=""
    for i in range(len(chat)):
        if no[i]!=1:
            kq=kq+str(no[i])
        kq=kq+chat[i]
        if i==len(thamgia)-1:
            kq+="="
        else:
            if i!=len(chat)-1:
                kq+="+"
    return kq

