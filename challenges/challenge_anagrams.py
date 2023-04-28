def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    indice_meio_da_lista = len(lista) // 2
    indice_inicio_lista = 0
    indice_fim_lista = len(lista)

    items_inicio_lista = lista[indice_inicio_lista:indice_meio_da_lista]
    sub_lista_esquerda = merge_sort(items_inicio_lista)

    items_fim_lista = lista[indice_meio_da_lista:indice_fim_lista]
    sub_lista_direita = merge_sort(items_fim_lista)

    return compara_items_das_listas_e_faz_a_juncao(
        sub_lista_esquerda,
        sub_lista_direita
    )


def compara_items_das_listas_e_faz_a_juncao(lista_esquerda, lista_direita):
    juncao_dos_items = []
    indice_um = 0
    indice_dois = 0

    while (
        indice_um < len(lista_esquerda) and indice_dois < len(lista_direita)
    ):
        item_lista_esquerda = lista_esquerda[indice_um]
        item_lista_direita = lista_direita[indice_dois]

        if item_lista_esquerda < item_lista_direita:
            juncao_dos_items.append(item_lista_esquerda)
            indice_um += 1
        else:
            juncao_dos_items.append(item_lista_direita)
            indice_dois += 1

    if indice_um < len(lista_esquerda):
        item_restante_da_esquerda = lista_esquerda[indice_um:]
        juncao_dos_items.extend(item_restante_da_esquerda)

    if indice_dois < len(lista_direita):
        item_restante_da_direita = lista_direita[indice_dois:]
        juncao_dos_items.extend(item_restante_da_direita)

    return juncao_dos_items


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    primeira_lista_ordenada = merge_sort(first_string)
    segunda_lista_ordenada = merge_sort(second_string)

    if len(primeira_lista_ordenada) == 0 or len(segunda_lista_ordenada) == 0:
        return (
            "".join(primeira_lista_ordenada),
            "".join(segunda_lista_ordenada),
            False
        )

    if primeira_lista_ordenada == segunda_lista_ordenada:
        return (
            "".join(primeira_lista_ordenada),
            "".join(segunda_lista_ordenada),
            True
        )
    else:
        return (
            "".join(primeira_lista_ordenada),
            "".join(segunda_lista_ordenada),
            False
        )


if __name__ == '__main__':
    # print(merge_sort('marcelo'))
    # print(merge_sort([3, 5, 7, 0, 8, 1, 6, 4, 2]))

    # print(is_anagram('amor', 'roma'))
    # print(is_anagram('pedra', 'perda'))
    # print(is_anagram('pato', 'tapo'))
    # print(is_anagram('coxinha', 'empada'))
    print(is_anagram('AmoR', 'roma'))
