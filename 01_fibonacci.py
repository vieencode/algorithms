import argparse
import time
import matplotlib.pyplot as plt

#container to hold arguments with description
parser = argparse.ArgumentParser(description='Fibonacci number calculation with runtime evaluation')
parser.add_argument('-n', '--number', type=int, required=True, metavar="", help='your desired nth fibonacci number')
parser.add_argument('--all', '--verbosity', action='store_true', dest='allnumbers', help='prints the fibonacci sequence up to n')
group = parser.add_mutually_exclusive_group()
group.add_argument('-i', '--ineff_plot', action='store_true', help='inefficient fibonacci algorithm runtime plot')
group.add_argument('-e', '--eff_plot', action='store_true', help='efficient fibonacci algorithm runtime plot')
group.add_argument('-b', '--both', action='store_true', help='runtime plot with both algorithms')
args = parser.parse_args()

starttime=time.time()
fibo_storage = {}

#function for dynamic programming algorithm
def efficient_fibo(n):
    if n in fibo_storage:
        return fibo_storage[n]

    if n == 1:
        fibo = 1
    elif n == 2:
        fibo = 1
    elif n > 2:
        fibo = efficient_fibo(n-1) + efficient_fibo(n-2)

    fibo_storage[n] = fibo
    return fibo

#function for recursive algorithm
def inefficient_fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return inefficient_fibo(n-1) + inefficient_fibo(n-2)

#function to get fibonacci sequence and time needed to calculate each value
def fibo_sequence(n, algorithm):
    sequence = []
    elapsed_time = []
    for n in range(1, n + 1):
        elapsed_time.append(time.time() - starttime)
        sequence.append(algorithm(n))
    return sequence, elapsed_time

#function to create runtime plots
def plot_fibo(x_axis, y_axis, plot_title, single=True, new_y=[]):
    #plt.style.use('ggplot')
    # plt.grid(True)
    #plt.xkcd()

    if single == True:
        plt.plot(x_axis, y_axis, color='b', marker='.', linewidth=1)
    else:
        plt.plot(x_axis, y_axis, color='g', marker='.', linewidth=1, label='Efficient algorithm')
        plt.plot(x_axis, new_y, color='r', linestyle='--', marker='.', linewidth=1, label='Inefficient algorithm')
        plt.legend()

    plt.xticks(x_axis)
    plt.title(plot_title)
    plt.xlabel('growing n')
    plt.ylabel('time (s)')
    plt.tight_layout()
    plt.savefig('fibonacci_runtime_plot.png')
    return plt.show()


if __name__ == '__main__':
    if args.allnumbers:
        print('Your requested fibonacci sequence is:')
        print(*(fibo_sequence(args.number, efficient_fibo))[0], sep=', ')
    else:
        print(f'The answer is: \n{efficient_fibo(args.number)}')

    if args.eff_plot:
        print('Your plot should pop up now and is also saved as plot.png in the respecitve directory.')
        title = 'Runtime of dynamic programming fibonacci'
        plot_fibo(range(1, args.number+1), fibo_sequence(args.number, efficient_fibo)[1], title)
    elif args.ineff_plot:
        print('Your plot should pop up now and is also saved as plot.png in the respecitve directory.')
        title = 'Runtime of recursive fibonacci'
        plot_fibo(range(1, args.number+1), fibo_sequence(args.number, inefficient_fibo)[1], title)
    elif args.both:
        print('Your plot should pop up now and is also saved as plot.png in the respecitve directory.')
        title = 'Comparison of runtime'
        plot_fibo(range(1, args.number+1), fibo_sequence(args.number, efficient_fibo)[1], title, False, fibo_sequence(args.number, inefficient_fibo)[1])
