def chatbot_response(user_input):
    user_input = user_input.lower()

    if "eligibility" in user_input:
        return "You must be 18+ and a citizen of India."

    elif "register" in user_input:
        return "You can register via NVSP portal: https://www.nvsp.in/"

    elif "documents" in user_input:
        return "You need ID proof (Aadhar, PAN) and address proof."

    elif "vote" in user_input:
        return "Visit your polling booth with your Voter ID on election day."

    elif "steps" in user_input:
        return """Steps:
1. Check eligibility
2. Register
3. Verify voter ID
4. Find polling booth
5. Vote"""

    elif "timeline" in user_input:
        return "Election phases: Registration → Campaign → Voting → Counting"

    else:
        return "Sorry, I didn’t understand. Try asking about voting, eligibility, or registration."