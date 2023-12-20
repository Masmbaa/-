import pygame
import random


pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Гача")

icon = pygame.image.load("Иконка.png")
pygame.display.set_icon(icon)

main_color = (238, 190, 241)

card_width = 100
card_height = 150

clock = pygame.time.Clock()

ramka = pygame.image.load("рамка.PNG")
ramka = pygame.transform.scale(ramka, (card_width, card_height))


class Character_Deck:
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self) -> list[str]:
        """Создает список всей колоды с гача-картами"""
        С_deck = []
        elements = ['р', 'к', 'д', 'с', 'ф']

        for element in elements:
            С_deck.extend([element] * 15)

        return С_deck

    def hand_card(self) -> list[str]:
        """Выбирает 4 карты для руки и удаляет из колоды эти карты"""
        if not self.deck:
            raise ValueError('Раздаем карты из пустой колоды')

        hand = []
        for _ in range(4):
            card = random.choice(self.deck)
            hand.append(card)
            self.deck.remove(card)
        return hand

    def player_hand(self) -> list[str]:
        if not self.deck:
            raise ValueError('Раздаем карты из пустой колоды')

        phand = []
        for _ in range(4):
            card = random.choice(self.deck)
            phand.append(card)
            self.deck.remove(card)
        return phand

    def size_hand(self):
        """Задает х и у карт"""
        card_x = []
        for i in range(4):
            card_x.append(display_width / 2 - card_width * 2 + i * card_width)
        card_y = display_height - card_height - 50
        return card_x, card_y

    def card_images(self, hand_card):
        """Формирует изображения карт в руке"""
        hand_card_images = []
        for i in range(4):
            hand_card_images.append(pygame.image.load(f"гача карты/{hand_card[i]}.jpg"))
            hand_card_images[i] = pygame.transform.scale(hand_card_images[i], (card_width, card_height))
        return hand_card_images


    def players_card_images(self, player_hand):
        """Формирует изображения карт в руке противника"""
        hand_card_images = []
        for i in range(4):
            hand_card_images.append(pygame.image.load(f"задники/{player_hand[i]}/Рубашка.jpg"))
            hand_card_images[i] = pygame.transform.scale(hand_card_images[i], (card_width, card_height))
        return hand_card_images


    def size_players_hand(self):
        """Задает х и у карт"""
        card_x = []
        for i in range(4):
            card_x.append(display_width / 2 - card_width * 2 + i * card_width)
        card_y = 0 - card_height / 2
        return card_x, card_y


class Reward_Cards:
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self) -> list[str]:
        """ Выводит все возможные комбинации карт составленных из 2, 3 и 4 персонажей и цифры. """
        character = ['р', 'к', 'д', 'с', 'ф', 'д']
        color_ticket = ['р', 'с', 'ж', 'к']
        points = [3, 5, 6, 7, 12]
        count = [2, 3, 4]
        deck = []  # Множество для хранения уникальных комбинаций
        for i in range(len(count)):
            if count[i] == 2:
                for j in character:
                    deck.append(j * 2 + str(points[0]) + color_ticket[0])
            if count[i] == 3:
                deck.append('c' + 'р' + 'д' + str(points[1]) + color_ticket[1])
                deck.append('c' + 'р' + 'ф' + str(points[1]) + color_ticket[1])
                deck.append('c' + 'ф' + 'к' + str(points[1]) + color_ticket[0])
                deck.append('c' + 'ф' + 'к' + str(points[1]) + color_ticket[3])
                deck.append('c' + 'ф' + 'д' + str(points[1]) + color_ticket[2])
                deck.append('д' + 'к' + 'р' + str(points[1]) + color_ticket[2])
                deck.append('д' + 'к' + 'р' + str(points[1]) + color_ticket[3])
            if count[i] == 4:
                deck.append('к' + 'р' + 'ф' + 'д' + str(points[3]) + color_ticket[1])
                deck.append('д' + 'р' + 'ф' + 'д' + str(points[3]) + color_ticket[2])
                deck.append('к' + 'с' + 'д' + 'д' + str(points[3]) + color_ticket[3])

        return deck

    def table_card(self) -> list[str]:
        """Выбирает 4 карты для стола и удаляет из колоды эти карты"""
        if not self.deck:
            raise ValueError('Раздаем карты из пустой колоды')

        table = []
        for _ in range(4):
            card = random.choice(self.deck)
            table.append(card)
            self.deck.remove(card)
        return table



    def size_table(self):
        """Задает х и у карт"""
        card_x = []
        for i in range(4):
            card_x.append(display_width / 2 - card_width * 2.5 + i * card_width)
        card_y = display_height / 2 - card_height
        return card_x, card_y

    def card_table_images(self, table_card):
        """Формирует изображения карт на столе"""
        table_card_images = []
        for i in range(4):
            table_card_images.append(pygame.image.load(f"награды/{table_card[i]}.jpg"))
            table_card_images[i] = pygame.transform.scale(table_card_images[i], (card_width, card_height))
        table_card_images.append(pygame.image.load(f"награды/рубашка.jpg"))
        table_card_images[4] = pygame.transform.scale(table_card_images[4], (card_width, card_height))
        return table_card_images


# class Player_card(Character_Deck):
#     def __init__(self):
#         super().__init__()
#         self.player_hand()
#
#     def player_hand(self) -> list[str]:
#         if not self.deck:
#             raise ValueError('Раздаем карты из пустой колоды')
#
#         phand = []
#         for _ in range(4):
#             card = random.choice(self.deck)
#             phand.append(card)
#             self.deck.remove(card)
#         return phand



class Player:
    HAND_SIZE = 4

    def __init__(self):
        self.hand = []  # инициализируйте пустую раздачу для каждого игрока

    @staticmethod
    def create_list(deck: Character_Deck(), player_size: int):
        players = []  # Создайте пустой список для хранения игроков
        for _ in range(player_size):
            hand = deck.hand_card()  # Собирает колоду карт
            player = Player()
            player.hand = hand
            players.append(player)
        return players


def ran_game():
    с_deck = Character_Deck()
    hand_card_list = с_deck.hand_card()
    c_card_x, c_card_y = с_deck.size_hand()
    hand_card_images = с_deck.card_images(hand_card_list)
    players_hand_card_list = с_deck.player_hand()
    p_card_x, p_card_y = с_deck.size_players_hand()
    players_hand_card_images = с_deck.players_card_images(players_hand_card_list)
    r_deck = Reward_Cards()
    table_card_list = r_deck.table_card()
    r_card_x, r_card_y = r_deck.size_table()
    card_table_images = r_deck.card_table_images(table_card_list)



    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        display.fill(main_color)

        for x in range(4):
            display.blit(hand_card_images[x], (c_card_x[x] + x * 5, c_card_y, card_width, card_height))
            display.blit(ramka, (c_card_x[x] + x * 5, c_card_y, card_width, card_height))

        for x in range(4):
            display.blit(card_table_images[x], (r_card_x[x] + x * 5, r_card_y, card_width, card_height))
            display.blit(ramka, (r_card_x[x] + x * 5, r_card_y, card_width, card_height))
        display.blit(card_table_images[4], (r_card_x[3] + card_width + 20, r_card_y, card_width, card_height))
        display.blit(ramka, (r_card_x[3] + card_width + 20, r_card_y, card_width, card_height))

        for x in range(4):
            display.blit(players_hand_card_images[x], (p_card_x[x] + x * 5, p_card_y, card_width, card_height))
            display.blit(ramka, (p_card_x[x] + x * 5, p_card_y, card_width, card_height))
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()


ran_game()
