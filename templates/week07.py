#!/usr/bin/env python3

import numpy as np

Game = ...
Player = ...
Strategy = ...
Sequence = ...

def convert_to_normal_form(
    game: Game, chance_strategy: Strategy | None = None
) -> tuple[np.ndarray, np.ndarray]:
    """ Convert an extensive-form game to an equivalent normal-form game.

    Parameters
    ----------
    game : Game
        An object representing the game tree
    chance_strategy : Strategy | None
        A strategy of the chance player, if present in the game

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        A pair of payoff matrices of the corresponding normal-form game
    """

    raise NotImplementedError


def convert_to_sequence_form(
    game: Game, chance_strategy: Strategy | None = None
) -> tuple[list[Sequence], list[Sequence], np.ndarray, np.ndarray]:
    """ Convert an extensive-form game to its sequence-form representation.

    Parameters
    ----------
    game : Game
        An object representing the game tree
    chance_strategy : Strategy | None
        A strategy of the chance player, if present in the game

    Returns
    -------
    tuple[list[Sequence], list[Sequence], np.ndarray, np.ndarray]
        Lists of sequences and utility matrices for both players
    """

    raise NotImplementedError


def calculate_constraints(
    game: Game, player: Player, sequences: list[Sequence]
) -> tuple[np.ndarray, np.ndarray]:
    """ Calculate the constraint matrix and the constraint vector for `player`.

    Parameters
    ----------
    game : Game
        An object representing the game tree
    player : Player
        A player for which to compute the constraints
    sequences : list[Sequence]
        A list of sequences of `player`

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        The constraint matrix and the constraint vector of `player`
    """

    raise NotImplementedError


def find_nash_equilibrium_sequence_form(
    game: Game, chance_strategy: Strategy | None = None
) -> tuple[np.ndarray, np.ndarray]:
    """ Find a Nash equilibrium of an extensive-form game using sequence-form linear programming.

    Parameters
    ----------
    game : Game
        An object representing the game tree
    chance_strategy : Strategy | None
        A strategy of the chance player, if present in the game

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        A strategy profile that forms a Nash equilibrium represented in the sequence-form
    """

    raise NotImplementedError


def main() -> None:
    pass


if __name__ == '__main__':
    main()
