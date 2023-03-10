from profanity_check import predict, predict_prob

def CheckProfanity(submission):
    if ( predict([submission]) == True ):
        return True
    else:
        return False