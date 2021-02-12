import os
import keyboard

class Map:
    def __init__(self):
        self.map = [[" " for i in range(34)]for i in range(40)]


    def update(self, thing, x, y):  
        self.map[y][x] = thing


    def draw(self):
        for layer in self.map:
            print(layer)


game_map =  Map()

class Player:
    def __init__(self):
        self.x = 1
        self.y = 38
        self.player = input("Enter your nickname: ").upper()
        try:
            self.player = self.player[0]
        except:
            pass


    def draw(self):
        game_map.update(self.player, self.x, self.y)


    def move(self):
            if keyboard.is_pressed("RIGHT"):
                self.x += 1
                game_map.map[self.y][self.x - 1] = " "
            if keyboard.is_pressed("LEFT"):
                self.x -= 1
                game_map.map[self.y][self.x + 1] = " "
            if keyboard.is_pressed("UP"):
                self.y -= 1
                game_map.map[self.y + 1][self.x] = " "
            if keyboard.is_pressed("DOWN"):
                self.y += 1
                game_map.map[self.y - 1][self.x] = " "


    def boundries(self):
        if self.x >= 33:
            self.x = 33
        if self.x <= 0:
            self.x = 0
        if self.y <= 38:
            self.y = 38
        if self.y >= 39:
            self.y = 38

player = Player()


class Bullet:
    def __init__(self):
        self.x = player.x
        self.y = player.y
        self.bullet = "*"               


class Game:
    def __init__(self):
        self.bullets = []


    def generate_bullet(self):
        if keyboard.is_pressed("w"):
            self.bullets.append(Bullet())



    def shoot(self):
        if self.bullets:
            for bullet in game.bullets:
                game_map.map[bullet.y - 1][bullet.x] = bullet.bullet
                game_map.map[bullet.y + 1][bullet.x] = " "
                bullet.y -= 1

                if bullet.y <= 1:
                    game_map.map[1][bullet.x] = " "
                    game_map.map[0][bullet.x] = " "


    def bullet_boundries(self):
        for b in self.bullets:
            if b.x >= 33:
                self.bullets.remove(b)
            if b.x <= 0:
                self.bullets.remove(b)
            if b.y <= 0:
                self.bullets.remove(b)
            if b.y >= 39:
                self.bullets.remove(b)


game = Game()



while True:
    game_map.draw()
    os.system("cls")
    player.draw()
    player.move()
    player.boundries()

    game.generate_bullet()
    game.shoot()
    game.bullet_boundries()