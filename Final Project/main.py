import pygame, sys, time, math
from scripts.UltraColor import *
from scripts.textures import *
from scripts.globals import *
from scripts.map_engine import *
from scripts.NPC import *
from scripts.player import *
from scripts.meloonatic_gui import *

pygame.init()

cSec = 0
cFrame = 0
FPS = 0
deltatime = 0

terrain = Map_Engine.load_map("maps\\world.map")



clock=pygame.time.Clock()

fps_font = pygame.font.Font("C:\\Windows\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky,(0, 0))
del sky

logo_img_temp = pygame.image.load("graphics\\logo.png")
# logo_img_temp = pygame.transform.scale(logo_img_temp, (239, 176))
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0, 0))
del logo_img_temp


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = 'Final Project'
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def count_fps():
    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime('%S')
        if FPS > 0:
            deltatime = 1 / FPS

create_window()


player = Player("Grimon")

player_w, player_h = player.width, player.height
player_x = ((window_width / 2 - player_w/ 2 - Globals.camera_x) / Tiles.Size)
player_y = ((window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)


#Initialize GUI
def Play():
    Globals.scene = "game"

def Exit():
    global isRunning
    isRunning = False

btnPlay = Menu.Button(text = "Play", rect = (0, 0, 300, 60),
                        tag = ("menu", None))
btnPlay.Left = window_width / 2 - btnPlay.Width / 2
btnPlay.Top = window_height / 2 - btnPlay.Height / 2
btnPlay.Command = Play

btnExit = Menu.Button(text = "Exit", rect = (0, 0, 300, 60),
                      tag = ("menu", None))
btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 3
btnExit.Command = Exit

menuTitle = Menu.Text(text = "Welcome to the Game", color = Color.Cyan,
                      font = Font.Large)
menuTitle.Left, menuTitle.Top = window_width / 2 - menuTitle.Width / 2, 0


logo = Menu.Image(bitmap = logo_img)
logo.Left = window_width / 2 - logo.Width / 2
logo.Top = window_height / 2 - logo.Height / 2


isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move=1
                player.facing = "north"
            if event.key == pygame.K_s:
                Globals.camera_move=2
                player.facing = "south"
            if event.key == pygame.K_a:
                Globals.camera_move=3
                player.facing = "east"
            if event.key == pygame.K_d:
                Globals.camera_move=4
                player.facing = "west"


        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #Left Click

                #Handle button click events
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command()       #DO BUTTON EVENT
                        btn.Rolling = False
                        break   #EXIT LOOP



    #Render Scene
    if Globals.scene == "game":

        #LOGIC
        if Globals.camera_move == 1:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
                Globals.camera_y += 100 * deltatime
        elif Globals.camera_move == 2:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= 100 * deltatime
        elif Globals.camera_move ==3:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
                Globals.camera_x += 100 * deltatime
        elif Globals.camera_move ==4:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= 100 * deltatime

        player_x = ((window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
        player_y = ((window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)


        #Render Graphics
        window.blit(Sky, (0, 0))

        window.blit(terrain, (Globals.camera_x, Globals.camera_y))

        player.render(window, (window_width / 2 - player_w / 2,
                               window_height /2 - player_h / 2))

    #PROCESS MENU
    elif Globals.scene == "menu":
        window.fill(Color.Fog)


        logo.Render(window)
        menuTitle.Render(window)

        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                btn.Render(window)


    show_fps()

    pygame.display.update()

    count_fps()

    # clock.tick(30)

pygame.quit()
sys.exit()