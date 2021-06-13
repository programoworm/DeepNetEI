import random
def mod(f):
    s=[]
    count=0
    for line in f:
        if(count>10000):
            break
        s.append(line.split(","))
        count+=1
    us=[]
    for i in range(1,len(s)):
        t=""
        if(int(s[i][len(s[i])-1])>1):
            s[i][len(s[i])-1]="1"
        for j in range(len(s[i])-1):
            t=t+s[i][j]+","
        t=t+s[i][len(s[i])-1][:-1]
        us.append(t)
    fn=open("covid_update.csv","a")
    c=list(range(len(us)))
    random.shuffle(c)
    print(us)
    while c:
        fn.write(us[c.pop()]+"\n")
def main():
    f=open("corona_tested_individuals_updated.csv")
    mod(f)
if __name__=='__main__':
    main()