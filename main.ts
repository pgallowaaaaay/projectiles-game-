//  Hitting With Projectiles
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_player1_button_a_pressed() {
    
    laser = sprites.createProjectileFromSprite(img`
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
        `, playership, 75, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    sprite.destroy()
    otherSprite.destroy(effects.fire, 100)
    //  As-destr-oid
    info.changeScoreBy(1)
})
//  Accurate Life Counter
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
let asteroid2 : Sprite = null
let laser : Sprite = null
let myEnemy = 0
let playership : Sprite = null
//  Prerequisites and Setting Up
info.setScore(0)
info.setLife(3)
//  Player's Sprite
playership = sprites.create(img`
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
    `, 0)
playership.setPosition(20, 120 / 2)
playership.setFlag(SpriteFlag.StayInScreen, true)
//  Getting Controls
controller.moveSprite(playership, 140, 140)
playership.setKind(SpriteKind.Player)
//  Enemies
let asteroid = sprites.create(img`
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
    `, myEnemy)
asteroid.setVelocity(-55, 0)
asteroid.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
asteroid.setKind(SpriteKind.Enemy)
game.onUpdateInterval(500, function on_update_interval() {
    
    asteroid2 = sprites.create(img`
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
        `, 0)
    asteroid2.setVelocity(-55, 0)
    asteroid2.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
})
