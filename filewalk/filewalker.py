
from fileposition import FilePosition
from typing import Tuple, Generator, TextIO 

import os
import syntax
import copy
import codecs


class FileWalker : 
   topdir : str  # Python uses strings for representing file names. 
  
   def __init__( self, topdir ) :
      self. topdir = topdir # No checks here. 


   def recDirIterator( self ) -> Generator[ Tuple[ str, str, FilePosition ], None, None ] : 
      if (not os.path.exists(self.topdir)) :
         raise FileNotFoundError("Top directory does not exist")
      elif not os.path.isdir(self.topdir) :
         raise NotADirectoryError("File specified as top directory is not a directory")
      else : 
         for (dir, subdir, files)  in os.walk(self.topdir) :
            for f in files :
               pat = os.path.join(dir, f)
               print(pat)
               for k, v in self.fileIterator(open(pat, "r", encoding = "utf-8")) :
                  yield pat, k, v

   @staticmethod 
   def fileIterator( f : TextIO ) -> Generator[ Tuple[ str, FilePosition ], None, None ] :
      ln = 0
      word = ""
      pos = FilePosition()
      for line in f :
         word = ""
         ln += 1
         if ln > 1 : pos.nextLine()
         for w in line :
            if syntax.inWord(w.lower()) :
               word += w
            elif word != "" : 
               yield word.lower(), pos
               pos.advance(len(word)+1)
               word = ""
            else :
               pos.advance(1)
         if word != "" : 
            yield word.lower(), pos
            pos.advance(len(word)+1)
            word = ""

   def __repr__( self ) -> str : 
      return "FileWalker: " + self. topdir 

   def __str__( self ) -> str :
      return "FileWalker: " + self. topdir


