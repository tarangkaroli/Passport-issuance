import epassport
##import country
import time
import os

visaCount = "002548"
visaIssueId = "VISA-801-"

class EVisa:
    def __init__(self, countryDest, duration, visaType):
        self.countryDest = countryDest
        self.duration = duration
        self.visaType = visaType
        self.visaIssueDate = time.strftime("%d/%m/%Y")

def issueVisaid():
        global visaCount
        visaCount = int(visaCount) + 1
        return visaIssueId + str(visaCount)

def applyVisa(UPI, destCountry, duration, visaType):
    status = epassport.validate_epassport(UPI)
    if 0 == status:
        visaID = issueVisaid()
        visa = EVisa(destCountry, duration, visaType)
        #adding the VISA ID issued by authority to the concerned UPI ID
        epassport.epassport_blockchain[UPI][1].visa_applied[visaID] = visa
        return visaID
    elif 2 == status:
        print("")
        print("Block chain has been attacked and not able to issue eVisas")
        v1 = input("Press enter to continue")
        os.system('cls')
    else:
        os.system('cls')
        print("")
        print("Invalid UPI ID provided")
        print("")
        return None

def viewvisa(upi):
    visa_list=[]
    if not epassport.validate_epassport(upi):
        return epassport.epassport_blockchain[upi][1].visa_applied

    else:
        os.system('cls')
        print("")
        print("Invalid UPI ID provided")
        print("")
        return None





