from nose.tools import *
from gothonweb.map import *

def test_room():
    gold = Room("GoldRoom", 
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
    
def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")
    
    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)
    
def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")
    
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up':start})
    
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
    
def test_gothon_game_map():
    assert_equal(START.go('shoot!'), corridor_shoot)
    assert_equal(START.go('dodge!'), corridor_dodge)
    assert_equal(START.go('*'), central_corridor)
    
    laser_fail = START.go('tell a joke')
    laser_success = START.go('tell a joke')
    
    assert_equal(laser_fail, laser_weapon_armory)
    assert_equal(laser_fail.go('gibberish'), laser_fail)
    count = 0
    while count < 9:
        laser_fail.go('gibberish')
        count += 1
    assert_equal(laser_fail.go('gibberish'), laser_weapon_armory_death)
    
    bridge = laser_success.go('penguin')
    assert_equal(bridge, the_bridge)
    assert_equal(bridge.go('*'), bridge)
    assert_equal(bridge.go('throw the bomb'), bridge_death)
    
    escape = bridge.go('slowly place the bomb')
    
    assert_equal(escape, escape_pod)
    assert_equal(escape.go('gibberish'), the_end_loser)
    assert_equal(escape.go('penguin'), the_end_winner)
    