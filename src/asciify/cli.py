import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="A tool to convert images to ascii"
    )

    parser.add_argument(
        "image-path",
        type=str,
        help="Path to image you want asciified"
    )

    return parser.parse_args()