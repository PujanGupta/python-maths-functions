triangleArea = lambda base, height : base * height * 0.5

def checkIfPrime(n):
    prime = True
    for i in range(2, n - 1):
        if n % i == 0:
            prime = False
            break
        else:
            pass
        
    if prime == True:
        return "Prime"
    elif prime == False:
        return "Composite"
    
def primeCompositeInRange(rangeLower,rangeUpper):
    composites = []
    primes = []

    for j in range(rangeLower,rangeUpper + 1):
        status_J = checkIfPrime(j)
        if status_J == "Prime":
            primes.append(j)
        elif status_J == "Composite":
            composites.append(j)

    return({"primes":primes,"composites":composites})

reverseme = lambda x: int("".join(reversed(str(x))))

def checkPalindrome(palindrome):
  if reverseme(palindrome) == palindrome:
    return(1)
  else:
    return(0)

def generatePalindromes(count):
  base = 11
  palindromes = []
  while not len(palindromes) == count:
    if checkPalindrome(base) == 1:
      palindromes.append(base)
      base += 1
    else: 
      base +=1
  return(palindromes)

def palindromicPyramidGenerator(rows):
    for i in range(0,rows+1):
      #Formatting (Spaces)
      for j in range(i,rows+1):
        print(" ",end=" ")
      #First Half of Pyramid
      for j in range(1,i+1):
        print(j,end=" ")
      #Second Half of Pyramid
      for j in range(i-1,0,-1):
        print(j,end=" ")
      print()
def getAllPalindromesinRange(start, end):

    palindromGenerator = getPalindrome()
    palindromeList = []
    
    for palindrome in palindromGenerator:
        if palindrome > end:
            break
        if palindrome < start:
            continue
        
        palindromeList.append(palindrome)
        
    return palindromeList

def findLCM(x, y):
    if x > y:
        greater = x
    else:
        greater = y
        
    while True:
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    
    return lcm

def checkIfPalindrome(s):
    return s == s[::-1]

def findHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
        
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
        else:
            continue
        
    return hcf

def findFactorsOf(n):
    factors = []
    for i in range(2, n - 1):
        if n % i == 0:
            factors.append(i)
        else:
            continue
    factors.insert(0, 1)
    factors.append(n)
    
    return factors

class Circle:
    def __init__(self):
        self.pi = 3.14
    def findDiameterBy(self,radius):
        self.diameter = 2 * radius
        return(self.diameter)
    def findRadiusBy(self,diameter):
        self.radius = diameter / 2
        return(self.radius)
    def setby(self,circumference):
        self.circumference = circumference
        self.diameter = (self.circumference / self.pi)
    def circumference(self):
        self.circumference = self.diameter * self.pi
    def area(self):
        self.area = (self.pi * (self.radius**2))
