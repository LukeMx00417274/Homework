import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cut the Fruit and Avoid the Bombs!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
PLAYER_STARTING_LIVES = 3
PLAYER_NORMAL_VELOCITY = 5
PLAYER_BOOST_VELOCITY = 10
STARTING_BOOST_LEVEL = 200
STARTING_FRUIT_VELOCITY = 3
FRUIT_ACCELRATION = .5
BUFFER_DISTANCE = 100

score = 0
fruit_points = 0
fruits_eaten = 0
power_up_points = 0

player_lives = PLAYER_STARTING_LIVES
player_velocity = PLAYER_NORMAL_VELOCITY

boost_level = STARTING_BOOST_LEVEL
bomb_velocity = STARTING_FRUIT_VELOCITY
fruit_velocity = STARTING_FRUIT_VELOCITY
double_points_velocity = STARTING_FRUIT_VELOCITY
power_up_velocity = STARTING_FRUIT_VELOCITY
#Set colors
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Set fonts
font = pygame.font.Font("Ninjafont.ttf", 32)

#Set Text
points_text = font.render("Fruit Points: " + str(fruit_points), True, CYAN)
points_rect = points_text.get_rect()
points_rect.topleft = (10, 10)

score_text = font.render("Score: " + str(score), True, CYAN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 50)

title_text = font.render("Cut the Fruit and Avoid the Bombs!", True, CYAN)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

eaten_text = font.render("Fruit Sliced: " + str(fruits_eaten), True, CYAN)
eaten_rect = eaten_text.get_rect()
eaten_rect.centerx = WINDOW_WIDTH//2
eaten_rect.y = 50

lives_text = font.render("Lives: " + str(player_lives), True, CYAN)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

boost_text = font.render("Boost: " + str(boost_level), True, CYAN)
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 10, 50)

game_over_text = font.render("FINAL SCORE: " + str(score), True, CYAN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, CYAN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#Set sounds and music
sword_sound = pygame.mixer.Sound("swordsound.wav")
miss_sound = pygame.mixer.Sound("apple_bite.ogg")
double_points_sound = pygame.mixer.Sound("doublepoints.mp3")
power_up_sound = pygame.mixer.Sound("powerup.mp3")
bomb_sound = pygame.mixer.Sound("boom.mp3")
pygame.mixer.music.load("Ninjabackground.ogg")

#Set images
player_image_right = pygame.image.load("ninjasword.png")
player_image_left = pygame.image.load("ninjasword.png")

player_image = player_image_left
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH//2
player_rect.bottom = WINDOW_HEIGHT

fruit_image = pygame.image.load("fruitninja.png")
fruit_rect = fruit_image.get_rect()
fruit_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)

bomb_image = pygame.image.load("BOMB!.png")
bomb_rect = bomb_image.get_rect()
bomb_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)

double_points_image = pygame.image.load("doublepoints.jpg")
double_points_rect = double_points_image.get_rect()
double_points_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)

power_up_image = pygame.image.load("Arrow-Up-2-icon.png")
power_up_rect = power_up_image.get_rect()
power_up_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)

current_sprite = player_image
current_rect = player_rect

player_image_left2 = pygame.image.load("Ninjaswordbigger.png")
player_image_right2 = pygame.image.load("Ninjaswordbigger.png")

player_image2 = player_image_left2
player_rect2 = player_image.get_rect()
player_rect2.centerx = WINDOW_WIDTH//2
player_rect2.bottom = WINDOW_HEIGHT


#The main game loop
pygame.mixer.music.play()
running = True
while running:
    #Check if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_velocity
        player_image = player_image_left
        
    if keys[pygame.K_LEFT] and player_rect2.left > 0:
        player_rect2.x -= player_velocity
        player_image2 = player_image_left2

    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_WIDTH:
        player_rect.x += player_velocity
        player_image = player_image_right

    if keys[pygame.K_RIGHT] and player_rect2.right < WINDOW_WIDTH:    
        player_rect2.x += player_velocity
        player_image2 = player_image_right2

    if keys[pygame.K_UP] and player_rect.top > 100:
        player_rect.y -= player_velocity

    if keys[pygame.K_UP] and player_rect2.top > 100:
        player_rect2.y -= player_velocity
        
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += player_velocity

    if keys[pygame.K_DOWN] and player_rect2.bottom < WINDOW_HEIGHT:
        player_rect2.y += player_velocity

    #Engage Boost
    if keys[pygame.K_SPACE] and boost_level > 0:
        player_velocity = PLAYER_BOOST_VELOCITY
        boost_level -= 1
    else:
        player_velocity = PLAYER_NORMAL_VELOCITY
    
    #Move the fruit and update fruit points
    fruit_rect.y += fruit_velocity
    fruit_points = int(fruit_velocity*(WINDOW_HEIGHT - fruit_rect.y + 100))
    bomb_rect.y += fruit_velocity

   




    #Player missed the fruit
    if fruit_rect.y > WINDOW_HEIGHT:
        player_lives -= 1
        miss_sound.play()

        fruit_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        fruit_velocity = STARTING_FRUIT_VELOCITY

        current_rect.centerx = WINDOW_WIDTH//2
        player_rect.bottom = WINDOW_HEIGHT
        boost_level = STARTING_BOOST_LEVEL
    if bomb_rect.y > WINDOW_HEIGHT:
        bomb_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        bomb_velocity += 3
    if power_up_rect.y > WINDOW_HEIGHT:
        power_up_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        power_up_velocity += 3
        

    #Check for collisions
    if current_rect.colliderect(fruit_rect):
        score += fruit_points
        fruits_eaten += 1
        sword_sound.play()

        fruit_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        fruit_velocity += FRUIT_ACCELRATION
 
        boost_level += 25
        if boost_level > STARTING_BOOST_LEVEL:
            boost_level = STARTING_BOOST_LEVEL
    if current_rect.colliderect(bomb_rect):
        player_lives = 0
        bomb_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        bomb_velocity += FRUIT_ACCELRATION
        power_up_points = 0
        bomb_sound.play()
    if fruits_eaten != 0 and fruits_eaten % 5 == 0:
        double_points_rect.y += fruit_velocity
    else: 
        double_points_rect.y = 0
        double_points_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
    if double_points_rect.y > WINDOW_HEIGHT:
        double_points_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        double_points_velocity = 0
    if current_rect.colliderect(double_points_rect):
        double_points_sound.play()
        score += fruit_points * 2
        double_points_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)

    if player_lives == 0:
        power_up_points = 0

    #POWER UP    
    if fruits_eaten != 0 and fruits_eaten == 4:
        power_up_rect.y += fruit_velocity
    else: 
        power_up_rect.y = 0
        power_up_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)


    if current_rect.colliderect(power_up_rect):
        power_up_sound.play()
        power_up_rect.topleft = (random.randint(0, WINDOW_WIDTH - 32), -BUFFER_DISTANCE)
        power_up_velocity = 0
        power_up_points = 1
        if power_up_points == 1:
            current_sprite = player_image2
            current_rect = player_rect2
        else:
            current_sprite = player_image
            current_rect = player_rect
    







    #Update HUD
    points_text = font.render("Fruit Points: " + str(fruit_points), True, CYAN)
    score_text = font.render("Score: " + str(score), True, CYAN)
    eaten_text = font.render("Fruits Eaten: " + str(fruits_eaten), True, CYAN)
    lives_text = font.render("Lives: " + str(player_lives), True, CYAN)
    boost_text = font.render("Boost: " + str(boost_level), True, CYAN)

    #Check for game over
    if player_lives == 0:
        game_over_text = font.render("FINAL SCORE: " + str(score), True, CYAN)
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #Pause the game until the player presses a key, then reset the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #The player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0
                    fruits_eaten = 0
                    player_lives = PLAYER_STARTING_LIVES
                    boost_level = STARTING_BOOST_LEVEL
                    fruit_velocity = STARTING_FRUIT_VELOCITY
                    bomb_velocity = STARTING_FRUIT_VELOCITY
                    double_points_velocity = STARTING_FRUIT_VELOCITY
                    power_up_points = 0
                    current_sprite = player_image
                    current_rect = player_rect
                    pygame.mixer.music.play()
                    is_paused = False
                #The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #Fill the surface
    display_surface.fill(BLACK)

    #Blit the HUD
    display_surface.blit(points_text, points_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(eaten_text, eaten_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(boost_text, boost_rect)
    pygame.draw.line(display_surface, WHITE, (0, 100), (WINDOW_WIDTH, 100), 3)

    #Blit assests
    display_surface.blit(current_sprite, current_rect)
    display_surface.blit(fruit_image, fruit_rect)
    display_surface.blit(bomb_image, bomb_rect)
    display_surface.blit(double_points_image, double_points_rect)
    display_surface.blit(power_up_image, power_up_rect)

    #Update the display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()