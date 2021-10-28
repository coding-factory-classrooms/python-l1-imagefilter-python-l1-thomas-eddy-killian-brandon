import datetime
now = datetime.datetime.now() # current date and time

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")


log_file ='imagefilter.log'

def log(message):
    with open(log_file,'a') as f:
        f.write(date_time +" "+ message+"\n")


def clear_log():
    with open(log_file,'w'):
        pass