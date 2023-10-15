class Computer:
    def  __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print("In init")



    def config(self):
        print("Config is ", self.cpu, self.ram)
 

com1 = Computer("I5", 16)
com2 = Computer("Ryzen 3", 8)

Computer.config(com1)
Computer.config(com2)

com1.config()

a = 5
print(a.bit_length())