#!/usr/bin/env python
# coding: utf-8

# In[9]:


import re
tonum= {'零': 0, '一':1, '二':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10} 
tochinese= {0:'零', 1:'一', 2:'二',3:'三', 4:'四', 5:'五', 6:'六', 7:'七', 8:'八', 9:'九', 10:'十'}
def hantoshuzi(x):  #汉字转为数字
    if x[0]=='负':
        if len(x)==2:                 #例：负一
            a=(-1)*tonum[x[1]]
        if len(x)==3:   
            if x[1:]=='一百':         #负一百
                a=-100
            if x[1]=='十':            #例：负十二
                a=(-1)*tonum[x[2]]-10
            if x[2]=='十':            #例：负六十
                a=(-10)*tonum[x[1]]
        if len(x)==4:                 #例：负六十二
            a=(-10)*tonum[x[1]]-tonum[x[3]]
    else:
        if len(x)==1:                 #例：一
            a=tonum[x]
        if len(x)!=1:
            if len(x)==2:
                if x=='一百':         #一百
                    a=100
                elif x[0]=='十':     #例：十二
                    a=10+tonum[x[1]]
                elif x[1]=='十':     #例：六十
                    a=tonum[x[0]]*10
            elif len(x)==3:          #例：六十二
                a=tonum[x[0]]*10+tonum[x[2]]
    return a  
def shuzitohan(x):  #数字转为汉字
    if x<0:
        x*=(-1)
    if x<=10:           #例：1 —> 一
        str=tochinese[x]
    elif x==100:
        str='一百'
    elif x>10 & x<100:
        a=x//10
        b=x%10
        if a==1:        #例：12 —> 十二
            str='十'+tochinese[b]
        elif a>1 & a<=9:    
            if b!=0:
                str=tochinese[a]+'十'+tochinese[b]   #例：62 —> 六十二
            else:
                str=tochinese[a]+'十'                #例：60 —> 六十
    return str
def yunsuan(s,x,y):    #判断运算
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
def bijiao(s,x,y):    #判断比较
    z=0
    if (s=='大于' and x>y) or (s=='小于' and x<y) or (s=='等于' and x==y) or (s=='不等于' and x!=y) or (s=='大于等于' and x>=y) or (s=='小于等于' and x<=y):
        z=1
    return z
def fenge(s):
    yuju=s.split(' ')
    return yuju
def main():
    an={}
    k=1
    pduan=['增加','减少','乘','除']
    while k==1:
        s=input()
        if s=='退出':
            break
        else:
            if fenge(s)[0]=='整数' and fenge(s)[2]=='等于': #整数 （变量名） 等于 （数字）
                an[fenge(s)[1]]=hantoshuzi(fenge(s)[3])
            if fenge(s)[1] in pduan:             #例：（变量名） 增加 （数字）
                if an.__contains__(fenge(s)[0])==True:
                    ss=fenge(s)[1]
                    x=an[fenge(s)[0]]
                    y=hantoshuzi(fenge(s)[2])
                    an[fenge(s)[0]]=yunsuan(ss,x,y)
                else:
                    print('(没有%s！)' %fenge(s)[0])
            if fenge(s)[0]=='看看':
                if an.__contains__(fenge(s)[1])==True:  #看看 （变量名）
                    if an[fenge(s)[1]]>=0:
                        print(shuzitohan(an[fenge(s)[1]]))
                    else:
                        print('负%s' %shuzitohan(an[fenge(s)[1]]))
                elif an.__contains__(fenge(s)[1])==False:
                        print('(没有%s！)' %fenge(s)[1])
            if fenge(s)[0]=='如果':   #如果 （判断语句） 则 （操作语句1） 否则 （操作语句2）
                ts=re.match('如果 (.*?) 则 (.*?) 否则 (.*)',s,re.S)
                m=ts.group(1)    #（判断语句）
                n=ts.group(2)    #（操作语句1）
                r=ts.group(3)    #（操作语句2）
                if an.__contains__(fenge(m)[0])==True:
                    x=an[fenge(m)[0]]
                    y=hantoshuzi(fenge(m)[2])
                    if bijiao(fenge(m)[1],x,y)==1:
                        if fenge(n)[0]=='看看':
                            str=fenge(n)[1].strip('“”')
                        elif n=='无':
                            str='(没有任何操作)'
                        else:
                            if an.__contains__(fenge(n)[0])==True:
                                t=hantoshuzi(fenge(n)[2])
                                x=an[fenge(n)[0]]
                                an[fenge(n)[0]]=yunsuan(fenge(n)[1],x,t)
                                str='(刚刚执行了“'+n+'”操作)'
                    else:
                        if fenge(r)[0]=='看看':
                            str=fenge(r)[1].strip('“”')
                        elif r=='无':
                            str='(没有任何操作)'
                        else:
                            if an.__contains__(fenge(r)[0])==True:
                                t=hantoshuzi(fenge(r)[2])
                                x=an[fenge(r)[0]]
                                an[fenge(r)[0]]=yunsuan(fenge(r)[1],x,t)
                                str='(刚刚执行了“'+r+'”操作)'
                    print(str)
                elif an.__contains__(fenge(m)[0])==False:
                    print('(没有%s！)' %fenge(m)[0])
            else:
                print('语句输入格式错误！')
        
main()

