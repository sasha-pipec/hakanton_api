from functools import lru_cache

from service_objects.services import ServiceWithResult

from models_app.models import Card

INDEX = {
    Card.TOP: [10, 9, 8, 7, 6, 5, 4, 3, 2],
    Card.RIGHT: [20, 19, 18, 17, 16, 15, 14, 13, 12],
    Card.BOTTOM: [30, 29, 28, 27, 26, 25, 24, 23, 22],
    Card.LEFT: [40, 39, 38, 37, 36, 35, 34, 33, 32],
    Card.CORNER: [31, 21, 11, 1],
}


class CardListService(ServiceWithResult):

    def process(self):
        self.result = self.collect_dict()
        return self

    def collect_dict(self):
        response_dict = {}
        for position in self._positions:
            cards = self._cards.filter(position=position)
            for cart in cards:
                cart.index = INDEX[position].pop(-1)
                cart.save()
            response_dict[position] = cards
        return response_dict

    @property
    @lru_cache
    def _cards(self):
        return Card.objects.all()

    @property
    def _positions(self):
        return self._cards.values_list('position', flat=True).distinct()
