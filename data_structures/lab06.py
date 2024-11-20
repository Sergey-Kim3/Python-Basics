from typing import List, Tuple, Dict, Optional, Union, Literal 
import random


class WrongDate( Exception ) :
    def __init__( self, reason ) :
        self. __reason = reason

    def __repr__( self ) :
        return self.__reason 


class Date :
    year : int
    month : int
    day : int

    # In monthnames, the first name is the 'preferred name', which will be used
    # when printing. Any further names are optional names. 
    # One can also add different languages. 

    monthnames : Tuple[ List[ Union[ str, int ] ], ... ] = ( 
        [ 'january', 'jan', 1, '1' ], [ 'february', 'feb', '2', 2 ], 
        [ 'march', 3, '3' ],
        [ 'april', 4, '4' ],  [ 'may', 5, '5' ], [ 'june', 6, '6' ], 
        [ 'july', 7, '7' ],  [ 'august', 8, '8' ],
        [ 'september', 'sept', 9, '9' ], [ 'october', 'oct', 10, '10' ],
        [ 'november', 'nov', 11, '11' ],
        [ 'december', 'dec', 12, '12' ] )

    monthindex : Dict[ Union[ str, int ], int ] = { name : ind 
        for ind, names in enumerate( monthnames ) for name in names  } 
 
    normalyear = ( 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 )
    leapyear =  ( 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 )
    
    weekdays = ( 'sunday', 'monday', 'tuesday', 'wednesday', 
                'thursday', 'friday', 'saturday' )
    
    @staticmethod
    def isleapyear( y : int ) -> bool : 
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            return True
        else:
            return False

    @classmethod
    def __init__( self, year : int, month : Union[int ,str], day : int ):
        if not isinstance(year, int):
            raise WrongDate("date.WrongDate: year {} is not an integer".format(year))
        elif not year<=2100:
            raise WrongDate("date.WrongDate: year {} is after 2100".format(year))
        elif not year>=1900:
            raise WrongDate("date.WrongDate: year {} is before 1900".format(year))
        elif month not in self.monthindex: 
            raise WrongDate("date.WrongDate: unknown month {}".format(month))
        elif not isinstance(day, int):
            raise WrongDate("date.WrongDate: day {} is not an integer".format(day))
        
        days_in_month = self.leapyear if self.isleapyear(year) else self.normalyear  
        
        if not 1 <= day <= days_in_month[self.monthindex[month]]:
            raise WrongDate("date.WrongDate: month {} does not have {} in year {}".format(month, day, year))
        
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def __repr__( self ) -> str :
        return "({}, {}, {})" .format( self.year, self.month, self.day )
            
    @classmethod
    def __str__( self ) -> str :
        strmonth = self.monthnames[self.monthindex[self.month]][0]
        return "{} {} {}" .format( self.day, strmonth, self.year )
    
    def weekday(self) -> str:
        totalDays = 0
        month = int(self.monthnames[self.monthindex[self.month]][2])-int(1)
        
        i=1900
        while i<self.year:
            if self.isleapyear(i):
                totalDays=totalDays+366
            else:
                totalDays=totalDays+365
            i=i+1
                
        j=0
        if self.isleapyear(self.year):
            while j<len(self.leapyear[:month]):
                totalDays=totalDays+self.leapyear[j]
                j=j+1
        else:
            while j<len(self.normalyear[:month]):
                totalDays=totalDays+self.normalyear[j]
                j=j+1

        totalDays=totalDays+self.day
        weekday = self.weekdays[totalDays%7]
        return weekday
        
        


def lucky_dates( ) :
    return [ ( 1956, 1, 31, 'tuesday', 'birthday of Guido Van Rossum' ),
        ( 1945, 'october', 24, 'wednesday', 'Founding of UN' ),
        ( 1969, 'july', 20, 'sunday', 'first moon landing' ),
        ( 1991, 'dec', 16, 'monday', 'independence of Kazakhstan' ),
        ( 1961, 'april', 12, 'wednesday', 'space flight of Yuri Gagarin' ), 
        ( 2022, 'september', 17, 'saturday', 'Nursultan renamed into Astana' ) ] 

def unlucky_dates( ) :
    return [ ( 1912, 'april', 15, 'monday', 'sinking of Titanic' ), 
        ( 1929, 'october', 29, 'tuesday',
                                    'Wall Street Market Crash (Black Tuesday)' ), 
        ( 1959, 'february', 3, 'tuesday', 'the day the music died' ), 
        ( 1977, 'march', 27, 'sunday', 'Los Rodeos collision' ),
        ( 2019, 'march', 23, 'saturday', 'Astana renamed into Nursultan' ), 
        ( 2022, 'october', 21, 'friday', '!! deadline of this exercise !!' ) ]


def tester( ) :
    for date in ( ( 'a', 1, 1 ), ( 2, 'x', 3 ), ( 3, 4, 'y' ), 
                ( 1900, 'x', 12 ),
                ( 1899, 1, 1 ), ( 1900, 1, 1 ), ( 1900, 'jan', 1 ),
                ( 1910, 12, 31 ), ( 1911, 3.14, 8 ),
                ( 1900, 'feb', 28 ), ( 1900, 'feb', 29 ) ) : 
        try :
            y,m,d = date
            print( "testing {} {} {}". format( y,m,d ))

            dt = Date(y,m,d) 
            print( "date = {}". format( dt )) 

        except WrongDate as w:
            print( "  exception {}". format(w) )
        print( "" ) 

    dates = lucky_dates( ) + unlucky_dates( ) 
    random. shuffle( dates )
    
    for date in dates: 
        y,m,d,w1, importance = date
        dt = Date(y,m,d) 
        w2 = dt. weekday( ) 
        print( "{} : {} ({})". format( importance, dt, w2 ))
        if w1 != w2 : 
            print( "function weekday returned {} but correct day is {} !!!". format( w2, w1 ))
        print( "" )

    print("Testing isleapyear():")
    test_years = [1900, 1904, 2000, 2004, 2022, 2024, 2100]
    expected_results = [False, True, True, True, False, True, False]
    for year, expected in zip(test_years, expected_results):
        result = Date.isleapyear(year)
        print(f"{year}: expected {expected}, got {result}")
        if result != expected:
            print(f"  ERROR: isleapyear({year}) returned {result}, expected {expected}")
        print("")

    print( "tests finished" )

tester()