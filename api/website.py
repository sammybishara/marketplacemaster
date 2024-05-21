import abc

# Main website class that other classes should inherit from
class Website(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def get_search_results(self, query):
        "Return search results from website"