# Ethan Murphy
# 11/18/2023
# This program will calculate new insurance policy information for customers.

import os
import sys
from datetime import datetime, timedelta

# Defining the main function (Function 1)

def main():

    # Initializing my variables that need to have values before starting the loop

    claims = []
    claim_num_ind = -6
    claim_date_ind = -5
    claim_tothst_ind = -4
    claim_num = 1
    fname = ''

    while True:

        # Resetting my variables after each loop as to not run into errors

        ex_liability_cost = 0
        glass_cov_cost = 0
        loan_cov_cost = 0
        totpremium = 0
        hst = 0
        tothst = 0
        downpayment = 0
        monthlypayment = 0
        process_fee = 39.99
        basicprem = 869.00

        fname = ''

        # Gathering input from the user, using the fname variable to determine wether the loop will break

        fname = input('Please enter your first name (type stop to exit): ').capitalize()
        if fname == 'Stop':
            print('Successfully Stopped')
            break
        lname = input('Please enter your last name: ').capitalize()
        addr = input('Please enter your address: ').capitalize()
        city = input('Please enter your city: ').capitalize()+','
        prov = input('Please enter your province (EX: NL, ON, ETC.): ').upper()

        # Validating provinces (Function 2)

        def validate_prov():
            isprovtrue = False
            provs = ['NL','PE','PEI','NS','NB','QC','ON','MB','SK','AB','BC','YT','NT','NU']
            for i in provs:
                if prov == i:
                    isprovtrue = True
            if isprovtrue == True:
                pass
            else:
                print('Invalid province, please try again.')
                os.system('pause;')
                os.system('cls;')
                os.execl(sys.executable, sys.executable, *sys.argv)
        validate_prov()

        # More inputs

        pstcode = input('Please enter your postal code: ').upper()
        pnum = input('Please enter your phone number: ')

        # Validating phone number (Function 3)

        def phone_validation():
            if len(pnum) != 10:
                print('Phone number invalid, please try again.')
                os.system('pause;')
                os.system('cls;')
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                pass
        phone_validation()

        # More boolean based inputs used for determining the extra coverage

        cars = int(input('How many cars will be insured: '))
        ex_liability = input('Do you need extra liability coverage? Y/N: ').upper()
        if ex_liability == 'Y':
            ex_liability = True
        else:
            ex_liability = False
        glass_cov = input('Do you need glass coverage? Y/N: ').upper()
        if glass_cov == 'Y':
            glass_cov = True
        else:
            glass_cov = False
        loan_cov = input('Will you be needing a loaned vehicle? Y/N: ').upper()
        if loan_cov == 'Y':
            loan_cov = True
        else:
            loan_cov = False

        # Defining my list

        paymethod = [1,2]

        # Using a list to validate the customers payment method

        print()
        print('How would you like to pay?')
        print('1. Pay in full')
        print('2. Pay Monthly')

        pickpaymethod = int(input('Enter 1 or 2: '))

        for i in paymethod:
            if pickpaymethod == i:
                choice = i

        if choice == 1:
            paymethod = 'full'
            print('Full payment selected')
            choice2 = input('Would you like to pay a downpayment? Y/N: ').upper()
            if choice2 == 'Y':
                downpayment = float(input('How much would you like to put down? '))
                paydown = 'down'
            elif choice2 == 'N':
                pass
            else:
                print('Invalid input')
                os.system('pause;')
                os.system('cls;')
                os.execl(sys.executable, sys.executable, *sys.argv)

        elif choice == 2:
            paymethod = 'monthly'
            print('Monthly payment selected')
            choice2 = input('Would you like to pay a downpayment? Y/N: ').upper()
            if choice2 == 'Y':
                downpayment = float(input('How much would you like to put down? '))
                paydown = 'down'
            elif choice2 == 'N':
                pass
            else:
                print('Invalid input')
                os.system('pause;')
                os.system('cls;')
                os.execl(sys.executable, sys.executable, *sys.argv)

        # Calculations for the total

        if cars > 1:
            cars_additional = cars-1
        else:
            cars_additional = 0
        add_car_cost = 651.75
        premiums = basicprem+(cars_additional*add_car_cost)

        if ex_liability == True:
            ex_liability_cost = 130.00*cars
        else:
            ex_liability_cost = 0.00

        if glass_cov == True:
            glass_cov_cost = 86.00*cars
        else:
            glass_cov_cost = 0.00

        if loan_cov == True:
            loan_cov_cost = 58.00*cars
        else:
            loan_cov_cost = 0.00

        totpremium = premiums+ex_liability_cost+glass_cov_cost+loan_cov_cost

        # Calculating total with downpayment and monthly payments

        if downpayment > totpremium:
            print('Error: Downpayment cannot equal more than the claim amount')
            os.system('pause;')
            os.system('cls;')
            os.execl(sys.executable, sys.executable, *sys.argv)
        totpremium = totpremium-downpayment
        hst = totpremium*0.15
        tothst = hst+totpremium
        monthlypayment = (tothst+process_fee)/8

        invoicenum = 1029

        # Formatting my values into strings for output

        ex_liability_cost = '${:,.2f}'.format(ex_liability_cost)
        glass_cov_cost = '${:,.2f}'.format(glass_cov_cost)
        loan_cov_cost = '${:,.2f}'.format(loan_cov_cost)
        totpremium = '${:,.2f}'.format(totpremium)
        hst = '${:,.2f}'.format(hst)
        tothst = '${:,.2f}'.format(tothst)
        downpayment = '${:,.2f}'.format(downpayment)
        monthlypayment = '${:,.2f}'.format(monthlypayment)
        process_fee = '${:,.2f}'.format(process_fee)

        # Getting the date for today

        date = str(datetime.today())
        date = date[0:10]

        # Getting the date for the first day of the next month

        date30 = datetime.today()
        date30 = date30.replace(day=1)
        date30 = date30 + timedelta(days=32)
        date30 = date30.replace(day=1)
        date30 = str(date30)
        date30 = date30[0:10]

        # Output

        print(f'-'*78)
        print()
        print(f'Honest Harry Car Insurance               Invoice Date:              {date:>10s}')
        print(f'Car Insurance and Coverage Receipt       Receipt No:                     #{invoicenum}')
        print()
        print(f'                                         Extra Liability Price:     {ex_liability_cost:>10s}')
        print(f'Sold to:                                 Glass Coverage Price:      {glass_cov_cost:>10s}')
        print(f'                                         Loaner Vehicle Payment:    {loan_cov_cost:>10s}')
        print(f'   {fname[0]:>1s}. {lname:<26s}         -------------------------------------')
        print(f'   {addr:<29s}         Down-Payment:              {downpayment:>10s}')
        print(f'   {city:<18s} {prov:<2s} {pstcode:<6s}                            ')
        print(f'                                         -------------------------------------')
        print(f'Total:                                   Subtotal:                  {totpremium:>10s}')
        print(f'                                         HST:                       {hst:>10s}')
        print(f'                                         -------------------------------------')
        print(f'                                         Total sale price:          {tothst:>10s}')
        print()

        # Output for monthly totals

        if paymethod == 'monthly':
            print(f'                                         -------------------------------------')
            print(f'                                         Processing Fee:            {process_fee:>10s}')
            print(f'                                         Monthly Payment:           {monthlypayment:>10s}')
            print(f'                                         -------------------------------------')
            print(f'                                         First payment date:        {date30:>10s}')

        # getting the amount of claims in the list, since there are always 3 values being added to the list you can get the amount of claims by dividing the length of the list by 3

        amount_of_claims = len(claims)/3

        # This code will not run if the amount of claims is 0, preventing empty variables from showing up on the first run of the code, causing errors

        if len(claims) != 0:
            claim_num_ind = 0
            claim_date_ind = 1
            claim_tothst_ind = 2
            print(f'-'*78)
            print(f'Previous Claims:')
            print(f'Claim #  Claim Date            Amount')
            print(f'-------------------------------------')

            # This prints each claim on its own line, and adds 3 to the variables we're using for the index, giving us the next set of claims

            while amount_of_claims != 0:
                print(f'   {claims[claim_num_ind]:>1d}.    {claims[claim_date_ind]:>10s}        {claims[claim_tothst_ind]:>10s}')
                amount_of_claims = amount_of_claims-1
                claim_date_ind = claim_date_ind+3
                claim_num_ind = claim_num_ind+3
                claim_tothst_ind = claim_tothst_ind+3
        
        # Appending this rounds values to the claims list for use on the next iteration of the loop, adding 1 to the claim number, and adding one to the invoice number

        claims.append(claim_num)
        claims.append(date)
        claims.append(tothst)
        amount_of_claims = len(claims)/3
        claim_num = claim_num+1
        invoicenum = invoicenum+1

# Running the function that will loop our code

main()