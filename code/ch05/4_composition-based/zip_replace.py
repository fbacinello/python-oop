from zip_processor import ZipProcessor
import sys
import os


# NO SUPE COMO RESOLVER EL TEMA DE QUE ACA TENGOQ UE PASARLE LOS STRINGS

class ZipReplace():
    def __init__(self, filename, search_string, replace_string):
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """perform a search and replace on all files in the
        temporary directory"""

        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)


if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).process_zip()
