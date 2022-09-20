class Solution(object):
   def isNumber(self, s):
      s = s.strip()
      try:
         s = float(s)
         return True
      except:
         return False

ob = Solution()
print(ob.isNumber("0"))
print(ob.isNumber("e"))
print(ob.isNumber(""))
print(ob.isNumber("."))
print(ob.isNumber("%"))
