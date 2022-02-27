
year_salary=250000*12
class tax_cal:
    def __init__(self):
        self.inner_cls_obj=self.inner_rate_calc()
        pass
        

    def salary_cagetory(self,year_salary, min_tax_amount, max_amount):
        additional_salary = 0
        if year_salary <= min_tax_amount:
            
            return self.inner_rate_calc().tax_calculation(year_salary, 1)
        else:
            additional_salary += self.inner_cls_obj.tax_calculation(min_tax_amount, 1)

        if year_salary-min_tax_amount <= 100000:
            return additional_salary+ self.inner_cls_obj.tax_calculation((year_salary-min_tax_amount), 10)
        else:
            additional_salary += self.inner_cls_obj.tax_calculation(100000, 10)

        if year_salary-(min_tax_amount+100000) <= 200000:
            return additional_salary+self.inner_cls_obj.tax_calculation((year_salary-min_tax_amount-100000), 20)
        else:
            additional_salary += self.inner_cls_obj.tax_calculation(200000, 20)
        if year_salary-(min_tax_amount+100000+20000) <= max_amount-min_tax_amount-100000-200000:
            return additional_salary+self.inner_cls_obj.tax_calculation(year_salary-min_tax_amount-300000, 30)
        else:
            additional_salary += self.inner_cls_obj.tax_calculation(
                2000000 - min_tax_amount-100000-200000, 30)
        return (additional_salary+self.inner_cls_obj.tax_calculation(year_salary-2000000, 36))

    class inner_rate_calc:
        def __init__(self) -> None:
            pass
        def tax_calculation(self,amount, rate):
            return amount*rate/100


if __name__ == "__main__":
    obj=tax_cal()
    print(obj.salary_cagetory(year_salary, 450000, 2050000))
