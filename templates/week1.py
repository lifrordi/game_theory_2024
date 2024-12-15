#!/usr/bin/env python3

import numpy as np

def evaluate_pair(
    row_strategy: np.ndarray, col_strategy: np.ndarray,
    row_matrix: np.ndarray, col_matrix: np.ndarray
) -> np.ndarray:
    """ Compute the expected utility of each player in a general-sum game.

    Parameters
    ----------
    row_strategy : np.ndarray
        The row player's strategy
    col_strategy : np.ndarray
        The column player's strategy
    row_matrix : np.ndarray
        The row player's payoff matrix
    col_matrix : np.ndarray
        The column player's payoff matrix

    Returns
    -------
    np.ndarray
        A vector of expected utilities of the players
    """

    raise NotImplementedError


def evaluate(
    row_strategy: np.ndarray, col_strategy: np.ndarray, matrix: np.ndarray
) -> np.ndarray:
    """ Compute the expected utility of each player in a zero-sum game.

    Parameters
    ----------
    row_strategy : np.ndarray
        The row player's strategy
    col_strategy : np.ndarray
        The column player's strategy
    matrix : np.ndarray
        The row player's payoff matrix

    Returns
    -------
    np.ndarray
        A vector of expected utilities of the players
    """

    raise NotImplementedError


def best_response_strategy_against_row(
    row_strategy: np.ndarray, col_matrix: np.ndarray
) -> np.ndarray:
    """ Compute a pure best response strategy of the column player against the row player.

    Parameters
    ----------
    row_strategy : np.ndarray
        The row player's strategy
    col_matrix : np.ndarray
        The column player's payoff matrix

    Returns
    -------
    np.ndarray
        The column player's strategy
    """

    raise NotImplementedError


def best_response_strategy_against_col(
    col_strategy: np.ndarray, row_matrix: np.ndarray
) -> np.ndarray:
    """ Compute a pure best response strategy of the row player against the column player.

    Parameters
    ----------
    col_strategy : np.ndarray
        The column player's strategy
    row_matrix : np.ndarray
        The row player's payoff matrix

    Returns
    -------
    np.ndarray
        The row player's strategy
    """

    raise NotImplementedError


def evaluate_row_against_best_response(
    row_strategy: np.ndarray, col_matrix: np.ndarray
) -> np.ndarray:
    """ Compute the utilities when the row player plays against a best response strategy.

    Note that this function works only for zero-sum games

    Parameters
    ----------
    row_strategy : np.ndarray
        The row player's strategy
    col_matrix : np.ndarray
        The column player's payoff matrix

    Returns
    -------
    np.ndarray
        A vector of expected utilities of the players
    """

    raise NotImplementedError


def evaluate_col_against_best_response(
    col_strategy: np.ndarray, row_matrix: np.ndarray
) -> np.ndarray:
    """ Compute the utilities when the column player plays against a best response strategy.

    Note that this function works only for zero-sum games

    Parameters
    ----------
    col_strategy : np.ndarray
        The column player's strategy
    row_matrix : np.ndarray
        The row player's payoff matrix

    Returns
    -------
    np.ndarray
        A vector of expected utilities of the players
    """

    raise NotImplementedError


def dominated_actions(
    row_matrix: np.ndarray, col_matrix: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """ Find strictly dominated actions for each player.

    Parameters
    ----------
    row_matrix : np.ndarray
        The row player's payoff matrix
    col_matrix : np.ndarray
        The column player's payoff matrix

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        A sequence of indices of dominated actions for each player
    """

    raise NotImplementedError


def iterated_removal_of_dominated_actions(
    row_matrix: np.ndarray, col_matrix: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """ Run the Iterated Removal of Dominated Actions algorithm.

    Parameters
    ----------
    row_matrix : np.ndarray
        The row player's payoff matrix
    col_matrix : np.ndarray
        The column player's payoff matrix

    Returns
    -------
    tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]
        A pair of reduced payoff matrices and a pair of remaining actions for each player
    """

    raise NotImplementedError


def main() -> None:
    pass


if __name__ == '__main__':
    main()
