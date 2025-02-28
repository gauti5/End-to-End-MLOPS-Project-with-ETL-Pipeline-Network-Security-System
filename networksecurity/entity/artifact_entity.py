from dataclasses import dataclass # acts as a decarator, creates a variable for empty class

@dataclass

class DataIngestionArctifact:
    trained_file_path:str
    test_file_path:str

