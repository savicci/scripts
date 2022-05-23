function createGate() {
    builder.mark()
    builder.turn(TurnDirection.Right)
    builder.move(FORWARD, 2)
    builder.mark()

    // start building
    builder.move(UP, 4)
    builder.turn(TurnDirection.Left)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 4)
    builder.move(DOWN, 4)
    builder.tracePath(OBSIDIAN)

    builder.turn(TurnDirection.Left)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 1)
    builder.mark()

    // closed gate
    builder.move(FORWARD, 2)
    builder.raiseWall(IRON_BARS, 4)

    builder.move(FORWARD, 2)
    builder.mark()
}

function createTower(){
    builder.mark()

    builder.turn(TurnDirection.Right)
    builder.move(FORWARD, 2)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 4)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 4)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 4)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 2)
    builder.turn(TurnDirection.Left)

    builder.raiseWall(COBBLESTONE, 9)
    builder.mark()
}

function towerAndPositionChange(){
    createTower()
    builder.move(FORWARD, 2)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 2)
    builder.mark()
}

function createFundamentals() {
    builder.move(FORWARD, 5)
    builder.raiseWall(STONE, 5)

    towerAndPositionChange()

    builder.move(FORWARD, 10)
    builder.raiseWall(STONE, 5)

    towerAndPositionChange()

    builder.move(FORWARD, 15)
    builder.raiseWall(STONE, 5)

    towerAndPositionChange()

    builder.move(FORWARD, 10)
    builder.raiseWall(STONE, 5)

    towerAndPositionChange()

    builder.move(FORWARD, 4)
    builder.raiseWall(STONE, 5)
}

function createGround(){
    builder.move(DOWN, 1)
    builder.move(BACK, 8)
    builder.move(RIGHT, 2)
    builder.mark()
    
    for(let i=0; i<9; ++i){
        builder.move(FORWARD, 23)
        builder.move(LEFT, 1)
        builder.move(BACK, 23)
        builder.move(LEFT, 1)
    }
    builder.move(FORWARD, 23)
    builder.move(LEFT, 1)

    builder.tracePath(GRASS)

    builder.move(RIGHT, 17)
    builder.move(BACK, 16)
    builder.mark()
}

function createWindows(){
    builder.move(UP, 3)
    builder.mark()
    builder.fill(GLASS)

    builder.move(FORWARD, 8)
    builder.mark()
    builder.fill(GLASS)

    builder.move(LEFT, 14)
    builder.mark()
    builder.fill(GLASS)

    builder.move(BACK, 8)
    builder.mark()
    builder.fill(GLASS)

    builder.move(RIGHT, 14)
    builder.mark()
}

function createMoat(){
    builder.move(FORWARD, 2)
    builder.move(DOWN, 3)
    builder.turn(TurnDirection.Right)
    builder.mark()

    for(let i=0; i<2; ++i){
        builder.move(FORWARD, 5)
        builder.move(LEFT, 1)
        builder.move(BACK, 5)
        builder.move(LEFT, 1)
    }
    builder.move(FORWARD, 5)

    builder.tracePath(PLANKS_OAK)
    builder.mark()
}

function createWater(){
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 1)
    builder.move(LEFT, 2)
    builder.mark()
    builder.move(FORWARD, 10)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 20)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 25)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 20)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 9)
    builder.tracePath(WATER)

    builder.move(FORWARD, 6)
    builder.move(RIGHT, 1)
    builder.mark()
    builder.move(FORWARD, 11)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 21)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 26)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 21)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 9)
    builder.tracePath(WATER)
    builder.mark()

    builder.move(FORWARD, 6)
    builder.move(RIGHT, 1)
    builder.mark()
    builder.move(FORWARD, 12)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 24)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 29)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 24)
    builder.turn(TurnDirection.Left)
    builder.move(FORWARD, 11)
    builder.tracePath(GRASS)
}

player.onChat("castle", function() {
    builder.teleportTo(pos(0, 0, -5))

    createGate()
    createFundamentals()
    createGround()
    createWindows()
    createMoat()
    createWater()

    builder.move(BACK, 11)
    builder.move(DOWN, 1)
    builder.mark()

    for(let i=0; i<12; ++i){
        builder.move(FORWARD, 29)
        builder.move(LEFT, 1)
        builder.move(BACK, 29)
        builder.move(LEFT, 1)
    }
    builder.move(FORWARD, 29)
    builder.tracePath(GRASS)
})