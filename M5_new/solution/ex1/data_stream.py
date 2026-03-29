"""
Polymorphic data stream processing.

This program demonstrates the use of polymorphism in data streams
using a unified interface `DataStream.process_batch()` across
different stream types (sensor, transaction and event streams).
"""
from typing import Any, Callable, Dict, List, Union


Number = Union[int, float]
Transform = Callable[[str], str]


def strip_transform(value: str) -> str:
    """Strip surrounding whitespace from *value*."""
    return value.strip()


def format_batch(batch: List[str]) -> str:
    """Format a list of strings as ``[a, b, c]`` without quotes."""
    return "[" + ", ".join(batch) + "]"


class DataStream:
    """
    Provide a shared workflow for processing batches of stream data.

    Subclasses override domain-specific behavior:
    - `label()` / `prefix()` to customize printed messages.
    - `analyze_batch()` to implement analysis logic.
    - `summary_from_cleaned()` to implement summary logic.
    - `is_high_priority()` to define high-priority filtering rules.

    Attributes:
        transforms: Transformation pipeline applied to each item in a batch.
        high_priority_only: If True, only high-priority items are processed.
    """

    def __init__(self, stream_id: str, stream_type: str) -> None:
        """Initialize the stream with its identifier and type label."""
        self._stream_id = stream_id
        self._stream_type = stream_type

        self.transforms: List[Transform] = [strip_transform]
        self.high_priority_only: bool = False

    def add_transform(self, transform: Transform) -> None:
        """
        Add a transformation function to the pipeline.

        Args:
            transform: Function that receives a string and returns a
            transformed string.
        """
        self.transforms.append(transform)

    def set_high_priority_only(self, enabled: bool) -> None:
        """
        Enable or disable high-priority-only processing.

        Args:
            enabled: If True, non-high-priority items are filtered out.
        """
        self.high_priority_only = enabled

    def process_batch(self, batch: List[str]) -> str:
        """
        Process a batch through transforms, optional filtering, and analysis.

        This is the polymorphic entry point: all stream subtypes can be
        processed through the same method call.

        Args:
            batch: List of raw batch items.

        Returns:
            A human-readable analysis message.

        Raises:
            ValueError: If the batch contents cannot be parsed/validated
                        by a subtype.
            TypeError: If a provided batch item is not compatible with the
                        pipeline.
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
        """
        Apply the configured transformation pipeline to a batch.

        Args:
            batch: Raw batch items.

        Returns:
            A new list containing the transformed items.
        """
        output: List[str] = []

        for item in batch:
            value = item
            for transform in self.transforms:
                value = transform(value)
            output.append(value)
        return output

    def filter_high_priority(self, batch: List[str]) -> List[str]:
        """
        Return only the items considered high priority.

        Args:
            batch: Transformed batch items.

        Returns:
            A list containing only the items for which `is_high_priority()`
            is True.
        """
        return [item for item in batch if self.is_high_priority(item)]

    def count_high_priority(self, batch: List[str]) -> int:
        """
        Count high-priority items in the given batch.

        Args:
            batch: Batch items to evaluate.

        Returns:
            The number of items that are considered high priority.
        """
        count: int = 0
        for item in batch:
            if self.is_high_priority(item):
                count += 1
        return count

    def batch_summary(self, batch: List[str]) -> str:
        """
        Return a short summary used by the stream processor demo.

        Args:
            batch: Raw batch items.

        Returns:
            A summary string produced by the subtype.
        """
        try:
            cleaned = self.apply_transforms(batch)
            return self.summary_from_cleaned(cleaned)
        except (ValueError, TypeError):
            return f"{self.prefix()} data: 0 processed"

    # ---- Methods implemented by child classes ----

    def is_high_priority(self, item: str) -> bool:
        """Return True if *item* should be treated as high priority."""
        _ = item
        return False

    def analyze_batch(self, batch: List[str]) -> str:
        """Analyze a transformed (and optionally filtered) batch."""
        raise NotImplementedError("Subclass must override analyze_batch()")

    def summary_from_cleaned(self, batch: List[str]) -> str:
        """Summarize a transformed batch for reporting purposes."""
        raise NotImplementedError(
            "Subclass must override summary_from_cleaned()"
        )

    def label(self) -> str:
        """
        Return the label used in 'Processing <label> batch: ...' messages.
        """
        raise NotImplementedError("Subclass must override label()")

    def prefix(self) -> str:
        """Return the prefix used in '<Prefix> analysis: ...' messages."""
        raise NotImplementedError("Subclass must override prefix()")


class SensorStream(DataStream):
    """Process environmental sensor readings (e.g., ``temp:22.5``)."""

    def __init__(self, stream_id: str):
        """Initialize the sensor stream."""
        print("Initializing Sensor Stream.")
        super().__init__(stream_id, "Enviromental Data")
        print(f"Stream ID: {self._stream_id}, Type: {self._stream_type}")

    @staticmethod
    def parse_readings(batch: List[str]) -> List[Dict[str, Any]]:
        """
        Parse a batch into structured reading dictionaries.

        Args:
            batch: Items like ``metric:value``.

        Returns:
            A list of dicts with keys ``metric`` and ``value``.

        Raises:
            ValueError: If any item does not follow the expected
            ``metric:value`` format.
        """
        readings: List[Dict[str, Any]] = []
        for item in batch:
            metric, value = SensorStream.split_kv(item)
            readings.append({"metric": metric, "value": value})
        return readings

    @staticmethod
    def avg_temperature(readings: List[Dict[str, Any]]) -> float:
        """
        Compute the average temperature from parsed readings.

        Args:
            readings: Parsed reading dictionaries.

        Returns:
            The average temperature.

        Raises:
            ValueError: If no temperature reading is present.
        """
        temps: List[float] = []
        for r in readings:
            if r.get("metric") == "temp":
                temps.append(float(r["value"]))
        if not temps:
            raise ValueError("No temperature reading found")
        total: float = 0.0
        for t in temps:
            total += t
        return total / float(len(temps))

    @staticmethod
    def split_kv(item: str) -> tuple[str, Number]:
        """
        Split a ``metric:value`` reading into metric and numeric value.

        Args:
            item: String like ``temp:22.5``.

        Returns:
            A tuple ``(metric, value)`` where value is int or float.

        Raises:
            ValueError: If the format is invalid or the value is not numeric.
        """
        parts: list[str] = item.split(':', 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid sensor reading: {item}")
        key = parts[0].strip()
        raw = parts[1].strip()
        try:
            if "." in raw:
                value: Number = float(raw)
            else:
                value = int(raw)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Invalid sensor value: {raw}") from exc
        return key, value

    @staticmethod
    def parse_value_after_colon(item: str) -> float:
        """Extract the numeric value from a ``metric:value`` string."""
        _key, value = SensorStream.split_kv(item)
        return float(value)

    def label(self) -> str:
        """Return the stream label used in output messages."""
        return "sensor"

    def prefix(self) -> str:
        """Return the analysis prefix used in output messages."""
        return "Sensor"

    def analyze_batch(self, batch: List[str]) -> str:
        """Analyze sensor readings and compute average temperature."""
        readings: List[Dict[str, Any]] = self.parse_readings(batch)
        avg_temp = SensorStream.avg_temperature(readings)
        return (
            f"Sensor analysis: {len(readings)} readings processed, "
            f"avg temp: {avg_temp:.1f}ºC"
        )

    def summary_from_cleaned(self, batch: List[str]) -> str:
        """Summarize the number of processed sensor readings."""
        readings: List[Dict[str, Any]] = self.parse_readings(batch)
        return f"Sensor data: {len(readings)} readomgs processed"

    def is_high_priority(self, item: str) -> bool:
        """Treat temperatures >= 30.0 as high priority."""
        if not item.startswith("temp:"):
            return False
        value = SensorStream.parse_value_after_colon(item)
        return value >= 30.0


class TransactionStream(DataStream):
    """Process financial transaction operations (e.g., ``buy:100``)."""

    def __init__(self, stream_id: str):
        """Initialize the transaction stream."""
        print("Initializing Transaction Stream.")
        super().__init__(stream_id, "Financial Data")
        print(f"Stram ID: {self._stream_id}, Type: {self._stream_type}")

    @staticmethod
    def net_flow(ops: List[Dict[str, Any]]) -> int:
        """
        Compute net flow from parsed operations.

        Args:
            ops: Parsed operations with keys ``kind`` and ``amount``.

        Returns:
            Net flow where buys add and sells subtract.

        Raises:
            ValueError: If an operation kind is unknown.
        """
        total = 0
        for op in ops:
            kind: str = str(op["kind"]).lower()
            amount: int = int(op["amount"])
            if kind == "buy":
                total += amount
            elif kind == "sell":
                total -= amount
            else:
                raise ValueError(f"Unknown operation: {kind}")
        return total

    @staticmethod
    def split_kind_amount(item: str) -> tuple[str, int]:
        """
        Split a ``kind:amount`` transaction string.

        Args:
            item: String like ``buy:100``.

        Returns:
            A tuple ``(kind, amount)``.

        Raises:
            ValueError: If the format is invalid or amount is not an int.
        """
        parts = item.split(':', 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid transaction: {item}")
        kind = parts[0].strip()
        raw = parts[1].strip()
        try:
            amount = int(raw)
        except (TypeError, ValueError) as ex:
            raise ValueError(f"Invalid transaction amount: {raw}") from ex
        return kind, amount

    @staticmethod
    def parse_ops(batch: List[str]) -> List[Dict[str, Any]]:
        """Parse transaction batch items into operation dictionaries."""
        ops: List[Dict[str, Any]] = []
        for item in batch:
            kind, amount = TransactionStream.split_kind_amount(item)
            ops.append({"kind": kind, "amount": amount})
        return ops

    def label(self) -> str:
        """Return the stream label used in output messages."""
        return "transaction"

    def prefix(self) -> str:
        """Return the analysis prefix used in output messages."""
        return "Transaction"

    def analyze_batch(self, batch: List[str]) -> str:
        """Analyze transactions and compute net flow."""
        ops: List[Dict[str, Any]] = TransactionStream.parse_ops(batch)
        net = TransactionStream.net_flow(ops)
        return (
            f"Transaction analysis: {len(ops)} operations, "
            f"net flow: {net:+d} units"
        )

    def summary_from_cleaned(self, batch: List[str]) -> str:
        """Summarize the number of processed operations."""
        ops: List[Dict[str, Any]] = TransactionStream.parse_ops(batch)
        return f"Transaction data: {len(ops)} operations processed"

    def is_high_priority(self, item: str) -> bool:
        """Treat absolute transaction amounts >= 300 as high priority."""
        _kind, amount = TransactionStream.split_kind_amount(item)
        return abs(amount) >= 300


class EventStream(DataStream):
    """Process system events (e.g., ``login``, ``error``)."""
    def __init__(self, stream_id: str):
        """Initialize the event stream."""
        print("Initializing Event Stream.")
        super().__init__(stream_id, "System Events")
        print(f"Stream ID: {self._stream_id}, Type: {self._stream_type}")

    @staticmethod
    def parse_events(batch: List[str]) -> List[str]:
        """
        Validate and return event names from a batch.

        Args:
            batch: Event names.

        Returns:
            The same list of event names (validated).

        Raises:
            ValueError: If an empty event is encountered.
        """
        events: List[str] = []
        for item in batch:
            if item == "":
                raise ValueError("Empty event")
            events.append(item)
        return events

    def label(self) -> str:
        """Return the stream label used in output messages."""
        return "event"

    def prefix(self) -> str:
        """Return the analysis prefix used in output messages."""
        return "Event"

    def analyze_batch(self, batch: List[str]) -> str:
        """Analyze events and count error occurrences."""
        events = self.parse_events(batch)
        errors = 0
        for e in events:
            if e.lower() == "error":
                errors += 1
        return f"Event analysis: {len(events)} events, {errors} error detected"

    def summary_from_cleaned(self, batch: List[str]) -> str:
        """Summarize the number of processed events."""
        events = EventStream.parse_events(batch)
        return f"Event data: {len(events)} events processed"

    def is_high_priority(self, item: str) -> bool:
        """Treat the event name 'error' as high priority."""
        return item.strip().lower() == "error"


class StreamProcessor:
    """Orchestrate multiple streams using a unified polymorphic interface."""

    def __init__(self) -> None:
        """Initialize the processor."""
        self.high_priority_mode: bool = False

    def enable_high_priority_mode(self) -> None:
        """Enable high-priority mode for the processor demo."""
        self.high_priority_mode = True

    def process_mixed_streams(self, streams: List[DataStream],
                              batches: List[List[str]]) -> None:
        """
        Process different stream types and display a combined report.

        Args:
            streams: Stream instances to process.
            batches: One batch per stream, aligned by index.
        """
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface.\n")
        print("Batch 1 Results:")

        count: int = 0
        for stream in streams:
            summary = stream.batch_summary(batches[count])
            print(f"- {summary}")
            count += 1

        self.enable_high_priority_mode()
        print("\nStream filtering active: High-priority data only")

        sensor_alerts: int = 0
        large_transactions: int = 0
        i = 0

        for stream in streams:
            batch = batches[i]
            if isinstance(stream, SensorStream):
                sensor_alerts += stream.count_high_priority(batch)
            elif isinstance(stream, TransactionStream):
                large_transactions += stream.count_high_priority(batch)
            i += 1

        print(
            "Filtered results: "
            f"{sensor_alerts} critical sensor alerts, "
            f"{large_transactions} large transaction"
        )


def main() -> None:
    """Run the module demo with example batches."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor: SensorStream = SensorStream("SENSOR_001")
    sensor_batch: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor.process_batch(sensor_batch)

    print('\n', end="")
    transaction: TransactionStream = TransactionStream("TRANS_001")
    trans_batch: List[str] = ["buy:100", "sell:150", "buy:75"]
    transaction.process_batch(trans_batch)

    print('\n', end="")
    event: EventStream = EventStream("EVENT_001")
    event_batch: List[str] = ["login", "error", "logout"]
    event.process_batch(event_batch)

    processor: StreamProcessor = StreamProcessor()
    batches: List[List[str]] = [
        ["temp:35.0", "temp:31.0"],
        ["buy:100", "sell:150", "buy:75", "buy:500"],
        ["login", "error", "logout"]
    ]
    processor.process_mixed_streams([sensor, transaction, event], batches)
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
