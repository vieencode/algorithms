import argparse

parser = argparse.ArgumentParser(prog='Towers of Hanoi Program',
                                 description='Enter desired number of disks and get total number of movements needed')
parser.add_argument('-n', '--number', type=int, required=True, help='Your desired number of disks')
args = parser.parse_args()


def towers(n, from_disk, aux_disk, to_disk):
    global count
    count += 1

    if n == 1:
        print(f'Move disk from {from_disk} to {to_disk}.')
    else:
        towers(n-1, from_disk, to_disk, aux_disk)
        print(f'Move disk from {from_disk} to {to_disk}.')
        towers(n-1, aux_disk, from_disk, to_disk)


if __name__ == '__main__':
    count = 0
    towers(args.number, 'A', 'B', 'C')
    print('Total number of moves:', count)
