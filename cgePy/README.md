
# Licence
Firstly, I prefer some credit for all programs made with cgePy, though this is your choice.
Claiming that this library's code is yours is explicitly NOT ALLOWED. If you would like to develop cgePy, please contact me at **lion712yt@gmail.com**.
***
# Basic Usage
First off, try this code:
```py
grid = cgepy.Grid()
grid.Update()
```
It will print (show the most recent version of) the grid!\
Now,
```py
grid.write(1,cgepy.RED+"  ")
#"  " is a blank pixel on the grid.
#Each pixel must be EXACTLY two characters long!
grid.Update()
```
The result will be the same as before, but the 2nd 'pixel' on the grid red. Try experimenting with this for a little.

## Maps

Now, this process of writing to the grid is very repetitive, right? Well, there's a solution to that: Maps.

```py
grid2 = cgepy.Map(
    '''
BB BB BB BB BB BB BB BB BB BB
BB BG BG BG BG BG BG BG BG BB
BB BG BG BG BG BG BG BG BG BB
BB BG BG BG BG BG BG BG BG BB
BB BG BG BG BG BG BG BG BG BB
BB BG BG BG BG BG BG BG BG BB
BB BG BG BG BG BG BG BG BG BB 
BB BG BG BG BG BG BG BG BG BB
BB BG BG BG BG BG BG BG BG BB
BB BB BB BB BB BB BB BB BB BB
''')
grid2.Paint()
grid2.Update()
```

Okay, that's a little confusing right?\
You might need to wait until I'm finished making this README. (sorry!)\
For now, try and figure out what each part of the code does.

## Sprites

Of course, you'll need a way to animate objects.\
Try this code:

```py
import time

grid = cgepy.Grid()
grid.Update()

sprite = cgepy.Sprite()

sprite.Drop(grid)
time.sleep(1)

grid.Update()
```

Do you see the red pixel in the corner of the grid? There's your sprite!

Now, try adding this to your code:

```py
time.sleep(1)
sprite.Move("down")
grid.Update()
```

I don't need to explain this.
To remove a sprite:
```py
grid.sprites.remove(sprite)
```
***
### Changing the sprite's color
***
When you create a sprite, you can provide the color as a parameter:
 ```py
 sprite = cgepy.Sprite(color=CYAN)
 ```
***
 Or, you can try this after a sprite is made:
 ```py
sprite.Color(CYAN)
 ```
 Alternately:

 ```py
 sprite.sprite = CYAN+"  "
```
You can replace `"  "` with anything, as long as it is two characters long.


# Customization

Now that you've learned the basics cgePy, you might get ask, "Can I change the color of the background" or "How do I make the grid bigger?"

Well, look no further as your problem is solved!
***
First off, cgePy uses two variables for this:
`gridsize`,  `background`.

 Please note that the gridsize should be a perfect square (9, 25, 100, etc) or else cgePy may not work.\
 `background` should be set to a background color variable. In cgePy, `red` = text color, `RED` = background color, etc. You can also use ansi codes if you need.
***

Sadly, I haven't finished with this README yet. However, I wish you good luck, and hope this helped!
