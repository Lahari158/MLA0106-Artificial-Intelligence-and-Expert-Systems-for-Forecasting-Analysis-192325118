rooms = {'A':'dirty','B':'dirty'}
pos = 'A'
while 'dirty' in rooms.values():
    if rooms[pos]=='dirty':
        print(f"Cleaning {pos}")
        rooms[pos]='clean'
    pos = 'B' if pos=='A' else 'A'
print("All rooms clean:", rooms)
