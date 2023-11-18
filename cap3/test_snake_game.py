import unittest
import pygame
pygame.init()
import snake_game

SNAKE = snake_game.SNAKE
Vector2 = snake_game.Vector2
Fruit = snake_game.Fruit
 
#Snake movement
class TestSnakeMovement(unittest.TestCase):
   def setUp(self):
       self.snake = SNAKE()

   def test_move_up(self):
       self.snake.direction = Vector2(0, 1)
       self.snake.move_snake()
       self.assertEqual(self.snake.direction, Vector2(0, -1))

   def test_move_down(self):
       self.snake.direction = Vector2(0, -1)
       self.snake.move_snake()
       self.assertEqual(self.snake.direction, Vector2(0, 1))

   def test_move_right(self):
       self.snake.direction = Vector2(-1, 0)
       self.snake.move_snake()
       self.assertEqual(self.snake.direction, Vector2(1, 0))

   def test_move_left(self):
       self.snake.direction = Vector2(1, 0)
       self.snake.move_snake()
       self.assertEqual(self.snake.direction, Vector2(-1, 0))

#Collision Detection
class TestCollisionDetection(unittest.TestCase):
   def setUp(self):
       self.snake = SNAKE()
       self.fruit = Fruit()

   def test_fruit_collision(self):
       self.snake.body[0] = self.fruit.pos
       self.fruit.randomize()
       self.assertNotEqual(self.snake.body[0], self.fruit.pos)

#Game over condition
class TestGameOverCondition(unittest.TestCase):
   def setUp(self):
       self.snake = SNAKE()

   def test_out_of_bounds(self):
       self.snake.body[0].x = -1
       self.assertTrue(self.snake.check_fail())

#Scoring
class TestScoring(unittest.TestCase):
    def setUp(self):
       self.snake = SNAKE()

    def test_score_increase(self):
       previous_score = len(self.snake.body) - 3
       self.snake.add_block()
       current_score = len(self.snake.body) - 3
       self.assertGreater(current_score, previous_score)

if __name__ == '__main__':
    unittest.main()


