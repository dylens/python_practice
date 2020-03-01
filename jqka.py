def gen():
    flower = ['♠', '♥', '♣', '♦']
    num = list(range(2, 11)) + ['J', 'Q', 'K', 'A']

    pk = [str(x) + str(y) for x in flower for y in num] + ['大王', '小王']
    print(pk)
    pass


if __name__ == '__main__':
    gen()
