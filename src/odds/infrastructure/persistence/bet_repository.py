from odds.domain.entities.bet import Bet


class BetRepository(object):

    def get(self, bet_id):
        bet = Bet('x1', 2)
        bet.id = 1
        return bet
