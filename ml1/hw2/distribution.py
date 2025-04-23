import numpy as np

class LaplaceDistribution:    
    @staticmethod
    def mean_abs_deviation_from_median(x: np.ndarray):
        '''
        Args:
        - x: A numpy array of shape (n_objects, n_features) containing the data
          consisting of num_train samples each of dimension D.
        '''
        ####
        # Do not change the class outside of this block
        # Your code here
        ####

    def __init__(self, features):
        '''
        Args:
            feature: A numpy array of shape (n_objects, n_features). Every column represents all available values for the selected feature.
        '''
        ####
        # Do not change the class outside of this block
        self.loc = np.median(features, axis=0)
        self.scale = np.mean(np.abs(features - self.loc, dtype=np.float64), axis=0)
        #self.scale = np.sum(np.abs(features - self.loc)) / len(features)

        ####


    def logpdf(self, values):
        '''
        Returns logarithm of probability density at every input value.
        Args:
            values: A numpy array of shape (n_objects, n_features). Every column represents all available values for the selected feature.
        '''
        ####
        # Do not change the class outside of this block

        res = np.zeros(values.shape)
        print(res.shape)
        #for i in range (values.shape[0]):
        #    for j in range(values.shape[1]):
        #        if values[i][j] <= self.loc[j]:
        #            res[i, j] = 1/self.scale[j] * (values[i, j] - self.loc[j]) * (1 + np.log(0.5))

        return np.log(0.5/self.scale) + -1 * 1/self.scale * np.abs(values - self.loc  )
        ####
        
    
    def pdf(self, values):
        '''
        Returns probability density at every input value.
        Args:
            values: A numpy array of shape (n_objects, n_features). Every column represents all available values for the selected feature.
        '''
        value = 0
        return np.exp(self.logpdf(value))
