#!/usr/bin/env python
# coding: utf-8

# In[9]:

import re
tonum= {'零': 0, '一':1, '二':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10} 
tochinese= {0:'零', 1:'一', 2:'二',3:'三', 4:'四', 5:'五', 6:'六', 7:'七', 8:'八', 9:'九', 10:'十'}
#判断数字格式
def num(s):
    pd=['负','零','一','二','三','四','五','六','七','八','九','十']
    if s=='一百' or s=='负一百':
        x=1
    else:
        for i in s:
            if i in pd:
                x=1
            else:
                x=0
                break
    if x==1:
        ss=s
        if s[0]=='负':
            ss=s[1:]
        if  re.match('^\w$',ss)!=None or re.match('^十\w$',ss)!=None or re.match('^\w十$',ss)!=None or re.match('^\w十\w$',ss)!=None or ss=='一百':
            str='True'
        else:
            str='False'
    else:
        str='False'
    return str
#汉字转为数字
def hantoshuzi(s):
    if s[0]=='负':
        if len(s)==2 and s[1]!='零': #例：负()  【排除：负零】
            x=(-1)*tonum[s[1]]
        elif len(s)==3:   
            if s[1:]=='一百':         #负一百
                x=-100
            elif s[1]=='十' and s[2]!='十':       #例：负十() 【排除：负十十】
                x=(-1)*tonum[s[2]]-10
            elif s[1]!='十' and s[1]!='一' and s[2]=='十':   #例：负()十 【排除：负十十，负一十】
                x=(-10)*tonum[s[1]]
            else:
                x='False'
        elif len(s)==4 and s[3]!='十' and s[1]!='十' and s[0]!='一': 
            x=(-10)*tonum[s[1]]-tonum[s[3]]      #例：负()十() 【排除：负六十十，负十十六，负一十六】
        else:
            x='False'
    else:
        if len(s)==1:                 #例：()
            x=tonum[s]
        if len(s)!=1:
            if len(s)==2:
                if s=='一百':         #一百
                    x=100
                elif s[0]=='十' and s[1]!='十':     #例：十()
                    x=10+tonum[s[1]]
                elif s[0]!='十' and s[0]!='一' and s[1]=='十':     #例：()十  【排除：十十，一十】
                    x=tonum[s[0]]*10
                else:
                    x='False'
            elif len(s)==3 and s[2]!='十' and s[0]!='十' and s[0]!='一': #例：()十() 【排除：六十十，十十六，一十六】
                x=tonum[s[0]]*10+tonum[s[2]]
            else:
                x='False'
    return x
#数字转为汉字
def shuzitohan(x):  
    if x>100 or x<-100:
        s='("'+str(x)+'",未能判断该数字!)'
    elif x<0 and x>=-100:
        if x==-100:
            s='负一百'
        elif x<-10:
            x*=(-1)
            a=x//10
            b=x%10
            if a==1:        #例：12 —> 十二
                s='负十'+tochinese[b]
            elif a>1 & a<=9:    
                if b!=0:
                    s='负'+tochinese[a]+'十'+tochinese[b]   #例：62 —> 六十二
                else:
                    s='负'+tochinese[a]+'十'   
        else:
            x*=(-1)
            s='负'+tochinese[x]
    else:
        if x<=10:           #例：1 —> 一
            s=tochinese[x]
        elif x==100:
            s='一百'
        elif x>10 & x<100:
            a=x//10
            b=x%10
            if a==1:        #例：12 —> 十二
                s='十'+tochinese[b]
            elif a>1 & a<=9:    
                if b!=0:
                    s=tochinese[a]+'十'+tochinese[b]   #例：62 —> 六十二
                else:
                    s=tochinese[a]+'十'                #例：60 —> 六十
    return s
#判断运算
def yunsuan(s,x,y):    
    if s=='增加':
        x+=y
    elif s=='减少':
        x-=y
    elif s=='乘':
        x*=y
    elif s=='除':
        if y!=0:
            x=x//y
    return x
#分割语句
def fenge(s):
    yuju=s.split(' ')
    return yuju

def main():
    an={}
    k=1
    pduan=['增加','减少','乘','除']
    while k==1:
        s=input()
        if len(fenge(s))==1:
            if s=='退出':
                break
            else:
                print('(语句输入格式错误！)') 
        else:
            if len(fenge(s))==4 and fenge(s)[0]=='整数' and fenge(s)[2]=='等于': #整数 （变量名） 等于 （数字）
                    if num(fenge(s)[3])=='True' and hantoshuzi(fenge(s)[3])!='False':
                        an[fenge(s)[1]]=hantoshuzi(fenge(s)[3])
                    else:
                        print('("%s",未能判断该数字!)' %fenge(s)[3])
            elif fenge(s)[1] in pduan:             #例：（变量名） 增加 （数字）
                if an.__contains__(fenge(s)[0])==True:
                    ss=fenge(s)[1]
                    x=an[fenge(s)[0]]
                    if num(fenge(s)[2])=='True' and hantoshuzi(fenge(s)[2])!='False':
                        y=hantoshuzi(fenge(s)[2])
                    else:
                        print('("%s",未能判断该数字!)' %fenge(s)[2])
                    an[fenge(s)[0]]=yunsuan(ss,x,y)
                else:
                    print('(没有%s！)' %fenge(s)[0])
            elif fenge(s)[0]=='看看' and len(fenge(s))==2:
                if fenge(s)[1]=='':
                    print('(语句输入格式错误！)')
                else:
                    s1=fenge(s)[1]
                    if s1[0]=='“' and s1[len(s1)-1]=='”':
                        print(s1.strip('“”'))
                    elif an.__contains__(s1)==True:  #看看 （变量名）
                            print(shuzitohan(an[s1]))
                    elif an.__contains__(s1)==False:
                            print('(没有%s！)' %s1)
            elif fenge(s)[0]=='如果':   #如果 （判断语句） 则 （操作语句1） 否则 （操作语句2）
                if len(fenge(s))>=8:
                    ts=re.match('如果 (.*?) 则 (.*?) 否则 (.*)',s,re.S)
                    m=ts.group(1)    #（判断语句）
                    n=ts.group(2)    #（操作语句1）
                    r=ts.group(3)    #（操作语句2）
                    if an.__contains__(fenge(m)[0])==True:
                        x=an[fenge(m)[0]]
                        if num(fenge(m)[2])=='True' and hantoshuzi(fenge(m)[2])!='False':
                            y=hantoshuzi(fenge(m)[2])
                        else:
                            str='("'+fenge(n)[2]+'",未能判断该数字!)'
                        if bijiao(fenge(m)[1],x,y)==1:
                            if fenge(n)[0]=='看看' and len(fenge(n))==2:
                                if fenge(n)[1]=='':
                                    str='(语句输入格式错误！)'
                                else:
                                    s1=fenge(n)[1]
                                    if s1[0]=='“' and s1[len(s1)-1]=='”':
                                        str=s1.strip('“”')
                                    elif an.__contains__(s1)==True: 
                                        str=shuzitohan(an[s1])
                                    elif an.__contains__(s1)==False:
                                        str='(没有'+s1+'！)'
                            elif n=='无':
                                str='(没有任何操作)'
                            else:
                                if an.__contains__(fenge(n)[0])==True:
                                    if num(fenge(n)[2])=='True' and hantoshuzi(fenge(n)[2])!='False':
                                        t=hantoshuzi(fenge(n)[2])
                                    else:
                                        str='("'+fenge(n)[2]+'",未能判断该数字!)'
                                    x=an[fenge(n)[0]]
                                    an[fenge(n)[0]]=yunsuan(fenge(n)[1],x,t)
                                    str='(刚刚执行了“'+n+'”操作)'
                        else:
                            if fenge(r)[0]=='看看'  and len(fenge(r))==2:
                                if fenge(r)[1]=='':
                                    str='(语句输入格式错误！)'
                                else:
                                    s1=fenge(r)[1]
                                    if s1[0]=='“' and s1[len(s1)-1]=='”':
                                        str=s1.strip('“”')
                                    elif an.__contains__(s1)==True: 
                                        str=shuzitohan(an[s1])
                                    elif an.__contains__(s1)==False:
                                        str='(没有'+s1+'！)'
                            elif r=='无':
                                str='(没有任何操作)'
                            else:
                                if an.__contains__(fenge(r)[0])==True:
                                    if num(fenge(r)[2])=='True' and hantoshuzi(fenge(r)[2])!='False':
                                        t=hantoshuzi(fenge(r)[2])
                                    else:
                                        str='("'+fenge(n)[2]+'",未能判断该数字!)'
                                    x=an[fenge(r)[0]]
                                    an[fenge(r)[0]]=yunsuan(fenge(r)[1],x,t)
                                    str='(刚刚执行了“'+r+'”操作)'
                    elif an.__contains__(fenge(m)[0])==False:
                        str='(没有'+fenge(m)[0]+'！)'
                else:
                    str='(语句输入格式错误！)'
                print(str)
            else:
                print('(语句输入格式错误！)')
main()