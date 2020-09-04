# String - Problem #2

x = True
response = []
while x:
    digit_failed, contract_agreed = map(str, input().split())

    if digit_failed != "0" and contract_agreed != "0":
        new_contract_agreed = contract_agreed.replace(digit_failed, "")

        if new_contract_agreed.startswith("0"):
            strip_agreed_contract = new_contract_agreed.lstrip("0")
            if strip_agreed_contract == "":
                response.append("0")
            else:
                response.append(strip_agreed_contract)
        else:
            if new_contract_agreed == "":
                response.append("0")
            else:
                response.append(new_contract_agreed)
    else:
        x = False

for i in range(0, len(response)):
    print(response[i])

