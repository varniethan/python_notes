import time
class Vehicle:
    
    number = 0 

    @classmethod
    def get_number(cls):

        cls.number += 1
        return cls.number

    def __init__(self, name):

        self._name = name
        self._number = self.get_number()

    def return_name(self):

        return self._name

    def set_name(self, name):

        self._name = name

    def test_function(self, number_plate):

        self._number_plate = number_plate



class Car(Vehicle):

    def __init__(self, name, number_plate):

        Vehicle.__init__(self, name)
        self._number_plate = number_plate



def main():

    car = Car("Mr. Beans car", "RE09 NWP")
    print(car.return_name())

if __name__ == "__main__":

    main()
