from typing import List


class CommandParser:
    """Parses simple voice commands and detects exit triggers."""

    EXIT_PHRASES: List[str] = ["exit", "quit", "goodbye", "stop"]

    def is_exit_command(self, text: str) -> bool:
        """Return True when the user wants to stop the assistant."""
        normalized = text.lower().strip()
        return any(phrase in normalized for phrase in self.EXIT_PHRASES)
