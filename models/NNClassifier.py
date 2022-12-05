import numpy as np
from models.NeuralNetwork import NeuralNetwork

class NNClassifier:
    
    def __init__(self, initial_weight=0.075):
        self.initial_weight = initial_weight
        self.model = None
        self.num_classes = 0

    def fit(self, X_train, y_train):
        self.model = NeuralNetwork(self.initial_weight)
        
        # Calculate the number of classes (this assumes we start at 0)
        self.num_classes = np.max(y_train) + 1
        
        # Initializes layer scheme -- output layers must be equal to the number of classes
        layer_sizes = [64, 50, 20, self.num_classes]

        # Adds the layers to the neural network using the default bias scheme
        self.model.add_layers(layer_sizes)

        # Trains the model
        costs = self.model.train(X_train, self._to_one_hot(y_train), \
            epochs=100, learning_rate=1, batch_size=40, regularization_weight=0.00025)

        return self

    def predict_proba(self, X_test):
        return self.model.predict(X_test)

    def predict(self, X_test):
        return np.argmax(self.predict_proba(X_test), axis=1)

    def score(self, X_test, y_test):
        self.model.predict(X_test)
        self.model.calc_accuracy(self._to_one_hot(y_test))
        return self.model.accuracy

    def _to_one_hot(self, y):
        y_transformed = np.zeros((y.shape[0], self.num_classes))
        y_transformed[np.arange(len(y)), y] += 1
        return y_transformed