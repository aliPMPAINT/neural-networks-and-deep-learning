import network
import mnist_loader
from time import process_time

# Hyper-parameters
epochs = 50
mini_batch_size = 10
eta = 4.0

parameters_seeds = [8323988, 6856221, 3484827, 2202620, 3325501, 3909291, 3738380, 3010278, 753857, 6842634]

data_seeds = [9378532, 5329960, 5517929, 6653044, 5284670, 1346193, 4037161, 4498556, 8215724, 3467963]

def seed_random(parameters_seed, data_seed):
    network.random.seed(data_seed)
    network.np.random.seed(parameters_seed)
    
def timer(function, *args):
    """Runs a function and measures the time it takes.

    Args:
        function (callable): The function to run.

    Returns:
        (func_return, time) (any, num): 'func_return' is the return value of the funtion. 'time' is the time it took to run.
    """
    start = process_time()
    func_return = function(*args)
    stop = process_time()
    return (func_return, stop - start)
    

def train_net(hidden_layer_size):
    """Train a network consisting of one input layer with 784 neurons,
    one output layer with 10 neurons, and one hidden layer
    with 'hidden_layer_size' neurons.

    Args:
        hidden_layer_size (int): number of neurons in the hidden layer
    """
    seed_random()
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    
    print(f"#Network size: [784, {hidden_layer_size}, 10]")
    net = network.Network([784, hidden_layer_size, 10])
    net.SGD(training_data, epochs, mini_batch_size, eta, test_data=test_data)
    print(f"Final epoch completed! \nWeights: {net.weights} \nBiases: {net.biases}")
    print("#.")

def main():
    print(f"#Running networks. Random seed data: {data_random_seed} Random seed parameters: {parameters_random_seed} Global hyper-parameters: epochs = {epochs}, mini_batch_size = {mini_batch_size}, eta = {eta}")
    train_net(5)
    train_net(10)
    train_net(30)
    train_net(50)
    train_net(70)
    train_net(90)
    train_net(120)
    train_net(784)
    
    
if __name__ == "__main__":
    main()