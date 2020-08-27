# Prerequisites and Setting Up
info.set_score(0)
info.set_life(3)

# Player's Sprite
playership = sprites.create(img("""

    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . b b . . . . . . . . . . . .
    . b b b b . . . . . . . . . . .
    . b b b b b . . . . . . . . . .
    . . b b b b b . . . . . . . . .
    . . b b b b b b . . . . . . . .
    . . b b b b b b b . . . . . . .
    . . b b b b b b . . . . . . . .
    . . b b b b b . . . . . . . . .
    . b b b b b . . . . . . . . . .
    . b b b b . . . . . . . . . . .
    . . b b . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
playership.set_position (20, 120/2)
playership.set_flag(SpriteFlag.StayInScreen, True)
#Getting Controls
controller.move_sprite(playership, 140, 140)

#Enemies