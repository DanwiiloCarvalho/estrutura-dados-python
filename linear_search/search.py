type Product = dict[str, str]


def linear_search(dataset: list[Product], target: str) -> list[int]:
    if not dataset:
        return []

    result: list[int] = []
    for index, data in enumerate(dataset):
        if target in data['name']:
            result.append(index)

    return result
