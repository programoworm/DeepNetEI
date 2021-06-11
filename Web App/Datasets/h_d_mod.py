import random
def mod(f):
    s=[]
    for line in f:
        s.append(line.split(","))
    us=[]
    for i in range(1,len(s)):
        t=""
        for j in range(len(s[i])-1):
            t=t+s[i][j]+","
        t=t+s[i][len(s[i])-1][:-1]
        us.append(t)
    fn=open("rand_heart.data","a")
    c=list(range(len(us)))
    random.shuffle(c)
    print(us)
    while c:
        fn.write(us[c.pop()]+"\n")
def main():
    f=open("heart.csv")
    mod(f)
if __name__=='__main__':
    main()
