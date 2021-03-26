import sys
from zip_processor import ZipProcessor


class ZipReplace:
    def __init__(self, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self, temp_directory):
        """perform a search and replace on all files in the
        temporary directory"""

        for filename in temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)


if __name__ == "__main__":
    processor = ZipProcessor(sys.argv[1], ZipReplace(*sys.argv[2:4]))
    processor.process_zip()

# Comando:
# python zip_replace.py zipeado.zip palo pal
