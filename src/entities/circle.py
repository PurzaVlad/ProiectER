class Circle:
    def __init__(self, x, y, radius, vx=150.0, vy=100.0):
        self.x = float(x)
        self.y = float(y)
        self.radius = radius
        self.vx = float(vx)   # pixels per second
        self.vy = float(vy)

    @property
    def position(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def update(self, dt=1.0):
        # dt in seconds
        self.x += self.vx * dt
        self.y += self.vy * dt

    def get_position(self):
        return (self.x, self.y)

    def get_radius(self):
        return self.radius

    def check_collision(self, obstacle):
        # Simple collision detection logic
        circle_distance_x = abs(obstacle.x - self.x)
        circle_distance_y = abs(obstacle.y - self.y)

        if circle_distance_x > (obstacle.width / 2 + self.radius):
            return False
        if circle_distance_y > (obstacle.height / 2 + self.radius):
            return False

        if circle_distance_x <= (obstacle.width / 2):
            return True
        if circle_distance_y <= (obstacle.height / 2):
            return True

        corner_distance_sq = (circle_distance_x - obstacle.width / 2) ** 2 + (circle_distance_y - obstacle.height / 2) ** 2

        return corner_distance_sq <= (self.radius ** 2)