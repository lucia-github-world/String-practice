import re
def extract_number(text):
    match = re.search(r'\d+\.?\d*$', text)
    if match:
        return f"{float(match.group()):.2f}"
    else:
        print("No number found")
        return ""

text ="sadjgsajd1873.99" #example
extract_number(text)
