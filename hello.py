import sys

from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import SmartContract
from fetchai.ledger.crypto import Entity, Address

import time
def main(source):
    # Create keypair for the contract owner
    entity = Entity()

    address = Address(entity)

    # Setting API up
    api = LedgerApi('localhost', 8000)

    # Need funds to deploy contract
    api.sync(api.tokens.wealth(entity, 100000))

    # Create contract
    contract = SmartContract(source)

    # Deploy contract
    api.sync(api.contracts.create(entity, contract, 100000))

    # Printing message
    contract.action(api, 'add', 100, [entity], "first")

    time.sleep(5)

    print(contract.query(api, 'getSize'))

if __name__ == '__main__':
    # Loading contract
    if len(sys.argv) != 2:
        print("Usage: ", sys.argv[0], "[filename]")
        exit(-1)

    with open(sys.argv[1], "r") as fb:
        source = fb.read()

    main(source)
