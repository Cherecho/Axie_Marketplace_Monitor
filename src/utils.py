"""
    This file will not be used while running the bot
    It will be used to if need to update the parts of the Axies
"""

def store_cards():
    """
    Store the cards of the axie.
    """
    url = 'https://7b00e2d6-641e-45cb-a705-390f8d062064.mock.pstmn.io/api/v1/cards'
    cards = ''
    try:
        data = requests.get(url).json()
    except Exception as e:
        print(f'Error fetching cards {e}')
        exit (-1)
    try:
        for card in data:
            cards += card['part'] + '-' + card['name'] + ' '
    except Exception as e:
        print(f'Error storing cards {e}')
        exit (-1)
    return cards.lower()

def store_by_part(cards_list):
    """
    Store the cards of the axie.
    """
    try:
        cards = cards_list.split(' ')
        horn_cards= ''
        tail_cards= ''
        back_cards= ''
        eyes_cards= ''
        ear_cards= ''
        mouth_cards= ''

        for e in range(len(cards)):
            if 'horn' in cards[e]:
                horn_cards += '"'+cards[e] + '"' + ', '
            elif 'tail' in cards[e]:
                tail_cards += '"'+cards[e] + '"' + ', '
            elif 'back' in cards[e]:
                back_cards += '"'+cards[e] + '"' + ', '
            elif 'eyes' in cards[e]:
                eyes_cards += '"'+cards[e] + '"' + ', '
            elif 'ear' in cards[e]:
                ear_cards += '"'+cards[e] + '"' + ', '
            elif 'mouth' in cards[e]:
                mouth_cards += '"'+cards[e] + '"' + ', '
    except Exception as e:
        print(f'Error storing cards {e}')
        exit (-1)
    return horn_cards, tail_cards, back_cards, eyes_cards, ear_cards, mouth_cards