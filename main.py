
confirmation = {
    "yes": "yes",
    "no": "no"
}

submit = ["Accepted ?", "Is there valid reason ? ", ]


marks = [
    "Full Mark", "10 marks minus from overall mark but not below 40", "Mark = 0", "Deferral reassessment"
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

        if convert_lowercase(answer) == confirmation["yes"]:
            print(marks[0])
            engine_mode = False

        elif convert_lowercase(answer) == confirmation["no"]:
            print("Within 24 hours ?")

            answer = get_input_response()
            if convert_lowercase(answer) == confirmation["yes"]:
                print("Your CW submitted on late time")
                print("Is there valid reason ?")

                answer = get_input_response()
                if convert_lowercase(answer) == confirmation["yes"]:
                    print("MC claim submission")
                    print(submit[0])

                    user_check = get_input_response()
                    if convert_lowercase(user_check) == confirmation["no"]:
                        print(marks[1])
                        engine_mode = False

                    elif convert_lowercase(user_check) == confirmation["yes"]:
                        print(marks[0])
                        engine_mode = False

                elif convert_lowercase(answer) == confirmation["no"]:
                    print(marks[1])
                    engine_mode = False

            elif convert_lowercase(answer) == confirmation["no"]:
                print("Sumitted within 5 days ?")

                answer = get_input_response()
                if convert_lowercase(answer) == confirmation["no"]:
                    print(submit[1])

                    answer = get_input_response()
                    if convert_lowercase(answer) == confirmation["yes"]:
                        print("MC (non-submission deferral) before specified deadline")
                        print(submit[0])
                        print(marks[3])
                        engine_mode = False
                    elif convert_lowercase(answer) == confirmation["no"]:
                        print("MC late submission option")
                        print(submit[0])

                        answer = get_input_response()
                        if convert_lowercase(answer) == confirmation["no"]:
                            print(marks[2])
                            engine_mode = False

                        elif convert_lowercase(answer) == confirmation["yes"]:
                            print(marks[0])
                            engine_mode = False

                elif convert_lowercase(answer) == confirmation["yes"]:
                    print(submit[1])

                    answer = get_input_response()
                    if convert_lowercase(answer) == confirmation["yes"]:
                        print("MC late submission option")
                        print(submit[0])

                        answer = get_input_response()
                        if convert_lowercase(answer) == confirmation["yes"]:
                            print(marks[0])
                            engine_mode = False

                        elif convert_lowercase(answer) == confirmation["no"]:
                            print(marks[2])
                            engine_mode = False

                    elif convert_lowercase(answer) == confirmation["no"]:
                        print(marks[2])
                        engine_mode = False

                else:
                    print("Other input value please retry")

            else:
                print("other input value please retry")

        else:
            print("other value inputted please retry again")

mc_claim_check()