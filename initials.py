def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    initials = [] #create list to append initials to
    name_list = fullname.split() #create list of given names
    for name in name_list:  # go through each name
       initials.append(name[0].upper())  # append the initial
    initials_ = ''.join(initials) #convert list to string without whitespace
    return initials_