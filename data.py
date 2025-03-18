import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

class data_handler():
    def __init__(self,file=None):
        if file is not None:
            self.load(file)
        else:
            self._data = None
            self._preview = None
    def load(self,file):
        if file is None:
            return False
        
        self._data = pd.read_csv(file)
        self._preview = self._data

        return not self.isempty()

    def isempty(self):
        if self._data is not None:
            if not self._data.empty:
                return False
        return True
    
    def apply_preview(self):
        self._data = self._preview
        return True
    
    def get_current_data(self):
        return self._data
    
    def get_preview_data(self):
        return self._preview
    
    def get_columns(self):
        return self._data.columns

class model_handler():
    def __init__(self,task=None, features=[], target=None, model=None):
        self._task = task
        self._features = features
        self._target = target
        self._model = model

    def set_config(self,task, features, target):
        self._task = task
        self.load()
        self._features = features
        self._target = target
        return True
    
    def get_config(self):
        return {
            "task":self._task,
            "features":self._features,
            "target":self._target
        }
    
    def load(self):
        if self._task is None:
            self._model=None
        if self._task == "Classification":
            self._model = KNeighborsClassifier()
        elif self._task == "Regression":
            self._model = LinearRegression()
        else:
            return False
        return True
    
    def train_model(self,data):
        try:
            self._model.fit(data[self._features],data[self._target])
        except:
            return False
        return True
    
    def eval_model(self,data):
        return self._model.score(data[self._features],data[self._target])

    def get_model(self):
        return self._model