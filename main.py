import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]

  if S == "":
    return len(T)

  elif T == "":
    return len(S)
  elif S[0] == T[0]:
    result = fast_MED(S[1:], T[1:], MED)
  else:
    insert = fast_MED(S, T[1:], MED)
    delete = fast_MED(S[1:], T, MED)
    result = 1 + min(insert, delete)
    MED[(S, T)] = result
  return result
    # TODO -  implement top-down memoization

def fast_align_MED(S, T, MED={}):
  return fast_align_MED_(S, T, MED={})[1:]

def fast_align_MED_(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]

  if S == "":
    return len(T), len(T) * '-', T

  elif T == "":
    return len(S), len(S) * '-', S
  elif S[0] == T[0]:
    result = fast_align_MED_(S[1:], T[1:], MED)[0], S[0] + fast_align_MED_(S[1:], T[1:], MED)[1], T[0] + fast_align_MED_(S[1:], T[1:], MED)[2]
  else:
    insert = fast_align_MED_(S, T[1:], MED)[0]
    delete = fast_align_MED_(S[1:], T, MED)[0]
    if insert<=delete:
      result=1+fast_align_MED_(S, T[1:], MED)[0], "-" + fast_align_MED_(S, T[1:], MED)[1], T[0] + fast_align_MED_(S, T[1:], MED)[2]
    else :
      result=1+fast_align_MED_(S[1:], T, MED)[0], S[0] + fast_align_MED_(S[1:], T, MED)[1], "-" + fast_align_MED_(S[1:], T, MED)[2]
    MED[(S, T)] = result
  return result



print(fast_align_MED('book', 'back'))
print(fast_align_MED('kookaburra', 'kookybird'))
print(fast_align_MED('relevant', 'elephant'))
print(fast_align_MED('AAAGAATTCA', 'AAATCA'))
# I think result is correct but different format
