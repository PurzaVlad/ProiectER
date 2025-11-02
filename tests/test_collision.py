import unittest
from src.entities.circle import Circle
from src.entities.obstacle import Obstacle
from src.physics.collision import check_collision

class TestCollision(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(x=5, y=5, radius=2)
        self.obstacle = Obstacle(x=4, y=4, width=2, height=2)

    def test_collision_with_obstacle(self):
        self.assertTrue(check_collision(self.circle, self.obstacle))

    def test_no_collision_with_obstacle(self):
        self.circle.x = 10
        self.circle.y = 10
        self.assertFalse(check_collision(self.circle, self.obstacle))

    def test_edge_collision(self):
        self.circle.x = 4
        self.circle.y = 5
        self.assertTrue(check_collision(self.circle, self.obstacle))

if __name__ == '__main__':
    unittest.main()