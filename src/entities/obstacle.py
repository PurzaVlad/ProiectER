class Obstacle:
    def __init__(self, x, y, width, height, vx=0, vy=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self, dt=1, bounds=None):
        # dt is frames or seconds consistent with your main loop
        self.x += self.vx * dt
        self.y += self.vy * dt

        if bounds:
            bw, bh = bounds
            if self.x < 0:
                self.x = 0
                self.vx *= -1
            if self.x + self.width > bw:
                self.x = bw - self.width
                self.vx *= -1
            if self.y < 0:
                self.y = 0
                self.vy *= -1
            if self.y + self.height > bh:
                self.y = bh - self.height
                self.vy *= -1

    def get_position(self):
        return (self.x, self.y)

    def get_dimensions(self):
        return (self.width, self.height)

    def is_colliding(self, circle):
        circle_x, circle_y = circle.get_position()
        circle_radius = circle.radius

        closest_x = max(self.x, min(circle_x, self.x + self.width))
        closest_y = max(self.y, min(circle_y, self.y + self.height))

        distance_x = circle_x - closest_x
        distance_y = circle_y - closest_y

        return (distance_x ** 2 + distance_y ** 2) < (circle_radius ** 2)