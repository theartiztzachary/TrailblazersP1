from abc import ABC, abstractmethod


class LogInServiceLayerInterface(ABC):

    @abstractmethod
    def service_select_employee_information(self, username: str, password: str):
        pass

