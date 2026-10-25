def remove_student (self, name: str) -> None:
    """Remove a student, or raise KeyError if missing."""
    if name not in self.marks:
        raise KeyError(f"No student named{name}")
    del self.marks[name]
