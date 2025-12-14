import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)
logger=logging.getLogger(__name__)

class StreamingstatisticsEngine():
    def __init__(self):
        logger.info("Starting statistics streaming engine....")
        self.count=0
        self.total=0
        self.maximum=None
        self.minimum=None
        
    def add(self, value:int | float):
        if not isinstance(value,(int,float)):
            logger.error("Non-numeric value detected")
            raise TypeError("Only numeric values allowed")
        self.count+=1
        self.total+=value
        if self.maximum is None or value>self.maximum:
            self.maximum=value
        if self.minimum is None or value<self.minimum:
            self.minimum=value
    
    def mean(self):
        if self.count==0:
            logger.error("Mean requested with no data")
            raise ValueError("No data available to compute mean")
        return self.total/self.count
    def max(self):
        
        if self.maximum is None:
            logger.error("Max requested with no data")
            raise ValueError("No data available to compute max")
        return self.maximum
    def min(self):
        if self.minimum is None:
            logger.error("Min requested with no data")
            raise ValueError("No data available to compute min")
        return self.minimum
        
def number_stream(n):
    for i in range(1,n+1):
        yield i
          
if __name__=="__main__":
    engine=StreamingstatisticsEngine()
    for value in number_stream(20):
        engine.add(value)
    print("Mean:",engine.mean())
    print("Max:",engine.max())
    print("Min:",engine.min())
    
    