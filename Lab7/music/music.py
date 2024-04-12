import datetime
import pygame as pg
pg.init()

size = [500, 500]
center = [250, 250]
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

pg.mixer.music.load("Then I See You [muzmo.ru].mp3")
pg.mixer.music.play()

volume = pg.mixer.music.get_volume()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                if(pg.mixer.music.get_busy()):
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_DOWN:
                if(volume > 0):
                    volume -= 0.1
                pg.mixer.music.set_volume(volume)
            elif event.key == pg.K_UP:
                if(volume < 1):
                    volume += 0.1
                pg.mixer.music.set_volume(volume)
    pg.display.flip()
    clock.tick(30)

pg.quit()