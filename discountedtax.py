
class discount_cal:
    def __init__(self) -> None:
        pass
    def check_insurance(self,year_salary,insurance_status):
        if insurance_status=="y" or insurance_status=="Y":
            year_salary=year_salary-20000
            insurance_status=" YES "
        else :
            year_salary=year_salary-0
            insurance_status=" NO "
        return (year_salary,insurance_status)
        
    def getDiplomatt(self,tax_amount, diplomat_job):
        discouted_tax = 0
        if diplomat_job == 'y':
            discouted_tax = (float(tax_amount)*0.75)
            diplomat_job = "YES"
        elif diplomat_job == 'n':
            discouted_tax = 0
            diplomat_job = "NO"

        return (discouted_tax, diplomat_job)


    def getDisability(self,tax_amount, disability_status):
        discounted_tax = 0

        if disability_status == 'y':
            discounted_tax = (float(tax_amount)*0.50)
            disability_status = "YES"
        elif disability_status == 'n':
            discounted_tax = (0)
            disability_status = "NO"
        return (discounted_tax, disability_status)


    def getWomenEmpowerment(self,tax_amount, gender):
        discounted_tax = 0
        if gender == 'f':
            discounted_tax = (float(tax_amount)*0.10)
            gender="Female"
        elif gender == 'm':
            discounted_tax = 0
            gender="Male"
        else:
            discounted_tax = 0
        return (discounted_tax, gender)


    def get_high_disocunt_amount(self,diplomat_discount, disability_disocunt, womenEmpowerment_discount):
        final_discounted_amt = 0
        if diplomat_discount+womenEmpowerment_discount >= disability_disocunt:
            final_discounted_amt = diplomat_discount+womenEmpowerment_discount
        elif disability_disocunt+womenEmpowerment_discount >= diplomat_discount:
            final_discounted_amt = disability_disocunt+womenEmpowerment_discount
        else:
            final_discounted_amt = (0)
        return final_discounted_amt


# if __name__ == "__main__":


#     diplomat_discount, diplomat_job = getDiplomatt(11000, "y")
#     disability_disocunt, disability_status = getDisability(11000, "y")
#     womenEmpowerment_discount,gender = getWomenEmpowerment(11000, "f")
#     # print(diplomat_discount, disability_disocunt, womenEmpowerment_discount)
#     get_high_disocunt_amount(disability_disocunt,diplomat_discount, womenEmpowerment_discount)
