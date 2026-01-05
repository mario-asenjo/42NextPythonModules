"""
This program demonstrates the use of polymorphism in data streams
"""

from typing import Any, Callable, Dict, List, Optional, Union


Number = Union[int, float]
Transform = Callable[[str], str]


def strip_transform(value: str) -> str:
    """Default transform, strip spaces"""
    return value.strip()


def format_batch(batch: List[str]) -> str:
    """Format List[str] as [a, b, c] without quotes"""
    return "[" + ", ".join(batch) + "]"


class DataStream:
    """Base stream with shared workflow"""
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self._stream_id = stream_id
        self._stream_type = stream_type

        self.transforms: List[Transform] = [strip_transform]
        self.high_priority_only: bool = False

    def add_transform(self, transform: Transform) -> None:
        self.transforms.append(transform)

    def set_high_priority_only(self, enabled: bool) -> None:
        self.high_priority_only = enabled

    def process_batch(self, batch: List[str]) -> str:
        """
        Unified processing, same call on any stream type
        Applies transforms and optional filtering, then delegates to overriden methods
        """
        try:
            cleaned = self.apply_transforms(batch)
            if self.high_priority_only:
                cleaned = self.filter_high_priority(cleaned)
            print(f"Processing {self.label()} batch: {format_batch(cleaned)}")
            result = self.analyze_batch(cleaned)
            print(result)
            return result
        except (ValueError, TypeError) as e:
            message: str = f"{self.prefix()} analysis error: {e}"
            print(message)
            return message

    def apply_transforms(self, batch: List[str]) -> List[str]:
        output: List[str] = []

        for item in batch:
            value = item
            for transform in self.transforms:
                value = transform(value)
            output.append(value)
        return output

    def filter_high_priority(self, batch: List[str]) -> List[str]:
        return [item for item in batch if self.is_high_priority(item)]

    def count_high_priority(self, batch: List[str]) -> int:
        count: int = 0
        for item in batch:
            if self.is_high_priority(item):
                count += 1
        return count

    def batch_summary(self, batch: List[str]) -> str:
        try:
            cleaned = self.apply_transforms(batch)
            return self.summary_from_cleaned(cleaned)
        except (ValueError, TypeError) as e:
            return f"{self.prefix()} data: 0 processed"

    def is_high_priority(self, item: str) -> bool:
        _ = item
        return False

    def analyze_batch(self, batch: List[str]) -> str:
        raise NotImplementedError("Subclass must override analyze_batch()")

    def summary_from_cleaned(self, batch: List[str]) -> str:
        raise NotImplementedError("Subclass must override summary_from_cleaned()")

    def label(self) -> str:
        raise NotImplementedError("Subclass must override label()")

    def prefix(self) -> str:
        raise NotImplementedError("Subclass must override prefix()")


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Enviromental Data")


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Financial Data")


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")


def main() -> None:
    pass


if __name__ == "__main__":
    main()
