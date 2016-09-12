
class Amount (object):

    __valid_codes = ['USD','CHF','SEK','GBP']
    
    def __init__( self, val=0, code="USD" ):
        """
        Initialize the amount attributes
        """

        if code in Amount.__valid_codes:
            self.__code = code
        else:
            self.__code = 'USD'

        if type(val) is int or type(val) is float:
            self.__val = val
        else:
            self.__val = 0


    def __str__( self ):
        """
        Output a string of the amount, rounded to 2 decimal places
        """

        out_str = str(round(self.__val,2))+" "+str(self.__code)

        return out_str


    def __repr__( self ):
        """
        Out put a string of the exact amount
        """

        out_str = str(self.__val)+" "+str(self.__code)

        return out_str


    def convert( self, code="USD" ):
        """
        Convert self to code
        returns a new Amount object
        """

        # set the exchange rates
        rate = {'USD':1.0,'CHF':0.959220,'SEK':7.38837,'GBP':0.638244}

        try:
            code = code.upper()
            
            # if not USD, convert to USD before calculating final value
            if self.__code == 'USD':
                new_val = self.__val * rate[code]
                new_code = code
            else:
                new_val = self.__val / rate[self.__code]
                new_val = new_val * rate[code]
                new_code = code

            new_amount = Amount(new_val, new_code)

            return new_amount

        # any unusual inputs will return default values
        except:
            print('Currency error.')
            
            return Amount()


    def __eq__( self, other ):
        """
        Tests if self is equal to other
        """

        try:
            if self.__code == other.__code:
                return self.__val == other.__val 
            else:
                tmp_self = self.convert()
                tmp_other = other.convert()

                #print(tmp_self, tmp_other)

                return tmp_self.__val == tmp_other.__val

        except:
            print('Error')
            return False
        

    def __ne__( self, other ):
        """
        Tests if self is not equal to other
        """

        try:
            if self.__code != other.__code:
                return self.__val != other.__val 
            else:
                tmp_self = self.convert()
                tmp_other = other.convert()

                #print(tmp_self, tmp_other)

                return tmp_self.__val != tmp_other.__val


        except:
            print('Error')
            return False
        

    def __lt__( self, other ):
        """
        Tests if self is less than other
        """

        try:
            if self.__code == other.__code:
                return self.__val < other.__val 
            else:
                tmp_self = self.convert()
                tmp_other = other.convert()

                #print(tmp_self, tmp_other)

                return tmp_self.__val < tmp_other.__val

        except:
            print('Error')
            return False


    def __le__( self, other ):
        """
        Tests if self is less than or equal to other
        """

        try:
            if self.__code == other.__code:
                return self.__val <= other.__val 
            else:
                tmp_self = self.convert()
                tmp_other = other.convert()

                #print(tmp_self, tmp_other)

                return tmp_self.__val <= tmp_other.__val

        except:
            print('Error')
            return False

    def __add__( self, other ):
        """
        Adds self to other
        returns a new Amount object
        """

        try:
            if self.__code == other.__code:
                new_amount = Amount(self.__val - other.__val, \
                                   self.__code)
                
                return new_amount
            
            else:
                tmp_other = other.convert(self.__code)
                new_amount = Amount(self.__val + tmp_other.__val,\
                                   self.__code)

                return new_amount
        
        # check for exceptions
        except:
            # if other is an int or float, continue calc
            if type(other) is int or type(other) is float:
                return self.__val + other
            else:
                return self.__val + 0.0


    def __radd__( self, other ):
        """
        Adds other to self
        returns an integer or float
        """

        if type(other) is int or type(other) is float:
            return other + self.__val
        else:
            return 0.0 + self.__val


    def __sub__( self, other ):
        """
        Subtracts other from self
        returns a new Amount object
        """

        try:
            if self.__code == other.__code:
                new_amount = Amount(self.__val - other.__val, self.__code)
                
                return new_amount
            else:
                tmp_other = other.convert(self.__code)
                new_amount = Amount(self.__val - tmp_other.__val,\
                                   self.__code)

                return new_amount
        
        # check for exceptions
        except:
            # if other is an int or float, continue calc
            if type(other) is int or type(other) is float:
                return self.__val - other
            else:
                return self.__val - 0.0
            

    def __rsub__( self, other ):
        """
        Subtracts self from other
        returns and integer or float
        """

        if type(other) is int or type(other) is float:
            return other - self.__val
        else:
            return 0.0 - self.__val
