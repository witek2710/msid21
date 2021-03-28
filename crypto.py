import requests
import time

DELAY_OF_EXPLORING_DATA = 20
LIMIT = 5


def connectToCryptoApi(crypto, currency):
    response = requests.get('https://bitbay.net/API/Public/' + crypto + currency + '/orderbook.json')
    if response.status_code == 200:
        return response.json()
    else:
        return None


def printCryptoOffers(jsonResponse, crypto, currency, limit):
    if jsonResponse is not None:
        print(crypto + '/' + currency + ', BUY OFFERS:')
        print('[RATE, AMOUNT]')
        for buyOffer in jsonResponse['bids'][:limit]:
            print(buyOffer)
        print(crypto + '/' + currency + ', SELL OFFERS:')
        print('[RATE, AMOUNT]')
        for sellOffer in jsonResponse['asks'][:limit]:
            print(sellOffer)


def calculateDifferenceRatio(crypto, currency, limit):
    jsonResponse = connectToCryptoApi(crypto, currency)
    buyPrice = 0
    sellPrice = 0
    if jsonResponse is not None:
            buyPrice = jsonResponse['bids'][0]
            sellPrice = jsonResponse['asks'][0]
    differenceRatio = 1 - ((sellPrice - buyPrice) / buyPrice)
    return differenceRatio


def showDifferenceRatio(crypto, currency, delayOfExploringData, limit):
    while True:
        differenceRatio = calculateDifferenceRatio(crypto, currency, limit)
        print('Difference ratio in %: ' + crypto + '/' + currency + ': ', differenceRatio)
        time.sleep(delayOfExploringData)


def main():
    printCryptoOffers(connectToCryptoApi('BTC', 'USD'), 'BTC', 'USD', LIMIT)
    printCryptoOffers(connectToCryptoApi('LTC', 'USD'), 'LTC', 'USD', LIMIT)
    printCryptoOffers(connectToCryptoApi('DASH', 'USD'), 'DASH', 'USD', LIMIT)

    # showDifferenceRatio('BTC', 'USD', DELAY_OF_EXPLORING_DATA, 1)
    showDifferenceRatio('LTC', 'USD', DELAY_OF_EXPLORING_DATA, 1)
    # showDifferenceRatio('DASH', 'USD', DELAY_OF_EXPLORING_DATA, 1)


if __name__ == '__main__':
    main()
