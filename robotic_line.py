

class Robot:
    def __init__(self, name, processing_time, supported_part):
        self.name = name
        self.processing_time = processing_time
        self.supported_part = supported_part

    def add_part(self, part):
        pass  

    def start_processing(self, part):
        pass 

    def tick(self, dt):
        pass  


class Welder(Robot):
    def __init__(self, name):
        super().__init__(name, 5, "metal")


class Inspector(Robot):
    def __init__(self, name):
        super().__init__(name, 2, "metal")


class Assembler(Robot):
    def __init__(self, name):
        super().__init__(name, 3, "assembled")



class ProductionLine:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def add_part(self, part):
        self.parts.append(part)

    def tick(self, dt=1):
        pass


if __name__ == "__main__":
    line = ProductionLine()

    line.add_robot(Welder())
    line.add_robot(Inspector())
    line.add_robot(Assembler())

    print("Production line has been cretaed.")
