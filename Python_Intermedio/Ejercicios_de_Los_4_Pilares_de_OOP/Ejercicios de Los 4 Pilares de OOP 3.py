# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def travel(self, destination):
        self.destination = destination


class PhotographyTool:
    def __init__(self, sensor_type, is_digital):
        self.sensor_type = sensor_type
        self.is_digital = is_digital

    
    def capture(self):
        return "\nTaking a high quality picture..."


class PhotoDrone(Vehicle, PhotographyTool):
    def __init__(self, brand, model, sensor_type, is_digital):
        Vehicle.__init__(self, brand, model)
        PhotographyTool.__init__(self, sensor_type, is_digital)

    
    def fly_and_shoot(self, place):
        self.travel(place)
        print(f"Traveling to {self.destination}...")
        print(self.capture())


my_drone = PhotoDrone("DJI", "Mini 5 Pro", 'CMOS 1"', True)

my_drone.fly_and_shoot("Volcan Irazu")

print(f"\n--- Tech Specs ---")
print(f"Device: {my_drone.brand} {my_drone.model}")
print(f"Sensor: {my_drone.sensor_type}")