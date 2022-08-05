import requests
from datetime import datetime as dt
from src.discord import discord_webhook

BUFFER_AXIES = 1

class Monitor:

    def __init__(self):
        self.data_dic = self.fetch_marketplace(BUFFER_AXIES)
        self.data_list = []

    def fetch_marketplace(self, limit: int) -> dict:
        """
        Fetch the market data from the given url.
        """
        try:
            url = "https://graphql-gateway.axieinfinity.com/graphql"
            params = {"operationName": "GetAxieLatest",
                "variables": {
                    'from': 1,
                    'size': limit,
                    'sort': "PriceAsc",
                    'auctionType': "Sale",
                    'criteria': {
                        'parts': []
                    }
                },
                "query": """query GetAxieLatest(
                    $auctionType: AuctionType,
                    $criteria: AxieSearchCriteria,
                    $from: Int,
                    $sort: SortBy,
                    $size: Int,
                    $owner: String)
                    {\n  axies(
                        auctionType: $auctionType,
                        criteria: $criteria,
                        from: $from,
                        sort: $sort,
                        size: $size,
                        owner: $owner
                        ){\n    total\n    results {\n      ...AxieRowData\n      __typename\n    }\n    __typename\n  }\n}\n\n
                        fragment AxieRowData on Axie {\n  id\n  image\n  class\n  name\n  genes\n  owner\n  class\n  stage\n  title\n  breedCount\n  level\n
                        parts {\n    ...AxiePart\n    __typename\n  }\n
                        stats {\n    ...AxieStats\n    __typename\n  }\n
                        auction {\n    ...AxieAuction\n    __typename\n  }\n  __typename\n}\n\n
                        fragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\n
                        fragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\n
                        fragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\n
                        fragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"""
                        }
            data = requests.post(url, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'authorization': ""},
                    json=params).json()


        except Exception as e:
            print(f'Error Axie Marketplace requests {e}')
            exit (-1)

        return data

    def get_id(self, data: dict, index: int) -> str:
        """
        Get the id of the axie.
        """
        if data == {}:
            return 0
        return data['data']['axies']['results'][index]['id']

    def get_url(self, data: dict, index: int) -> str:
        """
        Get the url of the axie.
        """
        return 'https://marketplace.axieinfinity.com/axie/'+data['data']['axies']['results'][index]['id']

    def get_image(self, data: dict, index: int) -> str:
        """
        Get the image of the axie.
        """
        return str(data['data']['axies']['results'][index]['image'])

    def get_all_cards(self, data: dict, index: int) -> list:
        """
        Print all the cards of the axie.
        """
        cards = []
        data = data['data']['axies']['results'][index]
        for card in data['parts']:
            cards.append(card['id'])
        return cards

    # def get_stats(self, data: dict, index: int) -> dict:
    #     """
    #     Get the stats of the axie.
    #     """
    #     stats = []
    #     data = data['data']['axies']['results'][index]['stats']
    #     stats.append(data['hp'])
    #     stats.append(data['speed'])
    #     stats.append(data['skill'])
    #     stats.append(data['morale'])
    #     return stats

    def get_price(self, data: dict, index: int) -> float:
        """
        Get the price of the axie.
        """
        return data['data']['axies']['results'][index]['auction']['currentPriceUSD']

    def run(self) -> None:
        """
        Run the axie class.
        """
        ts_start = dt.utcnow()
        self.data = self.fetch_marketplace(BUFFER_AXIES)

        ts_delta = (dt.utcnow() - ts_start).total_seconds()
        print('Fetching completed in {} seconds with {} axies to stored.'.format(ts_delta, BUFFER_AXIES))
        ts_start = dt.utcnow()
        for e in range(len(self.data['data']['axies']['results'])):
            url = self.get_url(self.data, e)
            image = self.get_image(self.data, e)
            cards = self.get_all_cards(self.data, e)
            price = self.get_price(self.data, e)

            # Uncommend to get stats
            # print('Buy link: {}'.format(url))
            # print('Img preview link: {}'.format(image))
            # print('Cards: \n   Eyes:   {}\n   Ears:   {}\n   Back:   {}\n   Mouth:  {}\n   Horn:   {}'.format(cards[0], cards[1], cards[2], cards[3], cards[4]))
            # print('Price: {} USD'.format(price))

            ts_start_dw = dt.utcnow()
            discord_webhook('CLICK TO OPEN THE MARKETPLACE',url, cards, image, price)
            ts_delta_dw = (dt.utcnow() - ts_start_dw).total_seconds()
            print('Discord webhook completed in {} seconds.'.format(ts_delta_dw))
        print(len(self.data['data']['axies']['results']))
        ts_delta = (dt.utcnow() - ts_start).total_seconds()
        print('Completed in {} seconds with {} axies stored.'.format(ts_delta, BUFFER_AXIES))
        exit(-1)

