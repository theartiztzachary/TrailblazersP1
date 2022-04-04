from abc import ABC, abstractmethod


class LogInDataAccessLayerInterface(ABC):

    @abstractmethod
    def select_employee_information(self, username: str):
        pass

    @abstractmethod
    def select_employee_id(self, username: str):
        pass
