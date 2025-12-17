# Production Line Simulation

This project simulates a simple production line where robots process parts through multiple stages.  
The simulation tracks processed parts, defective parts, robot idle times, and planned breakdowns.

---

## Project Structure

- `production_line.py` – main script containing the simulation code
- `README.md` – project documentation

---

## Features

- Multiple robot types:
  - **Welder** – welds raw parts
  - **Inspector** – checks quality and detects defective parts
  - **Assembler** – assembles finished products
- Robots can work in parallel
- Planned breakdowns after a specified number of processed parts
- Logging of all events (start/finish processing, defective parts, breakdowns)
- Calculation of statistics: number of finished parts, scrap rate, robot idle times

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/production-line-sim.git
cd production-line-sim
```
