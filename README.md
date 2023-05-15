# Software Architecture: Kyiv Polytechnic Institute course

This repository consists of 10 most popular Software Architecture design patterns implemented in Python.

Each pattern has a simple Python implementation example with tests.

All examples are implemented in different branches.

## Patterns:

1. [**Layered Arhitecture**](https://github.com/annavasylashko/kpi-architecture/tree/layered-architecture)
2. [**Client-Server Architecture**](https://github.com/annavasylashko/kpi-architecture/tree/client-server)
3. [**Master-Slave Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/master-slave)
4. [**Pipe-Filter Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/pipe-filter)
5. [**Broker Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/broker)
6. [**Peer-to-Peer Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/peer-to-peer)
7. [**Event Bus Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/event-bus)
8. [**Model-View-Controller Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/mvc)
9. [**Blackboard Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/blackboard)
10. [**Interpreter Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/interpreter)

# Master-Slave Pattern Example

This example demonstrates the Master-Slave pattern in Python. The pattern involves a master component that controls and coordinates one or more slave components. The master component distributes tasks or workloads to the slave components, and they perform the assigned tasks.

In this example, the master component generates a list of numbers, and the slave components calculate the square of each number in parallel.

## Implementation

**`main.py`** contains the main logic for the Master-Slave pattern implementation. It defines the square_worker function, which represents the worker task performed by each slave process. 

The `run_master_slave` function is responsible for coordinating the master-slave communication and task distribution. The script generates a list of numbers and calculates their squares using the Master-Slave pattern.

## Usage

To `run the example` and see the results, you can execute the following command in the terminal:

```zsh
python3 main.py
```

The script will generate a list of numbers and calculate their squares using the Master-Slave pattern. The calculated squares will be printed as the output.

*Output*:
```zsh
% python3 main.py 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

To `run the tests`, execute the following command:

```zsh
python3 test.py
```


## Dependencies

The implementation uses the following dependencies:

- **multiprocessing:** This built-in Python module is used for process-based parallelism and communication between processes.