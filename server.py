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
    
    def data_apply_preview(self):
        return self._data_connection.apply_preview()
    
    def init_model_training(self):
        return self._model_connection.train_model(self._data_connection.get_data())

    def model_get_score(self):
        return self._model_connection.eval_model(self._data_connection.get_data())

    def data_isempty(self):
        return self._data_connection.isempty()

    def data_get_current(self):
        return self._data_connection.get_current_data()
    
    def data_get_preview(self):
        return self._data_connection.get_preview_data()
    
    def data_get_columns(self):
        return self._data_connection.get_columns()

    def model_get_model(self):
        return self._model_connection.get_model()

    def get_user_config(self):
        return self._model_connection.get_config()
    
    def data_get_info(self):
        return self._data_connection.get_info()
    
    def data_get_num_rows(self):
        return self._data_connection.get_num_rows()
    
    def data_get_column_meta(self):
        return self._data_connection.get_column_meta()
    
    def data_get_dtype_meta(self):
        return self._data_connection.get_dtype_meta()
    
    def data_get_total_missing(self):
        return self._data_connection.get_total_missing()
    
    def data_get_total_memory(self):
        return self._data_connection.get_total_memory()
    
    def set_user_config(self,task,features,target):
        return self._model_connection.set_config(task,features,target)