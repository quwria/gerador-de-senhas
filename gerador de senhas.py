import string
import random
abc = string.ascii_letters
simbs = string.punctuation
abcssimbs = abc + simbs
print(
   ''.join(random.SystemRandom().choices(abcssimbs, k=8)))