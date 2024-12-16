from pathlib import Path

from ..utils import EXTENSION_TYPE_MAPPING

from .researchers import (
    AudioResearcher,
    ImageResearcher,
    PdfResearcher,
    VideoResearcher,
)


class ResearchRouter:
    def __init__(self):
        """
        Initializes the ResearchRouter instance.

        The ResearchRouter maps file extensions to the relevant Researcher objects.
        """
        self.researchers = {
            "Image": ImageResearcher(),
            "Document": PdfResearcher(),
            "Video": VideoResearcher(),
            "Audio": AudioResearcher(),
        }

    def get_file_info(self, file_path: str) -> dict:
        """
        Retrieves file information using the Researcher corresponding to the file extension.

        Args:
            file_path (str): The path to the file.

        Returns:
            dict: The file information if the file extension is supported, otherwise None.
        """
        file_path = Path(file_path)
        file_extension = file_path.suffix.lower()
        if file_extension in EXTENSION_TYPE_MAPPING:
            file_type = EXTENSION_TYPE_MAPPING[file_extension]
            try:
                file_info = self.researchers[file_type].get_file_info(file_path)

                return file_info
            except KeyError:
                return (file_type, None)
