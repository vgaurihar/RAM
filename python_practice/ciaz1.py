class Car(object):

    def move_steering(self, direction='straight'):
        # self = ciaz (the object through which we are calling)
        print "My car will move in %r direction" %(direction)

    def set_steeringType(self, stype='Manual'):
        self.type = stype

    def get_steeringType(self):
        return self.type

if __name__=='__main__':
    ciaz = Car()
    ciaz.set_steeringType('Automatic')
    print ciaz.get_steeringType()

    
    wagonR = Car()
    wagonR.set_steeringType()
    print wagonR.get_steeringType()


