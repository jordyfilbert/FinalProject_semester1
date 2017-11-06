import pygame
from scripts.textures import *

class Map_Engine:

    def add_tile(tile, pos, addTo):
        addTo.blit(tile, (pos[0] * Tiles.Size, pos[1] * Tiles.Size))

    def load_map(file):
        with open(file, "r") as mapfile:
            map_data = mapfile.read()

        #Read Map Data
        map_data = map_data.split("-")  #Split into list of tiles

        map_size = map_data[len(map_data) - 1]  #Get Map Dimensions
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * Tiles.Size
        map_size[1] = int(map_size[1]) * Tiles.Size

        tiles = []

        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":")) #Split pos from texture

        for tile in tiles:
            tile[0] = tile[0].split(",")    #Split pos into list
            pos = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p)  #Convert to integer

            tiles[tiles.index(tile)] = (pos, tile[1])   #Save to tile list


        #Create Terrain
        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in Tiles.Texture_Tags:
                Map_Engine.add_tile(Tiles.Texture_Tags[tile[1]], tile[0], terrain)


            if tile[1] in Tiles.Blocked_Types:
                Tiles.Blocked.append(tile[0])



        return terrain