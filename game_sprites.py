import pygame

class GameDrawer:
    FPS = 60
    WIDTH = 800
    HEIGHT = 500

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        dojo = pygame.image.load(f'img/dojo.png')
        self.bg_img = pygame.transform.scale(dojo, (self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Desafio Ninja")
        pygame.init()   

        self.player_hand = Hand()
        self.player_score = pygame.sprite.Group()
        self.npc_score = pygame.sprite.Group()
        self.played_cards = pygame.sprite.Group()
        self.result = pygame.sprite.Group()

    def tick(self):
        self.display.blit(self.bg_img, (0, 0))
        self.clock.tick(self.FPS)
    
    def draw(self):
        self.player_hand.draw(self.display)
        self.player_score.draw(self.display)
        self.npc_score.draw(self.display)
        self.played_cards.draw(self.display)
        self.result.draw(self.display)
        pygame.display.flip()

    def draw_result_msg(self, winner):
        self.result.add(FinalMsg(winner))

    def card_in(self, position):
        return self.player_hand.card_in(position)

class Hand(pygame.sprite.Group):
    def __init__(self) -> None:
        self.slots = { 0: None, 1: None, 2: None, 3: None}
        super().__init__(self)

    def buy(self, card_sprite):
        empty_slot = list(self.slots.values()).index(None)

        card_sprite.set_position_on(empty_slot)
        self.slots[empty_slot] = card_sprite
        self.add(card_sprite)
    
    def replace(self, old_card_sprite, new_card_sprite):
        slot_key = list(self.slots.values()).index(old_card_sprite)
        self.remove(old_card_sprite)

        if new_card_sprite:
            new_card_sprite.set_position_on(slot_key)
            self.slots[slot_key] = new_card_sprite
            self.add(new_card_sprite)

    def card_in(self, position):
        for card in list(self.slots.values()):
            if card != None and card.rect.collidepoint(position):
                return card
        return None

class CardSprite(pygame.sprite.Sprite):
    def __init__(self, card):
        if card and card.id > 0:
            pygame.sprite.Sprite.__init__(self)
            self.id = card.id
            self.image = self.get_img()
            self.rect = self.image.get_rect()
        else:
            self.rect = None
    
    def get_img(self):
        image = pygame.image.load(f'img/Card-Jitsu_Cards_full_{self.id}.png').convert()
        return pygame.transform.scale(image, (100, 120))

class HandCard(CardSprite):
    def set_position_on(self, slot):
        HEIGHT = 500
        HEIGHT_OFFSET = 225
        if self.rect:
            self.rect.center = (HEIGHT_OFFSET + (slot * 125), (HEIGHT * 3) // 4)

class PlayedCard(CardSprite):
    def __init__(self, card):
        super().__init__(card)
        if self.rect:
            self.owner = card.owner
            self.rect.center = self.rect_center_of()
    
    def rect_center_of(self):
        if self.owner == 'player':
            return 200, 250
        else:
            return 600, 250
        
class ScoreDrawer(pygame.sprite.Group):
    def __init__():
        pass

class FinalMsg(pygame.sprite.Sprite):
    def __init__(self, winner):
        pygame.sprite.Sprite.__init__(self)

        if winner == "player":
            print('Player Wins!')
            self.image = pygame.image.load(f'img/you_wins.png').convert()
        else:
            print('NPC Wins!')
            self.image = pygame.image.load(f'img/you_lost.png').convert()

        self.rect = self.image.get_rect()

        self.rect.center = 400, 250