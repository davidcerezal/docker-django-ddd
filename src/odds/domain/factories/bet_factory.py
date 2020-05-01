from odds.infrastructure.persistence.bet_repository import BetRepository
from odds.domain.entities.bet import Bet


class BetFactory(object):

    @classmethod
    def create(cls, price):
        if price is None or price < 0:
            raise Exception('...')

        bet = Bet('x1', price)

        # Other rules here

        return bet
