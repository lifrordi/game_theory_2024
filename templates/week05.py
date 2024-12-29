#!/usr/bin/env python3

from typing import Iterable
import numpy as np

def regret_minimization(
    row_matrix: np.ndarray, col_matrix: np.ndarray, epochs: int
) -> Iterable[tuple[np.ndarray, np.ndarray]]:
    """ Run the Regret Minimization algorithm to find a Nash equilibrium in a given game.

    Parameters
    ----------
    row_matrix : np.ndarray
        The row player's payoff matrix
    col_matrix : np.ndarray
        The column player's payoff matrix
    epochs : int
        The number of epochs to run the algorithm for

    Returns
    -------
    Iterable[tuple[np.ndarray, np.ndarray]]
        A sequence of average strategy profiles produced by the algorithm
    """

    raise NotImplementedError


def main() -> None:
    pass


if __name__ == '__main__':
    main()
