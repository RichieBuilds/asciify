from asciify.exceptions import UnsupportedFileFormat
from asciify.formats import Formart

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def identify_format(data: bytes) -> Formart:
    if data.startswith(PNG_SIGNATURE):
        return Formart.PNG
    raise UnsupportedFileFormat("Unsupported image format")