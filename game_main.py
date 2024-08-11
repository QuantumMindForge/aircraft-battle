import time
from game_prepare import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 853), 0, 32)
    background = Back('images/back.png')
    hero = hero_plane('images/me1.png', 'images/bullet.png', 'images/me_destroy_1.png','images/me_destroy_2.png',
                      'images/me_destroy_3.png','images/me_destroy_4.png')

    enemies = []

    while len(enemies) < 5:  # 初始化敌机数量为5
        enemy_type = random.choices(['enemy1', 'enemy2', 'enemy3'], [8, 2, 1])[0]
        if enemy_type == 'enemy1':
            enemies.append((enemy1_plane('images/enemy1.png', "images/enemy1_down1.png", "images/enemy1_down2.png",
                                         "images/enemy1_down3.png", "images/enemy1_down4.png"), "enemy1"))
        elif enemy_type == 'enemy2':
            enemies.append((enemy2_plane('images/enemy2.png', "images/enemy2_down1.png", "images/enemy2_down2.png",
                                         "images/enemy2_down3.png", "images/enemy2_down4.png"), "enemy2"))
        elif enemy_type == 'enemy3':
            enemies.append((enemy3_plane('images/enemy3_n1.png', "images/enemy3_down1.png", "images/enemy3_down2.png",
                                         "images/enemy3_down3.png", "images/enemy3_down4.png",
                                         "images/enemy3_down5.png",
                                         "images/enemy3_down6.png"), "enemy3"))

    font = pygame.font.SysFont("Arial", 36)

    while True:
        background.tie_tu(screen)
        hero.hero_move(screen)

        for enemy in enemies:
            enemy[0].enemy_move(screen)
            if hero.check_collision(enemy):
                return  # 碰撞发生，游戏结束

        enemies = [enemy for enemy in enemies if enemy[0].state != "done"]  # 移除已被摧毁的敌机

        while len(enemies) < 5:  # 保持敌机数量为5
            enemy_type = random.choices(['enemy1', 'enemy2', 'enemy3'], [8, 2, 1])[0]
            if enemy_type == 'enemy1':
                enemies.append((enemy1_plane('images/enemy1.png', "images/enemy1_down1.png", "images/enemy1_down2.png",
                                            "images/enemy1_down3.png", "images/enemy1_down4.png"),"enemy1"))
            elif enemy_type == 'enemy2':
                enemies.append((enemy2_plane('images/enemy2.png', "images/enemy2_down1.png", "images/enemy2_down2.png",
                                            "images/enemy2_down3.png", "images/enemy2_down4.png"),"enemy2"))
            elif enemy_type == 'enemy3':
                enemies.append((enemy3_plane('images/enemy3_n1.png', "images/enemy3_down1.png", "images/enemy3_down2.png",
                                            "images/enemy3_down3.png", "images/enemy3_down4.png", "images/enemy3_down5.png",
                                             "images/enemy3_down6.png"),"enemy3"))

        score_text = font.render(f"Score: {ans()}", True, (255, 255, 255))  # 计分
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        time.sleep(0.1)

if __name__ == '__main__':
    main()
