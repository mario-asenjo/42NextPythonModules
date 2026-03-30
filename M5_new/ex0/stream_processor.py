"""
This program demonsrtates how different data types can share common processing
interfaces while mantaining their unique characteristics.
"""
from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Base class that defines the common processing interface"""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the input data and return a result string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate the input data"""
        pass

    def format_output(self, result: str) -> str:
        """Default output formatter"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric lists"""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        
        total: int = sum(data)
        average: float = total / len(data)
        return (
            f"Processed {len(data)} numeric values, "
            f"sum={total}, avg={average:.1f}"
        )

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list)
            and len(data) > 0
            and all(isinstance(number, (int, float)) for number in data)
        )


class TextProcessor(DataProcessor):
    """Processor for text data"""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")
        
        words: list = data.split()
        return (
            f"Processed text: {len(data)} characters, "
            f"{len(words)} words"
        )

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data.strip()) > 0


class LogProcessor(DataProcessor):
    """Processor for log entries."""

    VALID_LEVELS = {"ERROR", "INFO", "WARNING"}

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")
        
        level, message = data.split(":", 1)
        level = level.strip().upper()
        message = message.strip()[:-1]

        tag: str = "[ALERT]" if level[1:] == "ERROR" else f"[{level[1:]}]"
        return f"{tag} {level[1:]} level detected: {message}"
        

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or ":" not in data:
            return False

        level, message = data.split(":", 1)
        return (
            level.strip().upper()[1:] in self.VALID_LEVELS
            and len(message.strip()) > 0
        )


def run_processor(processor: DataProcessor, data: Any) -> None:
    """Run the processing routine"""
    try:
        result = processor.process(data)

        if isinstance(processor, TextProcessor):
            p_type = "Text data"
        elif isinstance(processor, LogProcessor):
            p_type = "Log entry"
        else:
            p_type = "Numeric data"

        verified: str = "verified" if processor.validate(data) else "not verified"

        print(f'Processing data: {data}')
        print(f"Validation: {p_type} {verified}")
        print(processor.format_output(result))
    except ValueError as e:
        print(f"Error: {e}")


def polymorphic_demo() -> None:
    """Demonstrate polymorphism with different processor types"""
    print("\n=== Polymorphic Processing Demo === ")

    processors: list[tuple[DataProcessor, Any]] = [
        (NumericProcessor(), [2, 2, 2]),
        (TextProcessor(), "Hello Nexus World"),
        (LogProcessor(), '"INFO: System ready"')
    ]

    for i, (processor, data) in enumerate(processors, start=1):
        print(f"Result {i}: ", end="")
        try:
            result = processor.process(data)
            print(processor.format_output(result))
        except ValueError as e:
            print(f"Error: {e}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    run_processor(NumericProcessor(), [1, 2, 3, 4, 5])

    print("\nInitializing Text Processor...")
    run_processor(TextProcessor(), '"Hello Nexus World"')

    print("\nInitializing Log Processor...")
    run_processor(LogProcessor(), '"ERROR: Connection timeout"')

    polymorphic_demo()

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
