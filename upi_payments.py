import requests

def get_balance(upi_id):
    url = f'https://api.bankbazaar.com/upi/balance/{upi_id}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    balance = response.json()['balance']
    return balance

def main():
    upi_id = input('Enter your UPI ID: ')
    balance = get_balance(upi_id)
    print(f'Your UPI balance is: {balance}')

if __name__ == '__main__':
    main()