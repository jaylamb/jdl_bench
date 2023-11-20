# jdl_bench/resume/generate_resume.py

"""
TODO: JDL
"""

import logging
import os
import subprocess

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Generating document...")

    DOCUMENT_DIRECTORY = "resume"
    DOCUMENT_FILENAME = "resume.tex"
    repository_root_directory = os.environ["BUILD_WORKING_DIRECTORY"]
    DOCUMENT_FILEPATH = os.path.join(repository_root_directory, DOCUMENT_DIRECTORY)

    # Build document
    os.chdir(DOCUMENT_FILEPATH)
    GENERATE_DOCUMENT_COMMAND = [
        "pdflatex",
        DOCUMENT_FILENAME,
    ]
    subprocess.run(GENERATE_DOCUMENT_COMMAND, check=True)

    # Clean up
    logging.info("Cleaning up")
    files_to_remove = [
        DOCUMENT_FILENAME.replace("tex", "aux"),
        DOCUMENT_FILENAME.replace("tex", "log"),
        DOCUMENT_FILENAME.replace("tex", "out"),
    ]

    for file_to_remove in files_to_remove:
        filepath_to_remove = os.path.join(DOCUMENT_FILEPATH, file_to_remove)
        if os.path.exists(filepath_to_remove):
            os.remove(filepath_to_remove)
