import time

start_time = time.time()
name = input("Enter your name: ")

def reminder():
	print("Time to drink a glass of water"+name)

def main():
	while(True):
		if((time.time()-start_time)== 3600):
			reminder()

main()