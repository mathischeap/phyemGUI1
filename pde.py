# -*- coding: utf-8 -*-
"""
"""
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "DejaVu Sans",
    "text.latex.preamble": r"\usepackage{amsmath, amssymb}",
})
matplotlib.use('TkAgg')


class PDE(object):
    """"""

    def __init__(self, expression=None, interpreter=None):
        self._parse_expression(expression, interpreter)

    def _parse_expression(self, expression, interpreter):
        """Keep upgrading this method to let it understand more equations."""
        sign_dict = dict()
        term_dict = dict()
        ind_dict = dict()
        indexing = dict()
        for i, equation in enumerate(expression):

            equation = equation.replace(' ', '')  # remove all spaces
            equation = equation.replace('-', '+-')  # let all terms be connected by +

            sign_dict[i] = ([], [])  # for left terms and right terms of ith equation
            term_dict[i] = ([], [])  # for left terms and right terms of ith equation
            ind_dict[i] = ([], [])   # for left terms and right terms of ith equation

            k = 0
            for j, lor in enumerate(equation.split('=')):
                local_terms = lor.split('+')

                for loc_term in local_terms:
                    if loc_term == '' or loc_term == '-':  # found empty terms, just ignore.
                        pass
                    else:
                        if loc_term == '0':
                            pass
                        else:
                            if loc_term[0] == '-':
                                assert loc_term[1:] in interpreter, f"found term {loc_term[1:]} not interpreted."
                                indi = loc_term[1:]
                                sign = '-'
                                term = interpreter[loc_term[1:]]
                            else:
                                assert loc_term in interpreter, f"found term {loc_term} not interpreted"
                                indi = loc_term
                                sign = '+'
                                term = interpreter[loc_term]

                            sign_dict[i][j].append(sign)
                            term_dict[i][j].append(term)
                            if j == 0:
                                index = str(i) + '-' + str(k)
                            elif j == 1:
                                index = str(i) + '-' + str(k)
                            else:
                                raise Exception()
                            k += 1
                            indexing[index] = (indi, sign, term)
                            ind_dict[i][j].append(index)

        self._sign_dict = sign_dict
        self._term_dict = term_dict   # can be form or (for example L2-inner-product- or duality-) terms
        self._ind_dict = ind_dict
        self._indexing = indexing

    def __len__(self):
        """I have how many equations?"""
        return len(self._term_dict)

    def pr(self, figsize=(8, 6)):
        """Print representations"""

        number_equations = len(self._term_dict)

        symbolic = ''
        for i in self._term_dict:
            for t, forms in enumerate(self._term_dict[i]):
                if len(forms) == 0:
                    symbolic += '0'
                else:
                    for j, form in enumerate(forms):
                        sign = self._sign_dict[i][t][j]
                        form_sym_repr = form._sym_repr

                        if j == 0:
                            if sign == '+':
                                symbolic += form_sym_repr
                            elif sign == '-':
                                symbolic += '-' + form_sym_repr
                            else:
                                raise Exception()
                        else:
                            symbolic += ' ' + sign + ' ' + form_sym_repr

                if t == 0:
                    symbolic += ' &= '

            if i < number_equations - 1:
                symbolic += r' \\ '
            else:
                pass

        if len(self) > 1:
            symbolic = r"$\left\lbrace\begin{aligned}" + symbolic + r"\end{aligned}\right.$"
        else:
            symbolic = r"$\begin{aligned}" + symbolic + r"\end{aligned}$"

        starting_text = r'Given bla bla bla, '
        ending_text = r"for bla bla bla. "
        fig = plt.figure(figsize=figsize)
        plt.axis([0, 1, 0, 1])
        plt.axis('off')
        text = starting_text + '\n' + symbolic + '\n' + ending_text

        plt.text(0.05, 0.5, text, ha='left', va='center', size=15)
        plt.tight_layout()
        plt.show()

        return fig

    # operations
    def make_weak_formulation(self, *args, **kwargs):
        """"""
