class Car(object):
    def __init__(self,modal,colour,company,speedlimit):
        self.modal=modal
        self.colour=colour
        self.company=company
        self.speedlimit=speedlimit
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("acceleration")
    def gear(self):
        print("clutch")
Audi=Car("R8","red","company",120)
Audi.start()
Audi.stop()
Audi.accelerate()
Audi.gear()                     