import numpy as np


class Patient:
    def __init__(self, id, inflammation_scores:list):
        self.id = id
        self.inflammation_scores = inflammation_scores
    def data_mean(self):
        return np.mean(self.inflammation_scores)
    def data_max(self):
        return np.max(self.inflammation_scores)
    def data_min(self):
        return np.min(self.inflammation_scores)

class Trial:
    def __init__(self, id, filename:str):
        self.id = id
        self.data = self.load_csv(filename)

    @staticmethod
    def load_csv(filename):
        """Load a Numpy array from a CSV

        :param filename: Filename of CSV to load
        """
        return np.loadtxt(fname=filename, delimiter=',')

    def get_patient(self, id):
        """Get a Patient object by data row. The id of the object is the
        same as the row number."""
        patient = Patient(id, self.data[id, :])
        return patient

    @property
    def daily_mean(self):
        """Calculate the daily mean of a 2d inflammation data array."""
        return np.mean(self.data, axis=0)

    @property
    def daily_max(self):
        """Calculate the daily max of a 2d inflammation data array."""
        return np.max(self.data, axis=0)

    @property
    def daily_min(self):
        """Calculate the daily min of a 2d inflammation data array."""
        return np.min(self.data, axis=0)

    @property
    def patient_normalise(self):
        """
        Normalise patient data from a 2D inflammation data array.

        NaN values are ignored, and normalised to 0.

        Negative values are rounded to 0.
        """
        if np.any(self.data < 0):
            raise ValueError('Inflammation values should not be negative')
        max_data = np.nanmax(self.data, axis=1) # nanmax is like max, but it ignores nan values.
        # errstate - ignore runtime warnings related to division and validity
        with np.errstate(invalid="ignore", divide="ignore"):
            normalised = self.data / max_data[:, np.newaxis]
        normalised[np.isnan(normalised)] = 0 # use isnan to get a mask to set nans to 0
        normalised[normalised < 0] = 0 # any negative values are rounded to 0
        return normalised