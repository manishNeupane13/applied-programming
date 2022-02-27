from discountedtax import discount_cal
from databasewrite import *
from taxcalc import tax_cal
# import mysql.connector
# import databasewrite
# global user_name
# global user_age
# global user_address
# global user_salary
# global marital_stauts
# global tax_amount
# global user_gender
# global disability_status
# global diplomat_job
# global insurance_status


class individual_tax:
    def __init__(self, name, age, address, salary, marital_stauts, tax_amount, user_gender, disability_status, diplomat_job, insurance_status):
        self.person_name = name
        self.person_age = age
        self.person_address = address
        self.monthly_salary = salary
        self.marital_stauts = marital_stauts
        self.tax_amount = tax_amount
        self.user_gender = user_gender
        self.disability_status = disability_status
        self.diplomat_job = diplomat_job
        self.insurance_status = insurance_status

    def display_information(self, actual_discount_amt):
        print(
            f'Name :{self.person_name}\t\tAddress :{self.person_address}\nAge :{self.person_age}\t\tMarital_Status :{self.marital_stauts}\nGender:{self.user_gender}\t\tDisability_Status:{self.disability_status}\nDiplomat Job :{self.diplomat_job}\t\tMonthly_salary :{self.monthly_salary}\nTax_amount:{self.tax_amount}\t\tDiscounted Tax :{actual_discount_amt}\nAcutal Tax amount after previllages ::{self.tax_amount-actual_discount_amt}\t\tRemaining Salary After Taxiation = {float(self.monthly_salary*12)-float(self.tax_amount)}\n')

    def writeintodatabase(self, discount_amt):
        tax_after_discount = self.tax_amount-discount_amt
        mydb = connect_to_db()
        mycursor = mydb.cursor()
        sql = "INSERT INTO customer1(name, age, address, salary, marital_stauts, tax_amount,user_gender, disability_status, diplomat_job, insurance_status,discount_amt,tax_after_discount) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.person_name, self.person_age, self.person_address,
               self.monthly_salary, self.marital_stauts, self.tax_amount, self.user_gender, self.disability_status, self.diplomat_job, self.insurance_status, discount_amt, tax_after_discount)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


if __name__ == "__main__":
    user_name = (input(f'Enter the Name of User :: '))
    user_address = input(f'Enter the Address of user  :: ')
    user_age = (input(f'Enter the Age of user  :: '))
    user_salary = (float(input(f'Enter the Monthly of user  :: ')))
    user_gender = input(f'Enter the Gender of user :: ')

    print("="*100)
    marital_status = (input(f'Are you married or unmarried (Y/N) ? '))
    insurance_status = (input(f'Have your done Insruance or not (Y/N) ? '))
    diplomat_job = (input(f'Are you in diplomat job or not (Y/N) ? '))
    disability_status = (
        input(f'Are you different able person or not (Y/N) ? '))

    print("="*100)
    # salary after insurance check
    year_salary, insurance_status = discount_cal().check_insurance(
        user_salary*12, insurance_status)
    # checking marital status for tax calculations
    if marital_status == 'y':
        tax_amount = tax_cal().salary_cagetory(year_salary, 450000, 2050000)
        marital_status = " Married "
    elif marital_status == 'n':
        tax_amount = tax_cal().salary_cagetory(year_salary, 400000, 2000000)
        marital_status = " Unmarried "
    else:
        print("!! Error enter valid inputs !!!")

    diplomat_discount, diplomat_job = discount_cal().getDiplomatt(tax_amount, diplomat_job)
    disability_disocunt, disability_status =discount_cal().getDisability(
        tax_amount, disability_status)
    womenEmpowerment_discount, gender = discount_cal().getWomenEmpowerment(
        tax_amount, user_gender)
    discounted_amt = discount_cal().get_high_disocunt_amount(
        disability_disocunt, diplomat_discount, womenEmpowerment_discount)

    person_obj = individual_tax(user_name, user_age, user_address, user_salary, marital_status,
                                tax_amount, user_gender, disability_status, diplomat_job, insurance_status)
    person_obj.display_information(discounted_amt)
    person_obj.writeintodatabase(discounted_amt)
