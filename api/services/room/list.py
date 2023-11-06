from service_objects.services import ServiceWithResult

from models_app.models import Room


class RoomListService(ServiceWithResult):

    def process(self):
        self.result = self._rooms
        return self

    @property
    def _rooms(self):
        return Room.objects.filter(status=Room.WAITED)
