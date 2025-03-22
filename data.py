import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

import io

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
    
    def get_num_rows(self):
        return len(self._data)
    
    def get_total_missing(self):
        return self._data.isna().sum().sum()
    
    def get_total_memory(self):
        return self._data.memory_usage().sum() * 0.000001
    
    def get_column_meta(self):
        dtypes = self._data.dtypes.values
        columns = self._data.dtypes.index
        missing_count = self._data.isna().sum()
        non_missing_count = self._data.count(0)
        mem_usage = self._data.memory_usage(index=False)
        # return mem_usage
        return pd.DataFrame({
            "Columns": columns,
            "Data Types": dtypes,
            "Missing Value Count": missing_count,
            "Non-empty Value Count": non_missing_count,
            "Memory Usage": mem_usage * 0.000001
        })
    
    def get_dtype_meta(self):
        unique_dtypes = self._data.dtypes.unique()
        unique_dtype_counts = self._data.dtypes.value_counts()
        return pd.DataFrame({
            "Data Types": unique_dtypes,
            "Counts": unique_dtype_counts
        },index=unique_dtypes)
    
    def get_info(self):
        buffer = io.StringIO()
        self._data.info(buf=buffer)
        info = buffer.getvalue()
        return info

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