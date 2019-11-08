# Thanks StackOverflow for some of this code.
# Note from other guy who suddenly joined for no reason: I know right. StackOverflow is god.


def turn_list_into_integers(list_):
    """
    Turns all items inside a list into integers.
    :param list_: The list to turn into integers
    :return:
    """
    result = []
    for item in list_:
        result.append(int(item))

    return result


def main():
    while True:
        numbers = turn_list_into_integers(input('Type in your numbers, and seperate them with a "," to get the mean:')
                                          .split(','))
        average = sum(numbers)/int(len(numbers))
        print('Average: {}'.format(average))


if __name__ == '__main__':
    main()
