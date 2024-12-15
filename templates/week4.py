#!/usr/bin/env python3

import numpy as np

def find_nash_equilibrium(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """ Find a Nash equilibrium of a zero-sum normal-form game using linear programming.

    Parameters
    ----------
    matrix : np.ndarray
        The row player's payoff matrix

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        A strategy profile that forms a Nash equilibrium
    """

    raise NotImplementedError


def find_correlated_equilibrium(row_matrix: np.ndarray, col_matrix: np.ndarray) -> np.ndarray:
    """ Find a Correlated equilibrium of a normal-form game using linear programming.

    Parameters
    ----------
    row_matrix : np.ndarray
        The row player's payoff matrix
    col_matrix : np.ndarray
        The column player's payoff matrix

    Returns
    -------
    np.ndarray
        A distribution over joint actions that forms a Correlated equilibrium
    """

    raise NotImplementedError


def main() -> None:
    pass


if __name__ == '__main__':
    main()
