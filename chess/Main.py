# need to install pygame
import pygame

# part 1 : set up game loops and variable images
pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH,HEIGHT])
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freeansbold.tff',50)
pygame.display.set_caption('Chess game')
timer = pygame.time.Clock()
fps = 60
  # game variables and images
white_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn']  
white_locations =[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                  (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

black_pieces = ['rook','knight','bishop','king','queen','bishop','knight','rook',
                'pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                  (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
captured_piece_white = []
captured_piece_black = []

#  white turn: no selection: 1-whites turn piece selected; 2- black turn piece selected'
turn_step = 0
selection = 100
valid_moves = []

black_queen = pygame.transform.scale(pygame.image.load('chess/assets/black_queen.png'),(89,80))
black_queen_small = pygame.transform.scale(black_queen, (45,45))
black_bishop = pygame.transform.scale(pygame.image.load('chess/assets/black_bishop.png'),(89,80))
black_bishop_small = pygame.transform.scale(black_bishop, (45,45))
black_king = pygame.transform.scale(pygame.image.load('chess/assets/black_king.png'),(89,80))
black_king_small = pygame.transform.scale(black_king, (45,45))
black_pawn = pygame.transform.scale(pygame.image.load('chess/assets/black_pawn.png'),(65,65))
black_pawn_small = pygame.transform.scale(black_pawn, (45,45))
black_rook = pygame.transform.scale(pygame.image.load('chess/assets/black_rook.png'),(89,80))
black_rook_small = pygame.transform.scale(black_rook, (45,45))

white_queen = pygame.transform.scale(pygame.image.load('chess/assets/white_queen.png'),(89,80))
white_queen_small = pygame.transform.scale(white_queen, (45,45))
white_bishop = pygame.transform.scale(pygame.image.load('chess/assets/white_bishop.png'),(89,80))
white_bishop_small = pygame.transform.scale(white_bishop, (45,45))
white_king = pygame.transform.scale(pygame.image.load('chess/assets/white_king.png'),(89,80))
white_king_small = pygame.transform.scale(white_king, (45,45))
white_pawn = pygame.transform.scale(pygame.image.load('chess/assets/white_pawn.png'),(65,65))
white_pawn_small = pygame.transform.scale(white_pawn, (45,45))
white_rook = pygame.transform.scale(pygame.image.load('chess/assets/white_rook.png'),(89,80))
white_rook_small = pygame.transform.scale(white_rook, (45,45))

white_images = [white_queen, white_bishop ,white_king, white_pawn,white_rook]
black_images = [black_queen, black_bishop ,black_king, black_pawn,black_rook]

piece_list = ['queen', 'bishop' ,'king', 'pawn','rook']

# draw main game loop
def draw_board(): 
  for i in range(32):
    column = i % 4
    row = i//4
    if row % 2 == 0:
      pygame.draw.rect(screen, 'light gray', [(600-column*200), row*100,100,100])
    else:
      pygame.draw.rect(screen, 'light gray', [(700-column*200), row*100,100,100])
    pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 800])
    pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 800],5)
    pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT],5)
    status_text = ['White, select a Piece to move', 'white, select a destination',
                   'black, select a Piece to move', 'black, select a destination']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'),(20,8 20))
# part 2 : main game loop
    # event handling
run = True

while run:
    timer.tick(fps)
    screen.fill('dark grey')
    draw_board()
    # event handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    
    pygame.display.flip()
pygame.quit()