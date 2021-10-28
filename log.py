import datetime
now = datetime.datetime.now() # current date and time

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")


log_file ='imagefilter.log'

def log(message):

    """
    log(fonction) écrit dans les logs le message en paramètre avec la date du jour.
    :param message: str - message à écrire dans les logs.
    """

    with open(log_file,'a') as f:
        f.write(date_time +" "+ message+"\n")


def clear_log():

    """
    clear_log nettoie les logs encore plus rapidement que swiffer.
    """

    with open(log_file,'w'):
        pass