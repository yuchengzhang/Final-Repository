from random import randint

class Room(object):

    def __init__(self, name, description, code=None, tries=None, override=None):
        self.name = name
        self.description = description
        self.code = code
        self.tries = tries 
        self.override = override
        self.paths = {}
        
    def go(self, direction):
        if self.name == "Laser Weapon Armory": 
            if direction == self.override or direction == self.code:
                return self.paths.get('go', None) 
            elif self.tries == 0:
                return self.paths.get('*', None)
            else:
                self.tries -= 1
                return self
                
        elif self.name == "Escape Pod":
            if direction == self.override or direction == self.code:
                return self.paths.get('go', None)
            else:
                return self.paths.get('*', None)
        else:
            return self.paths.get(direction, None)
        
    def add_paths(self, paths):
        self.paths.update(paths)
        
def laser_weapon_code_generator():
    code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
    return code
        
def pod_generator():
    pod = "%d" % randint(1,5)
    return pod
    
central_corridor = Room("Central Corridor", 
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an 
escape pod.

You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body.  He's blocking the door to the
Armory and about to pull a weapon to blast you.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding.  It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container.  There's a keypad lock on the box
and you need the code to get the bomb out.  If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb.  The code is 3 digits.
""", laser_weapon_code_generator(), 10, 'penguin')

the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot.

You burst onto the Bridge with the neutron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship.  Each of them has an even uglier
clown costume than the last.  They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
""")

escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.
You inch backward to the door, open it, and then carefully
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pod to
get off this tin can.

You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes.  It seems like
hardly any Gothons are on the ship, so your run is clear of
interference.  You get to the chamber with the escape pods, and
now need to pick one to take.  Some of them could be damaged
but you don't have time to look.  There's 5 pods, which one
do you take?
""", randint(1,5), None, 'penguin')

the_end_winner = Room("The End",
"""
You jump into the escape pod and hit the eject button.
The pod easily slides out into space heading to
the planet below.  As it flies to the planet, you look
back and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same
time.  You won!
""")

the_end_loser = Room("The End",
"""
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body
into jam jelly.
""")

escape_pod.add_paths({
    'go': the_end_winner,
    '*': the_end_loser
})

bridge_death = Room("You died.", 
"""
In a panic you throw the bomb at the group of Gothons
and make a leap for the door.  Right as you drop it a
Gothon shoots you right in the back killing you.
As you die you see another Gothon frantically try to disarm
the bomb. You die knowing they will probably blow up when
it goes off.
""")

the_bridge.add_paths({
    'throw the bomb': bridge_death,
    'slowly place the bomb': escape_pod,
    '*': the_bridge
})

laser_weapon_armory_death = Room("You died.",
"""
The lock buzzes one last time and then you hear a sickening
melting sound as the mechanism is fused together.
You decide to sit there, and finally the Gothons blow up the
ship from their ship and you die.
""")

laser_weapon_armory.add_paths({
    'go': the_bridge,
    '*': laser_weapon_armory_death
})

corridor_shoot = Room("You died.", 
"""
Quick on the draw you yank out your blaster and fire it at the Gothon.
His clown costume is flowing and moving around his body, which throws
off your aim.  Your laser hits his costume but misses him entirely. This
completely ruins his brand new costume his mother bought him, which
makes him fly into an insane rage and blast you repeatedly in the face until
you are dead.  Then he eats you.
""")

corridor_dodge = Room("You died.",
"""
Like a world class boxer you dodge, weave, slip and slide right
as the Gothon's blaster cranks a laser past your head.
In the middle of your artful dodge your foot slips and you
bang your head on the metal wall and pass out.
You wake up shortly after only to die as the Gothon stomps on
your head and eats you.
""")


central_corridor.add_paths({
    'shoot!': corridor_shoot,
    'dodge!': corridor_dodge,
    'tell a joke': laser_weapon_armory,
    '*': central_corridor
})

START = central_corridor
LASER = laser_weapon_armory
BRIDGE = the_bridge
ESCAPE_POD = escape_pod