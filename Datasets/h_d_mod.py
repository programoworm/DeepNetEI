import random
def mod(f):
    s=[]
    for line in f:
        s.append(line)
    print(s)
def main():
    f=open("heart.csv")
    mod(f)
if __name__=='__main__':
    main()
