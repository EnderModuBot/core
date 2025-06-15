def str2bool(value: str) -> bool:
    """Convert string value to boolean."""
    return value.lower() in ("yes", "true", "t", "y", "1")
