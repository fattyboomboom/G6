import ast
from profanity_check import predict, predict_prob

def CheckProfanity(submission):
    if ( predict([submission]) == True ):
        return 'bad words detected'
    else:
        return 'good post'