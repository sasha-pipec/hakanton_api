from functools import lru_cache

from service_objects.services import ServiceWithResult

from models_app.models import Card


class CardListService(ServiceWithResult):

    def process(self):
        self.result = self.collect_dict()
        return self

    def collect_dict(self):
        response_dict = {}
        for position in self._positions:
            response_dict[position] = self._cards.filter(position=position)
        return response_dict

    @property
    @lru_cache
    def _cards(self):
        return Card.objects.all()

    @property
    def _positions(self):
        return self._cards.values_list('position', flat=True).distinct()
