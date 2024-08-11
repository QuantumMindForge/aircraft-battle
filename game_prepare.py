import pygame
import random
from pygame.locals import *

bullet = []
score = 0
def ans():
    return score

class Back(object):
    def __init__(self, s1):
        self.s1 = pygame.image.load(s1)

    def tie_tu(self, screen):
        screen.blit(self.s1, (0, 0))
        pygame.display.set_caption("飞机大战")

class hero_plane(object):
    def __init__(self, s1, s2, destroy1, destroy2, destroy3, destroy4):
        self.s1 = pygame.image.load(s1)
        self.s2 = pygame.image.load(s2)
        self.destroy_images = [pygame.image.load(destroy1), pygame.image.load(destroy2), pygame.image.load(destroy3), pygame.image.load(destroy4)]
        self.y = 700
        self.x = 590
        self.state = "live"
        self.destroy_index = 0

    def hero_move(self, screen):
        if self.state == "live":
            screen.blit(self.s1, (self.x, self.y))
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN or event.type == KEYUP:
                    if event.key == K_UP and self.y > 3:
                        self.y -= 20
                    elif event.key == K_DOWN and self.y < 720:
                        self.y += 20
                    elif event.key == K_LEFT and self.x > 51:
                        self.x -= 20
                    elif event.key == K_RIGHT and self.x < 1170:
                        self.x += 20
                    elif event.key == K_SPACE:
                        bullet.append({"x": self.x, "y": self.y})

            for i in bullet:
                screen.blit(self.s2, (i["x"] - 15, i["y"]))
                screen.blit(self.s2, (i["x"] + 55, i["y"]))
                i["y"] -= 70
        elif self.state == "destroyed":
            if self.destroy_index < len(self.destroy_images):
                screen.blit(self.destroy_images[self.destroy_index], (self.x, self.y))
                self.destroy_index += 1
            else:
                self.state = "done"

    def check_collision(self, enemy):
        if enemy[1] == "enemy2":
            if enemy[0].state == "live" and self.x < enemy[0].x + 30 and self.x + 30 > enemy[0].x and self.y < enemy[0].y + 30 and self.y + 30 > enemy[0].y:
                self.state = "destroyed"
                return True
            return False
        elif enemy[1] == "enemy1":
            if enemy[0].state == "live" and self.x < enemy[0].x + 30 and self.x + 30 > enemy[0].x and self.y < enemy[0].y + 30 and self.y + 30 > enemy[0].y:
                self.state = "destroyed"
                return True
            return False
        elif enemy[1] == "enemy3":
            if enemy[0].state == "live" and self.x < enemy[0].x + 80 and self.x + 80 > enemy[0].x and self.y < enemy[0].y + 80 and self.y + 80 > enemy[0].y:
                self.state = "destroyed"
                return True
            return False


class enemy1_plane(object):
    def __init__(self, s1, s2, s3, s4, s5):
        self.s1 = pygame.image.load(s1)
        self.s2 = pygame.image.load(s2)
        self.s3 = pygame.image.load(s3)
        self.s4 = pygame.image.load(s4)
        self.s5 = pygame.image.load(s5)
        self.state = "live"
        self.y = 0
        self.x = random.randint(0, 1280-62)
        self.v = random.randint(5, 15)
        self.num = 0
        self.hit_count = 0

    def enemy_move(self, screen):
        global score
        blow = [self.s2, self.s3, self.s4, self.s5]
        for i in bullet:
            if (i["x"] - 15 - 20 <= self.x <= i["x"] - 15 + 20 or i["x"] + 55 - 40 <= self.x <= i["x"] + 55 + 40) and i["y"] <= self.y <= i["y"] + 60:
                screen.blit(blow[0], (self.x, self.y))
                self.hit_count += 1
                bullet.remove(i)
                if self.hit_count >= 2:
                    self.state = "dead"
                    score += 1

        if self.state == "live":
            screen.blit(self.s1, (self.x, self.y))
            self.y += self.v
            if self.y > 853:  # 如果敌机超出屏幕，重置其位置
                self.y = 0
                self.x = random.randint(0, 1280-62)
                self.v = random.randint(5, 25)
        elif self.state == "dead":
            if self.num < 4:
                screen.blit(blow[self.num], (self.x, self.y))
                self.num += 1
            else:
                self.state = "done"

class enemy2_plane(object):
    def __init__(self, s1, s2, s3, s4, s5):
        self.s1 = pygame.image.load(s1)
        self.s2 = pygame.image.load(s2)
        self.s3 = pygame.image.load(s3)
        self.s4 = pygame.image.load(s4)
        self.s5 = pygame.image.load(s5)
        self.state = "live"
        self.y = 0
        self.x = random.randint(0, 1280-62)
        self.v = random.randint(5, 20)
        self.num = 0
        self.hit_count = 0

    def enemy_move(self, screen):
        global score
        blow = [self.s2, self.s3, self.s4, self.s5]
        for i in bullet:
            if (i["x"] - 15 - 25 <= self.x <= i["x"] - 15 + 25 or i["x"] + 55 - 45 <= self.x <= i["x"] + 55 + 45) and i["y"] <= self.y <= i["y"] + 80:
                screen.blit(blow[0], (self.x, self.y))
                self.hit_count += 1
                bullet.remove(i)
                if self.hit_count >= 4:
                    self.state = "dead"
                    score += 2

        if self.state == "live":
            screen.blit(self.s1, (self.x, self.y))
            self.y += self.v
            if self.y > 853:  # 如果敌机超出屏幕，重置其位置
                self.y = 0
                self.x = random.randint(0, 1280-62)
                self.v = random.randint(5, 20)
        elif self.state == "dead":
            if self.num < 4:
                screen.blit(blow[self.num], (self.x, self.y))
                self.num += 1
            else:
                self.state = "done"

class enemy3_plane(object):
    def __init__(self, s1, s2, s3, s4, s5, s6, s7):
        self.s1 = pygame.image.load(s1)
        self.s2 = pygame.image.load(s2)
        self.s3 = pygame.image.load(s3)
        self.s4 = pygame.image.load(s4)
        self.s5 = pygame.image.load(s5)
        self.s6 = pygame.image.load(s6)
        self.s7 = pygame.image.load(s7)
        self.state = "live"
        self.y = 0
        self.x = random.randint(0, 1280 - 62)
        self.v = random.randint(5, 10)
        self.num = 0
        self.hit_count = 0

    def enemy_move(self, screen):
        global score
        blow = [self.s2, self.s3, self.s4, self.s5, self.s6, self.s7]
        for i in bullet:
            if (i["x"] - 15 - 110 <= self.x <= i["x"] - 15 + 110 or i["x"] + 55 - 135 <= self.x <= i["x"] + 55 + 135) and i["y"] <= self.y <= i["y"] + 250:
                screen.blit(blow[0], (self.x, self.y))
                self.hit_count += 1
                bullet.remove(i)
                if self.hit_count >= 10:  # 需要6次击中
                    self.state = "dead"
                    score += 8

        if self.state == "live":
            screen.blit(self.s1, (self.x, self.y))
            self.y += self.v
            if self.y > 853:  # 如果敌机超出屏幕，重置其位置
                self.y = 0
                self.x = random.randint(0, 1280 - 62)
                self.v = random.randint(5, 10)
        elif self.state == "dead":
            if self.num < 6:
                screen.blit(blow[self.num], (self.x, self.y))
                self.num += 1
            else:
                self.state = "done"
