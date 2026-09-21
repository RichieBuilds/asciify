# asciify

Convert images into ASCII art — built entirely with Python's standard library, no third-party dependencies.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) for environment and dependency management

## Installation

```bash
git clone https://github.com/RichieBuilds/asciify.git
cd asciify
uv sync
```

## Usage

```bash
uv run asciify path/to/image.png
```

## Roadmap

- [x] PNG decoding
- [ ] JPEG decoding
- [ ] Configurable character ramps and output width
- [ ] Color / ANSI terminal output

## Why no libraries?

This project intentionally skips `Pillow` and other image libraries — the goal is understanding image file formats and pixel-level processing from first principles, not shipping the fastest possible converter.

## License

TBD