from diabetes import diabetes
from heart import heart

def choose(ch):
	if ch==3: exit()
	switcher = {
		1: diabetes,
		2: heart,
	}
	chosen=switcher.get(ch, "Invalid Choice")
	return chosen()

def main():
	while True:
		ch=input('\nType 1,2 or 3:\n1.Diabetes\n2.Heart\n3.Exit\nEnter your choice: ')
		choose(int(ch))

if __name__=='__main__':
	main()