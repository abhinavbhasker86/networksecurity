from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging #    import logging
import yaml
import os
import sys
import numpy as np
#import dill
import pickle

def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its content as a dictionary.
    
    Args:
        file_path (str): Path to the YAML file.
        
    Returns:
        dict: Content of the YAML file.
        
    Raises:
        NetworkSecurityException: If there is an error reading the file.
    """
    try:
        with open(file_path, 'rb') as yaml_file:
           return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """Writes content to a YAML file.
    Args:
        file_path (str): Path to the YAML file.
        content (object): Content to write to the file.
        replace (bool): If True, replaces the existing file. Defaults to False.
    Raises:
        NetworkSecurityException: If there is an error writing to the file.
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        # Use 'w' mode to write the file, which will create it if it doesn't exist
        # and overwrite it if it does exist.
        with open(file_path, 'w') as yaml_file:
            yaml.dump(content, yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e