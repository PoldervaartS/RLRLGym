import matplotlib.pyplot as plt
f = open("./Evaluation/blue_scores4.txt", 'r')
g = open("./Evaluation/orange_scores4.txt", 'r')
blue = [int(x) for x in f.readline().split(' ')[:-1]]
orange = [int(x) for x in g.readline().split(' ')[:-1]]

if True: #len(blue) == len(orange):
    plt.title("Type 0 50M Steps vs. Type 3 25M Steps")
    plt.plot(blue, label = 'Type 0 50M')
    plt.plot(orange, label = 'Type 3 25M Steps')
    plt.xlabel('/5 steps')
    plt.ylabel('scores')
    leg = plt.legend(loc='upper center')
    plt.show()
    print(len(blue), " ", len(orange))
else:
    print("error")