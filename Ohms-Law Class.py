# Ohm’s Law Class                        Tyrell Robbins                           4/18/18

class OhmsLaw():
    def __init__(self):
        #data members
        self.current = 0.0
        self.resistance = 0.0
        self.voltage = 0.0

    #accessor methods
    #sets
    def set_current(self, c):
        self.current = c

    def set_resistance(self,r):
        self.resistance = r

    def set_voltage(self, v):
        self.voltage = v

    #gets
    def get_current(self):
        return self.current

    def get_resistance(self):
        return self.resistance

    def get_voltage(self):
        return self.voltage

    # mutator methods to find current resistance and voltage
    def calc_current(self):
        self.current = self.voltage/self.resistance

    def calc_resistance(self):
        self.resistance = self.voltage/self.current

    def calc_voltage(self):
        self.voltage = self.resistance * self.current


#main()
Ol = OhmsLaw()
strloop = "Y"
while(strloop == "Y"):
    print("1. find Current 2. find Resistance 3. find Voltage 4. quit")
    strask = input("enter your choice")

    dblx = 0
    dbly = 0

    if(strask == "1"):
        print("Current")
        # calculate voltage
        v = float(input("Enter Voltage"))
        r = float(input("Enter Resistance"))
        Ol.set_voltage(v)
        Ol.set_resistance(r)
        Ol.calc_current()
        print("The Current is",format(Ol.get_current(),'.2f'))
        strask = 0
    elif(strask == "2"):
        print("Resistance")
        # calculate current
        v = float(input("Enter Voltage"))
        c = float(input("Enter Current"))
        Ol.set_voltage(v)
        Ol.set_current(c)
        Ol.calc_resistance()
        print("The Current is", format(Ol.get_resistance(), '.2f'))
        strask = 0

    elif(strask == "3"):
        print("Voltage")
        #calculate resistance
        c = float(input("Enter Current"))
        r = float(input("Enter Resistance"))
        Ol.set_current(c)
        Ol.set_resistance(r)
        Ol.calc_voltage()
        print("The Current is", format(Ol.get_current(), '.2f'))
        strask = 0

    elif(strask == "4"):
        strloop = "x"
    else:
        print("bad input")