type Product = dict[str, str]


def binary_search(dataset: list[Product], target: str) -> list[int]:
    """
    Realiza busca binária e retorna todos os índices de um elemento em um dataset ordenado.

    Argumentos:
        dataset: dataset ordenado de elementos.
        target: Elemento a ser buscado.

    Retorno:
        Uma lista com os todos os índices do elemento target no dataset.
    """
    if not dataset:
        return []

    indexes = []
    start, end = 0, len(dataset) - 1

    while start <= end:
        middle = (start + end) // 2
        if target in dataset[middle]['name']:
            indexes.append(middle)

            # Busca à esquerda
            i = middle - 1
            while i >= 0 and target in dataset[i]['name']:
                indexes.append(i)
                i -= 1

            # Busca à direita
            i = middle + 1
            while i < len(dataset) and target in dataset[i]['name']:
                indexes.append(i)
                i += 1

            return sorted(indexes)  # Retorna os índices ordenados

        elif dataset[middle]['name'] < target:
            start = middle + 1
        else:
            end = middle - 1

    return []  # Retorna dataset vazia se não encontrar
