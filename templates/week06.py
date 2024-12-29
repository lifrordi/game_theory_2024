#!/usr/bin/env python3

from typing import Iterable
import numpy as np

Game = ...
Player = ...
Strategy = ...

def evaluate(game: Game, strategies: dict[Player, Strategy]) -> np.ndarray:
    """ Compute the expected utility of each player in an extensive-form game.

    Parameters
    ----------
    game : Game
        An object representing the game tree
    strategies : dict[Player, Strategy]
        A dictionary mapping each player to their behavioural strategy

    Returns
    -------
    np.ndarray
        A vector of expected utilities of the players
    """

    raise NotImplementedError


def compute_best_response(
    game: Game, player: Player, strategies: dict[Player, Strategy]
) -> Strategy:
    """ Compute a best response strategy of `player` against its opponent.

    Parameters
    ----------
    game : Game
        An object representing the game tree
    player : Player
        The player for which to compute a best response strategy
    strategies : dict[Player, Strategy]
        A dictionary mapping each player to their behavioural strategy

    Returns
    -------
    Strategy
        A best response strategy of `player` against its opponent
    """

    raise NotImplementedError


def compute_average_strategy(
    game: Game, player: Player, strategies: list[Strategy],
    chance_strategy: Strategy, weights: np.ndarray
) -> Strategy:
    """ Compute a (weighted) average of a list of strategies of `player`.

    Parameters
    ----------
    game : Game
        An object representing the game tree
    player : Player
        The player whose strategies we want to average
    strategies : list[Strategy]
        A list of strategies to average
    chance_strategy : Strategy
        The strategy of the chance player
    weights : np.ndarray
        A vector of weights, one for each strategy in `strategies`

    Returns
    -------
    Strategy
        A strategy that is a (weighted) average of `strategies` of `player`
    """

    raise NotImplementedError


def fictitious_play(game: Game, epochs: int) -> Iterable[dict[Player, Strategy]]:
    """ Run the Fictitious Play algorithm to find a Nash equilibrium in a given game.

    Parameters
    ----------
    game : Game
        An object representing the game tree
    epochs : int
        The number of epochs to run the algorithm for

    Returns
    -------
    Iterable[dict[Player, Strategy]]:
        A sequence of average strategy profiles produced by the algorithm
    """

    raise NotImplementedError


def plot_exploitability(
    game: Game, strategies: Iterable[dict[Player, Strategy]], label: str
) -> list[float]:
    """ Compute and plot the exploitability of a sequence of strategy profiles.

    Parameters
    ----------
    game : Game
        An object representing the game tree
    strategies : dict[Player, Strategy]
        A dictionary mapping each player to their behavioural strategy
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
