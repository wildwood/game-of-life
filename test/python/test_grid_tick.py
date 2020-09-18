import unittest

from src.game_of_life import GridTick

class TestGridTick(unittest.TestCase):

    def test_init(self):
        tick = GridTick(3, 3, [(1,1)])

    def test_empty_grid(self):
        tick = GridTick(3, 3, [])
        grid = ((False, False, False), (False, False, False), (False, False, False))
        self.assertEqual(grid, tick.grid)
        
    def test_grid(self):
        tick = GridTick(3, 3, [(1,1)])
        grid = ((False, False, False), (False, True, False), (False, False, False))
        self.assertEqual(grid, tick.grid)

    def test_simple_trim(self):
        tick = GridTick(3, 3, [(1,1)])
        trim = ((True,),)
        self.assertEqual(trim, tick.trim())

    def test_simple_trim2(self):
        tick = GridTick(3, 3, [(1,1), (2,1)])
        trim = ((True,),(True,))
        self.assertEqual(trim, tick.trim())

    def test_simple_tick(self):
        tick = GridTick(3, 3, [(0,1),(1,1), (2,1)])
        new_tick_trim = ((False,False,False),(True,True,True),(False,False,False))
        self.assertEqual(new_tick_trim, tick.tick().grid)
        old_new_tick_trim = ((False,True,False),(False,True,False),(False,True,False))
        self.assertEqual(old_new_tick_trim, tick.tick().tick().grid)

if __name__ == '__main__':
    unittest.main()
