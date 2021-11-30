"""cw_deadline = "24.02.2020"
mark = 0
if cw_deadline == cw_submission:
    mark = float(input("Mark student's coursework: "))
elif cw_deadline <= cw_submission <= "25.02.2020":
"""

confirmation = {
    "yes": "yes",
    "no": "no"
}
submit = ["Accepted ?", "Is there valid reason ? "]
marks = [
    "Full Mark", "10 marks minus from overall mark but not below 40", "Mark = 0"
]


def convert_lowercase(string):
    return string.strip().lower()


def get_input_response():
    """ this gets answer from user and proceed to next process """
    answer = input("yes/no: ")
    return answer


def mc_claim_check():
    engine_mode = True
    while engine_mode:
        print("CW deadline CW submission \n\t on time?")
        answer = get_input_response()

        if convert_lowercase(answer) == confirmation["no"]:
            print(marks[2])
            engine_mode = False

        elif convert_lowercase(answer) == confirmation["yes"]:
            print("Within 24 hours ?")

            answer = get_input_response()
            if convert_lowercase(answer) == confirmation["no"]:
                print("Your CW submitted on late time")
                print("Is there valid reason ?")

                answer = get_input_response()
                if convert_lowercase(answer) == confirmation["no"]:
                    print("MC claim submission")
                    print(submit[0])

                    user_check = get_input_response()
                    if convert_lowercase(user_check) == confirmation["no"]:
                        print(marks[2])
                        engine_mode = False

                    elif convert_lowercase(user_check) == confirmation["yes"]:
                        print(marks[1])
                        engine_mode = False

