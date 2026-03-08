# Drone Interceptor Simulator

A Python simulation of a drone interception system that detects and eliminates enemy drones within radar range, logging all activity to a text file.

## How It Works

1. 5 enemy drones are spawned at random coordinates
2. A radar scans each drone's position
3. If a drone is within radar range → it is intercepted and marked as **DETECTED**
4. The interceptor moves toward the drone and eliminates it → **TARGET ELIMINATED**
5. All events are logged to `logs.txt` with timestamps

## Project Structure

```
drone_interceptor/
├── main.py        # Entry point — runs the simulation
├── drone.py       # Drone class — position, speed, fuel, movement
├── detector.py    # Radar class — scans for drones within range
└── logger.py      # Logger class — writes events to logs.txt
```

## Example Log Output

```
2026-03-08 23:45:50 | Drone(31.4, 63.1) | DETECTED
2026-03-08 23:45:50 | Drone(40.0, 50.0) | TARGET ELIMINATED
2026-03-08 23:45:50 | Drone(10.6, 67.1) | SAFE
```

## How to Run

```bash
python main.py
```

## Concepts Used

- Object-Oriented Programming (OOP)
- Math — distance calculation, unit vectors
- File I/O — logging to `.txt`
- Python standard libraries: `math`, `random`, `datetime`
