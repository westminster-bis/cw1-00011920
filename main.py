"""cw_deadline = "24.02.2020"
mark = 0
if cw_deadline == cw_submission:
    mark = float(input("Mark student's coursework: "))
elif cw_deadline <= cw_submission <= "25.02.2020":
"""

confirmation = {
    "yes" : "pass",
    "no": "fail"
}

def convert_lowercase(string):
    return string.strip().lower()

def get_input_response():
    """ this gets answer from user and proceed to next process """
    answer = input("yes/no: ")
    return answer
