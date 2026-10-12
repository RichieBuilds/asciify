from asciify.exceptions import UnsupportedFileFormat
from asciify.formats import Format

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def identify_format(data: bytes) -> Format:
    if data.startswith(PNG_SIGNATURE):
        return Format.PNG
    
    raise UnsupportedFileFormat("Unsupported image format")