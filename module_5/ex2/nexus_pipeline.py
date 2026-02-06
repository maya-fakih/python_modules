from typing import Protocol, Any

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        """Process the data and return result"""
        ...

#this is an abstract class
class ProcessingPipeline():
    def add_stage():
        pass
    def process(data) -> any:
        pass
    pass

class JSONAdapter(ProcessingPipeline):
    pass

class CSVAdapter(ProcessingPipeline):
    pass

class StreamAdapter(ProcessingPipeline):
    pass

class NexusManager():
    #this calls all the abv adapter classes polymorphically?
    #so i have a list of processing pipleine objects w keon
    # they have process() w he bi2oul 
    # for item in pipelines:
    # item.process() 
    # anu ma hamo which one of them heyi ;ahela based on their
    #class it works ahla shi simple inheritence
    pass


class ProcessingStage(Protocol):
    def process(data) -> any:
        pass
    #fi shi ma zabet bel syntax bs u get the idea

class InputStage():
    def process(data) -> Any:
        #some add ons for input???
        #balke validation
        pass

class TransformStage():
    def process(data) -> Any:
        #here it enriches the data makes sense anu transform
        pass

class OutputStage():
    def process(data) -> Any:
        #saraha no clue bs gottta do something
        pass