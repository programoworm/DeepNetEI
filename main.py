from diabetes import diabetes
from heart import heart


def main():
	while True :
		ch=input('Type 1,2 or 3:\n1.Diabetes\n2.Heart\n3.Exit\n')
		if(ch=='3'): exit()
		switcher={
			1: diabetes,
			2: heart
		}
	
		f=switcher.get(int(ch),"Invalid Input!!")
		f()
			
		

if __name__=='__main__':
	main()