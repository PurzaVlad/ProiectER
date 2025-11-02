class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.circle = None
        self.obstacles = []
        self.running = True

    def create_circle(self, x, y, radius):
        from entities.circle import Circle
        self.circle = Circle(x, y, radius)

    def add_obstacle(self, x, y, width, height):
        from entities.obstacle import Obstacle
        obstacle = Obstacle(x, y, width, height)
        self.obstacles.append(obstacle)

    def update(self, dt=1.0, restitution=0.9):
        """
        Advance physics by dt (seconds).
        Circle moves by its velocity, obstacles may update,
        collisions with obstacles are resolved with realistic reflection,
        and the circle bounces off world bounds with the same restitution.
        """
        # move the circle by its velocity
        if self.circle:
            # circle.update should accept dt in seconds
            self.circle.update(dt)

        # update obstacles (static by default)
        for ob in self.obstacles:
            if hasattr(ob, "update"):
                ob.update(dt, bounds=(self.width, self.height))

        # resolve collisions with obstacles
        from physics.collision import check_collision, resolve_collision
        if self.circle:
            for ob in self.obstacles:
                if check_collision(self.circle, ob):
                    resolve_collision(self.circle, ob, restitution=restitution)

        # bounce off world bounds (reflect normal component with restitution)
        if self.circle:
            # left
            if self.circle.x - self.circle.radius < 0:
                self.circle.x = self.circle.radius
                if self.circle.vx < 0:
                    self.circle.vx = -self.circle.vx * restitution
            # right
            if self.circle.x + self.circle.radius > self.width:
                self.circle.x = self.width - self.circle.radius
                if self.circle.vx > 0:
                    self.circle.vx = -self.circle.vx * restitution
            # top
            if self.circle.y - self.circle.radius < 0:
                self.circle.y = self.circle.radius
                if self.circle.vy < 0:
                    self.circle.vy = -self.circle.vy * restitution
            # bottom
            if self.circle.y + self.circle.radius > self.height:
                self.circle.y = self.height - self.circle.radius
                if self.circle.vy > 0:
                    self.circle.vy = -self.circle.vy * restitution

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            self.update()
            # Additional game loop logic (rendering, input handling, etc.) would go here