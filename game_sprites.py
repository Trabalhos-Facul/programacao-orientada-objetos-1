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

        new_card_sprite.set_position_on(slot_key)
        self.slots[slot_key] = new_card_sprite
        self.add(new_card_sprite)

    def card_in(self, position):
        for card in list(self.slots.values()):
            if card != None and card.rect.collidepoint(position):
                return card
        return None

class Card(pygame.sprite.Sprite):
    HEIGHT = 500
    HEIGHT_OFFSET = 225

    def __init__(self, id_carta):
        pygame.sprite.Sprite.__init__(self)
        self.id = id_carta
        self.image = pygame.image.load(f'img/Card-Jitsu_Cards_full_{id_carta}.png').convert()
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
    
    def set_position_on(self, slot):
        self.rect.center = (self.HEIGHT_OFFSET + (slot * 125), (self.HEIGHT * 3) // 4)

class ScoreDrawer(pygame.sprite.Group):
    def __init__():
        pass