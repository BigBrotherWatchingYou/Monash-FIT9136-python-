# need to install pygame
import pygame

# part 1 : set up game loops and variable images
pygame.init()
screen = pygame.display.set_mode([800,800])
font = pygame.font.Font('freesansbold.ttf', 20)
pygame.display.set_caption('Chess game')
timer = pygame.time.Clock(100)
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

black_queen = pygame.image.scale(pygame.image.load('chess/assets/black queen.png'),(89,80))
black_queen_small = pygame.image.scale(pygame.image.load('chess/assets/black queen.png'),(45,45))
black_bishop = pygame.image.scale(pygame.image.load('chess/assets/black bishop.png'),(89,80))
black_bishop_small = pygame.image.scale(pygame.image.load('chess/assets/black bishop.png'),(45,45))
black_king = pygame.image.scale(pygame.image.load('chess/assets/black king.png'),(89,80))
black_king_small = pygame.image.scale(pygame.image.load('chess/assets/black king.png'),(45,45))
black_pawn = pygame.image.scale(pygame.image.load('chess/assets/black pawn.png'),(89,80))
black_pawn_small = pygame.image.scale(pygame.image.load('chess/assets/black pawn.png'),(45,45))
black_rook = pygame.image.scale(pygame.image.load('chess/assets/black rook.png'),(89,80))
black_rook_small = pygame.image.scale(pygame.image.load('chess/assets/black rook.png'),(45,45))

white_queen = pygame.image.scale(pygame.image.load('chess/assets/white queen.png'),(89,80))
white_queen_small = pygame.image.scale(pygame.image.load('chess/assets/white queen.png'),(45,45))
white_bishop = pygame.image.scale(pygame.image.load('chess/assets/white bishop.png'),(89,80))
white_bishop_small = pygame.image.scale(pygame.image.load('chess/assets/white bishop.png'),(45,45))
white_king = pygame.image.scale(pygame.image.load('chess/assets/white king.png'),(89,80))
white_king_small = pygame.image.scale(pygame.image.load('chess/assets/white king.png'),(45,45))
white_pawn = pygame.image.scale(pygame.image.load('chess/assets/white pawn.png'),(89,80))
white_pawn_small = pygame.image.scale(pygame.image.load('chess/assets/white pawn.png'),(45,45))
white_rook = pygame.image.scale(pygame.image.load('chess/assets/white rook.png'),(89,80))
white_rook_small = pygame.image.scale(pygame.image.load('chess/assets/white rook.png'),(45,45))


# part 2 : main game loop
    # event handling
run = True
while run:
    timer.tick(fps)
    screen.fill('black')
    
    # event handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    
    pygame.display.flip()
pygame.quit()