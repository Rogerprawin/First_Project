'''e_count=0
o_count=0

for i in range (1,21):
    if (i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)'''
class laptop:

    def __init__(self):             
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)                         
        print("Processor:",self.processor)

hp=laptop()
dell=laptop()

hp.ram="8GB"
hp.processor="snapdragon"

dell.ram="16GB"
dell.processor="ios"

hp.display()
dell.display()