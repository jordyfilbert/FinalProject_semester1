import pygame

pygame.init()


class Tiles:
    Size = 32

    Blocked = []

    Blocked_Types = ["3"]

    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False

    def Load_Textures(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap,(0, 0))
        return surface

    Grass = Load_Textures("graphics\\grass.png", Size)

    Stone = Load_Textures("graphics\\stone.png", Size)

    Water = Load_Textures("graphics\\water.png", Size)

    Texture_Tags = {"1" : Grass, "2" : Stone, "3" : Water}
