from classes_animais import *

class AnimalTeste:

    def testar_veterinario():
        cachorro = Cachorro('Nome Cachorro', 10)
        cavalo = Cavalo('Nome Cavalo', 15)
        preguica = Preguica('Nome Preguiça', 16)
        veterinario = Veterinario()
        veterinario.examinar(cachorro)
        veterinario.examinar(cavalo)
        veterinario.examinar(preguica)

    def testar_zoologico():
        zoologico = Zoologico()
        cachorro1 = Cachorro('Nome Cachorro1', 1)
        cavalo1 = Cavalo('Nome Cavalo1', 1)
        preguica1 = Preguica('Nome Preguiça1', 1)
        cachorro2 = Cachorro('Nome Cachorro2', 2)
        cavalo2 = Cavalo('Nome Cavalo2', 2)
        preguica2 = Preguica('Nome Preguiça2', 2)
        cachorro3 = Cachorro('Nome Cachorro3', 3)
        cavalo3 = Cavalo('Nome Cavalo3', 3)
        preguica3 = Preguica('Nome Preguiça3', 3)
        cachorro4 = Cachorro('Nome Cachorro4', 4)

        zoologico.jaulas.extend([cachorro1, cavalo1, preguica1, cachorro2, cavalo2, preguica2, cachorro3, cavalo3, preguica3, cachorro4])

        for animal in zoologico.jaulas:
            print(f'{animal.emitir_som()}')
            if hasattr(animal, 'correr'):
                print(animal.correr())
            print('')

if __name__ == '__main__':
    at = AnimalTeste
    print('TESTE DO VETERINÁRIO')
    at.testar_veterinario()
    
    print('\nTESTE DO ZOOLÓGICO')
    at.testar_zoologico()