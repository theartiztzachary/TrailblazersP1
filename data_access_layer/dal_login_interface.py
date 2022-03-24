from abc import ABC, abstractmethod


class LogInDataAccessLayerInterface(ABC):

    @abstractmethod
    def select_employee_information(self, username: str, password: str):
        pass


