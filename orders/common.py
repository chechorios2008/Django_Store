from enum import Enum


class OrderStatus(Enum):
    CREATED = 'CREATED'
    PLAYED = 'PLATED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'


choices = [(tag, tag.value) for tag in OrderStatus]