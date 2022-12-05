class SingleSampleDecorator:
    def __init__(self, model):
        self.model = model
    
    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict_proba(self, X):
        return self.model.predict_proba(_sample_transform(X))

    def predict(self, X):
        return self.model.predict(_sample_transform(X))
    
    def score(self, X, y):
        return self.model.score(_sample_transform(X), y)

def _sample_transform(x):
    if len(x.shape) == 1:
        return x.reshape(1, -1)
    return x