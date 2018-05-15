import hashlib
import time
import os
epasspost_first_block = "UPI855000"
UPI_ID = "UPI"
UPI_Initial_value = "855000"
epassport_blockchain = {}

TRAS_ID = "T0000"
tras_first_id = "0"
etransaction_first_block = TRAS_ID + tras_first_id
etrasaction_blockchain = {}

class etransaction:
    def __init__(self, upi, visaid):
        self.upi = upi
        self.visaid = visaid

class epassport:
    def __init__(self, upi, fname, lname, dob, nationality, issueing_country):
        self.upi = upi
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.nationality = nationality
        self.issueing_country = issueing_country
        self.issuing_date = time.strftime("%d/%m/%Y")
        self.expiry_date = (time.strftime("%d/%m/%Y").split("/")[0] + "/" + time.strftime("%d/%m/%Y").split("/")[1] + "/" + str(int(time.strftime("%d/%m/%Y").split("/")[-1]) + 20))
        self.status = 0
        self.visa_applied = {}
        self.etransaction = {}



def allocate_UPI_id():
    global UPI_Initial_value
    UPI_Initial_value = int(UPI_Initial_value) + 1
    return UPI_ID + str(UPI_Initial_value)


def allocate_epassport(fname, lname, dob, nationality, issueing_country):
    global UPI_Initial_value
    previous_upi = UPI_ID + str(UPI_Initial_value)
    upi = allocate_UPI_id()
    passport = epassport(upi, fname, lname, dob, nationality, issueing_country)
    if len(epassport_blockchain) == 0:
        epassport_blockchain[upi] = [hashlib.md5(epasspost_first_block.encode('utf-8')).hexdigest(), passport]
    else:
        epassport_blockchain[upi] = [hashlib.md5(epassport_blockchain[previous_upi][1].upi.encode('utf-8')).hexdigest(), passport]
    return upi,epassport_blockchain[upi][1].issuing_date, epassport_blockchain[upi][1].expiry_date


#print(allocate_epassport("shivam", "garg", "06-11-1987", "indian", "india"))
#print(allocate_epassport("abhay", "garg", "06-11-1989", "indian", "india"))
#print(allocate_epassport("rahul", "garg", "06-11-1987", "indian", "india"))
#print(allocate_epassport("katoch", "garg", "06-11-1987", "indian", "india"))

def validate_epassport(upi):
    if upi in epassport_blockchain.keys():
        pre_upi = str("UPI" + str(int(upi.split("UPI")[1]) - 1))
        if pre_upi == "UPI855000":
            return 0

        if pre_upi in epassport_blockchain.keys():
            md5_pre_block = (hashlib.md5((pre_upi.encode('utf-8'))).hexdigest())
            if (md5_pre_block == epassport_blockchain[upi][0]):
                return 0
        else:
            return 2
    else:
        return 1

def reissuence_epassport(upi):
    if upi in epassport_blockchain.keys():
        epassport_blockchain[upi][1].status = 0
        epassport_blockchain[upi][1].expiry_date = (
        time.strftime("%d/%m/%Y").split("/")[0] + "/" + time.strftime("%d/%m/%Y").split("/")[1] + "/" + str(
            int(time.strftime("%d/%m/%Y").split("/")[-1]) + 20))
        return 0, epassport_blockchain[upi][1].issuing_date, epassport_blockchain[upi][1].expiry_date, \
               epassport_blockchain[upi][1].fname, epassport_blockchain[upi][1].lname
    else:
        return 1, None, None, None, None

def verify_upi_id(upi):
    if upi in epassport_blockchain.keys():
        return 0
    else:
        return 1

def verify_visa_id(upid, visa_id):
    if upid in epassport_blockchain.keys():
        if visa_id in epassport_blockchain[upid][1].visa_applied.keys():
            print("Visa ID is : valid")
            return 0
        else:
            return 1
    else:
        return 1


def allocate_tra_id(upi):
    if upi in epassport_blockchain.keys():
        return len(epassport_blockchain[upi][1].etransaction) + 1

def show_travel_history(upid):
    pass

def transit(upi, visaid):
    tid = allocate_tra_id(upi)
    t1 = etransaction( upi, visaid)

    status = validate_epassport(upi)
    if 0 == status:
        ret_val =  0
    elif 2 == status:
        print("")
        print("Block chain has been attacked and not able to issue eVisas")
        v1 = input("Press enter to continue")
        os.system('cls')
    else:
        print("Invalid UPI ID")
        return 1


    if not verify_visa_id(upi, visaid):
        ret_val = 0
    else:
        print("Invalid VISA ID")
        return 1

    epassport_blockchain[upi][1].etransaction[tid] = t1

    return ret_val


def show_travel_history(upi):
    if upi in epassport_blockchain.keys():
        ret_val = epassport_blockchain[upi][1].etransaction
        return ret_val



