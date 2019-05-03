''' page 33 GEB ''' 

class RuleNotApplicable(Exception): 
    """ throw if rule is not applicable """
    def __init__(self, value): 
        self.value = value
    def __str__(self): 
        return repr(self.value)


class MIU: 
    def __init__(self): 
        self.zero = "MI"
        self.bucket = set()

    def One(X: str) -> str: 
        if X[-1] != 'I': 
            raise RuleNotApplicable("Rule one is not applicable")
        else: 
            return X + 'U'

    def Two(X: str, length: int) -> str: 
        x = X[-length:]
        return X + x

    def Three(X: str) -> str: 
        if 'III' not in X: 
            raise RuleNotApplicable("Rule three is not applicable")
        else: 
            return X.replace('III', 'U')

    def Four(X: str) -> str: 
        if 'UU' not in X: 
            raise RuleNotApplicable("Rule four is not applicable. ")
        else: 
            return X.replace('UU', '')


