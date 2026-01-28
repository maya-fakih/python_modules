from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: any) -> str:
        pass

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    def format(self, result: str) -> str:
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):
    def __init__(self, data):
        self.data = data
        self.nbs = 0
        self.sum = 0
        self.avg = 0
        self.valid = False

    def process(self) -> str:
        prosessed = f"Processing data: {self.data}"
        return (prosessed)

    def validate(self):
        try:
            self.nbs = len(self.data)
            self.sum = sum(self.data)
            self.avg = self.sum / self.nbs
            self.valid = True
            return (True)
        except Exception:
            self.valid = False
            return (False)

    def format(self) -> str:
        if self.valid:
            return f"Processed {self.nbs} numeric values, sum = (\
                        {self.sum}, avg = {self.avg}"

        else:
            return "Non numeric input..."


class TextProcessor(DataProcessor):
    def __init__(self, data):
        self.data = data
        self.chars = 0
        self.words = 0
        self.valid = False

    def process(self) -> str:
        prosessed = f"Processing data: {self.data}"
        return (prosessed)

    def validate(self):
        try:
            self.chars = len(self.data)
            words = self.data.split(' ')
            self.words = len(words)
            self.valid = True
            return (True)
        except Exception:
            self.valid = False
            return (False)

    def format(self) -> str:
        if self.valid:
            out = (
                f"Processed text: {self.chars} characters, {self.words} words"
            )
        else:
            out = "Non string input..."
        return out


class LogProcessor(DataProcessor):
    def __init__(self, data):
        self.data = data
        self.valid = False
        self.error = False

    def process(self) -> str:
        prosessed = f"Processing data: {self.data}"
        return (prosessed)

    def validate(self):
        try:
            self.data = [(n.strip(' ')) for n in self.data.split(':')]
            if self.data[0] == "ERROR":
                self.error = True
            elif self.data[0] == "INFO":
                self.error = False
            else:
                raise ValueError()
            self.valid = True
            return (True)
        except Exception:
            return (False)

    def format(self) -> str:
        if self.valid:
            state = "INFO"
            case = "[INFO]"
            if self.error is True:
                state = "ERROR"
                case = "[ALERT]"

            out = f"{case} {state} level detected: {self.data[1]}"
        else:
            out = "Wrong input format..."
        return out


def evaluate(data: DataProcessor, type: str):
    print(data.process())
    if data.validate() is True:
        print(f"Validation: {type.capitalize()} data verified")
        print(f"Output: {data.format()}")
    else:

        print("Invalid data...")


def stream_processor():

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric_data = NumericProcessor([1, 2, 3, 4, 5])
    evaluate(numeric_data, "Numeric")

    print("\nInitializing faulty numeric data...")
    bad_num_data = NumericProcessor("a, b, c, d")
    evaluate(bad_num_data, "Numeric")

    print("\nInitializing Text Processor...")
    text_data = TextProcessor("Hello Nexue World")
    evaluate(text_data, "text")

    print("\nInitializing faulty text data...")
    bad_text = TextProcessor(7)
    evaluate(bad_text, "text")

    print("\nInitializing Log Processor...")
    log_data = LogProcessor("ERROR: Connection timeout")
    evaluate(log_data, "log")

    print("\nInitializing faulty log data...")
    bad_log = LogProcessor("INFO: Comms are active")
    evaluate(bad_log, "Log")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    stream = [
        NumericProcessor([1, 2, 3]),
        TextProcessor("Hello World"),
        LogProcessor("INFO: System ready")
    ]
    i = 1
    for item in stream:
        item.validate()
        print(f"Result {i}: {item.format()}")
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == '__main__':
    stream_processor()
