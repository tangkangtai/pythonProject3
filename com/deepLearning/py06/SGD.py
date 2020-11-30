# stochastic gradient descent
class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]

#---------------------------
# network = TwoLayerNet()
# optimizer = SGD()
# for i in range(10000):
#     ...
#      x_batch, t_batch = get_mini_batch(...) #mini-batch
#      grads = network.gradient(x_batch, t_batch)
#      params = network.params
#      optimizer.update(params, grads)
#---------------------------