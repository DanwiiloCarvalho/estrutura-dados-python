from .cache import Cache


if __name__ == '__main__':

    cache: Cache = Cache(5)
    user_counter: int = 0
    option: str | None = None
    while True:
        option = input('Gostaria de adicionar um item? s/n: ')
        if option == 's':
            name: str = input('Digite o nome: ')
            ttl_input: str = input('Defina o TTL do item: ')
            ttl: int | None = None
            if ttl_input == '':
                ttl = None
            else:
                ttl = int(ttl_input)

            user_counter += 1
            cache.set(f'user:{user_counter}', {'name': name}, ttl)

        cache.print_store()
        option = input('Gostaria de finalizar o programa? s/n: ')
        if option == 's':
            break
