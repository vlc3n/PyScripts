import random, sys

class KeyGen():

    def __init__(self):
        global i
        i = int(input("Start the Program \n"))
        print("")
        self.main(i)

    def main(self, count):
        seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        
        for i in range(count): # 
            print('-'.join(''.join(random.choice(seq) for _ in range(5)) for _ in range(3)))
        print("\nCreated {} serial keys.".format(count))

if __name__ == '__main__':
    app = KeyGen()
