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
