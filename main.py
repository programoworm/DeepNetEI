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
	ch=input('Type 1,2 or 3:\n1.Diabetes\n2.Heart\n3.Exit\n')
	while True:
		choose(int(ch))
		ch=input('Type 1,2 or 3:\n1.Diabetes\n2.Heart\n3.Exit\n')
if __name__=='__main__':
	main()