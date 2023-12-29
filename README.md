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
In order to choose game mode, number of pieces, colors and size of the board, go to constants.py change values of the parametrs. Attention! The number of pieces can only be 6, 13 or 19. However in case of other parameters you can choose any.


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


## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.


## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.


## Author
Klaudia Niedziałkowska


## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

Line 263 can't be shortened