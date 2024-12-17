#!/usr/bin/env python3

from typing import Iterable
import numpy as np

def compute_deltas(
    row_strategy: np.ndarray, col_strategy: np.ndarray,
    row_matrix: np.ndarray, col_matrix: np.ndarray
) -> np.ndarray:
    """ Compute players' incentives to deviate from their strategies.

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
        An incentive to deviate for each player
    """

    raise NotImplementedError


def compute_nash_conv(
    row_strategy: np.ndarray, col_strategy: np.ndarray,
    row_matrix: np.ndarray, col_matrix: np.ndarray
) -> float:
    """ Compute the NashConv value of a given strategy profile.

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
    float
        The NashConv value of the given strategy profile
    """

    raise NotImplementedError


def compute_exploitability(
    row_strategy: np.ndarray, col_strategy: np.ndarray,
    row_matrix: np.ndarray, col_matrix: np.ndarray
) -> float:
    """ Compute the exploitability of a given strategy profile.

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
    float
        The exploitability value of the given strategy profile
    """

    raise NotImplementedError


def compute_epsilon(
    row_strategy: np.ndarray, col_strategy: np.ndarray,
    row_matrix: np.ndarray, col_matrix: np.ndarray
) -> float:
    """ Compute the epsilon of a given epsilon-Nash equilibrium strategy profile.

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
    float
        The epsilon value
    """

    raise NotImplementedError


def fictitious_play(
    row_matrix: np.ndarray, col_matrix: np.ndarray, epochs: int, naive: bool
) -> Iterable[tuple[np.ndarray, np.ndarray]]:
    """ Run the Fictitious Play algorithm to find a Nash equilibrium in a given game.

    Parameters
    ----------
    row_matrix : np.ndarray
        The row player's payoff matrix
    col_matrix : np.ndarray
        The column player's payoff matrix
    epochs : int
        The number of epochs to run the algorithm for
    naive : bool
        Whether to calculate the best response against the last
        opponent's strategy or the mean opponent's strategy

    Returns
    -------
    Iterable[tuple[np.ndarray, np.ndarray]]
        A sequence of average strategy profiles produced by the algorithm
    """

    raise NotImplementedError


def plot_exploitability(
    row_matrix: np.ndarray, col_matrix: np.ndarray,
    strategies: Iterable[tuple[np.ndarray, np.ndarray]], label: str
) -> list[float]:
    """ Compute and plot the exploitability of a sequence of strategy profiles.

    Parameters
    ----------
    row_matrix : np.ndarray
        The row player's payoff matrix
    col_matrix : np.ndarray
        The column player's payoff matrix
    strategies : Iterable[tuple[np.ndarray, np.ndarray]]
        The sequence of strategy profiles
    label : str
        The name of the algorithm that produced `strategies`

    Returns
    -------
    list[float]
        A sequence of exploitability values, one for each strategy profile
    """

    raise NotImplementedError


def main() -> None:
    pass


if __name__ == '__main__':
    main()
