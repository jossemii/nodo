import typing
from web3.middleware import geth_poa_middleware
from web3 import HTTPProvider, Web3
import asyncio, time, pymongo

async def log_loop(event_filter, poll_interval: int, event_name: str, opt, w3, contract):
    while True:
        for event in event_filter.get_new_entries():
            receipt = w3.eth.waitForTransactionReceipt(event['transactionHash'])
            result = getattr(contract.events, event_name)().processReceipt(receipt)
            opt(args = result[0]['args'])
            time.sleep(poll_interval)


def catch_event(contractAddress, w3, contract, event_name, opt, init_delay: int = 0, poll_interval: int = 1):
    block: int = w3.eth.get_block('latest')['number'] - init_delay
    print("Catching event from block number: ", block)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(
                    event_filter = w3.eth.filter({
                        'fromBlock': block,
                        'address': contractAddress
                    }),
                    poll_interval = poll_interval, event_name = event_name, opt = opt, w3 = w3, contract = contract
                )))
    finally:
        # close loop to free up system resources
        loop.close()


def transact(
    w3, method, priv, value = 0, gas = 2000000, pub = None
) -> str:
    pub = w3.eth.account.privateKeyToAccount(priv).address if not pub else pub  # Not verify the correctness, 
                                                                                #     pub param is only for skip that step.
    
    transaction = method.buildTransaction({'gasPrice': w3.eth.gasPrice})
    transaction.update({
        'from': pub, # Only 'from' address, don't insert 'to' address
        'value': value, # Add how many ethers you'll transfer during the deploy
        'gas': gas, # Trying to make it dynamic ..
        'nonce': w3.eth.getTransactionCount(pub), # Get Nonce
        'chainId': w3.eth.chainId,
    })
    # Sign the transaction using your private key
    signed = w3.eth.account.signTransaction(transaction, priv)
    tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    return tx_hash.hex()


def check_provider_availability(provider) -> bool:
    return True  # TODO check if the provider is avialable.  ¿ping?

def w3_generator_factory(ledger: str) -> typing.Generator:
    while True:
        for provider in get_ledger_providers(ledger = ledger):
            if not check_provider_availability(provider = provider): continue
            w3  = Web3(HTTPProvider(provider))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            yield w3

def get_ledger_and_contract_addr_from_contract(contract_hash: bytes) -> typing.List[typing.Dict[str, str]]:
    return pymongo.MongoClient("mongodb://localhost:27017/")["mongo"]["contracts"].find({"contract_hash": contract_hash})[0]["instances"]

def get_ledger_providers(ledger: str) -> typing.List[str]:
    return pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )["mongo"]["contracts"].find({"ledger": ledger})[0]["providers"]

def get_priv_from_ledger(ledger: str) -> str:
    return pymongo.MongoClient(
            "mongodb://localhost:27017/"
        )["mongo"]["contracts"].find({"ledger": ledger})[0]["priv"]


def set_ledger_on_mongodb(ledger: str):
    pass

def set_provider_on_mongodb(provider: str, ledger: str):
    pass