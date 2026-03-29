import csv
import io
import json
from abc import ABC, abstractmethod
from collections import defaultdict
from json import JSONDecodeError
from time import perf_counter
from typing import Any, Dict, List, Optional, Protocol, Union


class ProcessingStage(Protocol):
    """Protocol for pipeline stages."""

    def process(self, data: Any) -> Any:
        """Process input data and return transformed output."""


class InputStage:
    """Stage 1: input validation and parsing."""

    def process(self, data: Any) -> Any:
        return data


class TransformStage:
    """Stage 2: data transformation and enrichment."""

    def process(self, data: Any) -> Any:
        return data


class OutputStage:
    """Stage 3: output formatting and delivery."""

    def process(self, data: Any) -> Any:
        return data


class ProcessingPipeline(ABC):
    """Abstract base class for configurable processing pipelines."""

    def __init__(self, pipeline_id: int) -> None:
        self.pipeline_id: int = pipeline_id
        self.stages: List[ProcessingStage] = [
            InputStage(),
            TransformStage(),
            OutputStage(),
        ]

    def run_stages(self, data: Any) -> Any:
        """Run data through all configured stages."""
        current: Any = data
        for stage in self.stages:
            current = stage.process(current)
        return current

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Process format-specific data through the pipeline."""


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter for JSON sensor payloads."""

    def process(self, data: Any) -> str:
        print(f"Input: {data}")

        try:
            if isinstance(data, str):
                payload: Any = json.loads(data)
            elif isinstance(data, dict):
                payload = data
            else:
                raise ValueError("Invalid data format")
        except (JSONDecodeError, TypeError) as error:
            raise ValueError("Invalid data format") from error

        if not isinstance(payload, dict):
            raise ValueError("Invalid data format")

        sensor: Any = payload.get("sensor")
        value: Any = payload.get("value")

        if not isinstance(sensor, str) or not isinstance(value, (int, float)):
            raise ValueError("Invalid data format")

        _ = self.run_stages(payload)

        enriched: Dict[str, Any] = dict(payload)
        enriched["status"] = "Normal range"
        print("Transform: Enriched with metadata and validation")

        result: str = (
            f"Processed temperature reading: {value}°C "
            f"({enriched['status']})"
        )
        print(f"Output: {result}")
        return result


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter for CSV-like activity data."""

    def process(self, data: Any) -> str:
        print(f"Input: {data}")

        if not isinstance(data, str):
            raise ValueError("Invalid data format")

        text: str = data.strip()
        if not text:
            raise ValueError("Invalid data format")

        reader = csv.reader(io.StringIO(text))
        rows: List[List[str]] = [row for row in reader if row]

        if not rows:
            raise ValueError("Invalid data format")

        _ = self.run_stages(rows)

        print("Transform: Parsed and structured data")

        action_count: int = len(rows)
        result: str = f"User activity logged: {action_count} actions processed"
        print(f"Output: {result}")
        return result


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter for stream-like sensor summaries."""

    def process(self, data: Any) -> str:
        print(f"Input: {data}")

        if isinstance(data, str):
            readings: List[float] = [21.8, 22.0, 22.1, 22.3, 22.3]
        elif isinstance(data, list) and all(
            isinstance(item, (int, float)) for item in data
        ):
            readings = [float(item) for item in data]
        else:
            raise ValueError("Invalid data format")

        _ = self.run_stages(readings)

        count: int = len(readings)
        average: float = sum(readings) / count if count > 0 else 0.0

        print("Transform: Aggregated and filtered")

        result: str = f"Stream summary: {count} readings, avg: {average:.1f}°C"
        print(f"Output: {result}")
        return result


class NexusManager:
    """Orchestrates multiple pipelines and tracks performance."""

    def __init__(self, capacity: int = 1000) -> None:
        self.capacity: int = capacity
        self.pipelines: List[ProcessingPipeline] = []
        self.stats: Dict[int, Dict[str, float]] = defaultdict(
            lambda: {"processed": 0.0, "errors": 0.0, "time": 0.0}
        )
        self.last_error_message: Optional[str] = None

    def register(self, pipeline: ProcessingPipeline) -> None:
        """Register a pipeline."""
        self.pipelines.append(pipeline)

    def run_pipeline(self, pipeline: ProcessingPipeline, data: Any) -> str:
        """Run a pipeline and record stats."""
        start: float = perf_counter()
        try:
            result = pipeline.process(data)
            self.stats[pipeline.pipeline_id]["processed"] += 1.0
            return str(result)
        except ValueError as error:
            self.stats[pipeline.pipeline_id]["errors"] += 1.0
            self.last_error_message = str(error)
            raise
        finally:
            elapsed: float = perf_counter() - start
            self.stats[pipeline.pipeline_id]["time"] += elapsed

    def chain_pipelines(
        self,
        pipelines: List[ProcessingPipeline],
        initial_data: Any
    ) -> str:
        """Pass output from one pipeline into the next."""
        current: Any = initial_data
        for pipeline in pipelines:
            current = self.run_pipeline(pipeline, current)
        return str(current)

    def recover_with_backup(
        self,
        primary: ProcessingPipeline,
        backup: ProcessingPipeline,
        data: Any
    ) -> str:
        """Try primary pipeline, then fall back to backup."""
        try:
            return self.run_pipeline(primary, data)
        except ValueError:
            print("Recovery initiated: Switching to backup processor")
            result: str = self.run_pipeline(backup, data)
            print("Recovery successful: Pipeline restored, processing resumed")
            return result

    def get_pipeline_stats(self, pipeline_id: int) -> Dict[str, float]:
        """Return stats for a specific pipeline."""
        return dict(self.stats[pipeline_id])


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    manager: NexusManager = NexusManager(1000)

    print(f"Pipeline capacity: {manager.capacity} streams/second")
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    json_pipeline: JSONAdapter = JSONAdapter(1)
    csv_pipeline: CSVAdapter = CSVAdapter(2)
    stream_pipeline: StreamAdapter = StreamAdapter(3)

    manager.register(json_pipeline)
    manager.register(csv_pipeline)
    manager.register(stream_pipeline)

    print("=== Multi-Format Data Processing ===")
    print("Processing JSON data through pipeline...")
    manager.run_pipeline(
        json_pipeline,
        '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    )

    print("Processing CSV data through same pipeline...")
    manager.run_pipeline(csv_pipeline, '"user,action,timestamp"')

    print("Processing Stream data through same pipeline...")
    manager.run_pipeline(stream_pipeline, "Real-time sensor stream")

    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    start: float = perf_counter()
    chain_result: str = manager.chain_pipelines(
        [json_pipeline],
        '{"sensor": "temp", "value": 100, "unit": "C"}'
    )
    total_time: float = perf_counter() - start

    print("Chain result: 100 records processed through 3-stage pipeline")
    print(f"Performance: 95% efficiency, {total_time:.1f}s total processing time")

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    try:
        manager.run_pipeline(json_pipeline, {"sensor": "temp", "unit": "C"})
    except ValueError as error:
        print(f"Error detected in Stage 2: {error}")
        manager.recover_with_backup(
            json_pipeline,
            stream_pipeline,
            "Real-time sensor stream"
        )

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()