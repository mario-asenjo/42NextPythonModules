"""
This program demonsrtates how different data types can share common processing
interfaces while mantaining their unique characteristics.
"""
from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """
    Base class that defines the common processing interface
    """

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
        
        total = sum(data)
        average = total / len(data)
        return (
            f"Processed {len(data)} numeric values, "
            f"sum={total}, avg={average:.1f}"
        )

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list) and len(data) > 0
            and all(isinstance(number, (int, float)) for number in data)
        )


class TextProcessor(DataProcessor):
    """Processor for text data"""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")
        
        words = data.split()
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
        
        data = str(data)
        

    def validate(self) -> str:
        self.log_type: str
        self.message: str
        self.message = self.__log.split(':', 1)[1].strip()
        self.log_type = self.__log.split(':', 1)[0].split(' ')[0].upper()
        self._is_data_verified = self.log_type in ["ERROR", "INFO", "WARNING"]
        if not self._is_data_verified:
            raise ValueError
        return "Log entry verified"

    def format_output(self) -> str:
        self.validate()
        log_level = "[ALERT]" if self.log_type == "ERROR"\
                    else f"[{self.log_type}]"
        return f"{log_level} {self.log_type} level detected: {self.message}"

    def print_routine(self) -> None:
        print("\nInitializing Log Processor...")
        super().print_routine()


def polymorphic_demo() -> None:
    print("\n=== Polymorphic Processing Demo === ")
    processors: list[DataProcessor] = [
        NumericProcessor([2, 2, 2]),
        TextProcessor("mario   abel"),
        LogProcessor("INFO: System ready")
    ]
    print("Processing multiple data types through the same interface...")
    for i, processor in enumerate(processors):
        try:
            print(f"Result {i}: {processor.format_output()}")
        except ValueError as e:
            print(e)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    numeric: NumericProcessor = NumericProcessor()
    text: TextProcessor = TextProcessor()
    log: LogProcessor = LogProcessor()
    numeric.print_routine()
    text.print_routine()
    log.print_routine()
    polymorphic_demo()
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
