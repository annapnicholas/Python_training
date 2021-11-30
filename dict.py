sounds = {
    "cat": "meow", 
    "dog": "woof",
    "penguin": "meep",
    "fox": "screech",
    "duck": "honk",
    "sheep": "baaa",
         }


for sound in sounds.values():
    print(sound)
    
for animal in sounds.keys():
    print(animal)

for thing in sounds.items():
    print(thing)
    
for animal, sound in sounds.items():
    print(animal, "goes", sound)
