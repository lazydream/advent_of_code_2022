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
        self._size: int = 0

    def add_file(self, file: File):
        self.content.append(file)
        self.file_size += file.size

    def add_directory(self, directory: 'Directory'):
        self.child_directories[directory.name] = directory

    def get_all_subdirectories(self):
        for directory in self.child_directories.values():
            yield directory
            
            for directory in directory.get_all_subdirectories():
                yield directory

    @property
    def size(self):
        if self._size:
            return self._size
        else:
            self._size = self.file_size
            for directory in self.child_directories.values():
                self._size += directory.size
            return self._size


root_directory = Directory(name="/")

with open(input_file, "r") as file:
    for line in file:
        line = line.strip()
        line_items = line.split()
        if line_items[0] == "$":
            if line_items[1] == "cd":
                dir_name = line_items[2]
                if dir_name == "/":
                    current_directory = root_directory
                elif dir_name == "..":
                    current_directory = current_directory.parent
                else:
                    child_directory = Directory(name=dir_name, parent=current_directory)
                    current_directory.add_directory(child_directory)
                    current_directory = child_directory
        else:
            if line_items[0] != "dir":
                current_file = File(name=line_items[1], size=int(line_items[0]))
                current_directory.add_file(current_file)


matched_directories_size = 0
root_subdirectories_flat = list(root_directory.get_all_subdirectories())

for subdir in root_subdirectories_flat:
    if subdir.size <= 100000:
        matched_directories_size += subdir.size

print("Part 1 answer: ", matched_directories_size)

root_size = root_directory.size
required_space = 30000000
need_to_free_up_space = required_space - (70000000 - root_size)

for subdir in sorted(root_subdirectories_flat, key=lambda s: s.size):
    if subdir.size >= need_to_free_up_space:
        print("Part 2 answer: ", subdir.size)
        break
