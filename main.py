# Hitting With Projectiles

def on_player1_button_a_pressed():
    global laser
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
        """),
        playership,
        75,
        0)
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    # As-destr-oid
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

# Accurate Life Counter

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

asteroid2: Sprite = None
laser: Sprite = None
myEnemy = 0
playership: Sprite = None
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
    """),
    0)
playership.set_position(20, 120 / 2)
playership.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
# Getting Controls
controller.move_sprite(playership, 140, 140)
playership.set_kind(SpriteKind.player)
# Enemies
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
    """),
    myEnemy)
asteroid.set_velocity(-55, 0)
asteroid.set_position(scene.screen_width(), randint(0, scene.screen_height()))
asteroid.set_kind(SpriteKind.enemy)

def on_update_interval():
    global asteroid2
    asteroid2 = sprites.create(img("""
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
        """),
        0)
    asteroid2.set_velocity(-55, 0)
    asteroid2.set_position(scene.screen_width(), randint(0, scene.screen_height()))
game.on_update_interval(500, on_update_interval)
