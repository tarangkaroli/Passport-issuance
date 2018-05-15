import sys
import os
import epassport
import eVisa
#import country
import time
class passport_managment():
    """Possport office and migration system
    """

    def __init__(self):
        """Return a Customer object whose name is *name*."""
        os.system('cls')
        print('********************************************************************************')
        print('Welcome to the ePassport/eVisa Managment System')
        print('********************************************************************************')

    def issuedPassport(self):
        upid=100000
        issueDate = '21/09/2000'
        expiryDate = '21/09/2020'

        print('********************************************************************************')
        print('Passport Details')
        print('********************************************************************************')
        print ('Unique Passport Identification Number :', upid)
        print ('Date of Issue(DD/MM/YYYY) :', issueDate)
        print ('Date of Expiry(DD/MM/YYYY) :', expiryDate)
        print('********************************************************************************')


    def createPassportdata(self):
        os.system('cls')
        print('********************************************************************************')
        print('Welcome to the New Passport Issue system')
        print('********************************************************************************')
        fname = input('Enter First Name:')
        lname = input('Enter Last Name:')
        dob = input('Enter Date of Birth(DD/MM/YYYY) :')
        nationality = input('Nationality:')
        icountry = input('Issueing Country:')

        upid, dateofissue, dateofexpiry = epassport.allocate_epassport(fname, lname, dob, nationality, icountry)
        os.system('cls')
        time.sleep(1)
        print('Passport has been issued based on provided information: ')
        print ("")
        print ("UPI ID : ", upid)
        print ("First Name : ", fname)
        print("Last Name:", lname)
        print("Date of Issue:",dateofissue )
        print("Date of Expiry:", dateofexpiry)



        value = input('Do you want to print the same (y/n) : ')
        if value == 'y':
            os.system('cls')
            self.passportMangmt()




    def reissuePassportdata(self):
        os.system('cls')
        print('********************************************************************************')
        print('Welcome to the Re-issue Passport Issue system')
        print('********************************************************************************')
        upid = input('Enter Unique Passport Identification Number:')
        print('********************************************************************************')
        status , doi, doe, fname, lname = epassport.reissuence_epassport(upid)
        if status:
            print("Not a valid passport")
        else:
            time.sleep(1)
            os.system('cls')
            print("Passport has been reissued..")
            print("")
            print("UPI ID : ", upid)
            print("First Name : ", fname)
            print("Last Name:", lname)
            print("Date of Issue:", doi)
            print("Date of Expiry:", doe)


        value = input('Do you want to print the same (y/n) : ')
        if value == 'y':
            os.system('cls')
            self.passportMangmt()

    def passportData(self):
        os.system('cls')
        print('********************************************************************************')
        print('Welcome to the Passport issue system')
        print('********************************************************************************')
        i = 0
        while (i != 4):
            os.system('cls')
            print('Choose the Passport Managment Option')
            print ('1. Issue Passport')
            print ('2. Reissue Passport')
            print ('3. Back ')
            passportOption = input('Enter option 1, 2, 3:')
            print (passportOption)
            if (passportOption == '1'):
                self.createPassportdata()
            elif (passportOption == '2'):
                self.reissuePassportdata()
            elif (passportOption == '3'):
                os.system('cls')
                break
    def visaIssueOpertion(self):
        print ("1. Issue Visa")
        print ("2. View Visa details")
        visaOp = input('Enter option:')
        return visaOp


    def visaIssue(self):
        os.system('cls')
        print('********************************************************************************')
        print('Welcome to the Visa Issue system')
        print('********************************************************************************')
        visaOperation=self.visaIssueOpertion()
        if (visaOperation=='1'):
            upid = input('Enter Unique Passport Identification Number:')
            destCountry = input('Destination Country name:')
            duration = input('Duration (in days):')
            visaType = input('Visa type (TRANSIT/BUSINESS/TOURIST):')
            visaIssueID = eVisa.applyVisa(upid, destCountry, duration, visaType)
            if (None == visaIssueID):
                pass
            else:
                time.sleep(1)
                os.system('cls')
                print('Visa has been issued: ')
                print("")
                print("UPID: ", upid)
                print("VISA ID: ", visaIssueID)
                print("Destination Country: ", destCountry)
                print("Duration of Journey: ", duration)
                print("Visa Type: ", visaType.upper())
                v1 = input("Press enter to continue")
                os.system('cls')
        elif (visaOperation=='2'):
            os.system('cls')
            upid = input('Enter Unique Passport Identification Number:')
            visa_list=eVisa.viewvisa(upid)
            if (len(visa_list)==0):
                pass
            else:
                for key in visa_list.keys():
                    print("")
                    print ("Visa ID : ", key)
                    print("Destination : ", visa_list[key].countryDest)
                    print("Visa type: ", visa_list[key].visaType)
                    print("")
                    v1 = input("Press enter to continue")
                    os.system('cls')

        else:
            print ("Please provide valid option 1/2")

            print('********************************************************************************')



    def transitdetail(self):
        os.system('cls')
        print('********************************************************************************')
        print('Welcome to the Migration system')
        print('********************************************************************************')
        upid = input('Enter Unique Passport Identification Number:')
        visaid = input('Enter Visa Id:')
        status = epassport.transit(upid, visaid)
        if ( status == 0):
            print("Access granted")
            print("")
        else:
            print("Migration denied")
            print("")

        val_dic = epassport.show_travel_history(upid)
        print('Travel History')
        for tid in val_dic:
            if val_dic[tid].visaid in epassport.epassport_blockchain[upid][1].visa_applied.keys():
                print("")
                print("Travel Destination : ", epassport.epassport_blockchain[upid][1].visa_applied[val_dic[tid].visaid].countryDest)
                print("Travel Type : ", epassport.epassport_blockchain[upid][1].visa_applied[val_dic[tid].visaid].visaType)
        v1 = input("Press enter to continue")
        os.system('cls')

    def performAttack(self):
        epassport.epassport_blockchain["UPI855010"] = epassport.epassport_blockchain["UPI855002"]
        del epassport.epassport_blockchain["UPI855002"]
        v1 = input("Press enter to continue")
        os.system('cls')

    def passportMangmt(self):
        i = 0
        while (i != 5):

            print('Choose the Passport/Visa Managment option')
            print ('1. ePassport Issue/Reissue')
            print ('2. eVisa Issue/List Visas')
            print ('3. Transits')
            print ('4. Attack')
            print ('5. Exit')
            passportOption = input('Enter option 1, 2, 3, 4, 5: ')
            print (passportOption)
            if (passportOption == '1'):
                self.passportData()
            elif (passportOption == '2'):
                self.visaIssue()
            elif (passportOption == '3'):
                self.transitdetail()
            elif (passportOption == '4'):
                self.performAttack()
            elif (passportOption == '5'):
                sys.exit(0)




if __name__ == '__main__':
    pm = passport_managment()
    pm.passportMangmt()
    #print(approximate_size(1000000000000, False))
    #print(approximate_size(1000000000000))