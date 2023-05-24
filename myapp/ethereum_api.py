from web3 import Web3
from web3.utils.address import to_checksum_address
import requests

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/6419ac601b774b1fa3b252c97bde3ea2'))

def get_balance(ethereum_address):
    checksum_address = web3.to_checksum_address(ethereum_address)

    balance_wei = web3.eth.get_balance(checksum_address)
    balance_eth = web3.from_wei(balance_wei, 'ether')

    return balance_eth


def get_recent_transactions(ethereum_address):
    api_key = 'YAPAXVWAH9ACSATV19EX77E5ZD1V3IZN26'

    endpoint = f'https://api.etherscan.io/api?module=account&action=txlist&address={ethereum_address}&sort=desc&apikey={api_key}'

    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            transactions = response.json()['result'][:5]

            extracted_transactions = []
            for transaction in transactions:
                extracted_transaction = {
                    'transactionIndex': transaction['transactionIndex'],
                    'from': transaction['from'],
                    'to': transaction['to'],
                    'value': transaction['value'],
                    'blockNumber': transaction['blockNumber'],
                    'hash': transaction['hash'],
                }
                extracted_transactions.append(extracted_transaction)

            return extracted_transactions
        else:
            print(f"Error: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")

    return []