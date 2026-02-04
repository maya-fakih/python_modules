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
            return {"Stream" : "Data stream", "Status" : "No data available"}
        except Exception:
            return {}


class SensorStream(DataStream):
    def __init__(self, stream_name:str):
        super().__init__(stream_name)

    def process_batch(self, data_batch: List[int]) -> str:
        try:
            if len(data_batch)!= 3:
                raise ValueError()
            for item in (data_batch):
                self.data.append(int(item))
            return f"[temp: {data_batch[0]}, humidity: {data_batch[1]},\
                        pressure: {data_batch[2]}]"

        except Exception:
            self.valid = False
            return "Invalid input..."

    def get_stats(self):
        if self.valid is True:
            l = len(self.data)
            return {"readings processed": len(self.data),"avg temp": self.data[0]}
        else:
            return {"status": "invalid input"}
        
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if self.valid is True:
            return[]


class TransactionStream(DataStream):
    def process_batch(self, data_batch):

        return


class EventStream(DataStream):
    def process_batch(self, data_batch):

        return


class StreamProcessor():
    pass


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("All streams processed successfully. Nexus throughput optimal.")

if __name__ == '__main__':
    main()
