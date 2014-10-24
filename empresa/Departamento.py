__author__ = 'ezequiel'
from Empleado import *

class Departamento:

    def __init__(self, nombre_depto, id_depto):
        """
        Init function

        :param nombre_depto: Department name
        :param id_depto: Department ID
        """

        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.empleados = []


    def add_empleado(self, empleado):
        """
        Add empleado function

        :param empleado:
        """

        self.empleados.append(empleado)


    def get_salario_total(self):
        """
        Get salario total function

        :return: sum of all employee's salary
        """

        total = 0
        for emp in self.empleados:
            total = total + emp.get_salario()
        return float(total)