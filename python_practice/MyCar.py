    class Car(object):
        no_of_tyres = 5
        steering_type = 'Manual'

        def move_steering(self, direction='straight'):
            # self = ciaz (the object through which we are calling)
            print "My car will move in %r direction" %(direction)


    if __name__=='__main__':
        ciaz = Car()
        ciaz.move_steering = ('Right')
