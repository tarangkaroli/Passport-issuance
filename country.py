country = {"USA":{}, "UK":{}, "GERMANY":{}, "RUSSIA":{}, "ARGENTINA":{}}

class Country:
    def __init__(self, visaID, countryDest, issueDate):
        self.visaID = visaID
        self.countryDest = countryDest.upper()
        self.issueDate = issueDate

def updateVisaList(visaID, countryDest, issueDate):
    for countryDest in country:
        country[countryDest][visaID]=issueDate


