:- use_module(library(clpfd)).

% Sudoku Solver

% The main predicate to solve the Sudoku puzzle
solve_sudoku(Board) :-
    flatten(Board, FlatBoard),   % Flatten the 9x9 grid into a list
    domain(FlatBoard, 1, 9),      % Define the domain of values (1-9)

    % Define constraints
    all_different(FlatBoard),
    rows(Board),
    columns(Board),
    squares(Board),

    % Search for a solution
    labeling([ff], FlatBoard).

% Constraint for distinct values in rows
rows([]).
rows([Row | Rest]) :-
    all_different(Row),
    rows(Rest).

% Constraint for distinct values in columns
columns(Board) :-
    transpose(Board, Transposed),
    rows(Transposed).

% Constraint for distinct values in 3x3 squares
squares(Board) :-
    squares_helper(Board, 1, 1).

squares_helper(_, 10, _).
squares_helper(Board, Row, Col) :-
    get_square(Board, Row, Col, Square),
    all_different(Square),
    next_square(Row, Col, NextRow, NextCol),
    squares_helper(Board, NextRow, NextCol).

% Get the values of a 3x3 square
get_square(Board, Row, Col, Square) :-
    RowStart is (Row - 1) * 3 + 1,
    ColStart is (Col - 1) * 3 + 1,
    get_square_helper(Board, RowStart, ColStart, 1, Square).

get_square_helper(_, _, _, 10, []).
get_square_helper(Board, Row, Col, Count, [Value | Rest]) :-
    nth1(Row, Board, RowList),
    nth1(Col, RowList, Value),
    NextCount is Count + 1,
    next_square_position(Row, Col, NextRow, NextCol),
    get_square_helper(Board, NextRow, NextCol, NextCount, Rest).

% Determine the next square position
next_square_position(Row, Col, NextRow, NextCol) :-
    NextCol is Col + 1,
    NextRow = Row.

next_square_position(Row, Col, NextRow, NextCol) :-
    NextCol = Col,
    NextRow is Row + 1.

% Determine the next square in the Sudoku grid
next_square(Row, Col, NextRow, NextCol) :-
    NextCol is Col + 3,
    NextRow = Row.

next_square(Row, Col, NextRow, NextCol) :-
    NextCol = Col,
    NextRow is Row + 3.

% Example Sudoku puzzle
example_sudoku([
    [5, 3, _, _, 7, _, _, _, _],
    [6, _, _, 1, 9, 5, _, _, _],
    [_, 9, 8, _, _, _, _, 6, _],
    [8, _, _, _, 6, _, _, _, 3],
    [4, _, _, 8, _, 3, _, _, 1],
    [7, _, _, _, 2, _, _, _, 6],
    [_, 6, _, _, _, _, 2, 8, _],
    [_, _, _, 4, 1, 9, _, _, 5],
    [_, _, _, _, 8, _, _, 7, 9]
]).

% Example usage:
% ?- example_sudoku(Board), solve_sudoku(Board), print_board(Board).

% Print the solved Sudoku board
print_board(Board) :-
    print_rows(Board).

print_rows([]).
print_rows([Row | Rest]) :-
    print_row(Row),
    print_rows(Rest).

print_row([]) :- nl.
print_row([Cell | Rest]) :-
    (var(Cell) -> write('_') ; write(Cell)),
    write(' '),
    print_row(Rest).