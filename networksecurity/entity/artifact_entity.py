from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Data class to hold the  artifacts generated during data ingestion.
    """
    trained_file_path: str
    test_file_path: str
