def solution(participant, completion):
        
    # sort
    participant.sort()
    completion.sort()
    
    # find not completed
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]
        
    return participant[len(participant)-1]