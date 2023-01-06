# exception names

"""
████████╗███████╗███╗░░██╗███╗░░██╗██╗░██████╗░██╗░░░░░░░██╗░█████╗░██╗███████╗██╗░░░██╗
╚══██╔══╝██╔════╝████╗░██║████╗░██║██║██╔════╝░██║░░██╗░░██║██╔══██╗██║██╔════╝██║░░░██║
░░░██║░░░█████╗░░██╔██╗██║██╔██╗██║██║╚█████╗░░╚██╗████╗██╔╝███████║██║█████╗░░██║░░░██║
░░░██║░░░██╔══╝░░██║╚████║██║╚████║██║░╚═══██╗░░████╔═████║░██╔══██║██║██╔══╝░░██║░░░██║
░░░██║░░░███████╗██║░╚███║██║░╚███║██║██████╔╝░░╚██╔╝░╚██╔╝░██║░░██║██║██║░░░░░╚██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝╚═╝░░░░░░╚═════╝░

Here's a snippet of code that I've written to test of how to check for import errors within your 
scripts and is very useful if your module got corrupted and you can fix them with these methods
with exception handling. The 'Try' and 'except' statements will come in handy in your programs
later down the road. Exception handling can prevent from your programs crashing prematurely and
has alot of benefits and one of those benefits are making sure your software runs at its fastest
and best! No more exceptions!

                        ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
                        ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
                        ⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
                        ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄ NO MOAR EXCEPTIONS!
                        ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
                        ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤    BE GONE ERRORS!
                        ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
                        ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄      SEE YA LATER FREAKS!
                        ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
                        ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
                        ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
                        ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
                        ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
                        ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
                        ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿


"""
""" 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 """

# exception handling
try: # check for import errors
    
    import asdiuahfuiwhefuihwuifhwuif # intentional fake module name to trigger except clause
    
    pass

except ImportError: # resolve exception
    
    import sys, time, random
    
    print("The module and import proccess were unsuccessful! Please check if the module was installed correctly.")
    
    # prompt
    resp = input("Would you like to close the program or load up a backup module? y/b >")
    
    # flow control for what user decides to do after error was found!
    if resp == "y":
        
        sys.exit()
        
    elif resp == "b":
        
        print("This version of software does not have backup capability")
        
        time.sleep(1)
        
        print("Shutting down. . .")
        
        time.sleep(1)
        
        sys.exit()
        pass
    pass

print("Import proccess successful!")


