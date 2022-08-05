import requests


def fetch_marketplace():
    """
    Fetch the market data from the given url.
    """
    try:
        url = "https://graphql-gateway.axieinfinity.com/graphql"
        params = {"operationName": "GetAxieLatest",
            "variables": {
                'from': 0,
                'size': 1,
                'sort': "Latest",
                'auctionType': "Sale",
                'criteria': {
                    "parts": ["tail-yam", "horn-rose-bud"]
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

def format_market(data):
    """
    Format the market data.
    """
    axies = []
    return axies


data = fetch_market()
print(data)