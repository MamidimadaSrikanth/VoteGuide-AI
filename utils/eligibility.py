def check_eligibility(age, citizen):
    if age < 18:
        return " You are not eligible to vote."
    if citizen.lower() != "yes":
        return "Only Indian citizens can vote."
    return " You are eligible to vote!"