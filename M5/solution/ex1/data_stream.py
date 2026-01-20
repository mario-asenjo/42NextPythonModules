"""
This program demonstrates the use of polymorphism in data streams
"""
from ipaddress import summarize_address_range
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
        """
        Used by StreamProcessor
        :param batch:
        :return:
        """
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
        print("Initializing Sensor Stream.")
        super().__init__(stream_id, "Enviromental Data")
        print(f"Stream ID: {self._stream_id}, Type: {self._stream_type}")

    @staticmethod
    def parse_readings(batch: List[str]) -> List[Dict[str, Any]]:
        readings: List[Dict[str, Any]] = []
        for item in batch:
            metric, value = SensorStream.split_kv(item)
            readings.append({"metric": metric, "value": value})
        return readings

    @staticmethod
    def avg_temperature(readings: List[Dict[str, Any]]) -> float:
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
        _key, value = SensorStream.split_kv(item)
        return float(value)

    def label(self) -> str:
        return "sensor"

    def prefix(self) -> str:
        return "Sensor"

    def analyze_batch(self, batch: List[str]) -> str:
        readings: List[Dict[str, Any]] = self.parse_readings(batch)
        avg_temp = SensorStream.avg_temperature(readings)
        return (
            f"Sensor analysis: {len(readings)} readings processed, "
            f"avg temp: {avg_temp:.1f}ºC"
        )

    def summary_from_cleaned(self, batch: List[str]) -> str:
        readings: List[Dict[str, Any]] = self.parse_readings(batch)
        return f"Sensor data: {len(readings)} readomgs processed"

    def is_high_priority(self, item: str) -> bool:
        if not item.startswith("temp:"):
            return False
        value = SensorStream.parse_value_after_colon(item)
        return value >= 30.0


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Transaction Stream.")
        super().__init__(stream_id, "Financial Data")
        print(f"Stram ID: {self._stream_id}, Type: {self._stream_type}")

    @staticmethod
    def net_flow(ops: List[Dict[str, Any]]) -> int:
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
        ops: List[Dict[str, Any]] = []
        for item in batch:
            kind, amount = TransactionStream.split_kind_amount(item)
            ops.append({"kind": kind, "amount": amount})
        return ops

    def label(self) -> str:
        return "transaction"

    def prefix(self) -> str:
        return "Transaction"

    def analyze_batch(self, batch: List[str]) -> str:
        ops: List[Dict[str, Any]] = TransactionStream.parse_ops(batch)
        net = TransactionStream.net_flow(ops)
        return (
            f"Transaction analysis: {len(ops)} operations, "
            f"net flow: {net:+d} units"
        )

    def summary_from_cleaned(self, batch: List[str]) -> str:
        ops: List[Dict[str, Any]] = TransactionStream.parse_ops(batch)
        return f"Transaction data: {len(ops)} operations processed"

    def is_high_priority(self, item: str) -> bool:
        _kind, amount = TransactionStream.split_kind_amount(item)
        return abs(amount) >= 300


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        print("Initializing Event Stream.")
        super().__init__(stream_id, "System Events")
        print(f"Stream ID: {self._stream_id}, Type: {self._stream_type}")

    @staticmethod
    def parse_events(batch: List[str]) -> List[str]:
        events: List[str] = []
        for item in batch:
            if item == "":
                raise ValueError("Empty event")
            events.append(item)
        return events

    def label(self) -> str:
        return "event"

    def prefix(self) -> str:
        return "Event"

    def analyze_batch(self, batch: List[str]) -> str:
        events = self.parse_events(batch)
        errors = 0
        for e in events:
            if e.lower() == "error":
                errors += 1
        return f"Event analysis: {len(events)} events, {errors} error detected"

    def summary_from_cleaned(self, batch: List[str]) -> str:
        events = EventStream.parse_events(batch)
        return f"Event data: {len(events)} events processed"

    def is_high_priority(self, item: str) -> bool:
        return item.strip().lower() == "error"


class StreamProcessor:
    def __init__(self) -> None:
        self.high_priority_mode: bool = False

    def enable_high_priority_mode(self) -> None:
        self.high_priority_mode = True

    def process_mixed_streams(self, streams: List[DataStream], batches: List[List[str]]) -> None:
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
