# load_env.py
from pathlib import Path
from dotenv import load_dotenv
import os

def load_env(env_file: str = "./env") -> None:
    """Load environment variables from a file."""
    env_path = Path(env_file).resolve()
    if not env_path.exists():
        raise FileNotFoundError(f"{env_file} not found")
    
    load_dotenv(dotenv_path=env_path)
    print(f"Environment loaded from {env_path}")

def get_env(var_name: str) -> str:
    """Get an environment variable and raise error if missing."""
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable {var_name} is not set")
    return value
