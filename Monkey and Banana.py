# Monkey and Banana Problem in AI

# Initial states
monkey = 'A'      # Monkey starts at corner A
box = 'B'         # Box is at corner B
banana = 'C'      # Bananas are hanging at corner C
monkey_on_box = False

def move(monkey_pos, target):
    print(f"Monkey moves from {monkey_pos} to {target}")
    return target

def push_box(monkey_pos, box_pos, target):
    print(f"Monkey pushes box from {box_pos} to {target}")
    return target, target

def climb_box():
    print("Monkey climbs onto the box")
    return True

def get_banana():
    print("Monkey takes the bananas! 🐒🍌")

# Step 1: Move monkey to box
monkey = move(monkey, box)

# Step 2: Push box to bananas
monkey, box = push_box(monkey, box, banana)

# Step 3: Climb onto the box
monkey_on_box = climb_box()

# Step 4: Get the banana
if monkey_on_box and monkey == banana:
    get_banana()
else:
    print("Monkey failed to get the bananas.")
