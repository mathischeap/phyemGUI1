# -*- coding: utf-8 -*-
""""""
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "DejaVu Sans",
    "text.latex.preamble": r"\usepackage{amsmath, amssymb}",
})
matplotlib.use('TkAgg')

_global_forms = {}  # cache all forms


class Form(object):
    """"""

    def __init__(self, lin_repr, sym_repr):
        """"""
        self._lin_repr = lin_repr
        self._sym_repr = sym_repr
        _global_forms[id(self)] = self


def pr(variable_dict, figsize=(8, 6)):
    """print all forms"""
    text = ''
    for form_id in _global_forms:
        form = _global_forms[form_id]
        label = None
        for label in variable_dict:
            if variable_dict[label] is form:
                break

        text += r'\texttt{' + label + '}:  ' + form._lin_repr + ' = $' + form._sym_repr + '$\n'

    fig = plt.figure(figsize=figsize)
    plt.axis([0, 1, 0, 1])
    plt.axis('off')
    plt.text(0.05, 0.5, text, ha='left', va='center', size=15)
    plt.tight_layout()
    plt.show()

    return fig
