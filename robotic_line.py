from collections import deque

class Robot:
    def __init__(self, name, processing_time, supported_part):
        self.name = name
        self.processing_time = processing_time
        self.supported_part = supported_part
        self.queue = deque()
        self.current_part = None
        self.time_left = 0
        self.state = "idle"
        self.processed_count = 0

    def add_part(self, part):
        if part == self.supported_part:
            self.queue.append(part)
        else:
            print(f"{self.name} is unable to process {part}.")

    def start_processing(self, part):
        self.current_part = part
        self.time_left = self.processing_time
        self.state = "working"

    def tick(self, dt):
        finished_part = None

        if self.state == "working":
            self.time_left -= dt
            if self.time_left <= 0:
                finished_part = self.current_part
                self.current_part = None
                self.state = "waiting"
                self.processed_count += 1

        if self.state == "waiting" and self.queue:
            next_part = self.queue.popleft()
            self.start_processing(next_part)

        return finished_part



class Welder(Robot):
    counter = 1

    def __init__(self):
        name = f"Welder {Welder.counter}"
        Welder.counter += 1
        super().__init__(name, 5, "metal")


class Inspector(Robot):
    counter = 1

    def __init__(self):
        name = f"Inspector {Inspector.counter}"
        Inspector.counter += 1
        super().__init__(name, 2, "metal")


class Assembler(Robot):
    counter = 1

    def __init__(self):
        name = f"Assembler {Assembler.counter}"
        Assembler.counter += 1
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

    print("Production line has been created.")
