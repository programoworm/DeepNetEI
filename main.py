from diabetes import diabetes
from heart import heart

def main():
	ch=input('Type 1,2 or 3:\n1.Diabetes\n2.Heart\n3.Exit\n')
	while ch!=3:
		if ch=='1':
			diabetes()
		elif ch=='2':
			heart()
		elif ch=='3':
			exit()
		else:
			print("Invalid input!!")
		ch=input('Type 1,2 or 3:\n1.Diabetes\n2.Heart\n3.Exit\n')

if __name__=='__main__':
	main()