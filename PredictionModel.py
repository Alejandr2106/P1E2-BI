from joblib import load
import numpy as np

class Model:
    def __init__(self, columns):
        # Cargar el modelo desde un archivo joblib
        self.model = load("assets/modelo.joblib")
        self.columns = columns

    def make_predictions(self, data):
        # Asegurarse de que los datos estén en el formato correcto (numpy array)
        data_array = np.array([data[col] for col in self.columns])
        data_array = data_array.reshape(1, -1)  # Asegurarse de que sea un array 2D
        # Realizar la predicción
        result = self.model.predict(data_array)
        return result
