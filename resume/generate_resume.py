# jdl_bench/resume/generate_resume.py

"""
TODO: JDL
"""

import logging
import os
import subprocess
from pathlib import Path

from rich.logging import RichHandler


class GenerateResume:
    """
    TODO
    """

    DEFAULT_DOCUMENT_FILEPATH = Path("resume/resume.tex")

    def __init__(self, document_filepath: Path = DEFAULT_DOCUMENT_FILEPATH) -> None:
        """
        Initialize the instance's logger, validate the inputs, and generate the document.

        Args:
            document_filepath: Optional, a filepath where the generated tocument will be
                placed.

        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.INFO)
        self.logger.info("Generating document...")

        self.repository_root_directory = os.environ["BUILD_WORKING_DIRECTORY"]
        self.document_filepath = document_filepath
        self.document_filename = self.document_filepath.stem

    def _cleanup(self) -> None:
        """
        Attempt to remove any unused files generated during the production of the
        document.
        """
        self.logger.info("Cleaning up")
        files_to_remove = [
            self.repository_root_directory
            / self.document_filepath.parent
            / f"{self.document_filename}.aux",
            self.repository_root_directory
            / self.document_filepath.parent
            / f"{self.document_filename}.log",
            self.repository_root_directory
            / self.document_filepath.parent
            / f"{self.document_filename}.out",
        ]

        for file_to_remove in files_to_remove:
            if file_to_remove.exists():
                self.logger.info(f"Removing {file_to_remove}")
                file_to_remove.unlink(missing_ok=True)

    def generate_document(self):
        """
        Generate the resume as a PDF using pdflatex.

        Raises:
            TODO
        """
        generate_command = [
            "pdflatex",
            f"{self.document_filename}.tex",
        ]
        try:
            subprocess.run(
                generate_command,
                check=True,
                cwd=Path(self.repository_root_directory) / "resume",
            )

        except subprocess.CalledProcessError as called_process_error_message:
            self.logger.error(called_process_error_message)

        self._cleanup()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, show_path=False)],
    )

    resume_generator = GenerateResume()
    resume_generator.generate_document()
