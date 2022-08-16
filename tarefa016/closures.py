
# Define um método com outro método dentro, retornando o método interior
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

