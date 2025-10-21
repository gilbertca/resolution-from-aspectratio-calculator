import argparse
import math

def main(aspect_ratio, width_range, height_range):
    # aspect_ratio as float:
    try:
        aspect_ratio = float(aspect_ratio) 
        return _main(aspect_ratio, width_range, height_range)
    except ValueError: pass

    # aspect_ratio as string:
    try:
        aspect_ratio = str(aspect_ratio)
        index = aspect_ratio.find(":") # Find index of ":"
        first_num = float(aspect_ratio[:index]) # Slice and cast first num
        second_num = float(aspect_ratio[index+1:]) # Slice and cast
        aspect_ratio = first_num / second_num
        return _main(aspect_ratio, width_range, height_range)
    except ValueError as e:
        print(f"""The provided aspect ratio '{aspect_ratio}'
              is neither a float or a string. Please try again.""")
        raise e

def _main(aspect_ratio, width_range, height_range):
    # Main loop:
    for width in range(1, int(width_range)):
        for height in range(1, int(height_range)):
            if math.isclose(aspect_ratio, width / height):
                print(f"{width}x{height}:{aspect_ratio}")

if __name__ == "__main__":
    # Config cmdline args:
    parser = argparse.ArgumentParser(
            prog="main.py",
            description="""Find all resolutions which match an aspect ratio 
            provided as a float, or as as string (e.g. '16:9').

            Using string representation is preferred,
            since it is *usually* difficult to manually include
            repeating, trailing decimals.""",
            epilog="""Example: `python3 main.py "16:9" 10000 10000` 
            or `python3 main.py 2.0121 2000 4000`""")
    parser.add_argument("aspect_ratio",
                        help="Aspect ratio as a string or float.")
    parser.add_argument('width_range',
                        help="The maximum resolution width to search for.")
    parser.add_argument('height_range',
                        help="The maximum resolution height to search for.")

    # Run program:
    args = parser.parse_args()
    main(args.aspect_ratio, args.width_range, args.height_range)
