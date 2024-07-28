import pygame
import math
import sys
from fractal import Fractal


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# constants
WIDTH, HEIGHT = pygame.display.get_surface().get_size()
BLACK = (0, 0, 0)

l_system_text = sys.argv[1]
start = int(sys.argv[2]), int(sys.argv[3])
length = int(sys.argv[4])
ratio = float(sys.argv[5])


with open(l_system_text) as f:
    axiom = f.readline()
    num_rules = int(f.readline())
    rules = {}
    for i in range(num_rules):
        rule = f.readline().split(" ")
        rules[rule[0]] = rule[1]
    angle = math.radians(int(f.readline())) 
    

def main():
    pygame.mouse.set_visible(False)

    fractal = Fractal(axiom, rules, angle, start, length, ratio)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]:
                screen.fill(BLACK)
                fractal.draw(screen)
                fractal.generate()
            
            if keystate[pygame.K_ESCAPE]:
                running = False
        
        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()