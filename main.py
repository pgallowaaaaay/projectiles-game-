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
asteroid = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . c c . . . . .
    . . . . . . . . c c . c c c . .
    . . . . . . . c c b c b c c c .
    . . . . . . c c c c c c b c c .
    . . . c c c c c b c c b . c . .
    . . c . b b c c c c c c c c . .
    . . c b c c c c c c . b c . . .
    . . c c c c c . b c c c . . . .
    . . . c c c . c . . . . . . . .
    . . . . c c c . . . . . . . . .
    . . . . . c . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
asteroid.set_velocity(-55, 0)
asteroid.set_position(scene.screen_width(), randint(0, scene.screen_height()))

def on_update_interval():
    asteroid = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . c c . . . . .
    . . . . . . . . c c . c c c . .
    . . . . . . c c c b c b c c c .
    . . . . . c . c c c c c b c c .
    . . . c c . c c b c c b . c . .
    . . c . b b c c c c c c c c . .
    . . c b c c c c c c . b c . . .
    . . c c c c c . b c c c . . . .
    . . . c c c . c . . . . . . . .
    . . . . c c c . . . . . . . . .
    . . . . . c . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    """))
    asteroid.set_velocity(-55, 0)
    asteroid.set_position(scene.screen_width(), randint(0, scene.screen_height()))





game.on_update_interval(500, on_update_interval)

#Hitting With Projectiles 

def on_button_event_a_pressed():
    laser = sprites.create_projectile_from_sprite(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . 8 6 6 9 . . . . . . .
        . . . . . 8 6 6 9 . . . . . . .
        . . . . . 8 6 6 9 . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """), playership, 75, 0)
controller.player1.on_button_event(ControllerButton.A, ControllerButtonEvent.PRESSED, on_button_event_a_pressed)