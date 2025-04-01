security_channel = []
cage_quality_channel = []
animal_condition_channel = []
general_channel = []

class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload  
        
class Sensor:
    def __init__(self, id_number, sensor_type, cage):
        self.id_number = id_number
        self.sensor_type = sensor_type
        self.cage = cage

    def emit_event(self, name, payload):
        new_event = Event(name, payload)
        security_channel.append(new_event)

class Employee:
    def __init__(self, id_number, name, role):
        self.id_number = id_number 
        self.name = name
        self.role = role

    def handle_sensor_event(self, event):
        print(event.name)
        if event.name == 'motion sensor triggered':
            print('my role is', self.role)
            if self.role == 'guard':
                cage = event.payload['sensor'].cage
                self.check_cage(cage)
        elif event.name == 'humidity sensor triggered':
            print('my role is', self.role)
            if self.role == 'zookeeper':
                cage = event.payload['sensor'].cage
                self.check_cage(cage)

    def check_cage(self, number):
        print('I am going to check the cage:', number)

zookeeper1 = Employee(1, 'Piotr', 'zookeeper')
cleaner1 = Employee(2, 'Kraiven', 'cleaner')
guard1 = Employee(3, 'John', 'guard')
vet1 = Employee(4, 'Mable', 'vet')
manager1 = Employee(5, 'Jane', 'manager')
zookeeper2 = Employee(6, 'Serhat', 'zookeeper')
cleaner2 = Employee(7, 'Tom', 'cleaner')
guard2 = Employee(8, 'Serhat', 'guard')
system_admin = Employee(9, 'Piotr', 'admin')

humidity_sensor1 = Sensor(1, 'humidity', 'elephants 1')
humidity_sensor2 = Sensor(2, 'humidity', 'tigers 1')
humidity_sensor3 = Sensor(3, 'humidity', 'elephants 2')

temperature_sensor1 = Sensor(4, 'temperature', 'elephants 1')
temperature_sensor2 = Sensor(5, 'temperature', 'tigers 1')

motion_sensor1 = Sensor(6, 'motion', 'elephants 1')
motion_sensor2 = Sensor(7, 'motion', 'tigers 1')
motion_sensor3 = Sensor(8, 'motion', 'tigers 2')


motion_sensor1.emit_event('motion sensor triggered', {'sensor': motion_sensor1,'timestamp': '10:12:05 31.03.2025'}) 
guard1.handle_sensor_event(security_channel[0])

humidity_sensor1.emit_event('humidity sensor triggered', {'sensor': humidity_sensor1, 'timestamp': '13:34:23 01.04.2025'})
zookeeper1.handle_sensor_event(security_channel[1])