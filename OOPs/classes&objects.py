class Computer:
    def config(self):
        print("I5, 16gb, 1TB")


com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()

a = 5
print(a.bit_length())