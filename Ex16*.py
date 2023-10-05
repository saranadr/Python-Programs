''' Write a program to maintain server/network details in a dictionary and do below operations.
    Input:
     ***** Server Maintenance Program *****
     1. Add a New Server 
     2. Remove Server   
     3. Display Available Servers
     4. Search a Server 
     5. Sort Servers
     6. Clear Servers
     7. Exit program
     Choose your option [1-7]:
     '''
servers={}
while True:
    print('''***** Server Maintenance Program *****
    1. Add a New Server
    2. Remove Server   
    3. Display Available Servers
    4. Search a Server 
    5. Sort Servers
    6. Clear Servers
    7. Exit program''')
    op=input('Choose your option [1-7]:')
    if op=='1':
        sname=input('Enter the server name: ')
        if sname in servers.keys():
            print('Server is already available')
            op=input('Do you want to overwrite (Y/N): ')
            if op.upper()=='Y':
                pass
            elif op.upper()=='N':
                continue
            else:
                print('invalid option')
                continue
        sip=input('Enter the server ip: ')
        servers[sname]=sip
        print('Server details added successfully')
    elif op=='2':
        sname=input('Enter the server name: ')
        if sname in servers.keys():
            servers.pop(sname)
            print('Server details removed successfully')
        else:
            print('Server name is not available')
    elif op=='3':
        print('Available servers: ')
        for k,v in servers.items():
            print(k,v)
    elif op=='4':
        search=input('Enter the server name: ')
        if search in servers.keys():
            print('server is available')
            print(search,servers[search])
        else:
            print('server not is available')
    elif op=='5':
        print('Sorted servers: ')
        for k,v in sorted(servers.items()):
            print(k,v)
    elif op=='6':
        servers.clear()
        print('servers details are cleared')
    elif op=='7':
        print('Exiting program')
        break
    else:
        print('Invalid option')
        pass
    
    
