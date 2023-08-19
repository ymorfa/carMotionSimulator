# carMotionSimulator
Simulador de vehículo con Python: movimiento, acelerómetro y giroscopio.

Figura 1
<img src="/Multimedia/CarModel 1.png" alt="CarModel 1" width="600"/>

## Vehicle Dynamics


Let's consider a vehicle as shown in Figure 1. To understand how this car moves, we need some key concepts:

* **State**: We think of the car as a position $XY = (x, y)$ in the plane and an orientation $\theta$ (an angle indicating the direction the car is pointing in). As shown in Figure...

* **Input**: The car can be controlled, so we have a velocity $v$ (how much it's moving forward) and a steering angle $\delta$ (the direction the steering wheel is turned to).

* **System Parameters**: There are features of the car that affect its behavior, such as the distance between the wheels (wheelbase) $L$, the distance between the rear wheels and the reference point (refoffset) $l$, and the maximum angle it can steer (maxsteer).

**Goal**: We aim to understand how $(x, y)$ and $\theta$ change as $v$ and $\delta$ change.

Additional condition: **No Slipping** (In this model, we assume the wheels do not slip.)

Figura 2
<img src="/Multimedia/CarModel 2.png" alt="CarModel 1" width="800"/>


Figura 3
<img src="/Multimedia/CarModel 3.png" alt="CarModel 1" width="800"/>


Using the constructions shown in Figure 3:
We can obtain $\beta$

$$ \tan(\beta) = \frac{l}{S}; \quad\quad \tan(\delta) = \frac{L}{S} \quad\Rightarrow\quad  S = \frac{L}{\tan(\delta)}$$

$$ \tan(\beta) = \frac{l\tan(\delta)}{L} \quad\Rightarrow\quad  \beta = \arctan(\frac{l\tan(\delta)}{L}) $$

We can obtain $R$

$$\cos(\beta) = \frac{S}{R} \quad\Rightarrow\quad R = \frac{S}{\cos(\beta)}  \quad\Rightarrow\quad R = \frac{L}{\tan(\delta)\cos(\beta)} $$

At a given time instant $t$, given the linear velocity, we can calculate the velocities in the axes and the angular velocity.

For the velocities in the x and y axes, we can use the following equations based on the current state of the vehicle and the linear velocity:
$$v_x = v\cos(\beta+\theta)$$ 
$$v_y = v\sin(\beta+\theta)$$ 
Here, $v$ is the linear velocity, $\theta$ is the current orientation of the vehicle, and $\beta$ is the angle calculated as you mentioned earlier.

For the angular velocity $\omega$, it can be calculated using the following equation:

$$\omega = v/R = v\frac{\tan(\delta)\cos(\beta)}{L}$$ 

The state update, using the Euler method, would then appear as:

$$x_{t+1} = x_{t} + v_{x}\Delta t$$
$$y_{t+1} = y_{t} + v_{y}\Delta t$$
$$\theta_{t+1} = \theta_{t} + w\Delta t$$

Now, let's imagine that instead of the mentioned velocity $v$ (how much it's moving forward) and a steering angle $\delta$ (the direction the steering wheel is turned to), we have the acceleration $a$ and the angle. We can calculate the velocity at a time instant $t$ as follows:

$$v_t = v_{t-1} + a\Delta t$$
