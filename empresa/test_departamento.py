from unittest import TestCase
from Departamento import *
from mockito import *

__author__ = 'ezequiel'


class TestDepartamento(TestCase):

    def test_getSalarioTotal(self):

        # create emp mocks
        e1 = mock(Empleado)
        e2 = mock(Empleado)
        e3 = mock(Empleado)

        # define methods
        when(e1).get_salario().thenReturn(1000.0)
        when(e2).get_salario().thenReturn(1000.0)
        when(e3).get_salario().thenReturn(1000.0)

        # create department
        dpt = Departamento("Contabilidad", 1)

        # empty dpt
        self.assertIsNotNone(dpt.get_salario_total())
        self.assertIsInstance(dpt.get_salario_total(), float)
        self.assertEqual(dpt.get_salario_total(), 0.0)

        # add the first employee
        dpt.add_empleado(e1)
        self.assertIsNotNone(dpt.get_salario_total())
        self.assertIsInstance(dpt.get_salario_total(), float)
        self.assertEqual(dpt.get_salario_total(), 1000.0)

        # add second employee
        dpt.add_empleado(e2)
        self.assertIsNotNone(dpt.get_salario_total())
        self.assertIsInstance(dpt.get_salario_total(), float)
        self.assertEqual(dpt.get_salario_total(), 2000.0)

        # add third employee
        dpt.add_empleado(e3)
        self.assertIsNotNone(dpt.get_salario_total())
        self.assertIsInstance(dpt.get_salario_total(), float)
        self.assertEqual(dpt.get_salario_total(), 3000.0)

