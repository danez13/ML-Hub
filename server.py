import data

class connection_handler():
    def __init__(self):
        self._data_connection = data.data_handler()
        self._model_connection = data.model_handler()

    def isdata(self):
        return self._data_connection.isempty()
        
    def load_data(self,file):
        if self._data_connection.load(file):
            return True
        else:
            return self.isdata() and file
    
    def load_model(self):
        return self._model_connection.load()
    
    def init_model_training(self):
        return self._model_connection.train_model(self._data_connection.get_data())

    def get_model_score(self):
        return self._model_connection.eval_model(self._data_connection.get_data())

    def data_isempty(self):
        return self._data_connection.isempty()

    def get_data(self):
        return self._data_connection.get_data()
    
    def get_columns(self):
        return self._data_connection.get_columns()

    def get_model(self):
        return self._model_connection.get_model()

    def get_user_config(self):
        return self._model_connection.get_config()
    
    def set_user_config(self,task,features,target):
        return self._model_connection.set_config(task,features,target)