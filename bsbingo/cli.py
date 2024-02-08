import argparse
from bsbingo.bsbingo import game_loop, RenderConfig, read_buzzwords, buzzwords_to_grid


def main(args):
    words = read_buzzwords(args.words)
    longest = max(len(w) for w in words)
    render_config = RenderConfig(padding=longest + args.margin)

    buzzwords = buzzwords_to_grid(words, args.grid_size)
    game_loop(buzzwords, render_config)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("words", type=str, help="file with words as lines")
    parser.add_argument(
        "-g", "--grid-size", type=int, default=5, help="grid size (default 5)"
    )
    parser.add_argument("-m", "--margin", type=int, default=5, help="word margin size")
    args = parser.parse_args()

    main(args)


if __name__ == "__main__":
    cli()
