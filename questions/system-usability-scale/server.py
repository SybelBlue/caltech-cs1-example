# according to the canonical SUS paper:
# To calculate the SUS score, first sum the score contributions from
# each item. Each item's score contribution will range from 0 to 4. For
# items 1,3,5,7,and 9 the score contribution is the scale position minus
# 1. For items 2,4,6,8 and 10, the contribution is 5 minus the scale
# position. Multiply the sum of the scores by 2.5 to obtain the overall
# value of SU.  SUS scores have a range of 0 to 100.

def generate(data): 
    data['params']['questions'] = [
        {'q': 'I think that I would like to use this system frequently.', 'n': '1'},
        {'q': 'I found the system unnecessarily complex.', 'n': '2'},
        {'q': 'I thought the system was easy to use.', 'n': '3'},
        {'q': 'I think that I would need the support of a technical person to be able to use this system.', 'n': '4'},
        {'q': 'I found the various functions in this system were well integrated.', 'n': '5'},
        {'q': 'I thought there was too much inconsistency in this system.', 'n': '6'},
        {'q': 'I would imagine that most people would learn to use this system very quickly.', 'n': '7'},
        {'q': 'I found the system very cumbersome to use.', 'n': '8'},
        {'q': 'I felt very confident using the system.', 'n': '9'},
        {'q': 'I needed to learn a lot of things before I could get going with this system.', 'n': '10'}
    ]
    return(data)

def grade(data): 
    # student gets full credit no matter what their answers
    data["score"] = 1
    # prevent PL from displaying any particular MCQ responses as 'wrong'
    for question in data['params']['questions']:
        data['partial_scores']['q'+ question['n']] = {'score': None}
