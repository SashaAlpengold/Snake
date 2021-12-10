import pygame as p
import random

p.init()

dis_width = 800
dis_height = 600
dis = p.display.set_mode((dis_width, dis_height))
p.display.set_caption('Snake')

blue = (50, 153, 213)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)

clock = p.time.Clock()

snake_block = 10
snake_speed = 15

font_style = p.font.SysFont("TimesNewRoman", 25)
score_font = p.font.SysFont("comicsansms", 35)


def show_score(score):
    value = score_font.render(f"Ваш счет: {score}", True, yellow)
    dis.blit(value, [0, 0])


def draw_snake(snake_list):
    for i in snake_list:
        p.draw.rect(dis, black, [i[0], i[1], snake_block, snake_block])


def show_message(msg, color):
    mesg = font_style.render(msg, True, color)
    message_width = mesg.get_width()
    dis.blit(mesg, [(dis_width - message_width) / 2, dis_height / 2])


def set_game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = random.randrange(0, dis_width - snake_block, snake_block)
    food_y = random.randrange(0, dis_height - snake_block, snake_block)

    while not game_over:

        while game_close:
            dis.fill(black)
            show_message("Вы проиграли! Нажмите Q для выхода или C чтобы снова сыграть", red)
            show_score(length_of_snake - 1)
            p.display.update()

            for event in p.event.get():
                if event.type == p.KEYDOWN:
                    if event.key == p.K_q:
                        game_close = False
                        game_over = True
                    if event.key == p.K_c:
                        set_game_loop()

        for event in p.event.get():
            if event.type == p.QUIT:
                game_over = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT and x1_change <= 0:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == p.K_RIGHT and x1_change >= 0:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == p.K_UP and y1_change <= 0:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == p.K_DOWN and y1_change >= 0:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)
        p.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        draw_snake(snake_list)
        show_score(length_of_snake - 1)

        p.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = random.randrange(0, dis_width - snake_block, snake_block)
            food_y = random.randrange(0, dis_height - snake_block, snake_block)
            length_of_snake += 1

        clock.tick(snake_speed)

    p.quit()
    quit()


if __name__ == '__main__':
    set_game_loop()
