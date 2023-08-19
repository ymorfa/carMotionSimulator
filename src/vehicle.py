import numpy as np


class Vehicle:
    def __init__(self, inicial_state: np.ndarray, inicial_motion: np.ndarray, params: dict = {}):
        # Obtener los parámetros para el Vehiculo.
        self.refoffset      = params.get('refoffset', 1.5)  # distancia entre las ruedas traseras y el punto de referencia
        self.wheelbase      = params.get('wheelbase', 3.)   # distancia entre las ruedas del vehiculo
        self.maxsteer       = params.get('maxsteer', 0.5)   # el ángulo máximo al que se puede girar (rad)
        self.current_state  = inicial_state                 # Estado Actual del Vehiculo array([x, y, alpha])
        self.current_acc    = inicial_motion[1]             # Acceleración Inicial
        self.current_vel    = inicial_motion[0]             # Velocidad Inicial
        self.current_time   = 0                             # Tiempo de Inicio
        
        self.states         = []                            # Registro de Status del Vehiculo
        self.time           = []                            # Time Index
        self.lineal_acc     = []                            # Registro de Aceleración Lineal
        self.lineal_vel     = []                            # Registro de las Velocidades
        self.accelerometer  = []                            # Registro de la Acelereción en sus ejes ax, ay
        self.gyroscope      = []                            # Registro de la Acelereción en sus ejes gx, gy

        # Calculo de la aceleración en los ejes x e y en función de la orientación del vehículo
        acc_x = self.current_acc * np.cos(self.current_state[2])
        acc_y = self.current_acc * np.sin(self.current_state[2])

        self.states.append(self.current_state)      
        self.time.append(self.current_time)
        self.lineal_acc.append(self.current_acc)
        self.lineal_vel.append(self.current_vel)
        self.accelerometer.append(np.array([acc_x, acc_y]))
    
    
    def calculate_states_velocities(self, v: float, delta: float):
        delta = np.clip(delta, -self.maxsteer, self.maxsteer)
        theta = self.current_state[2]
        beta  = np.arctan2(self.refoffset * np.tan(delta), self.wheelbase) 
        # Calcular las velocidades del estado
        x_v     = v * np.cos(theta + beta) 
        y_v     = v * np.sin(theta + beta)
        theta_v = v * np.tan(delta) * np.cos(beta) / self.wheelbase 
        return np.array([x_v, y_v, theta_v])
    

    def vehicle_update(self, t: float, acc: float, delta: float):

        # Obtener variables de iteración anterior
        previous_x, previous_y, previous_theta = self.states[-1]
        previous_time                          = self.time[-1]
        previous_vel                           = self.lineal_vel[-1]

        # Actualizamos Tiempo y delta time
        self.current_time                      = t
        delta_time                             = self.current_time - previous_time

        # Actualización de Aceleracón Lineal y Velocidad Lineal
        self.current_acc                       = acc
        self.current_vel                       = previous_vel + self.current_acc*delta_time

        # Calculo de Velocidad en los Ejes y calcular los estados del vehiculo
        vel                                    = self.calculate_states_velocities(self.current_vel, delta)
        current_x                              = previous_x     + vel[0]*delta_time
        current_y                              = previous_y     + vel[1]*delta_time
        current_theta                          = previous_theta + vel[2]*delta_time

        # Actualizamos Estados
        self.current_state                     = np.array([current_x, current_y, current_theta])

        # Calculo de la aceleración en los ejes x e y en función de la orientación del vehículo
        acc_x = self.current_acc * np.cos(self.current_state[2])
        acc_y = self.current_acc * np.sin(self.current_state[2])

        # Actualizamos Registros de Estados, Tiempo, Aceleración y Velocidad
        self.states.append(self.current_state)
        self.time.append(self.current_time)
        self.lineal_acc.append(self.current_acc)
        self.lineal_vel.append(self.current_vel)
        self.accelerometer.append(np.array([acc_x, acc_y]))