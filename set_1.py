def savings(gross_pay, tax_rate, expenses):
    after_tax = gross_pay * (1-tax_rate) // 1
    remaining = int(after_tax - expenses)
    return remaining 

def interest (principal, rate, periods):
    investment = principal * rate * periods
    final = (principal + investment) //1
    return int(final)

def material_waste(total_material, material_units, num_jobs, job_consumption):
    consumed = num_jobs * job_consumption
    remaining = total_material - consumed
    return f"{remaining}{material_units}"