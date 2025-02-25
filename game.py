import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("first game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

fart = [pygame.image.load('fart-1.png'), pygame.image.load('fart-2.png'), pygame.image.load('fart-3.png'), pygame.image.load('fart-4.png'), pygame.image.load('fart-5.png'), pygame.image.load('fart-6.png'), pygame.image.load('fart-7.png'), pygame.image.load('fart-8.png'), pygame.image.load('fart-9.png')]

bg = pygame.image.load('bg.jpg')

char = pygame.image.load('standing.png')

pygame.time.delay(100)


clock = pygame.time.Clock()

screenwith=500
x=50
y=400
width=64
height=64
boost=10
vel=5
boostBol=False
#boostCount=5
left=False
right=False
walkCount=0

isJump=False
jumpCount=10


def reDrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if boostBol and right:
        fartpic=fart[walkCount//3]
        fartpic=pygame.transform.scale(fartpic, (100,100))
        win.blit(fartpic, (x-30, y-10))
        walkCount += 1
    if boostBol and left:
        fartpic=fart[walkCount//3]
        fartpic=pygame.transform.scale(fartpic, (100,100))
        win.blit(fartpic, (x+30, y-10))
        walkCount += 1
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
    pygame.display.update()

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
     
#    if not(boostBol):
#        if keys[pygame.K_DOWN]:
#
#            boostBol=True
#            right = False
#            left = False
#            walkcount=0
#    elif boostBol:
#        if boostCount <=0 and keys[pygame.K_RIGHT]:
#            x+=boost
#            boostCount -=1
#        elif boostCount <= 0 and keys[pygame.K_LEFT]:
#            X-=boost
#            boostcount -=1
#        else:
#            boostBol=False
#            boostCount=5
    if keys[pygame.K_LEFT] and x != vel:
        if keys[pygame.K_DOWN]:
            x-=boost
            left=True
            right=False
            boostBool=True
        else:
            x -= vel
            left=True
            right=False
            boostBol=False
    elif keys[pygame.K_RIGHT] and x <= (screenwith-width-vel):
        if keys[pygame.K_DOWN]:
            x+=boost
            right=True
            left=False
            boostBol=True
        else:
            x += vel
            right=True
            left=False
            boostBol=False
    else:
        boostBol=False
        right=False
        left==False
        walkCount=0 

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkcount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    reDrawGameWindow()

pygame.quit()
