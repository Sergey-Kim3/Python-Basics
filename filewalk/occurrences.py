
from fileposition import FilePosition
from typing import List, Dict, Set, Optional 

class Occurrences : 
   occs : Dict[ str, Dict[ str, Set[ FilePosition ]]] 

   def __init__( self ) :
      self. occs = dict( ) 


   def add( self, word : str, filename : str, pos : FilePosition ) -> None :
      if not self.occs.get(word) : 
         occsSet = {(pos.line, pos.column)}
         occsDict = [{filename : occsSet}]
         self.occs.update({word : occsDict})
      elif not self.occs.get(word)[0].get(filename) :
         occsSet = {(pos.line, pos.column)}
         self.occs.get(word)[0].update({filename : occsSet})
      elif self.occs.get(word)[0].get(filename) :
         for k, v in self.occs.get(word)[0].get(filename).copy() : 
            if k != pos.line or v != pos.column : 
               self.occs.get(word)[0].get(filename).add((pos.line, pos.column))
         

   # Should return the number of distinct words:
 
   def distinctWords( self ) -> int :
      count = 0
      occsKeys = self.occs.keys() 
      for key in occsKeys :
         count += 1
      return count
    
   # Should return the total number of words occurrences: 
 
   def totalOccurrences( self, word : Optional[str] = None, 
                               fname : Optional[str] = None ) -> int : 
      if (not bool(self.occs)) :
         return 0
      elif word == None :
         count = 0
         occsKeys = self.occs.keys()
         for key in occsKeys :
            for occurrence in self.occs.get(key)[0].keys():
               count += len(self.occs.get(key)[0].get(occurrence))
         return count
      elif word != None and fname == None :
         count = 0
         if not self.occs.get(word) :
            return 0
         else:
            for i in self.occs.get(word)[0] :
               count += len(self.occs.get(word)[0].get(i))
            return count
      else :
         count = 0
         if not self.occs.get(word) or not self.occs.get(word)[0].get(fname) :
            return 0
         else :
            for key in self.occs.get(word)[0].get(fname) :
               count += 1
            return count


   # This is for debugging, so it doesn't need to be pretty: 

   def __repr__( self ) -> str : 
      return str( self. occs )

 
   # Here the occurrences must be sorted and shown in a nice way: 

   def __str__( self ) -> str : 
      string = ""
      for wordAndDict in sorted(self.occs.items()) :
         string += "\"{}\" has {} occurrences(s):\n".format(wordAndDict[0], self.totalOccurrences(wordAndDict[0]))
         for filename in sorted(wordAndDict[1][0].keys()) :
            string += "   in file {}\n".format(filename)
            for pos in sorted(wordAndDict[1][0].get(filename)) :
               string += "      at line {}, column {}\n".format(pos[0], pos[1])
      return string

