from dataclasses import dataclass

from asciify.exceptions import InvalidRasterError

VALID_CHANNELS = (1, 2, 3, 4)


@dataclass
class Raster:
    width: int
    height: int
    channels: int
    pixels: bytes

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise InvalidRasterError(
                f"Dimensions must be positive, got {self.width}x{self.height}"
            )

        if self.channels not in VALID_CHANNELS:
            raise InvalidRasterError(
                f"Unsupported channel count: {self.channels}. Supported channel counts are {VALID_CHANNELS}"
            )

        expected = self.width * self.height * self.channels
        if len(self.pixels) != expected:
            raise InvalidRasterError(
                f"Expected {expected} bytes "
                f"({self.width} x {self.height} x {self.channels}), got {len(self.pixels)} bytes"
            )
