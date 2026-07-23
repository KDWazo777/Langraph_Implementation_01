from langchain.tools import tool


@tool
def company_info(question: str) -> str:
    """
    Answer questions about the company.
    """

    data = {
        "ceo": "Salim Aktar",
        "company_name": "Wazo Solutions Private Limited",
        "location": "Kolkata",
        "founded": "2024",
        "employees": "11"
    }

    question = question.lower()

    if "ceo" in question:
        return data["ceo"]

    if "company" in question and "name" in question:
        return data["company_name"]

    if "location" in question:
        return data["location"]

    if "founded" in question:
        return data["founded"]
    if "employees" in question:
        return data["employees"]

    return "No information found."