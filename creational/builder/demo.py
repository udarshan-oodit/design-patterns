from house_director import HouseDirector


def main():
    print('Building a basic house...')
    house = HouseDirector.build_basic_house()
    print(house)
    print()

    print('Building a fancy house...')
    house = HouseDirector.build_fancy_house()
    print(house)
    print()

    print('Building an apartment block...')
    house = HouseDirector.build_apartment_block()
    print(house)
    print()


if __name__ == '__main__':
    main()
