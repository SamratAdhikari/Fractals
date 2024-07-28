import pygame
import math
import colorsys

class Fractal:
    def __init__(self, axiom, rules, angle, start, length, ratio):
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.start = start
        self.x, self.y = start
        self.length = length
        self.ratio = ratio
        self.theta = math.pi / 2
        self.positions = []

    def __str__(self):
        return self.axiom

    def hsv2rgb(self, h, s, v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

    def generate(self):
        self.x, self.y = self.start
        self.theta = math.pi / 2
        self.length *= self.ratio

        new_axiom = ""
        for char in self.axiom:
            mapped = self.rules.get(char, char)
            new_axiom += mapped

        self.axiom = new_axiom

    def draw(self, screen):
        hue = 0

        for char in self.axiom:
            if char == 'F':
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
                color = self.hsv2rgb(hue, 1, 1)

                pygame.draw.line(screen, color, (self.x, self.y), (x2, y2), 2)
                self.x, self.y = x2, y2

            elif char == "+":
                self.theta += self.angle

            elif char == "-":
                self.theta -= self.angle

            elif char == "[":
                self.positions.append({'x': self.x, 'y': self.y, 'theta': self.theta})

            elif char == "]":
                position = self.positions.pop()
                self.x, self.y, self.theta = position['x'], position['y'], position['theta']

            hue += 0.0005
