# APPADOO APOORVA SRINIVAS | BURDESE YAEL
import copy
import math
import random
import time

try:
    from modules.rendering_engine import RenderingEngine
except ModuleNotFoundError as e:
    print(e)


def calculate_parts(_currently_playing):
    """
    :param _currently_playing: pointer to the part of the _objects_up_list
    :returns tuple of the ranges of each split list
    function that splits a range in 2 ranges"""
    # create a list from the ranges
    _list = range(_currently_playing[0], _currently_playing[1] + 1)
    length = len(_list)
    if length % 2 == 0:
        # if the list contains only 2 elements send instruction to delete the line
        if length == 2:
            return "del line"
        # split the list into two lists while removing the two middle elements as the list has an even count of elements
        part1 = _list[:length // 2 - 1]
        part2 = _list[length // 2 + 1:]
    else:
        # split the list into two lists while removing the middle elements as the list has an odd count of elements
        part1 = _list[:length // 2]
        part2 = _list[length // 2 + 1:]
    return [part1[0], part1[-1]], [part2[0], part2[-1]]


def calculate_parts_w_random(_currently_playing):
    """
    :param _currently_playing: pointer to the part of the _objects_up_list
    :returns tuple of the ranges of each split list
    function that splits a range in 2 ranges"""
    # create a list from the ranges
    _list = range(_currently_playing[0], _currently_playing[1] + 1)
    length = len(_list)
    if length % 2 == 0:
        # if the list contains only 2 elements send instruction to delete the line
        if length == 2:
            return "del line"
        # split the list into two lists while removing the two middle elements as the list has an even count of elements
        part1 = _list[:length // 2 - 1]
        part2 = _list[length // 2 + 1:]
    else:
        # random bool
        if random.getrandbits(1):
            # split the list into two lists while removing the 2 left-middle elements |||--> |..
            part1 = _list[:length // 2 - 1]
            part2 = _list[length // 2 + 1:]
        else:
            # split the list into two lists while removing the 2 right-middle elements |||--> ..|
            part1 = _list[:length // 2]
            part2 = _list[length // 2 + 2:]
        if not part1:
            # if there is no part1 return only part2
            return 1, part2[0], part2[-1]
        if not part2:
            # if there is no part2 return only part1
            return 1, part1[0], part1[-1]

    return [part1[0], part1[-1]], [part2[0], part2[-1]]


def check_binary_input(_input):
    """:param _input: input to check
        return: bool: if the input is valid or not
        """
    try:
        _input = int(_input)
    except ValueError:
        raise ValueError(f'{_input} is not 0 nor 1')

    if _input == 0:
        return False
    elif _input == 1:
        return True
    else:
        raise ValueError(f'{_input} is not 0 nor 1')


class Game:
    """ Game class handles all game logic and call redering engine for the graphical interface"""

    def __init__(self, object_num_random_range, player_names, mode='1vai', max_minimax_iteration=1000000):
        """
        :param player_names: dict of the player names associated with their playing_index
        :param mode: way to play the game 1_vs_ai,1_vs_1,ai_vs_ai
        :param object_num_random_range: the range of the possible object_num
        :param max_minimax_iteration: iteration limit for the minimax algorithm

        function to initialise the variables for the game"""
        # creating variables of passed arguments
        self.max_minimax_iteration = max_minimax_iteration
        self.object_num_random_range = object_num_random_range
        self.object_num = random.randint(object_num_random_range[0], object_num_random_range[1])  # number of objects
        self._objects_up_list = [[0, self.object_num - 1]]  # list of ranges of objects facing upwards
        self.mode = mode
        self.player_names = player_names

        # init turtle rendering engine but if failed use the terminal
        self.rendering_engine = True
        try:
            self.rendering_engine = RenderingEngine(self.object_num)
            self.rendering_engine.initialise_turtles()
        except NameError:
            self.rendering_engine = None
            print('rendering_engine module not found switching to terminal only rendering')
        # creating variables
        self.minimax_iteration_counter = 0  # minimax iteration counter
        self.render_list = []  # used to store the text of the output in a list
        self.current_input = ''  # current input that needs processing
        self.playing_index = 0  # id of the currently playing index
        self.winner = None  # id of the winner
        self.game_states = []  # states of every turn of the game
        # adding the first game state
        self.game_states.append(copy.deepcopy(self._objects_up_list))

    def render_w_text(self):
        """Renders the game in the terminal in text form"""
        _render_list = ["."] * self.object_num  # initialise a list of "."
        # fill in the list with "|" in the indexes of the upwards facing objects
        for _range in self._objects_up_list:
            for _index in range(_range[0], _range[1] + 1):
                _render_list[_index] = '|'
        print(f"Voici les quilles, il y a {len(self._objects_up_list)} lignes")
        # convert list into string
        self.render_list = "".join(_render_list)
        print(self.render_list)
        return self.render_list

    def make_move_ai(self):
        """Ai for the game, picks random moves if number of objects higher than 9 else use minimax algorithm"""
        if self.render_list.count('|') > 10:
            _line_index = random.randint(0, len(self._objects_up_list) - 1)
            _shooting_key = random.choice(["G", "M", "D"])
            print('jouez (format {ligne}:{tirer}):', f"{_line_index + 1}:{_shooting_key}")
            self.current_input = f"{_line_index + 1}:{_shooting_key}"
        else:
            self.current_input = self.make_best_move()

    def get_possible_moves(self):
        """Get all the possible moves of the game"""
        possible_moves = []
        for _line_index in range(len(self._objects_up_list)):
            for _shooting_key in ["G", "M", "D"]:
                possible_moves.append(f"{_line_index + 1}:{_shooting_key}")
        # print(possible_moves)
        return possible_moves

    def make_best_move(self):
        """get the best move
        source:source:https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f"""
        best_score = -math.inf
        best_move = None
        self.minimax_iteration_counter = 0
        for i, move in enumerate(self.get_possible_moves()):
            self.rendering_engine.write_text((0, - 320), 'bot calculating: ' + str(
                round(100 * i / len(self.get_possible_moves()))) + '%', True)
            self.current_input = move
            self.update()
            score = self.minimax(False, 1)

            self.reverse_move()
            if score > best_score:
                best_score = score
                best_move = move
        self.rendering_engine.write_text((0, - 320), 'bot calculating: 100 %', True)
        print(best_move)
        self.rendering_engine.write_text((0, - 350), "done: playing " + str(best_move))
        return best_move

    def minimax(self, is_max_turn, maximizer_key):
        """minimax algorithm
        source:https://levelup.gitconnected.com/mastering-tic-tac-toe-with-minimax-algorithm-3394d65fa88f"""

        if self.winner is not None:  # check if winner
            # print(self.winner)
            return 1 if self.winner is maximizer_key else -1
        # check if reached iteration limit
        if self.minimax_iteration_counter > self.max_minimax_iteration:
            self.rendering_engine.write_text((0, - 320), "skipping moves, over iteration limit", percentage=True)
            return 0
        # check every possible move
        scores = []
        for move in self.get_possible_moves():
            self.minimax_iteration_counter += 1
            # try a move
            self.current_input = move
            self.update()
            # go in deeper until a win or a loss and add the score of that move to scores
            scores.append(self.minimax(not is_max_turn, maximizer_key))
            # reverse the move to try the next one
            self.reverse_move()
        # update possiblities calculated on screen
        if self.minimax_iteration_counter % 1000 == 0 and not (
                self.minimax_iteration_counter > self.max_minimax_iteration):
            self.rendering_engine.write_text((0, - 350), "possibility: " + str(self.minimax_iteration_counter))
        # return max or min depending if it's the maximizing player turn or the minimizing player turn
        return max(scores) if is_max_turn else min(scores)

    def make_move_player(self):
        # While there is not a valid input try to get an input from user
        _valid_input = False
        error_text = None
        while not _valid_input:
            try:
                # if we are using turtle ask input via the rendering engine
                if self.rendering_engine:
                    self.current_input = self.rendering_engine.get_input(("format {ligne}:{tirer})", error_text))
                    print(self.current_input)
                else:
                    # else get input from terminal
                    self.current_input = str(input("input (format {ligne}:{tirer}): "))
                # check inputs raises Value error if inputs are not valid
                self.check_inputs()
                _valid_input = True
            except ValueError as _e:
                error_text = str(_e)
                print(_e)

    def check_inputs(self):
        """Checks if the inputs are valid else raise value error"""
        _input = self.current_input
        _input = _input.split(":")  # split input
        # check if the input has the required format
        if len(_input) != 2:
            raise ValueError('must be in format "format {ligne}:{tirer})"')
        _shooting_key = _input[1]
        try:
            _line_index = int(_input[0]) - 1
        except ValueError:
            print('wrong input for line index, must be an int')
        # check if the shooting key is valid
        if _shooting_key not in ["G", "D", "M"]:
            raise ValueError('wrong input for shooting, input must be M for middle D for right and G for left')
        # check if the line index is valid
        if not (0 <= _line_index < len(self._objects_up_list)):
            raise ValueError('line index not valid')

    def play_turn(self):
        """method that chooses who plays(ai or user)"""
        # TODO make changes for different modes
        print(f'tour de {self.playing_player_name()}:')
        self.get_possible_moves()
        if self.rendering_engine:
            self.rendering_engine.drawing_turtles['percentage'].clear()
        if self.mode == '1vai':
            # play user once and ai once
            if self.playing_index == 1:
                # self.make_best_move()
                self.make_move_ai()
            else:
                self.make_move_player()
        if self.mode == 'aivai':
            self.player_names = {
                0: 'bot1',
                1: 'bot2'
            }
            # self.make_best_move()

    def reverse_move(self):
        """reverse move used for bot maybe in the future"""
        # copy game state in current game state(_object_up_list)
        self._objects_up_list = copy.deepcopy(self.game_states[-2])
        self.game_states.pop(-1)
        self.winner = None
        self.playing_index = not self.playing_index

    def playing_player_name(self):
        """get the name of the player who's playing"""
        return self.player_names[self.playing_index]

    def update(self):
        """update method for the game"""
        # get input and check input
        # inverting players
        self.playing_index = int(not self.playing_index)

        # processing input
        _input = self.current_input
        _input = _input.split(":")
        _shooting_key = _input[1]
        _line_index = int(_input[0]) - 1

        # focusing on the line that is played on
        currently_playing = self._objects_up_list[_line_index]
        # if the line contains only 1 item delete the line
        if currently_playing[0] == currently_playing[1]:
            self._objects_up_list.pop(_line_index)
        else:
            # remove the beginning of the line
            if _shooting_key == 'G':
                currently_playing[0] += 1
            # remove the end of the line
            if _shooting_key == 'D':
                currently_playing[1] -= 1
            # split the line into 2 lines
            if _shooting_key == 'M':
                # get the 2 split lines
                output = calculate_parts_w_random(currently_playing)
                # if line is of length 2 delete the line
                if output == "del line":
                    self._objects_up_list.pop(_line_index)
                else:
                    # adding 1 line to the list
                    if len(output) == 3:
                        self._objects_up_list.pop(_line_index)
                        # noinspection PyTypeChecker
                        self._objects_up_list.insert(_line_index, (output[1], output[2]))
                    else:
                        # add the two lines to the list
                        part1, part2 = output
                        self._objects_up_list.pop(_line_index)
                        self._objects_up_list.insert(_line_index, part2)
                        self._objects_up_list.insert(_line_index, part1)
        # add the game state to the game states lists
        self.game_states.append(copy.deepcopy(self._objects_up_list))
        # if there are no objects facing upwards left assign winner
        # (opposite of playing index as we changed the index at the start of the method)
        if not self._objects_up_list:
            self.winner = int(not self.playing_index)

    def is_winner(self):
        """check if there is a winner
        :return index: winner_index"""
        if not self._objects_up_list:
            self.winner = int(not self.playing_index)
            return self.player_names[self.winner]

    def parse_winner(self):
        """check if there is a winner and ask the user if they want to play again(reset game) else quit program"""
        _running_main = True
        # if game has ended print winner
        winner = self.is_winner()
        if winner:
            print("the winner is ", winner)
            self.render()
            # TODO change the way reverse moves are displayed
            #        print("rolling back moves")
            #        for _ in range(len(game.game_states) - 1):
            #            game.reverse_move()
            #            game.render_w_text()
            # if we are using turtle rendering engine render winner
            if self.rendering_engine:
                self.rendering_engine.show_winner(winner)
            # ask user if they want to play again
            _valid_input = False
            while not _valid_input:
                try:
                    # with rendering engine if it exits else through terminal input
                    if self.rendering_engine:
                        _running_main = self.rendering_engine.get_input(text=('play again?', '0/1'))
                    else:
                        _running_main = input('play again? 1/0:')
                    # check if valid else try again
                    _running_main = check_binary_input(_running_main)
                    _valid_input = True
                except ValueError as _e:
                    print(_e)
            # if play again reset else close
            if _running_main:
                self.reset()
            else:
                quit()

    def render(self):
        """method that handles the rendering"""
        # if we are using turtle use the rendering engine
        if self.rendering_engine:
            # update the objects and print to terminal
            self.rendering_engine.update(self.render_w_text(), self.playing_index)
            # render the player name of the player who's playing
            if self.playing_player_name() == 'bot':
                self.rendering_engine.write_text((0, - 350), self.playing_player_name() + "'s turn -->")
            else:
                self.rendering_engine.write_text((0, - 350), '<-- ' + self.playing_player_name() + "'s turn")
        else:
            # render in the terminal
            self.render_w_text()

    def reset(self):
        # reseting game variables
        self.object_num = random.randint(self.object_num_random_range[0], self.object_num_random_range[1])
        self._objects_up_list = [[0, self.object_num - 1]]
        # creating variables
        if self.rendering_engine:
            self.rendering_engine.reset(self.object_num)
            self.rendering_engine.initialise_turtles()
        else:
            self.rendering_engine = None
        self.current_input = ''
        self.playing_index = 0
        self.winner = None
        self.game_states = []
        #   adding the first game state
        self.game_states.append(copy.deepcopy(self._objects_up_list))


def main(nb_random_range=(15, 15)):
    # initialising game
    _running_main = True
    # TODO make inputs to get the names of players and check for 1v1 or 1vai
    player_dict = {
        0: str(input('Donnez votre nom :')),
        1: "bot"
    }
    print('''Regles du Jeu 
        Le joueur joue contre l'ordinateur. Au départ, un nombre de quilles est tiré au hasard. Le 
        joueur commence puis à chaque tour, le joueur ou l'ordinateur choisit de tirer au milieu, à gauche ou à droite 
        d'une ligne de quilles. Quand on tire au milieu, 2 quilles sont descendues, quand on tire à droite ou à gauche, 
        une seule quille est descendue. Quand on descend 2 quilles au milieu, la ligne de quille est coupée en deux. 
        Celui qui descend la dernière quille a gagné.
    Comment jouer?
        On joue en ecrivant la ligne(de 1 jusqu'au nombre de ligne du jeu) ou l'on veut jouer 
        suivit de ":" 
        puis de ou on veut tirer dans la ligne("G" a gauche, "M" au milieu, "D" a droite)
        exemple: 1:M  on tire sur la premiere ligne au milieu ''')
    input('press enter to continue')
    game = Game(nb_random_range, player_dict, mode='1vai')
    game.render()
    running = True
    while running:
        time.sleep(0.1)
        # update
        game.play_turn()
        game.update()
        # check winner
        game.parse_winner()
        # rendering
        game.render()


if __name__ == '__main__':
    running_main = True
    while running_main:
        main()
