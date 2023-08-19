# carMotionSimulator
Simulador de vehículo con Python: movimiento, acelerómetro y giroscopio.

Figura 1
![CarModel 1-2.png](<attachment:CarModel 1-2.png>)

## Vehicle Dynamics

Let's consider a vehicle as shown in Figure 1. To understand how this car moves, we need some key concepts:

* **State**: We think of the car as a position $XY = (x, y)$ in the plane and an orientation $\theta$ (an angle indicating the direction the car is pointing in). As shown in Figure...

* **Input**: The car can be controlled, so we have a velocity $v$ (how much it's moving forward) and a steering angle $\delta$ (the direction the steering wheel is turned to).

* **System Parameters**: There are features of the car that affect its behavior, such as the distance between the wheels (wheelbase) $L$, the distance between the rear wheels and the reference point (refoffset) $l$, and the maximum angle it can steer (maxsteer).

**Goal**: We aim to understand how $(x, y)$ and $\theta$ change as $v$ and $\delta$ change.

Additional condition: **No Slipping** (In this model, we assume the wheels do not slip.)
