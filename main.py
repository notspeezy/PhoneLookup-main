import time, requests, json, sys
from pystyle import Colorate, Colors, System, Write, Center

with open('config.json', 'r') as file:
    config = json.load(file)
    
apikey = config["apikey"]
plprint = """
╭━┳╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╭╮
┃╋┃╰┳━┳━┳┳━╮┃┃╭━┳━┫┣┳┳┳━╮
┃╭┫┃┃╋┃┃┃┃┻┫┃╰┫╋┃╋┃━┫┃┃╋┃
╰╯╰┻┻━┻┻━┻━╯╰━┻━┻━┻┻┻━┫╭╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
"""

def plookup():
    System.Size('100', '30')
    System.Title('Loading..')
    Write.Print('[+] Loading..', Colors.green_to_blue, interval=0.010)
    time.sleep(0.5)
    System.Clear()
    System.Title('Phone Lookup - Made by speezy#0444')
    print(Colorate.Horizontal(Colors.cyan_to_blue, Center.XCenter(plprint)))
    phonenumber = Write.Input('[+] Phone Number -> ', Colors.blue_to_cyan, interval=0.000)
    countrycode = Write.Input('[+] Country Code -> ', Colors.blue_to_cyan, interval=0.000)
    
    r = requests.post(f'http://apilayer.net/api/validate?access_key={apikey}&number={phonenumber}&country_code={countrycode}&format=1')
    print(r.text)
    
    try:
        choice = Write.Input('Would you lookup another number? y/n: ', Colors.blue_to_cyan, interval=0.010)
        if choice == 'y':
            time.sleep(1)
            System.Clear()
            plookup()
        elif choice == 'n':
            Write.Print('Closing the program..', Colors.blue_to_cyan, interval=0.010)
            time.sleep(1)
            sys.exit()
    except Exception as e:
        Write.Print(e, Colors.red_to_yellow, interval=0.000)
        sys.exit()

if __name__ == "__main__":
    plookup()