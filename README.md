# Cap2-PyGame-Snake
# unit test
-Testing snake movement: The TestSnakeMovement class is a test case for testing the movement of the snake. It has a setUp method that is run before each test method. This method creates a new SNAKE object. The test methods (test_move_up, test_move_down, test_move_right, test_move_left) test the movement of the snake in different directions.
-Testing collision detection: The TestCollisionDetection class is a test case for testing the collision detection of the game. It has a setUp method that is run before each test method. This method creates a new SNAKE object and a new Fruit object. The test_fruit_collision method tests if the snake's head collides with the fruit.
-Testing game over condition: The TestGameOverCondition class is a test case for testing the game over condition of the game. It has a setUp method that is run before each test method. This method creates a new SNAKE object. The test_out_of_bounds method tests if the game is over when the snake goes out of bounds.
-Testing scoring: The TestScoring class is a test case for testing the scoring of the game. It has a setUp method that is run before each test method. This method creates a new SNAKE object. The test_score_increase method tests if the score increases when the snake eats a fruit.
