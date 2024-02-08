from dataclasses import dataclass


QUIT_COMMAND = "quit"
PROMPT = f"put coordinate 0,0 -> 4,4 (or  '{QUIT_COMMAND}' to exit)\n"
TICKED = "[x]"
UNTICKED = "[ ]"


@dataclass
class RenderConfig:
    padding: int = 28


WordGrid = list[list[str]]


def parse_coordinate(string: str) -> tuple[int, int]:
    row, col = string.split(",")
    return int(row), int(col)


def is_coordinate(string: str) -> bool:
    try:
        parse_coordinate(string)
        return True
    except Exception:
        return False


def is_ticked(string: str):
    return string.startswith(TICKED)


def tick(string: str) -> str:
    base = string.split("]")[-1]
    return TICKED + base


def untick(string: str) -> str:
    base = string.split("]")[-1]
    return UNTICKED + base


def render(buzzwords: WordGrid, render_config: RenderConfig) -> None:
    rendered = ""
    for rows in buzzwords:
        for col in rows:
            rendered += col.ljust(render_config.padding, " ")
        rendered += "\n"
    print(rendered)


def update_buzzwords(buzzwords: WordGrid, command: str) -> WordGrid:
    row, col = parse_coordinate(command)
    if is_ticked(buzzwords[row][col]):
        buzzwords[row][col] = untick(buzzwords[row][col])
    else:
        buzzwords[row][col] = tick(buzzwords[row][col])
    return buzzwords


def game_loop(buzzwords: WordGrid, render_config: RenderConfig) -> None:
    render(buzzwords, render_config)
    while True:
        command = input(PROMPT).strip()

        if command == QUIT_COMMAND:
            print("did you win son?")
            break
        elif is_coordinate(command):
            buzzwords = update_buzzwords(buzzwords, command)
            render(buzzwords, render_config)
        else:
            print(PROMPT)


def read_buzzwords(file: str) -> list[str]:
    with open(file, "r") as fin:
        words = fin.readlines()
    return [w.strip() for w in words]


def buzzwords_to_grid(words: list[str], grid_size: int) -> WordGrid:
    unticked = [untick(w) for w in words]
    as_grid = []
    for i in range(len(unticked) // grid_size):
        start = i * grid_size
        end = i * grid_size + grid_size
        row = unticked[start:end]
        as_grid.append(row)

    return as_grid
