class Ball:
    def __init__(self, x, y, colour, size, maxAcceleration, maxSpeed):
        self.position = [x, y]
        self.maxAcceleration = maxAcceleration
        self.maxSpeed = maxSpeed
        self.colour = colour
        self.size = size

        self.velocity = [0, 0]
    
    def updatePosition(self, mousePos):
        for i in range(0, 2):
            # Acceleration
            difference = mousePos[i] - self.position[i]
            difference = float(max(min(float(difference / 2), self.maxAcceleration), (-1 * self.maxAcceleration)))

            # Velocity
            self.velocity[i] += difference
            if self.velocity[i] > self.maxSpeed:
                self.velocity[i] = self.maxSpeed
            elif self.velocity[i] < self.maxSpeed * -1:
                self.velocity[i] = self.maxSpeed * -1
            
            # Displacement
            self.position[i] += self.velocity[i]
    