Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_pickle.py
Traceback (most recent call last):
  File "C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_pickle.py", line 7, in <module>
    pickle.dump(data, pickleOut)
NameError: name 'pickleOut' is not defined. Did you mean: 'pikcleOut'?

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_pickle.py

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_pickle.py
{'Name': 'Kevin', 'Age': 30, 'City': 'Trumbull', 'Contact': '222-333-8888'}
import math
import calss3_pickle
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import calss3_pickle
ModuleNotFoundError: No module named 'calss3_pickle'
import class3_pickle
{'Name': 'Kevin', 'Age': 30, 'City': 'Trumbull', 'Contact': '222-333-8888'}

============================== RESTART: Shell =============================
import eqs
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    import eqs
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\eqs.py", line 2
    def add(x, y, x=0):
                  ^
SyntaxError: duplicate argument 'x' in function definition

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/eqs.py =
import eqs
eqs.add(20, 30, 40)
90
 = []
 
SyntaxError: unexpected indent
x = []
import test
import sample
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    import sample
ModuleNotFoundError: No module named 'sample'
import sys
sys.path
['C:/Users/bolluk/AppData/Local/Programs/Python/Python310', 'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib', 'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
for i in sys.path:
    i

    
'C:/Users/bolluk/AppData/Local/Programs/Python/Python310'
'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib'
'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip'
'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\DLLs'
'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\lib'
'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310'
'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages'

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/eqs.py =
import eqs
help(eqs)
Help on module eqs:

NAME
    eqs - This has two functions add and mul

FUNCTIONS
    add(x, y, z=0)
    
    mul(x, y, z=1)

FILE
    c:\users\bolluk\appdata\local\programs\python\python310\eqs.py


import random
help(random)

x = help(random)
Help on module random:

NAME
    random - Random variable generators.

MODULE REFERENCE
    https://docs.python.org/3.10/library/random.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
        bytes
        -----
               uniform bytes (values between 0 and 255)
    
        integers
        --------
               uniform within range
    
        sequences
        ---------
               pick random element
               pick random sample
               pick weighted random sample
               generate random permutation
    
        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull
    
        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises
    
    General notes on the underlying Mersenne Twister core generator:
    
    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(builtins.object)
        Random
            SystemRandom
    
    class Random(_random.Random)
     |  Random(x=None)
     |  
     |  Random number generator base class used by bound module functions.
     |  
     |  Used to instantiate instances of Random to get generators that don't
     |  share state.
     |  
     |  Class Random can also be subclassed if you want to use a different basic
     |  generator of your own devising: in that case, override the following
     |  methods:  random(), seed(), getstate(), and setstate().
     |  Optionally, implement a getrandbits() method so that randrange()
     |  can cover arbitrarily large ranges.
     |  
     |  Method resolution order:
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getstate__(self)
     |      # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
     |      # longer called; we leave it here because it has been here since random was
     |      # rewritten back in 2001 and why risk breaking something.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      Helper for pickle.
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randbytes(self, n)
     |      Generate n random bytes.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k, *, counts=None)
     |      Chooses k unique random elements from a population sequence or set.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      Repeated elements can be specified one at a time or with the optional
     |      counts parameter.  For example:
     |      
     |          sample(['red', 'blue'], counts=[4, 2], k=5)
     |      
     |      is equivalent to:
     |      
     |          sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
     |      
     |      To choose a sample from a range of integers, use range() for the
     |      population argument.  This is especially fast and space efficient
     |      for sampling from a large population:
     |      
     |          sample(range(10000000), 60)
     |  
     |  seed(self, a=None, version=2)
     |      Initialize internal state from a seed.
     |      
     |      The only supported seed types are None, int, float,
     |      str, bytes, and bytearray.
     |      
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |      
     |      If *a* is an int, all bits are used.
     |      
     |      For version 2 (the default), all of the bits are used if *a* is a str,
     |      bytes, or bytearray.  For version 1 (provided for reproducing random
     |      sequences from older versions of Python), the algorithm for str and
     |      bytes generates a narrower range of seeds.
     |  
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |  
     |  shuffle(self, x, random=None)
     |      Shuffle list x in place, and return None.
     |      
     |      Optional argument random is a 0-argument function returning a
     |      random float in [0.0, 1.0); if it is the default None, the
     |      standard random.random will be used.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  __init_subclass__(**kwargs) from builtins.type
     |      Control how subclasses generate random integers.
     |      
     |      The algorithm a subclass can use depends on the random() and/or
     |      getrandbits() implementation available to it and determines
     |      whether it can generate random integers from arbitrarily large
     |      ranges.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  getrandbits(self, k, /)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  random(self, /)
     |      random() -> x in the interval [0, 1).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    class SystemRandom(Random)
     |  SystemRandom(x=None)
     |  
     |  Alternate random number generator using sources provided
     |  by the operating system (such as /dev/urandom on Unix or
     |  CryptGenRandom on Windows).
     |  
     |   Not available on all systems (see os.urandom() for details).
     |  
     |  Method resolution order:
     |      SystemRandom
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  getrandbits(self, k)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  getstate = _notimplemented(self, *args, **kwds)
     |  
     |  randbytes(self, n)
     |      Generate n random bytes.
     |  
     |  random(self)
     |      Get the next random number in the range [0.0, 1.0).
     |  
     |  seed(self, *args, **kwds)
     |      Stub method.  Not used for a system random number generator.
     |  
     |  setstate = _notimplemented(self, *args, **kwds)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |  
     |  __getstate__(self)
     |      # Issue 17489: Since __reduce__ was defined to fix #759889 this is no
     |      # longer called; we leave it here because it has been here since random was
     |      # rewritten back in 2001 and why risk breaking something.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      Helper for pickle.
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu, sigma)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu, sigma)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1)
     |      Choose a random item from range(start, stop[, step]).
     |      
     |      This fixes the problem with randint() which includes the
     |      endpoint; in Python this is usually not what you want.
     |  
     |  sample(self, population, k, *, counts=None)
     |      Chooses k unique random elements from a population sequence or set.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      Repeated elements can be specified one at a time or with the optional
     |      counts parameter.  For example:
     |      
     |          sample(['red', 'blue'], counts=[4, 2], k=5)
     |      
     |      is equivalent to:
     |      
     |          sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
     |      
     |      To choose a sample from a range of integers, use range() for the
     |      population argument.  This is especially fast and space efficient
     |      for sampling from a large population:
     |      
     |          sample(range(10000000), 60)
     |  
     |  shuffle(self, x, random=None)
     |      Shuffle list x in place, and return None.
     |      
     |      Optional argument random is a 0-argument function returning a
     |      random float in [0.0, 1.0); if it is the default None, the
     |      standard random.random will be used.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from Random:
     |  
     |  __init_subclass__(**kwargs) from builtins.type
     |      Control how subclasses generate random integers.
     |      
     |      The algorithm a subclass can use depends on the random() and/or
     |      getrandbits() implementation available to it and determines
     |      whether it can generate random integers from arbitrarily large
     |      ranges.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Random:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

FUNCTIONS
    betavariate(alpha, beta) method of Random instance
        Beta distribution.
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.
    
    choice(seq) method of Random instance
        Choose a random element from a non-empty sequence.
    
    choices(population, weights=None, *, cum_weights=None, k=1) method of Random instance
        Return a k sized list of population elements chosen with replacement.
        
        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.
    
    expovariate(lambd) method of Random instance
        Exponential distribution.
        
        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.
    
    gammavariate(alpha, beta) method of Random instance
        Gamma distribution.  Not the gamma function!
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        
        The probability distribution function is:
        
                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    
    gauss(mu, sigma) method of Random instance
        Gaussian distribution.
        
        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.
        
        Not thread-safe without a lock around calls.
    
    getrandbits(k, /) method of Random instance
        getrandbits(k) -> x.  Generates an int with k random bits.
    
    getstate() method of Random instance
        Return internal state; can be passed to setstate() later.
    
    lognormvariate(mu, sigma) method of Random instance
        Log normal distribution.
        
        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.
    
    normalvariate(mu, sigma) method of Random instance
        Normal distribution.
        
        mu is the mean, and sigma is the standard deviation.
    
    paretovariate(alpha) method of Random instance
        Pareto distribution.  alpha is the shape parameter.
    
    randbytes(n) method of Random instance
        Generate n random bytes.
    
    randint(a, b) method of Random instance
        Return random integer in range [a, b], including both end points.
    
    random() method of Random instance
        random() -> x in the interval [0, 1).
    
    randrange(start, stop=None, step=1) method of Random instance
        Choose a random item from range(start, stop[, step]).
        
        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.
    
    sample(population, k, *, counts=None) method of Random instance
        Chooses k unique random elements from a population sequence or set.
        
        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).
        
        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.
        
        Repeated elements can be specified one at a time or with the optional
        counts parameter.  For example:
        
            sample(['red', 'blue'], counts=[4, 2], k=5)
        
        is equivalent to:
        
            sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
        
        To choose a sample from a range of integers, use range() for the
        population argument.  This is especially fast and space efficient
        for sampling from a large population:
        
            sample(range(10000000), 60)
    
    seed(a=None, version=2) method of Random instance
        Initialize internal state from a seed.
        
        The only supported seed types are None, int, float,
        str, bytes, and bytearray.
        
        None or no argument seeds from current time or from an operating
        system specific randomness source if available.
        
        If *a* is an int, all bits are used.
        
        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.
    
    setstate(state) method of Random instance
        Restore internal state from object returned by getstate().
    
    shuffle(x, random=None) method of Random instance
        Shuffle list x in place, and return None.
        
        Optional argument random is a 0-argument function returning a
        random float in [0.0, 1.0); if it is the default None, the
        standard random.random will be used.
    
    triangular(low=0.0, high=1.0, mode=None) method of Random instance
        Triangular distribution.
        
        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.
        
        http://en.wikipedia.org/wiki/Triangular_distribution
    
    uniform(a, b) method of Random instance
        Get a random number in the range [a, b) or [a, b] depending on rounding.
    
    vonmisesvariate(mu, kappa) method of Random instance
        Circular data distribution.
        
        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.
    
    weibullvariate(alpha, beta) method of Random instance
        Weibull distribution.
        
        alpha is the scale parameter and beta is the shape parameter.

DATA
    __all__ = ['Random', 'SystemRandom', 'betavariate', 'choice', 'choices...

FILE
    c:\users\bolluk\appdata\local\programs\python\python310\lib\random.py


type(x)
<class 'NoneType'>
dir(random)
               
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
help(random.randint)
               
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

random.__doc__
               
'Random variable generators.\n\n    bytes\n    -----\n           uniform bytes (values between 0 and 255)\n\n    integers\n    --------\n           uniform within range\n\n    sequences\n    ---------\n           pick random element\n           pick random sample\n           pick weighted random sample\n           generate random permutation\n\n    distributions on the real line:\n    ------------------------------\n           uniform\n           triangular\n           normal (Gaussian)\n           lognormal\n           negative exponential\n           gamma\n           beta\n           pareto\n           Weibull\n\n    distributions on the circle (angles 0 to 2pi)\n    ---------------------------------------------\n           circular uniform\n           von Mises\n\nGeneral notes on the underlying Mersenne Twister core generator:\n\n* The period is 2**19937-1.\n* It is one of the most extensively tested generators in existence.\n* The random() method is implemented in C, executes in a single Python step,\n  and is, therefore, threadsafe.\n\n'
random.__file__
               
'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310\\lib\\random.py'
random.__dict__
               

random.__name__
               
'random'

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/eqs.py =
__main__
import eqs
eqs
eqs.__name__
'eqs'

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/eqs.py =
60
import eqs

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/eqs.py =
60
help('modules')

Please wait a moment while I gather a list of all available modules...


Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\PublicKey\test_ECC_NIST.py", line 758
    tv_pai = load_test_vectors(("PublicKey", "ECC"),
UserWarning: Warning: skipping extended tests for P-192 tests from point-at-infinity.org

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\PublicKey\test_ECC_NIST.py", line 779
    tv_pai = load_test_vectors(("PublicKey", "ECC"),
UserWarning: Warning: skipping extended tests for P-224 tests from point-at-infinity.org

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\PublicKey\test_ECC_NIST.py", line 800
    tv_pai = load_test_vectors(("PublicKey", "ECC"),
UserWarning: Warning: skipping extended tests for P-256 tests from point-at-infinity.org

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\PublicKey\test_ECC_NIST.py", line 821
    tv_pai = load_test_vectors(("PublicKey", "ECC"),
UserWarning: Warning: skipping extended tests for P-384 tests from point-at-infinity.org

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\PublicKey\test_ECC_NIST.py", line 842
    tv_pai = load_test_vectors(("PublicKey", "ECC"),
UserWarning: Warning: skipping extended tests for P-521 tests from point-at-infinity.org

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_pkcs1_15.py", line 70
    test_vectors_verify = load_test_vectors(("Signature", "PKCS1-v1.5"),
UserWarning: Warning: skipping extended tests for Signature Verification 186-3

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_pkcs1_15.py", line 117
    test_vectors_sign  = load_test_vectors(("Signature", "PKCS1-v1.5"),
UserWarning: Warning: skipping extended tests for Signature Generation 186-2

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_pkcs1_15.py", line 122
    test_vectors_sign += load_test_vectors(("Signature", "PKCS1-v1.5"),
UserWarning: Warning: skipping extended tests for Signature Generation 186-3

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_pss.py", line 117
    test_vectors_verify = load_test_vectors(("Signature", "PKCS1-PSS"),
UserWarning: Warning: skipping extended tests for Signature Verification 186-3

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_pss.py", line 169
    test_vectors_sign = load_test_vectors(("Signature", "PKCS1-PSS"),
UserWarning: Warning: skipping extended tests for Signature Generation 186-2

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_pss.py", line 174
    test_vectors_sign += load_test_vectors(("Signature", "PKCS1-PSS"),
UserWarning: Warning: skipping extended tests for Signature Generation 186-3

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_dss.py", line 159
    test_vectors_verify = load_test_vectors(("Signature", "DSA"),
UserWarning: Warning: skipping extended tests for Signature Verification 186-3

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_dss.py", line 197
    test_vectors_sign = load_test_vectors(("Signature", "DSA"),
UserWarning: Warning: skipping extended tests for Signature Creation 186-3

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_dss.py", line 307
    test_vectors_verify = load_test_vectors(("Signature", "ECDSA"),
UserWarning: Warning: skipping extended tests for ECDSA Signature Verification 186-3

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_dss.py", line 314
    test_vectors_verify += load_test_vectors(("Signature", "ECDSA"),
UserWarning: Warning: skipping extended tests for ECDSA Signature Verification 186-3

Warning (from warnings module):
  File "C:\Users\bolluk\AppData\Local\Programs\Python\Python310\lib\site-packages\Cryptodome\SelfTest\Signature\test_dss.py", line 357
    test_vectors_sign = load_test_vectors(("Signature", "ECDSA"),
UserWarning: Warning: skipping extended tests for ECDSA Signature Verification 186-3
Cryptodome          autoexpand          idlelib             runpy
PIL                 base64              idna                runscript
__future__          bdb                 imapclient          s3transfer
__main__            binascii            imaplib             sched
_abc                binhex              imghdr              scrolledlist
_aix_support        bisect              imp                 search
_ast                boto3               importlib           searchbase
_asyncio            botocore            inspect             searchengine
_bisect             browser             instagram_explore   secrets
_blake2             bs4                 instagrapi          select
_bootsubprocess     builtins            io                  selectors
_bz2                bz2                 iomenu              setuptools
_codecs             cProfile            ipaddress           shelve
_codecs_cn          calendar            isoduration         shlex
_codecs_hk          calltip             itertools           shutil
_codecs_iso2022     calltip_w           itsdangerous        sidebar
_codecs_jp          certifi             jinja2              signal
_codecs_kr          cgi                 jmespath            site
_codecs_tw          cgitb               json                six
_collections        chardet             keyword             smtpd
_collections_abc    charset_normalizer  lib2to3             smtplib
_compat_pickle      chunk               linecache           sndhdr
_compression        class3_pickle       locale              socket
_contextvars        click               logging             socketserver
_csv                cmath               lxml                socks
_ctypes             cmd                 lzma                sockshandler
_ctypes_test        code                macosx              soupsieve
_datetime           codecontext         mailbox             sqlite3
_decimal            codecs              mailcap             squeezer
_distutils_hack     codeop              mainmenu            sre_compile
_elementtree        collections         markupsafe          sre_constants
_functools          colorama            marshal             sre_parse
_hashlib            colorizer           math                ssl
_heapq              colorsys            mimetypes           stackviewer
_imp                compileall          mmap                stat
_io                 concurrent          modulefinder        statistics
_json               config              mouseinfo           statusbar
_locale             config_key          msilib              string
_lsprof             configdialog        msvcrt              stringprep
_lzma               configparser        multicall           struct
_markupbase         contextlib          multiprocessing     subprocess
_md5                contextvars         netrc               sunau
_msi                copy                nntplib             symtable
_multibytecodec     copyreg             nt                  sys
_multiprocessing    crypt               ntpath              sysconfig
_opcode             csv                 nturl2path          tabnanny
_operator           ctypes              numbers             tarfile
_osx_support        curses              opcode              telnetlib
_overlapped         dataclasses         openpyxl            tempfile
_pickle             datetime            operator            test
_py_abc             dateutil            optparse            textview
_pydecimal          dbm                 os                  textwrap
_pyio               debugger            outwin              this
_queue              debugger_r          parenmatch          threading
_random             debugobj            pathbrowser         time
_sha1               debugobj_r          pathlib             timeit
_sha256             decimal             pdb                 tkinter
_sha3               delegator           percolator          token
_sha512             difflib             pickle              tokenize
_signal             dis                 pickletools         tooltip
_sitebuiltins       distutils           pip                 trace
_socket             doctest             pipes               traceback
_sqlite3            dynoption           pkg_resources       tracemalloc
_sre                editor              pkgutil             tree
_ssl                email               platform            tty
_stat               encodings           plistlib            turtle
_statistics         ensurepip           poplib              turtledemo
_string             enum                posixpath           types
_strptime           eqs                 pprint              typing
_struct             errno               pptx                typing_extensions
_symtable           et_xmlfile          profile             undo
_testbuffer         faulthandler        pstats              unicodedata
_testcapi           filecmp             pty                 unittest
_testconsole        fileinput           py_compile          urllib
_testimportmultiple filelist            pyautogui           urllib3
_testinternalcapi   flask               pyclbr              uu
_testmultiphase     fnmatch             pydantic            uuid
_thread             format              pydoc               venv
_threading_local    fractions           pydoc_data          warnings
_tkinter            ftplib              pyexpat             wave
_tracemalloc        functools           pygetwindow         weakref
_uuid               gc                  pymsgbox            webbrowser
_warnings           genericpath         pyparse             werkzeug
_weakref            getopt              pyperclip           wikipedia
_weakrefset         getpass             pyrect              window
_winapi             gettext             pyscreeze           winreg
_xxsubinterpreters  glob                pyshell             winsound
_zoneinfo           googlesearch        pytweening          wsgiref
abc                 graphlib            pytz                xdrlib
aifc                grep                pywhatkit           xlsxwriter
antigravity         gzip                query               xml
argparse            hashlib             queue               xmlrpc
array               heapq               quopri              xxsubtype
arrow               help                random              zipapp
ast                 help_about          re                  zipfile
asynchat            history             redirector          zipimport
asyncio             hmac                replace             zlib
asyncore            html                reprlib             zoneinfo
atexit              http                requests            zoomheight
audioop             hyperparser         rlcompleter         zzdummy
autocomplete        idle                rpc                 
autocomplete_w      idle_test           run                 

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

import os
os.getcwd()
'C:\\Users\\bolluk\\AppData\\Local\\Programs\\Python\\Python310'
files = os.listdir()
len(files)
22
for i in files:
    i

    
'class3_pickle.py'
'data'
'data.pickle'
'DLLs'
'Doc'
'eqs.py'
'include'
'Lib'
'libs'
'LICENSE.txt'
'NEWS.txt'
'python.exe'
'python3.dll'
'python310.dll'
'pythonw.exe'
'Scripts'
'tcl'
'Tools'
'vcruntime140.dll'
'vcruntime140_1.dll'
'__pycache__'
'~$sample_data.xlsx'
textFiles = []
for file in files:
    if file.endswith('.txt'):
        textFiles.append(file)

        
textFiles
['LICENSE.txt', 'NEWS.txt']

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py
['4/5/2022', ' 13:34', 'Apples', '73']
['4/5/2022', ' 3:41', 'Cherries', '85']
['4/6/2022', ' 12:46', 'Pears', '14']
['4/8/2022', ' 8:59', 'Oranges', '52']
['4/10/2022', ' 2:07', 'Apples', '152']
['4/10/2022', ' 18:10', 'Bananas', '23']
['4/10/2022', ' 2:40', 'Strawberries', '98']

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py
<class '_csv.reader'>
['4/5/2022', ' 13:34', 'Apples', '73']
['4/5/2022', ' 3:41', 'Cherries', '85']
['4/6/2022', ' 12:46', 'Pears', '14']
['4/8/2022', ' 8:59', 'Oranges', '52']
['4/10/2022', ' 2:07', 'Apples', '152']
['4/10/2022', ' 18:10', 'Bananas', '23']
['4/10/2022', ' 2:40', 'Strawberries', '98']

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py
['4/5/2022', ' 13:34', 'Apples', '73']
['4/5/2022', ' 3:41', 'Cherries', '85']
['4/6/2022', ' 12:46', 'Pears', '14']
['4/8/2022', ' 8:59', 'Oranges', '52']
['4/10/2022', ' 2:07', 'Apples', '152']
['4/10/2022', ' 18:10', 'Bananas', '23']
['4/10/2022', ' 2:40', 'Strawberries', '98']

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py
Traceback (most recent call last):
  File "C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py", line 17, in <module>
    f = open('class3sample.csv', 'w', newline='')
PermissionError: [Errno 13] Permission denied: 'class3sample.csv'

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py
['4/5/2022', ' 13:34', 'Apples', '73']
['4/5/2022', ' 3:41', 'Cherries', '85']
['4/6/2022', ' 12:46', 'Pears', '14']
['4/8/2022', ' 8:59', 'Oranges', '52']
['4/10/2022', ' 2:07', 'Apples', '152']
['4/10/2022', ' 18:10', 'Bananas', '23']
['4/10/2022', ' 2:40', 'Strawberries', '98']

= RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class3_csv.py
['4/5/2022', ' 13:34', 'Apples', '73']
['4/5/2022', ' 3:41', 'Cherries', '85']
['4/6/2022', ' 12:46', 'Pears', '14']
['4/8/2022', ' 8:59', 'Oranges', '52']
['4/10/2022', ' 2:07', 'Apples', '152']
['4/10/2022', ' 18:10', 'Bananas', '23']
['4/10/2022', ' 2:40', 'Strawberries', '98']
['Kevin@30@CSIT']
['Dave@45@BA']
['Dom@50@MBA']
import random
from random import randint
from random import *
import random as r
