from collections import OrderedDict
from time import time


class Cache[T]:
    def __init__(self, max_size: int = 0) -> None:
        self.__store: OrderedDict = OrderedDict()
        self.__max_size: int = max_size

    def print_store(self) -> None:
        print('-' * 10 + 'Cache Values' + '-' * 10)
        if len(self.__store) == 0:
            print('Cache vazio!')

        expirated_keys = []

        for key in self.__store.keys():
            _, expiration = self.__store[key]
            now: float = time()
            if expiration and now > expiration:
                expirated_keys.append(key)

        for key in expirated_keys:
            del self.__store[key]
        for key in self.__store.keys():
            print(f'Chave: {key} Valor: {self.__store[key]}')

    def get(self, key: str) -> tuple[T, float] | None:
        if not self.__store.get(key):
            return None
        key_value, expiration = self.__store[key]
        now: float = time()
        if expiration and now > expiration:
            del self.__store[key]
            return None
        return key_value

    def set(self, key: str, data: T, ttl: int | None = None) -> None:
        if len(self.__store) == self.__max_size:
            self.__store.popitem(last=False)
        expires_at: float | None = time() + ttl if ttl else None
        self.__store[key] = (data, expires_at)
