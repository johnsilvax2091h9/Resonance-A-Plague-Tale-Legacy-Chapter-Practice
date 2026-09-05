# Build: 046a040f96dcf1befa6f20b39de7aef5

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
