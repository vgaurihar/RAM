class Car(object):
    def __init__(self, no_of_tyres, dashboardColor):
        self.no_of_tyres = no_of_tyres
        self.dashboardColor = dashboardColor
    
    def move_steering(self, direction='straight'):
        # self = ciaz (the object through which we are calling)
        print "My car will move in %r direction" %(direction)

    def set_steeringType(self, stype='Manual'):
        self.type = stype

    def get_steeringType(self):
        return self.type

    def get_tyresNumber(self):
        return self.no_of_tyres

if __name__=='__main__':
    ciaz = Car(5, 'Black')
    ciaz.set_steeringType('Automatic')
    print ciaz.get_steeringType()
    print ciaz.get_typesNumber()
    
    wagonR = Car()
    wagonR.set_steeringType()
    print wagonR.get_steeringType()
