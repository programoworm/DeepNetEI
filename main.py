from diabetes import diabetes
from heart import heart
from covid_txt import corona

def main():
	while True :
		ch=input('Type 1,2 or 3:\n1.Diabetes\n2.Heart\n3.COVID\n4.Exit\n')
		if(ch=='4'): exit()
		switcher={
			1: diabetes,
			2: heart,
			3: corona
		}
	
		f=switcher.get(int(ch),"Invalid Input!!")
		f()
	
if __name__=='__main__':
	main()