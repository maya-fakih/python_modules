from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_name: str):
        self.name = stream_name
        self.data = []
        self.valid = True
        pass

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria:
                return [item for item in data_batch if item == criteria]
            else:
                return data_batch
        except Exception:
            return []

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        try:
            return {"Stream": "Data stream", "Status": "No data available"}
        except Exception:
            return {}


class SensorStream(DataStream):
    def __init__(self, stream_name: str):
        super().__init__(stream_name)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if len(data_batch) != 3:
                raise ValueError()
            batch_tuple = (
                (float(data_batch[0]), int(data_batch[1]), int(data_batch[2]))
            )
            self.data.append(batch_tuple)
            t, h, p = batch_tuple
            return f"[temp: {t}, humidity: {h}, pressure: {p}]"

        except Exception:
            self.valid = False
            return "Invalid input..."

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        if self.valid is True:
            data_len = len(self.data)
            temps = [batch[0] for batch in self.data]
            avg_t = sum(temps) / len(temps)
            return {"readings processed": data_len * 3, "avg temp": avg_t}
        else:
            return {"status": "invalid input"}

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if self.valid is True:
            filtered = []
            if criteria is None:
                filtered = data_batch.copy()
            elif criteria == "temperature":
                filtered.append(data_batch[0])
            elif criteria == "humidity":
                filtered.append(data_batch[1])
            elif criteria == "pressure":
                filtered.append(data_batch[2])
            else:
                print("Invalid criteria...")
            return filtered
        return []


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[str]) -> str:
        try:
            for item in data_batch:
                self.data.append(item)
            return f"[{', '.join(data_batch)}]"
        except Exception:
            self.valid = False
            return "Invalid transaction data..."

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        if self.valid is True and self.data:
            buy_total = 0
            sell_total = 0

            for transaction in self.data:
                if "buy:" in transaction:
                    try:
                        buy_total += int(transaction.split(":")[1])
                    except Exception:
                        pass
                elif "sell:" in transaction:
                    try:
                        sell_total += int(transaction.split(":")[1])
                    except Exception:
                        pass

            net_flow = buy_total - sell_total
            return {
                "operations": len(self.data),
                "net flow": f"{'+' if net_flow >= 0 else ''}{net_flow} units"
            }
        else:
            return {"status": "invalid input"}


class EventStream(DataStream):
    def process_batch(self, data_batch: List[str]) -> str:
        try:
            for item in data_batch:
                self.data.append(item)
            return f"[{', '.join(data_batch)}]"
        except Exception:
            self.valid = False
            return "Invalid event data..."

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        if self.valid is True and self.data:
            error_count = (
                sum(1 for event in self.data if "error" in event.lower())
            )
            return {
                "events": len(self.data),
                "errors": error_count
            }
        else:
            return {"status": "invalid input"}


class StreamProcessor():
    def __init__(self):
        self.streams = []

    def add_streams(self, streams: List[DataStream]):
        try:
            for s in streams:
                if not (isinstance(s, DataStream)):
                    raise ValueError()
            self.streams.extend(streams)
        except Exception:
            print("Couldn't add stream data...")

    def process_all(self, all_data: Dict[str, List[Any]]):
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("Batch 1 Results:")

        sensor_readings = 0
        transaction_ops = 0
        event_events = 0

        for stream in self.streams:
            if stream.name in all_data:
                stream.process_batch(all_data[stream.name])
                stats = stream.get_stats()

                if isinstance(stream, SensorStream):
                    count = stats.get("readings processed", 0)
                    sensor_readings += count
                    print(f"- Sensor data: {count} readings processed")
                elif isinstance(stream, TransactionStream):
                    count = stats.get("operations", 0)
                    transaction_ops += count
                    print(f"- Transaction data: {count} operations processed")
                elif isinstance(stream, EventStream):
                    count = stats.get("events", 0)
                    event_events += count
                    print(f"- Event data: {count} events processed")

        print("\nStream filtering active: High-priority data only")

        s = 0
        t = 0

        for stream in self.streams:
            if isinstance(stream, SensorStream) and stream.data:
                for batch in stream.data:
                    if batch[0] > 30:
                        s += 1

            elif isinstance(stream, TransactionStream) and stream.data:
                for trans in stream.data:
                    if "buy:" in trans:
                        try:
                            amount = int(trans.split(":")[1])
                            if amount > 80:
                                t += 1
                        except Exception:
                            pass

        print(f"Filtered results: {s} critical sensor alerts,\
{t} large transaction")

        return {
            "sensor_readings": sensor_readings,
            "transaction_ops": transaction_ops,
            "event_events": event_events,
            "filtered_alerts": s,
            "filtered_transactions": t
        }


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    batch = [22.5, 65, 1013]
    print(f"Stream ID: {sensor.name}, Type: Environmental Data")
    print(f"Processing sensor batch: {sensor.process_batch(batch)}")
    print(f"Sensor analysis: {sensor.get_stats()}")

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Stream ID: {transaction.name}, Type: Financial Data")
    print(f"Procesing transaction batch: {transaction.process_batch(batch)}")
    print(f"Transaction analysis: {transaction.get_stats()}")

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    batch = ["login", "error", "logout"]
    print(f"Stream ID: {event.name}, Type: System Events")
    print(f"Processing event batch: {event.process_batch(batch)}")
    print(f"Event analysis: {event.get_stats()}")

    processor = StreamProcessor()
    processor.add_streams([sensor, transaction, event])

    processor_data = {
        "SENSOR_001": [35, 70, 1010],
        "TRANS_001": ["buy:100", "sell:50", "buy:30", "buy:90"],
        "EVENT_001": ["login", "error", "logout", "timeout"]
    }

    processor.process_all(processor_data)

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == '__main__':
    main()
