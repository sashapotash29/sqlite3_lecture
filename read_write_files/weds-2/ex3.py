####################################################################

######### Part 1 ################################3


from datetime import datetime
import string
import csv

    
def first_name(name):
    first_name = name.split(' ')[0]
    first_name = string.capwords(first_name)
    return first_name
            
def last_name(name):
    last_name = name.split(' ')[1]
    last_name = string.capwords(last_name)
    return last_name

def zip_code(_zip):
    # add 0 at the beggining if 4 digits
    if len(_zip) == 4:
        zip_code = ''.join(('0',_zip))
    else:
        zip_code = _zip
    return zip_code

def ssnumber(snumber):
    if len(snumber) == 3:
        ssn = ''.join(('0',snumber))
    else:
        ssn = snumber
            # print(ssn)
    return ssn

def split_numbers(date):

    year = date[-4::]
    day = date[-6:-4:]
    month = date[-8:-6:]
    cal = ''.join((year,"-",month,"-",day))
    date_object = datetime.strptime(cal, '%Y-%m-%d').date()
    
    return date_object

def date_slashes(date):
    y = date.split('/')[-1]
    year = ''.join(('20',y))
    day = date.split('/')[1]

    if len(date) == 7:
        m = date.split('/')[0]
        month = ''.join(('0',m))
    else:
        month = date.split('/')[0]

    new_date = ''.join((year,"-",month,"-",day))
    date_object = datetime.strptime(new_date, '%Y-%m-%d').date()
    return date_object


def file_opener():


    data = []
    
    with open('Book11.csv','r',errors='replace') as etf_data:
        for line in etf_data.readlines()[1:]:
            split_line = line.strip().split(',')
            duedeillac, name, snumber, addone,\
            city, state, _zip, dob, issued_date, \
            charge_date, last_pay_date, origin_fico, \
            curr_fico = split_line

            clean_first_name = first_name(name)
            clean_last_name = last_name(name)
            # print(clean_first_name, clean_last_name)
            clean_zip = zip_code(_zip)
            # print(_zip)
            clean_ssn = ssnumber(snumber)
            # print(clean_ssn)

            clean_street = string.capwords(addone)
            # print(clean_street)
            clean_city = string.capwords(city)
            # print(clean_city)
            clean_st = state.upper()
            # print(clean_st)
            clean_dob = split_numbers(dob)
            # print(clean_dob)

            clean_issuied_date = split_numbers(issued_date)
            # print(clean_issuied_date)
            
            clean_charge_date = date_slashes(charge_date)
            # print(charge_date)
            clean_pay_date = split_numbers(last_pay_date)
            # print(clean_pay_date)

            # fico_difference = calculate_difference(origin_fico, curr_fico)

            row = [
                clean_first_name,
                clean_last_name,
                clean_ssn,
                clean_street,
                clean_city,
                clean_st,
                clean_zip,
                clean_issuied_date,
                clean_charge_date,
                clean_pay_date,
                origin_fico, 
                curr_fico,
                # fico_difference,
            ]
            data.append(row)

    # print(data)
    return data

# file_opener()

def file_writer():

    row_list = file_opener()
    # print(row_list)
    header = [[
            'First',
            'Last',
            'SSN',
            'Address',
            'City',
            'State',
            'Zip',
            'Issuied Date',
            'Charge Date',
            'Pay Date',
            'Original Fico', 
            'Current Fico',
    ]]

    with open("myfile5.csv", 'w', newline='') as data:
        data_writer = csv.writer(data)
        data_writer.writerows(header)
        for row in row_list:
            data_writer.writerow(row)

file_writer()




# def insert_data_in_db():
#       data = file_opener()
#       Account.objects.bulk_create([Account(
#               first_name=first_name,
#               last_name=last_name,
#               ssn=ssn,
#           ) for first_name, last_name, ssn in data.get('data')])
        
#       Address.objects.bulk_create([Address(
#               street=street,
#               city=city,
#               zip_code=zip_code,
#           ) for street, city, zip_code in data.get('data')])

#       Fico.objects.bulk_create([Fico(
#               origin_fico=origin_fico,
#               current_fico=curr_fico,
#           ) for origin_fico, curr_fico in data.get('data')])

#       Dates.objects.bulk_create([Dates(
#               issued_date=issuied_date,
#               charge_off_date=charge_off_date,
#               last_pay_date=last_pay_date,
#           ) for issuied_date, charge_off_date, last_pay_date in data.get('data')])                        
        



# insert_data_in_db()


