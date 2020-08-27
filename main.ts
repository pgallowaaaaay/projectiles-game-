//  Prerequisites and Setting Up
info.setScore(0)
info.setLife(3)
//  Player's Sprite
let playership = sprites.create(img`

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
`)
playership.setPosition(20, 120 / 2)
playership.setFlag(SpriteFlag.StayInScreen, true)
// Getting Controls
controller.moveSprite(playership, 140, 140)
// Enemies
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
`)
asteroid.setVelocity(-55, 0)
asteroid.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
game.onUpdateInterval(500, function on_update_interval() {
    let asteroid = sprites.create(img`
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
    `)
    asteroid.setVelocity(-55, 0)
    asteroid.setPosition(scene.screenWidth(), randint(0, scene.screenHeight()))
})
