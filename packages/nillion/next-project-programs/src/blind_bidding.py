from nada_dsl import *

def nada_main():
    seller = Party(name="Seller")
    bidder1 = Party(name="Bidder1")
    bidder2 = Party(name="Bidder2")

    seller_price = SecretInteger(Input(name="seller_price", party=seller))
    bid1 = SecretInteger(Input(name="bid1", party=bidder1))
    bid2 = SecretInteger(Input(name="bid2", party=bidder2))

    diff1 = seller_price - bid1
    diff2 = seller_price - bid2

    is_bidder1_winner = diff1 <= diff2

    return [
        Output(is_bidder1_winner, "is_bidder1_winner", seller),
        Output(seller_price, "seller_price", seller)
    ]