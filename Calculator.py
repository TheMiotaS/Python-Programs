
def main():
    while True:
        try:

            print('Answer: {}'.format(eval(input('Calculate: '))))
            input('(Press enter to continue)')

        except Exception:
            print('Uh oh! Calculator just broke down. Try again!')


if __name__ == '__main__':
    main()
