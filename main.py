# -*- coding: utf-8 -*-
"""
python main.py
"""

from form import Form
from form import pr as form_pr
from pde import PDE

a = Form('velocity', r"\alpha")    # a form is a variable
b = Form('vorticity', r'\omega')
c = Form('pressure', r'\nabla P')

form_pr()   # plot all forms

expression = [    # the expressions of the PDE
    'a + b = 0',
    'c = 0'
]

interpreter = {    # how to interpret the terms in the expression.
    'a': a,
    'b': b,
    'c': c
}

pde = PDE(expression, interpreter)  # make the pde

pde.pr()   # plot the pde
