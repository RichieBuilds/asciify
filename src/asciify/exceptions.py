class UnsupportedFileFormatError(ValueError):
    """Raised when an image format is not supported."""


class InvalidRasterError(ValueError):
    """Raised when raster dimensions or pixel data are invalid."""