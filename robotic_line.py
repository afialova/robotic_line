from collections import deque
import random

# Třída reprezentující díl na výrobní lince
class Part:
    counter = 1
    def __init__(self, part_type):
        self.part_type = part_type
        self.stage = 0
        self.defective = False
        self.id = f"ID-{Part.counter:04d}"
        Part.counter += 1

    def advance_stage(self):
        self.stage += 1

# Třída reprezentující robota na výrobní lince
class Robot:
    def __init__(self, name, processing_time, stage):
        self.name = name
        self.processing_time = processing_time
        self.stage = stage
        self.current_part = None
        self.time_left = 0
        self.state = "idle" # stavy robota: idle / working / broken
        self.processed_count = 0
        self.idle_time = 0
        self.breakdown_time = 0
        self.breakdown_after = 40

    def start_processing(self, part):
        self.current_part = part
        self.time_left = self.processing_time
        self.state = "working"

    # Jedna časová jednotka simulace pro robota
    def tick(self, dt):
        processed_part = None

        if self.state == "broken":
            self.breakdown_time -= dt
            if self.breakdown_time <= 0:
                self.state = "idle"
            else:
                self.idle_time += dt
                return None
            
        elif self.state == "working":
            self.time_left -= dt
            if self.time_left <= 0:
                processed_part = self.current_part
                self.current_part = None
                self.state = "idle"
                self.processed_count += 1

        elif self.state == "idle":
            self.idle_time += dt

            # pokud robot zpracoval určité množství dílů (40), nastává plánovaná porucha
            if self.processed_count > 0 and self.processed_count % self.breakdown_after == 0:
                self.state = "broken"
                self.breakdown_time = 5
                return None

        return processed_part

# Konkrétní typy robotů
class Welder(Robot):
    counter = 1
    def __init__(self):
        name = f"Welder-{Welder.counter}"
        Welder.counter += 1
        super().__init__(name, 5, 0)

class Inspector(Robot):
    def __init__(self):
        super().__init__("Inspector", 2, 1)

class Assembler(Robot):
    def __init__(self):
        super().__init__("Assembler", 3, 2)

# Třída reprezentující celou výrobní linku
class ProductionLine:
    def __init__(self):
        self.robots = []
        self.stage_queues = {0: deque(), 1: deque(), 2: deque()}  # fronty dílů pro jednotlivé fáze - jednotlivé roboty
        self.finished_parts = []
        self.scrap_parts = []
        self.time = 0
        self.log = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def add_part(self, part):
        self.stage_queues[0].append(part)

    def tick(self, dt=1):
        self.time += dt

        for robot in self.robots:
            while True:
                current_part = robot.tick(dt)
                if current_part:
                    # kontrola zmetků
                    if robot.stage == 1 and random.random() < 0.1:
                        current_part.defective = True
                        self.scrap_parts.append(current_part)
                        self.log.append({"time": self.time, "robot": robot.name, "part_id": current_part.id, "event": "finished_processing", "result": "zmetek"})
                    else:
                        current_part.advance_stage()
                        if current_part.stage >= 3:
                            self.finished_parts.append(current_part)
                            self.log.append({"time": self.time, "robot": robot.name, "part_id": current_part.id, "event": "finished_processing"})
                        else:
                            self.stage_queues[current_part.stage].append(current_part)
                            self.log.append({"time": self.time, "robot": robot.name, "part_id": current_part.id, "event": "finished_processing"})

                if robot.state == "idle" and self.stage_queues[robot.stage]:
                    next_part = self.stage_queues[robot.stage].popleft()
                    robot.start_processing(next_part)
                    self.log.append({"time": self.time, "robot": robot.name, "part_id": next_part.id, "event": "start_processing"})
                else:
                    break

    def all_parts_done(self):
        total_remaining = sum(len(q) for q in self.stage_queues.values())
        robots_busy_or_broken = any(r.current_part is not None or r.state == "broken" for r in self.robots)
        return total_remaining == 0 and not robots_busy_or_broken
    
    def run_until_done(self):
        while not self.all_parts_done():
            self.tick(dt=1)

    def print_statistics(self):
        print("**Aktuální stav výrobní linky**")
        print(f"Provozní doba: {self.time}")
        print(f"Počet hotových dílů: {len(self.finished_parts)}")
        print(f"Počet zmetků: {len(self.scrap_parts)}")
        for r in self.robots:
            print(f"{r.name} - zpracováno: {r.processed_count}, prostoje: {r.idle_time}")
        total = len(self.finished_parts) + len(self.scrap_parts)
        scrap_rate = (len(self.scrap_parts)/total*100) if total else 0
        print(f"Zmetkovitost: {scrap_rate:.1f}%")

# základní testy - smoke tests
def basic_tests():
    print("\nZákladní testy pro otestování funkčnosti výrobní linky:")
    test_line = ProductionLine()
    welder1 = Welder()
    welder2 = Welder()
    inspector = Inspector()
    assembler = Assembler()
    
    test_line.add_robot(welder1)
    test_line.add_robot(welder2)
    test_line.add_robot(inspector)
    test_line.add_robot(assembler)

    assert len(test_line.robots) == 4, "Roboti nebyli správně přidáni"

    for i in range(10):
        test_line.add_part(Part("Test Díl"))
    assert sum(len(q) for q in test_line.stage_queues.values()) == 10, "Díly nebyly správně přidány"

    test_line.run_until_done()
    total_processed = len(test_line.finished_parts) + len(test_line.scrap_parts)
    assert total_processed == 10, "Všechny díly nebyly zpracovány"

    for robot in test_line.robots:
        assert robot.processed_count >= 0, "Počet zpracovaných dílů nesmí být záporný"
        assert robot.idle_time >= 0, "Idle time nesmí být záporný"

    print("Všechny testy prošly!")

# simulace výrobní linky
if __name__=="__main__":
    line = ProductionLine()
    line.add_robot(Welder())
    line.add_robot(Welder())
    line.add_robot(Inspector())
    line.add_robot(Assembler())

    for i in range(142):
        line.add_part(Part("Díl"))

    line.run_until_done()
    line.print_statistics()

    print("\nUkázka záznamů v logu:")
    for entry in line.log[:20]:
        print(entry)

    # Spuštění základních testů
    basic_tests()
