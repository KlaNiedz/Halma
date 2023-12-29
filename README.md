# HalmaGame



## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab-stud.elka.pw.edu.pl/kniedzia/halmagame/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)


## Name
Halma Game


## Description
This project enable to play Halma game with another user, computer or watch play computer vs computer.
Rules of Halma:
PL - https://bonaludo.com/2018/08/06/halma-piekno-tkwi-w-prostocie/
ENG - https://bonaludo.com/2018/08/17/halma-the-beauty-of-simplicity/

I decided to consider 3 options of number of pieces and every imgaginable size of board. User can change detalis in constants.py. Every parameter is listed and change there will influence whole project without breaking it.
In order to improve testing I added option of play with 6 pieces per player. This is not accroding to Halma rules, but it significantly decrease gameplay time.


## Instruction manual
In order to choose game mode, number of pieces, colors and size of the board, go to constants.py change values of the parametrs. Attention! The number of pieces can only be 6, 13 or 19. In case of other parameters you can choose size of board between 6 and 16 while playing with 6 pieces and size board between 8 and 16 while playing with 13 or 19 pieces.
However, if you are playing with 6 pieces, I recommend choosing a board with a maximum of 10 by 10.
Also, as rules of the game says, while playing with 19 pieces it is better to choose board 16x16.

## Construction

Game is based on pygame library to better visualise board and moves of pieces.
Project consists of main.py, board.py, game.py, piece.py, test_board.py, test_piece.py, algorithm.py and constants.py.
I decided to divide project into such files as it is more readable.

Files:
main.py - contains most of the pygame visualization and check different events such mouse press on window, it also initialize minimax algorithm depending on game mode

board.py - the most developed file - consists of creating board from drawing it to placement of pieces, it checks winner, implements moves of pieces to every direction and add evaluation used in algorithm of computer - it is so developed as most of the game logic is based on "self.board" which is description of every square of the board

piece.py - contains mechanism of creating single piece

constants.py - it is a separate file, beacause it enables changing basic parameters at the pleasure of user (such as mode of the game, size of the board, colors of pieces and board)

game.py - contains basic functions, which are necessary to proper swaping turns

algorithm.py - contains minimax algorithm, which is a module implementing the computer game algorithm


Classes:
Board - while initializing there is created board which is two-dimensional list which "first demenstion" are rows and "second demension" are columns. It also consists the number of pieces and how many pieces are in the winning zone.

Piece - enable ti create single piece with parameteres such as color, position (x, y) and placement on board (row, column)

Game - handles game logic


## Visuals
[An example of a game player vs player](https://youtu.be/hypF6F5U-0w)


## Author
Klaudia Niedziałkowska


## Project status
Game mode 'COMPUTERvsCOMPUTER' doesn't work good.

Line 263 can't be shortened