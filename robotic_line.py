from collections import deque

class Part:
    def __init__(self, part_type):
        self.part_type = part_type
        self.stage = 0

    def advance_stage(self):
        self.stage += 1


class Robot:
    def __init__(self, name, processing_time, stage):
        self.name = name
        self.processing_time = processing_time
        self.stage = stage
        self.queue = deque()
        self.current_part = None
        self.time_left = 0
        self.state = "idle"
        self.processed_count = 0

    def add_part(self, part):
        self.queue.append(part)

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
    stage = 0

    def __init__(self):
        name = f"Welder {Welder.counter}"
        Welder.counter += 1
        super().__init__(name, 5, Welder.stage)


class Inspector(Robot):
    counter = 1
    stage = 1

    def __init__(self):
        name = f"Inspector {Inspector.counter}"
        Inspector.counter += 1
        super().__init__(name, 2, Inspector.stage)


class Assembler(Robot):
    counter = 1
    stage = 2

    def __init__(self):
        name = f"Assembler {Assembler.counter}"
        Assembler.counter += 1
        super().__init__(name, 3, Assembler.stage)



class ProductionLine:
    def __init__(self):
        self.robots = []
        self.parts = deque()
        self.finished_parts = []
        self.time = 0
        self.log = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def add_part(self, part):
        self.parts.append(part)

    def tick(self, dt=1):
        self.time += dt

        for robot in self.robots:
            for part in list(self.parts):
                if part.stage == robot.stage:
                    robot.add_part(part)
                    self.parts.remove(part)
                    break

            processed_part = robot.tick(dt)
            if processed_part:
                processed_part.advance_stage()
                if processed_part.stage >= 3:
                    self.finished_parts.append(processed_part)
                else:
                    self.parts.append(processed_part)



if __name__ == "__main__":
    line = ProductionLine()

    line.add_robot(Welder())
    line.add_robot(Inspector())
    line.add_robot(Assembler())

    print("Production line has been created.")
