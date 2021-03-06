import sys

from fetchai.ledger.api import LedgerApi
from fetchai.ledger.contract import SmartContract
from fetchai.ledger.crypto import Entity, Address


def main(source):
    # Create keypair for the contract owner
    entity = Entity()
    address = Address(entity)

    # Setting API up
    api = LedgerApi('10.168.172.59', 8000)

    # Need funds to deploy contract
    api.sync(api.tokens.wealth(entity, 100000))

    # Create contract
    contract = SmartContract(source)

    # Deploy contract
    api.sync(api.contracts.create(entity, contract, 10000))

    # Printing message
    print(contract.query(api, 'register', owner='artyom', scooter='bike1', price='100'))


if __name__ == '__main__':
    # Loading contract
    if len(sys.argv) != 2:
        print("Usage: ", sys.argv[0], "[filename]")
        exit(-1)

    with open(sys.argv[1], "r") as fb:
        source = fb.read()

    main(source)