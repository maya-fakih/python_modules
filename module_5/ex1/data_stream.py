from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_name: str, init: Optional[List[Any]] = None):
        self.name = stream_name
        self.data = []
        self.valid = True
        if init:
            self.process_batch(init)

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

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        try:
            return {"Stream": "Data stream", "Status": "No data available"}
        except Exception:
            return {}


class SensorStream(DataStream):
    def __init__(self, stream_name: str, init: Optional[List[Any]] = None):
        super().__init__(stream_name, init)

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

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        if self.valid is True and self.data:
            data_len = len(self.data)
            temps = [batch[0] for batch in self.data]
            avg_t = sum(temps) / len(temps)
            return {"readings processed": data_len * 3, "avg temp": avg_t}
        else:
            return {"status": "invalid input"}

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if self.valid is True and len(data_batch) == 3:
            if criteria is None:
                return [data_batch]
            elif criteria == "temperature":
                return [data_batch[0]]
            elif criteria == "humidity":
                return [data_batch[1]]
            elif criteria == "pressure":
                return [data_batch[2]]
            else:
                print("Invalid criteria...")
                return []
        return []


class TransactionStream(DataStream):
    def __init__(self, stream_name: str, init: Optional[List[Any]] = None):
        super().__init__(stream_name, init)

    def process_batch(self, data_batch: List[str]) -> str:
        try:
            for item in data_batch:
                self.data.append(item)
            return f"[{', '.join(data_batch)}]"
        except Exception:
            self.valid = False
            return "Invalid transaction data..."

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
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

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if self.valid is True:
            if criteria is None:
                return data_batch.copy()
            elif criteria == "buy":
                return [item for item in data_batch if "buy:" in item]
            elif criteria == "sell":
                return [item for item in data_batch if "sell:" in item]
            else:
                print("Invalid criteria...")
                return []
        return []


class EventStream(DataStream):
    def __init__(self, stream_name: str, init: Optional[List[Any]] = None):
        super().__init__(stream_name, init)

    def process_batch(self, data_batch: List[str]) -> str:
        try:
            for item in data_batch:
                self.data.append(item)
            return f"[{', '.join(data_batch)}]"
        except Exception:
            self.valid = False
            return "Invalid event data..."

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
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

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if self.valid is True:
            if criteria is None:
                return data_batch.copy()
            elif criteria.lower() == "error":
                return [item for item in data_batch if "error" in item.lower()]
            else:
                return [i for i in data_batch if criteria in i.lower()]
        return []


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

    def process_all(self):
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        sensor_readings = 0
        transaction_ops = 0
        event_events = 0

        for stream in self.streams:
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
                    if (stream.filter_data(list(batch), "temperature")
                            and list(batch)[0] > 30):
                        s += 1

            elif isinstance(stream, TransactionStream) and stream.data:
                buy_transactions = stream.filter_data(stream.data, "buy")
                for trans in buy_transactions:
                    try:
                        amount = int(trans.split(":")[1])
                        if amount > 80:
                            t += 1
                    except Exception:
                        pass
        f = "Filtered results: "
        print(f"{f}{s} critical sensor alerts, {t} large transaction")

        return {
            "sensor_readings": sensor_readings,
            "transaction_ops": transaction_ops,
            "event_events": event_events,
            "filtered_alerts": s,
            "filtered_transactions": t
        }


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream with data...")
    sensor = SensorStream("SENSOR_001", [22.5, 65, 1013])
    print(f"Stream ID: {sensor.name}, Type: Environmental Data")
    print(f"Sensor analysis: {sensor.get_stats()}")

    print("\nInitializing Transaction Stream with data...")
    transaction = TransactionStream("TRANS_001", ["buy:100", "sell:150"])
    print(f"Stream ID: {transaction.name}, Type: Financial Data")
    print(f"Transaction analysis: {transaction.get_stats()}")

    print("\nInitializing Event Stream with data...")
    event = EventStream("EVENT_001", ["login", "error", "logout"])
    print(f"Stream ID: {event.name}, Type: System Events")
    print(f"Event analysis: {event.get_stats()}")

    sensor2 = SensorStream("SENSOR_002", [35, 70, 1010])
    transaction2 = TransactionStream("TRANS_002", ["buy:1", "sell:5", "buy:9"])
    event2 = EventStream("EVENT_002", ["login", "error", "logout", "timeout"])

    processor = StreamProcessor()
    processor.add_streams([sensor2, transaction2, event2])

    processor.process_all()

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == '__main__':
    main()
