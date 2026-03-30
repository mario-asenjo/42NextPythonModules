"""
Polymorphic data stream processing.

This program demonstrates the use of polymorphism in data streams
using a unified interface `DataStream.process_batch()` across
different stream types (sensor, transaction and event streams).
"""
from abc import abstractmethod
from typing import Any, Callable, Dict, List, Union, Optional


class DataStream:
    """Abstract base class for all data streams"""

    def __init__(self, stream_id: str, stream_type: str) -> None:
        """Initialize the stream with its identifier and type label."""
        self._stream_id = stream_id
        self._stream_type = stream_type

        self.last_processed_count: int = 0
        self.last_filtered_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a result string"""
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        """Default filter: return the batch unchanged"""
        _ = criteria
        self.last_filtered_count = len(data_batch)
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return default stream statistics"""
        return {
            "stream_id": self._stream_id,
            "stream_type": self._stream_type,
            "last_processed": self.last_processed_count,
            "last_filtered": self.last_filtered_count
        }


class SensorStream(DataStream):
    """Process environmental sensor data"""

    def __init__(self, stream_id: str) -> None:
        print("Initializing Sensor Stream...")
        super().__init__(stream_id, "Environmental Data")
        print(f"Stream ID: {self._stream_id}, Type: {self._stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        average: float = 0
        try:
            cleaned_batch: List[str] = [
                str(item).strip() for item in data_batch if str(item).strip()
            ]
            print(
                "Processing sensor batch: "
                f"[{','.join(cleaned_batch)}]"
            )

            temperatures: List[float] = []
            for item in cleaned_batch:
                if ":" not in item:
                    raise ValueError(f"Invalid sensor reading: {item}")

                metric, value = item.split(":", 1)
                metric = metric.strip().lower()
                value = value.strip()

                if metric == "temp":
                    temperatures.append(float(value))

                average = sum(temperatures) / len(temperatures)
        except (ValueError, TypeError) as error:
            raise ValueError(f"Sensor processing failed: {error}") from error
        return (
            f"Sensor analysis: {len(cleaned_batch)} readings processed, "
            f"avg temp: {average:.1f} ºC"
        )

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        cleaned_batch: List[str] = [
            str(item).strip() for item in data_batch if str(item).strip()
        ]

        if criteria == "high":
            filtered: List[Any] = []
            for item in cleaned_batch:
                if item.lower().startswith("temp:"):
                    _metric, value = item.split(":", 1)
                    if float(value.strip()) >= 30.0:
                        filtered.append(item)
            self.last_filtered_count = len(cleaned_batch)
            return cleaned_batch

        self.last_filtered_count = len(cleaned_batch)
        return cleaned_batch


class TransactionStream(DataStream):
    """Process financial transaction data"""

    def __init__(self, stream_id: str) -> None:
        print("Initializing Transaction Stream...")
        super().__init__(stream_id, "Financial Data")
        print(f"Stram ID: {self._stream_id}, Type: {self._stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            cleaned_batch: List[str] = [
                str(item).strip() for item in data_batch if item.strip()
            ]
            print(
                "Processing transaction batch: "
                f"[{', '.join(cleaned_batch)}]"
            )

            net_flow: int = 0
            for item in cleaned_batch:
                if ":" not in item:
                    raise ValueError(f"Invalid transaction: {item}")

                operation, amount_text = item.split(":", 1)
                operation = operation.strip().lower()
                amount = int(amount_text.strip())

                if operation == "buy":
                    net_flow += amount
                elif operation == "sell":
                    net_flow -= amount
                else:
                    raise ValueError(f"Unknown operation: {operation}")

            self.last_filtered_count = len(cleaned_batch)

            return (
                f"Transaction analysis: {len(cleaned_batch)} operations, "
                f"net flow: {net_flow:+d} units"
            )
        except (ValueError, TypeError) as error:
            raise ValueError(
                f"Transaction processing failed: {error}"
            ) from error

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        cleaned_batch: List[str] = [
            str(item).strip() for item in data_batch if str(item).strip()
        ]

        if criteria == "high":
            filtered: List[Any] = []
            for item in cleaned_batch:
                if ":" in item:
                    _operation, amount_text = item.split(":", 1)
                    if abs(int(amount_text.strip())) >= 300:
                        filtered.append(item)
            self.last_filtered_count = len(filtered)
            return filtered

        self.last_filtered_count = len(cleaned_batch)
        return cleaned_batch


class EventStream(DataStream):
    """Process system event data"""

    def __init__(self, stream_id: str) -> None:
        print("Initializing Event Stream...")
        super().__init__(stream_id, "System Events")
        print(f"Stream ID: {self._stream_id}, Type: {self._stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            cleaned_batch: List[str] = [
                str(item).strip() for item in data_batch if str(item).strip()
            ]
            print(
                "Processing event batch: "
                f"[{', '.join(cleaned_batch)}]"
            )

            if not cleaned_batch:
                raise ValueError("Empty event batch")

            error_count: int = 0
            for item in cleaned_batch:
                if item.lower() == "error":
                    error_count += 1

            self.last_processed_count = len(cleaned_batch)

            return (
                f"Event analysis: {len(cleaned_batch)} events, "
                f"{error_count} error detected"
            )
        except (ValueError, TypeError) as e:
            raise ValueError(f"Event processing failed: {e}") from e

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        cleaned_batch: List[str] = [
            str(item).strip() for item in data_batch if str(item).strip()
        ]

        if criteria == "high":
            filtered: List[Any] = [
                item for item in cleaned_batch if item.lower() == "error"
            ]
            self.last_filtered_count = len(filtered)
            return filtered

        self.last_filtered_count = len(cleaned_batch)
        return cleaned_batch


class StreamProcessor:
    """Handle multiple stream types through polymorphism"""

    def process_mixed_streams(
            self,
            streams: List[DataStream],
            batches: List[List[Any]]
    ) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("\nBatch 1 Results:")

        for stream, batch in zip(streams, batches):
            try:
                filtered_batch: List[Any] = stream.filter_data(batch)
                stream.last_processed_count = len(filtered_batch)

                if isinstance(stream, SensorStream):
                    print(
                        f"- Sensor data: {len(filtered_batch)} readings processed"
                    )
                elif isinstance(stream, TransactionStream):
                    print(
                        f"- Transaction data: "
                        f"{len(filtered_batch)} operations processed"
                    )
                elif isinstance(stream, EventStream):
                    print(
                        f"- Event data: {len(filtered_batch)} events processed"
                    )
            except ValueError as err:
                print(f"- Stream error: {err}")

        print("\nStream filtering active: High-priority data only")

        sensor_alerts: int = 0
        large_transactions: int = 0

        for stream, batch in zip(streams, batches):
            try:
                filtered_batch = stream.filter_data(batch, "high")
                if isinstance(stream, SensorStream):
                    sensor_alerts = len(filtered_batch)
                elif isinstance(stream, TransactionStream):
                    large_transactions = len(filtered_batch)
            except ValueError:
                continue

        print(
            "Filtered results: "
            f"{sensor_alerts} critical sensor alerts, "
            f"{large_transactions} large transactions"
        )


def main() -> None:
    """Run the module demo with example batches."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor: SensorStream = SensorStream("SENSOR_001")
    sensor_batch: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    try:
        print(sensor.process_batch(sensor_batch))
    except ValueError as error:
        print(error)

    print()
    transaction: TransactionStream = TransactionStream("TRANS_001")
    trans_batch: List[str] = ["buy:100", "sell:150", "buy:75"]
    try:
        print(transaction.process_batch(trans_batch))
    except ValueError as error:
        print(error)

    print()
    event: EventStream = EventStream("EVENT_001")
    event_batch: List[str] = ["login", "error", "logout"]
    try:
        print(event.process_batch(event_batch))
    except ValueError as error:
        print(error)

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
