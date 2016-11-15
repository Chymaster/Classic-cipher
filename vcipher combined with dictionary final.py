# to use further fuctions, it's :
#98 to reset the code
#99 to reset the lists
#100 to autorun dictionarys on caiser shift
from collections import Counter
import time
global possible
possible = 0
global anscode
anscode = []
global wherethe
wherethe = ['the']
global wherebe
wherebe = ['be']
global wherejamelia
wherejamelia = ['jamelia']
global wherelike
wherelike = ['like']
global wherethis
wherethis = ['this']
global whereis
whereis = ['is']
global wheregravity
wheregravity = ['gravity']
global whereyou
whereyou = ['you']
global oucode
oucode = []
global upass
upass = []
global oupass
oupass = []
global gcd
gcd = 0
repeat1= []
repeat2 = []
repeat3 = []
repeat4 = []
repeat5 = []
reploc = []
uword = []
cache3 = ['0','0','0']#cache with three digit
rep3 = []
rep4 = []
rep5 = []
cache4 = ['0','0','0','0']
cache5 = ['0','0','0','0','0']
def code(ucode):
    for individualc in ucode:    #individualc for individuals in code
        upass.append(ord(individualc)- 96)
        oupass.append(ord(individualc) - 96)
        uword.append(individualc)
        oucode.append(individualc)
def shift():       #everything in the list +1
    numn = 0     #numn for loops in shift
    nums = 0
    count = 0
    lenlist = len(upass) - 1
    while lenlist >= 0 : # select range, make sure it don't overflow
        upass[lenlist] = int(upass[lenlist] + 1)   #every letter rotate one
        lenlist = lenlist - 1 # time done +1
    for individualn in upass:  #if one number goes over z, it will start again
        if individualn >= 27:
            upass[numn] = int(individualn - 26)
        numn = numn + 1
    for individuals in upass:  # put the arranged number into another list that has string
        uword[count]=(chr(individuals + 96))
        count = count + 1
def vcipher1():
    loca = 0
    reapt1 = 0
    while reapt1 <= len(upass)-1:  #reapt1 = which letter in text
        if (chr(upass[reapt1]+96) in repeat1) == False:
            reapt2 = reapt1 + 1   #reapt2 = which letter to try
            repeat1.append(chr(upass[reapt1]+96))  #every letter in list before it's result
            repeat1.append(reapt1+1) #where the first letter is
            while reapt2 <= len(upass)- 1:
                if upass[reapt1] == upass[reapt2]:
                    repeat1.append(reapt2+1)
                    consequence = True# to show working
                else:
                    consequence = False
                #print(chr(upass[reapt1]+97),chr(upass[reapt2]+97),consequence)# show working ends here
                reapt2 = reapt2 + 1
        reapt1 = reapt1 + 1
    print(Counter(uword))
    print('Location',repeat1)
def vcipher3():
    v3num = 0
    loca = 0
    reapt1 = 0
    x = 0 #
    while v3num <= (len(uword) - 3): #cache to store the first three letters to let be in the next step
        cache3[0] = uword[v3num]
        cache3[1] = uword[v3num+1]
        cache3[2] = uword[v3num+2]
        rep3.append(''.join(cache3))
        v3num = v3num + 1
    while reapt1 <= len(rep3) - 1:
        x = x + 1#
        print(x)#
        if(rep3[reapt1] in repeat3) == False:
            reapt2 = reapt1 + 1
            repeat3.append(rep3[reapt1])
            repeat3.append(reapt1 + 1)
            while reapt2 <= len(rep3) - 1:
                if rep3[reapt1] == rep3[reapt2]:
                    repeat3.append(reapt2 + 1)
                    print(reapt2 + 1)
                    reploc.append(reapt2 - reapt1)
                    consequence = True
                else:
                    consequence = False
                #print(rep3[reapt1],rep3[reapt2],consequence)
                reapt2 = reapt2 + 1
        reapt1 = reapt1 + 1
    print(Counter(rep3))
    print('Location',repeat3)
def vcipher4():
    v4num = 0
    loca = 0
    reapt1 = 0
    x = 0 #
    while v4num <= (len(uword) - 4):
        cache4[0] = uword[v4num]
        cache4[1] = uword[v4num+1]
        cache4[2] = uword[v4num+2]
        cache4[3] = uword[v4num+3]
        rep4.append(''.join(cache4))
        v4num = v4num + 1
    while reapt1 <= len(rep4) - 1:
        x = x + 1#
        print(x)#
        if(rep4[reapt1] in repeat4) == False:
            reapt2 = reapt1 + 1
            repeat4.append(rep4[reapt1])
            repeat4.append(reapt1 + 1)
            while reapt2 <= len(rep4) - 1:
                if rep4[reapt1] == rep4[reapt2]:
                    repeat4.append(reapt2 + 1)
                    print(reapt2 + 1)
                    reploc.append(reapt2 - reapt1)
                    consequence = True
                else:
                    consequence = False
                #print(rep4[reapt1],rep4[reapt2],consequence)
                reapt2 = reapt2 + 1
        reapt1 = reapt1 + 1
    print(Counter(rep4))
    print('Location',repeat4)
def vcipher5():
    v5num = 0
    loca = 0
    reapt1 = 0
    x = 0 #
    while v5num <= (len(uword) - 5):
        cache5[0] = uword[v5num]
        cache5[1] = uword[v5num+1]
        cache5[2] = uword[v5num+2]
        cache5[3] = uword[v5num+3]
        cache5[4] = uword[v5num+4]
        rep5.append(''.join(cache5))
        v5num = v5num + 1
    while reapt1 <= len(rep5) - 1:
        x = x + 1#
        print(x)#
        if(rep5[reapt1] in repeat5) == False:
            reapt2 = reapt1 + 1
            repeat5.append(rep5[reapt1])
            repeat5.append(reapt1 + 1)
            while reapt2 <= len(rep5) - 1:
                if rep5[reapt1] == rep5[reapt2]:
                    repeat5.append(reapt2 + 1)
                    print(reapt2 + 1)
                    reploc.append(reapt2 - reapt1)
                    consequence = True
                else:
                    consequence = False
                #print(rep5[reapt1],rep5[reapt2],consequence)
                reapt2 = reapt2 + 1
        reapt1 = reapt1 + 1
    print(Counter(rep5))
    print('Location',repeat5)
def revers():
    uword.reverse()
    upass.reverse()
    print(uword)
def the():
    numthe = 0
    while numthe <= len(upass) - 3:
        if upass[numthe] == 20 and upass[numthe + 1] == 8 and upass[numthe + 2] == 5:
            wherethe.append(numthe+1)
            global possible
            possible = possible + 1
        numthe = numthe + 1
def be():
    numbe = 0
    while numbe <= (len(upass) - 2):
        if upass[numbe] == 2 and upass[numbe + 1] == 5:
            wherebe.append(numbe+1)
        numbe = numbe + 1
def jamelia():
    numjamelia = 0
    while numjamelia <= len(upass) - 7:
         if upass[numjamelia] == 10 and upass[numjamelia + 1] == 1 and upass[numjamelia + 2] == 13 and upass[numjamelia + 3] == 5 and upass[numjamelia+4] == 12 and upass[numjamelia+5] == 9 and upass[numjamelia + 6] == 1:
            wherejamelia.append(numjamelia+1)
            global possible
            possible = possible + 1
         numjamelia = numjamelia + 1
def like():
    numlike = 0
    while numlike <= len(upass) - 4:
         if upass[numlike] == 12 and upass[numlike + 1] == 9 and upass[numlike + 2] == 11 and upass[numlike + 3] == 5:
            wherelike.append(numlike+1)
            global possible
            possible = possible + 1
         numlike = numlike + 1
def this():
    numthis = 0
    while numthis <= len(upass) - 4:
        if upass[numthis] == 20 and upass[numthis + 1] == 8 and upass[numthis + 2] == 9 and upass[numthis + 3] == 19:
            wherethis.append(numthis+1)
            global possible
            possible = possible + 1
        numthis = numthis + 1
def gravity():
    numgravity = 0
    while numgravity <= len(upass)- 7:
        if upass[numgravity] == 7 and upass[numgravity + 1] == 18 and upass[numgravity + 2] == 1 and upass[numgravity + 3] == 22 and upass[numgravity + 4] == 9 and upass[numgravity + 5] == 20 and upass[numgravity + 6] == 25:
            wheregravity.append(numgravity + 1)
            global possible
            possible = possible + 1
        numgravity = numgravity + 1
def deis():   # deis stand for detect is
    numdeis = 0
    while numdeis <= len(upass) - 2:
        if upass[numdeis] == 9 and upass[numdeis + 1] == 19:
            whereis.append(numdeis + 1)
        numdeis = numdeis  + 1
def you():
    numyou = 0
    while numyou <= len(upass) - 3:
        if upass[numyou] == 25 and upass[numyou + 1] == 15 and upass[numyou + 2] == 21:
            whereyou.append(numyou + 1)
            global possible
            possible = possible + 1
        numyou = numyou + 1
def diction():
    rangep = 10
    global possible
    possible = 0
    the()
    be()
    jamelia()
    like()
    this()
    deis()
    gravity()
    you()
    global possible
    if possible >= rangep:
        global uword
        global upass
        uword = [chr(i + 96) for i in upass]
        anscode = uword
        print(''.join(anscode))
p = input('put the text in there')
code(p)
def password():
    trynum2 = 26
    while trynum2 >> 0:
        diction()
        trynum2 = trynum2 - 1
        shift()
def replace(): 
    n = 0
    global gcd
    gcd = reploc[0]
    b = 0
    l = 0
    while l <= len(reploc) - 1:
        tempa = gcd
        tempb = reploc[l]
        if tempa >> tempb:
            tempa,tempb = tempb,tempa
        while tempb != 0:
            temp = tempa%tempb
            tempa = tempb
            tempb = temp
        l = l + 1
        gcd = tempa
        print(gcd)
def vigen2() :
    vg1 = []
    vg2 = []
    b = 1
    global upass
    for a in upass:      #use b to separate upass into three groups
        if b >= 4:
            b = 1
        if b == 1:
            vg1.append(a)
        elif b == 2:
            vg2.append(a)
        b = b + 1
    print(vg1)
    print(vg2)
    loop1 = 0
    while loop1 <= 25:     #loop on the first list
        vg1 = [i+1 for i in vg1]
        lvg1 = 0
        while lvg1 <= len(vg2) - 1:
            if vg1[lvg1] >= 27:
                vg1[lvg1] = vg1[lvg1] -26
            lvg1 = lvg1 + 1
        loop2 = 0
        #print('loop1')
        loop1 = loop1+1
        print(possible)
        while loop2 <= 25:  # loop on the second list
            vg2 = [i+1 for i in vg2]
            lvg2 = 0
            while lvg2 <= len(vg2) -1:
                if vg2[lvg2] >= 27:
                    vg2[lvg2] = vg2[lvg2] - 26
                lvg2 = lvg2 + 1
            #print('loop2')
                #print('loop3')
            upass = []
            l = 0
            while l <= len(vg1)- 1:   #put back into upass
                if l <= len(vg1)-1:
                        upass.append(vg1[l])
                if l <= len(vg2)-1:
                        upass.append(vg2[l])
                l = l + 1
            diction()
                #print(loop1,loop2,loop3)
            loop2 = loop2 + 1
def vigen3() :
    vg1 = []
    vg2 = []
    vg3 = []
    b = 1
    global upass
    for a in upass:      #use b to separate upass into three groups
        if b >= 4:
            b = 1
        if b == 1:
            vg1.append(a)
        elif b == 2:
            vg2.append(a)
        elif b == 3:
            vg3.append(a)
        b = b + 1
    print(vg1)
    print(vg2)
    print(vg3)
    loop1 = 0
    while loop1 <= 25:     #loop on the first list
        vg1 = [i+1 for i in vg1]
        lvg1 = 0
        while lvg1 <= len(vg1) - 1:
            if vg1[lvg1] >= 27:
                vg1[lvg1] = vg1[lvg1] -26
            lvg1 = lvg1 + 1
        loop2 = 0
        #print('loop1')
        loop1 = loop1+1
        print(possible)
        while loop2 <= 25:  # loop on the second list
            vg2 = [i+1 for i in vg2]
            lvg2 = 0
            while lvg2 <= len(vg2) -1:
                if vg2[lvg2] >= 27:
                    vg2[lvg2] = vg2[lvg2] - 26
                lvg2 = lvg2 + 1
            loop3 = 0
            loop2 = loop2 + 1
            #print('loop2')
            while loop3 <=25:   #loop on the third list
                vg3 = [i+1 for i in vg3]
                lvg3 = 0
                while lvg3 <= len(vg3) -1:
                    if vg3[lvg3] >= 27:
                        vg3[lvg3] = vg3[lvg3] - 26
                    lvg3 = lvg3 + 1
                #print('loop3')
                upass = []
                l = 0
                while l <= len(vg1)- 1:   #put back into upass
                    if l <= len(vg1)-1:
                        upass.append(vg1[l])
                    if l <= len(vg2)-1:
                        upass.append(vg2[l])
                    if l <= len(vg3)-1:
                        upass.append(vg3[l])
                    l = l + 1
                
                diction()
                #print(loop1,loop2,loop3)
                loop3 = loop3 + 1
def vigen4() :
    vg1 = []
    vg2 = []
    vg3 = []
    vg4 = []
    b = 1
    global upass
    for a in upass:      #use b to separate upass into three groups
        if b >= 5:
            b = 1
        if b == 1:
            vg1.append(a)
        elif b == 2:
            vg2.append(a)
        elif b == 3:
            vg3.append(a)
        elif b == 4:
            vg4.append(a)
        b = b + 1
    print(vg1)
    print(vg2)
    print(vg3)
    print(vg4)
    loop1 = 0
    while loop1 <= 25:     #loop on the first list
        vg1 = [i+1 for i in vg1]
        lvg1 = 0
        while lvg1 <= len(vg1) - 1:
            if vg1[lvg1] >= 27:
                vg1[lvg1] = vg1[lvg1] -26
            lvg1 = lvg1 + 1
        loop2 = 0
        #print('loop1')
        loop1 = loop1+1
        print(possible)
        while loop2 <= 25:  # loop on the second list
            vg2 = [i+1 for i in vg2]
            lvg2 = 0
            while lvg2 <= len(vg2) -1:
                if vg2[lvg2] >= 27:
                    vg2[lvg2] = vg2[lvg2] - 26
                lvg2 = lvg2 + 1
            loop3 = 0
            loop2 = loop2 + 1
            #print(loop1,loop2)
            while loop3 <=25:   #loop on the third list
                #print('     ',loop3)
                vg3 = [i+1 for i in vg3]
                lvg3 = 0
                while lvg3 <= len(vg3) -1:
                    if vg3[lvg3] >= 27:
                        vg3[lvg3] = vg3[lvg3] - 26
                    lvg3 = lvg3 + 1
                loop4 = 0
                loop3 = loop3 + 1
                while loop4 <= 25:
                    #print(loop4)
                    vg4 = [i+1 for i in vg4]
                    lvg4 = 0
                    while lvg4 <= len(vg4) - 1:
                        if vg4[lvg4] >= 27:
                            vg4[lvg4] = vg4[lvg4] - 26
                        lvg4 = lvg4 + 1
                    loop4 = loop4 + 1
                    global upass
                    upass = []
                    l = 0
                    while l <= len(vg1)- 1:   #put back into upass
                        global upass
                        if l <= len(vg1)-1:
                            upass.append(vg1[l])
                        if l <= len(vg2)-1:
                            upass.append(vg2[l])
                        if l <= len(vg3)-1:
                            upass.append(vg3[l])
                        if l <= len(vg4)-1:
                            upass.append(vg4[l])
                        l = l + 1
                    diction()
def vigen5() :
    vg1 = []
    vg2 = []
    vg3 = []
    vg4 = []
    vg5 = []
    b = 1
    global upass
    for a in upass:      #use b to separate upass into three groups
        if b >= 6:
            b = 1
        if b == 1:
            vg1.append(a)
        elif b == 2:
            vg2.append(a)
        elif b == 3:
            vg3.append(a)
        elif b == 4:
            vg4.append(a)
        elif b == 5:
            vg5.append(a)
        b = b + 1
    print(vg1)
    print(vg2)
    print(vg3)
    print(vg4)
    print(vg5)
    loop1 = 0
    while loop1 <= 25:     #loop on the first list
        vg1 = [i+1 for i in vg1]
        lvg1 = 0
        while lvg1 <= len(vg1) - 1:
            if vg1[lvg1] >= 27:
                vg1[lvg1] = vg1[lvg1] -26
            lvg1 = lvg1 + 1
        loop2 = 0
        #print('loop1')
        loop1 = loop1+1
        print(possible)
        while loop2 <= 25:  # loop on the second list
            vg2 = [i+1 for i in vg2]
            lvg2 = 0
            while lvg2 <= len(vg2) -1:
                if vg2[lvg2] >= 27:
                    vg2[lvg2] = vg2[lvg2] - 26
                lvg2 = lvg2 + 1
            loop3 = 0
            loop2 = loop2 + 1
            #print(loop1,loop2)
            while loop3 <=25:   #loop on the third list
                #print('     ',loop3)
                vg3 = [i+1 for i in vg3]
                lvg3 = 0
                while lvg3 <= len(vg3) -1:
                    if vg3[lvg3] >= 27:
                        vg3[lvg3] = vg3[lvg3] - 26
                    lvg3 = lvg3 + 1
                loop4 = 0
                loop3 = loop3 + 1
                while loop4 <= 25:
                    #print(loop4)
                    vg4 = [i+1 for i in vg4]
                    lvg4 = 0
                    while lvg4 <= len(vg4) - 1:
                        if vg4[lvg4] >= 27:
                            vg4[lvg4] = vg4[lvg4] - 26
                        lvg4 = lvg4 + 1
                    loop4 = loop4 + 1
                    loop5 = 0
                    while loop5 <= 25:
                        vg5 = [i+1 for i in vg5]
                        lvg5 = 0
                        while lvg5 <= len(vg5) - 1:
                            if vg5[lvg5] >= 27:
                                vg5[lvg5] = vg5[lvg5] - 26
                            lvg5 = lvg5 + 1
                        loop5 = loop5 + 1
                        global upass
                        upass = []
                        l = 0
                        while l <= len(vg1)- 1:   #put back into upass
                            global upass
                            if l <= len(vg1)-1:
                                upass.append(vg1[l])
                            if l <= len(vg2)-1:
                                upass.append(vg2[l])
                            if l <= len(vg3)-1:
                                upass.append(vg3[l])
                            if l <= len(vg4)-1:
                                upass.append(vg4[l])
                            if l <= len(vg5)-1:
                                upass.append(vg5[1])
                            l = l + 1
                        #print[chr(i + 96) for i in upass]
                        #print(upass)
                        diction()
def trans5() :
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    tp1 = []
    tp2 = []
    tp3 = []
    tp4 = []
    tp5 = []
    b = 1
    global upass
    for a in upass:     
        if b >= 6:
            b = 1
        if b == 1:
            l1.append(a)
        elif b == 2:
            l2.append(a)
        elif b == 3:
            l3.append(a)
        elif b == 4:
            l4.append(a)
        elif b == 5:
            l5.append(a)
        b = b + 1
    global tl
    tl = [l1,l2,l3,l4,l5]
    print(tl)
    print(l1,l2,l3,l4,l5)
    loop1 = 0
    while loop1 <= 3:
        loop1 = loop1 + 1
        tp1 = tl[loop1]
        loop2 = -1
        while loop2 <= 3:
            loop2 =  loop2 + 1
            if loop2 != loop1:
                tp2 = tl[loop2]
                loop3 = -1
                while loop3 <= 3:
                    loop3 = loop3 + 1
                    if loop3 != loop1 and loop3 != loop2:
                        tp3 = tl[loop3]
                        loop4 = -1
                        while loop4 <= 3:
                            loop4 = loop4 + 1
                            if loop4 != loop1 and loop4 != loop2 and loop4 != loop3:
                                global tl
                                tp4 =  tl[loop4]
                                loop5 = -1
                                while loop5 <= 3:
                                    loop5 = loop5 + 1
                                    if loop5 != loop1 and loop5 != loop2 and loop5 != loop3 and loop5 != loop4:
                                        tp5 = tl[loop5]
                                        #print('here')
                                        #print(tp1,tp2,tp3,tp4,tp5)
                                        #time.sleep(6000)
                                        global upass
                                        upass = []
                                        l = 0
                                        while l <= max(len(tp1),len(tp2),len(tp3),len(tp4),len(tp5))- 1:   #put back into upass
                                            global upass
                                            if l <= len(tp1)-1:
                                                upass.append(tp1[l])
                                            if l <= len(tp2)-1:
                                                upass.append(tp2[l])
                                            if l <= len(tp3)-1:
                                                upass.append(tp3[l])
                                            if l <= len(tp4)-1:
                                                upass.append(tp4[l])
                                            if l <= len(tp5)-1:
                                                upass.append(tp5[l])
                                            l = l + 1
                                        diction()
                                
                
        

    
while 1:
    print('6 for transposition with 5 letter keywords')
    q = input('If you want to shift, press 0\nIf you want to check the dictionary, press 8\nIf you want to reverse, press 9\nIf you want to check 1 repeats,press1\nIf you want to check 3 repeats, press 3\nIf you want to check 4 repeats,press 4\nIf you want to check 5 repeat,press 5\n')
    if q == 0:
        shift()
        print(uword)
    elif q == 9:
        revers()
    elif q == 8:
        the()
        be()
        jamelia()
        like()
        this()
        deis()
        gravity()
        you()
        print(wherethe,wherebe,wherejamelia,wherelike,wherethis,whereis,wheregravity,whereyou)
    elif q == 1:
        vcipher1()
    elif q == 3:
        vcipher3()
    elif q == 4:
        vcipher4()
    elif q == 5:
        vcipher5()
    elif q == 98:   #ucode to reset
        ucode = oucode
        upass = oupass
    elif q == 99:
        wherethe = ['the']
        wherebe = ['be']
        wherejamelia = ['jamelia']
        wherelike = ['like']
        wherethis = ['this']
        whereis = ['is']
        wheregravity = ['gravity']
        possible = 0
    elif q == 100:   #auto run password
        password()
    elif q == 'consequence':
        print reploc
    elif q == 'vigen':
        replace()
        if gcd == 3:
            vigen3()
        elif gcd == 4:
            vigen4()
        elif gcd == 2:
            vigen2()
        elif gcd == 5:
            vigen5()
    elif q == 6:
        trans5()
            
                    
                    
        
