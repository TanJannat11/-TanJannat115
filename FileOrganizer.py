import os
import shutil

class FileOrganizer:
    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir
        self.destination_dir = destination_dir

    def organize_files(self):
        if not os.path.exists(self.destination_dir):
            os.makedirs(self.destination_dir)

        for filename in os.listdir(self.source_dir):
            file_path = os.path.join(self.source_dir, filename)

            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1][1:]
                destination_folder = os.path.join(self.destination_dir, file_extension)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                destination_path = os.path.join(destination_folder, filename)
                shutil.move(file_path, destination_path)

        print("File organization complete.")

def main():
    source_dir = "path/to/source/directory"
    destination_dir = "path/to/destination/directory"

    organizer = FileOrganizer(source_dir, destination_dir)
    organizer.organize_files()

if __name__ == "__main__":
    main()
