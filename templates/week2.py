#!/usr/bin/env python3

from typing import Iterable
import numpy as np

def best_response_value_func(matrix: np.ndarray, step_size: float) -> None:
    """ Plot the best response value function of the row player in a 2xN zero-sum matrix game.

    Parameters
    ----------
    matrix : np.ndarray
        The row player's payoff matrix
    step_size : float
        The step size for the probability of the first action of the row player
    """

    raise NotImplementedError


def verify_support_one_side(
    row_support: np.ndarray, col_support: np.ndarray, matrix: np.ndarray
) -> np.ndarray | None:
    """ Construct a set of linear equations to check whether there exists a Nash equilibrium

    Parameters
    ----------
    row_support : np.ndarray
        The row player's support
    col_support : np.ndarray
        The column player's support
    matrix : np.ndarray
        The row player's payoff matrix

    Returns
    -------
    np.ndarray | None
        The column player's strategy, if it exists, otherwise `None`
    """

    raise NotImplementedError


def support_enumeration(
    row_matrix: np.ndarray, col_matrix: np.ndarray
) -> Iterable[tuple[np.ndarray, np.ndarray]]:
    """ Run the Support Enumeration algorithm to find all Nash equilibria in a given game.

    Parameters
    ----------
    row_matrix : np.ndarray
        The row player's payoff matrix
    col_matrix : np.ndarray
        The column player's payoff matrix

    Returns
    -------
    Iterable[tuple[np.ndarray, np.ndarray]]
        A sequence of strategy profiles corresponding to found Nash equilibria
    """

    raise NotImplementedError


def main() -> None:
    pass


if __name__ == '__main__':
    main()
