from linear_search.search import linear_search
import json
import os

type Product = dict[str, str]

if __name__ == '__main__':

    while True:
        json_data: list[Product] | None = None

        current_script_directory = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_script_directory, 'dataset.json')

        with open(json_path) as json_file:
            json_data = json.load(json_file)
            json_data_lower = list(map(
                lambda product: {'id': product['id'], 'name': product['name'].lower()}, json_data))

        input_search = input('Busque um produto: ')
        search_result: list[int] = linear_search(
            json_data_lower, input_search)
        if len(search_result) > 0:
            for index in search_result:
                print(
                    f'\nID do Produto: {json_data[index]['id']} | Nome: {json_data[index]['name']}\n')
        else:
            print('Produto não encontrado!')

        option: str = input('Deseja continuar buscando? s/n: ')
        if option == 'n':
            break
