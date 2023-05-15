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

# Broker Pattern Example

This example demonstrates the Broker pattern, also known as the Event-Driven Architecture, in Python.

The Broker pattern involves a central component called the broker that facilitates communication and coordination between different components or services. 

Components can subscribe to events, and the broker distributes events to the subscribed components.

## Implementation

The implementation consists of the following files:

- `broker.py`: This file contains the implementation of the Broker class, which serves as the central component in the Broker pattern. It provides methods for subscribing to events and publishing events. The subscribe method allows components to subscribe to specific events, and the publish method distributes events to the subscribed components.

- `components/component_a.py`: This file contains the implementation of ComponentA class, an example component that subscribes to the 'event' event in the broker. It has a handle_event method that is called when the event is published. In this example, it simply prints a message to demonstrate event handling.

- `components/component_b.py`: This file contains the implementation of ComponentB class, another example component that also subscribes to the 'event' event in the broker. It has a handle_event method that is called when the event is published. In this example, it also prints a message to demonstrate event handling.

- `main.py`: This file initializes the broker and the components, subscribes the components to the 'event' event, and publishes an event using the broker.

## Usage

To run the example and see the results, execute the following command in the terminal:

```zsh
python3 main.py
```

The `main.py` script demonstrates the usage of the Broker pattern. 

It initializes the broker and the components (ComponentA and ComponentB), subscribes them to the 'event' event using the broker, and publishes an event. 

The event is then handled by the subscribed components, and they print messages to demonstrate the event handling.

*Output:*
```zsh
Component A handling event: ('Hello',) {'name': 'John'}
Component B handling event: ('Hello',) {'name': 'John'}
```