
def media_numeros(x, y, z):
    return (x + y + z) / 3

if __name__ == '__main__':
    media1 = media_numeros(8, 9, 7)
    media2 = media_numeros(4, 5, 6)
    soma = media1 + media2
    media_medias = soma / 2
    print(f'Média de 8, 9 e 7: {media1}')
    print(f'Média de 4, 5 e 6: {media2}')
    print(f'Soma das duas médias: {soma}')
    print(f'Média das médias: {media_medias}')
