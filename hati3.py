#```python
import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I Love You 💜")

clock = pygame.time.Clock()

BLACK = (5, 0, 12)
PURPLE = (170, 70, 255)
LILAC = (210, 160, 255)
PINK = (255, 130, 220)
WHITE = (255, 240, 255)

small_font = pygame.font.SysFont("Arial", 13, bold=True)
medium_font = pygame.font.SysFont("Arial", 17, bold=True)
big_font = pygame.font.SysFont("Georgia", 48, bold=True)

# Kalp koordinatları
points = []

for i in range(900):
    t = i / 900 * 2 * math.pi

    x = 16 * math.sin(t) ** 3

    y = (
        13 * math.cos(t)
        - 5 * math.cos(2*t)
        - 2 * math.cos(3*t)
        - math.cos(4*t)
    )

    points.append((x, y))

# Kalbin içini doldur
particles = []

for scale in [0.35, 0.55, 0.75, 1.0]:
    for x, y in points[::3]:
        particles.append((x * scale, y * scale))

random.shuffle(particles)

# Yazılar
words = [
    "I LOVE YOU",
    "LOVE",
    "I LOVE YOU",
    "FOREVER",
    "I LOVE YOU"
]

texts = []

for i, (x, y) in enumerate(particles):
    texts.append({
        "x": x,
        "y": y,
        "delay": i * 0.012,
        "size": random.choice([small_font, medium_font]),
        "word": random.choice(words),
        "color": random.choice([PURPLE, LILAC, PINK]),
    })

start_time = pygame.time.get_ticks()

running = True

while running:

    screen.fill(BLACK)

    elapsed = (pygame.time.get_ticks() - start_time) / 1000

    pulse = 1 + math.sin(elapsed * 2.5) * 0.025

    center_x = WIDTH // 2
    center_y = HEIGHT // 2 - 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Yazıları sırayla oluştur
    for item in texts:

        if elapsed < item["delay"]:
            continue

        x = center_x + item["x"] * 18 * pulse
        y = center_y - item["y"] * 17 * pulse

        color = item["color"]

        text = item["size"].render(
            item["word"], True, color
        )

        # Neon parıltı
        glow = item["size"].render(
            item["word"], True, PURPLE
        )

        glow.set_alpha(70)

        screen.blit(glow, (x-2, y-2))
        screen.blit(glow, (x+2, y+2))
        screen.blit(text, (x, y))

    # Kalp tamamlandıktan sonra ortadaki yazı
    if elapsed > len(texts) * 0.012 + 1:

        title = big_font.render(
            "I Love You", True, WHITE
        )

        rect = title.get_rect(
            center=(center_x, center_y)
        )

        glow = big_font.render(
            "I Love You", True, PURPLE
        )

        screen.blit(glow, rect.move(-3, 0))
        screen.blit(glow, rect.move(3, 0))
        screen.blit(title, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
