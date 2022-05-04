import pandas as pd


# setting our item DTO
class Items(object):

    def __init__(self, *kwargs: dict):
        self.kwargs = kwargs[0]

    def jsonify_input(self):
        self.kwargs["date"] = pd.to_datetime(self.kwargs["date"])
        self.kwargs['year'] = self.kwargs["date"].year
        self.kwargs['day'] = self.kwargs["date"].day
        self.kwargs['month'] = self.kwargs["date"].month
        del self.kwargs["date"]
        self.kwargs = pd.DataFrame(data=[self.kwargs])
        return self.kwargs
