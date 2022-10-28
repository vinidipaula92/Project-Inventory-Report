from abc import ABC, abstractclassmethod


class Importer(ABC):
    @classmethod
    @abstractclassmethod
    def import_data(cls, file_path: str):
        raise NotImplementedError
