# Production Line Simulation

This project simulates a simple robotic production line using Python.
Parts move through multiple processing stages, where they are handled by different robots.
The simulation tracks production flow, defective parts, robot idle times, and planned breakdowns.

The project was created as a semester assignment and demonstrates basic concepts of
discrete-time simulation, object-oriented programming, and simple testing.

---

## Project Structure

- `robotic_line.py` – main script containing the simulation and tests  
- `README.md` – project documentation

---

## Features

- Multiple robot types:
  - **Welder** – welds raw parts (two welders working in parallel)
  - **Inspector** – inspects parts and detects defective ones
  - **Assembler** – assembles final products
- Parallel robot processing
- Shared queues between robots
- Planned robot breakdowns after a fixed number of processed parts
- Event logging:
  - start of processing
  - end of processing
  - defective parts
- Production statistics:
  - total simulation time
  - number of finished parts
  - number of defective parts
  - robot idle times
  - scrap rate
- Basic automated tests using `unittest`

---

## Installation

This project does **not** require any external libraries.
It uses only the Python standard library.

### Requirements

- Python **3.8 or newer**

### Steps

1. Clone the repository:

```bash
git clone https://github.com/afialova/robotic_line.git
```

2. Navigate to the project directory:

```bash
cd robotic_line
```

3. Run the simulation:

```bash
python robotic_line.py
```

> If your system uses `python3` instead of `python`, run:
>
> ```bash
> python3 robotic_line.py
> ```

---

## Running Tests

Basic tests are included directly in the project to verify core functionality
(e.g. part ID generation, stage progression, robot processing).

To run the tests:

```bash
python -m unittest robotic_line.py
```

---

## How It Works

1. Parts are inserted into the first queue (stage 0).
2. Two **Welder** robots take parts from the same input queue and work in parallel.
3. Finished welded parts move to the **Inspector** stage.
4. The **Inspector** may mark parts as defective (scrap).
5. Non-defective parts move to the **Assembler**.
6. Assembled parts are stored as finished products.
7. The simulation runs until:
   - all queues are empty
   - no robot is working or broken

---

## Example Output

```
Aktuální stav výrobní linky
Provozní doba: 180
Počet hotových dílů: 136
Počet zmetků: 6
Welder-1 - zpracováno: 71, prostoje: 24
Welder-2 - zpracováno: 71, prostoje: 26
Inspector - zpracováno: 142, prostoje: 98
Assembler - zpracováno: 136, prostoje: 102
Zmetkovitost: 4.2%
```

---

## License

This project is intended for educational purposes.
