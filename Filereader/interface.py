from abc import ABC, abstractmethod


class FileInterface(ABC):

    @abstractmethod
    def read_all_lines(self):
        pass

    @abstractmethod
    def read_first_two_lines(self):
        pass
    
    @abstractmethod
    def read_last_two_lines(self):
        pass

    @abstractmethod
    def __iter__(self):
        return self.filename

    @abstractmethod
    def __next__(self):
        pass
    
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass