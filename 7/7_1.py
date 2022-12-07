# https://adventofcode.com/2022/day/7
import os
from dataclasses import dataclass

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")


@dataclass
class File:
    name: str
    size: int


class Directory:
    def __init__(self, name: str, parent: 'Directory' = None) -> None:
        self.name = name
        self.parent = parent
        self.content: list[File] = []
        self.child_directories: dict[str, 'Directory'] = {}
        self.file_size: int = 0
        self._total_size: int = 0

    def add_file(self, file: File):
        self.content.append(file)
        self.file_size += file.size

    def add_directory(self, directory: 'Directory'):
        self.child_directories[directory.name] = directory

    @property
    def total_size(self):
        if self._total_size:
            return self._total_size
        else:
            self._total_size = self.file_size
            for directory in self.child_directories.values():
                self._total_size += directory.total_size
            return self._total_size
s = set()
l = set()
c = {'ljv', 'wqcsrw', 'jllhmmf'}


directories: dict[str, Directory] = dict()
matched_directories_total_size = 0
root_directory = None
current_path = []


def construct_path(path: list[int]) -> str:
    p = "/".join(path)
    return "/".join(path)


with open(input_file, "r") as file:
    for line in file:
        line = line.strip()
        line_items = line.split()
        if line_items[0] == "$":
            if line_items[1] == "cd":
                dir_name = line_items[2]
                if dir_name == "/":
                    root_directory = current_directory = Directory(name=dir_name)
                elif dir_name == "..":
                    if current_directory.total_size <= 100000:
                        matched_directories_total_size += current_directory.total_size
                        if current_directory.name in c:

                            print("match", construct_path(current_path), current_directory.name)
                    else:
                        if current_directory.name in c:
                            print("dismatch", construct_path(current_path), current_directory.name)
                    current_directory = current_directory.parent
                    current_path.pop()
                else:
                    current_path.append(current_directory.name)
                    current_directory = current_directory.child_directories[dir_name]
        else:
            if line_items[0] == "dir":
                child_directory = Directory(name=line_items[1], parent=current_directory)
                current_directory.add_directory(child_directory)
            else:
                current_file = File(name=line_items[1], size=int(line_items[0]))
                current_directory.add_file(current_file)
    if root_directory.total_size <= 100000:
        matched_directories_total_size += root_directory.total_size

print(matched_directories_total_size)
