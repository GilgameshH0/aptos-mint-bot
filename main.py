from concurrent.futures import process
from dataclasses import dataclass
from threading import Thread
from aptos_sdk.account import Account, AccountAddress
from aptos_sdk.transactions import TransactionArgument, RawTransaction, EntryFunction, TransactionPayload
from aptos_sdk.client import FaucetClient, RestClient
from aptos_sdk.bcs import Serializer
from common import FAUCET_URL, NODE_URL
from aptos_sdk.type_tag import StructTag, TypeTag
import time
import json


rest_client = RestClient(NODE_URL)

#private key
account = Account.load_key("")

def mint_coin(
    #  minter: Account
) -> str:

    #LMNFT
    payload = EntryFunction.natural(
        #контракт и функция
        "0x9b9812f618c67f447aeaa93605074433f2f11489e23d7e775f2d705d2f40f86::minting",
        "mint",
        [],
        [
            #public кей
            TransactionArgument(AccountAddress.from_hex("0x4a746cbbf5e63ddff26863756dd7f90b3ea4550478047ea0cdba02897ea79099"), Serializer.struct),
            TransactionArgument(0, Serializer.u64),
            TransactionArgument(1, Serializer.u64),
            TransactionArgument(0, Serializer.u8)
        ]
    )
    signed_transaction = rest_client.create_single_signer_bcs_transaction(
        account, TransactionPayload(payload)
    )
    return rest_client.submit_bcs_transaction(signed_transaction)
    

while True:
    try:
        "success"
        process = Thread(target=mint_coin())
    except:
        "error"



#CANDY MACHINE V2
# {
#   "function": "0xc071ef709539f7f9372f16050bf984fe6f11850594b8394f11bc74d22f48836b::candy_machine_v2::mint_tokens",
#   "type_arguments": [],
#   "arguments": [
#     "0xe54f7a86a4312c8189600b614dcd17a4be0afd30fb1569719aaf0aaae433df56",
#     "DolphinOceanClub",
#     "1"
#   ],
#   "type": "entry_function_payload"
# }    

# {
#       "name": "mint_nft_public",
#       "visibility": "public",
#       "is_entry": true,
#       "generic_type_params": [],
#       "params": [
#         "&signer"
#       ],
#       "return": []
#     },

#LMNFT
# payload = EntryFunction.natural(
#     "0x9b9812f618c67f447aeaa93605074433f2f11489e23d7e775f2d705d2f40f86::minting",
#     "mint",
#     [],
#     [
#         TransactionArgument(AccountAddress.from_hex("0x4a746cbbf5e63ddff26863756dd7f90b3ea4550478047ea0cdba02897ea79099"), Serializer.struct),
#         TransactionArgument(0, Serializer.u64),
#         TransactionArgument(1, Serializer.u64),
#         TransactionArgument(0, Serializer.u8)
#     ]
# )
# signed_transaction = rest_client.create_single_signer_bcs_transaction(
#     account, TransactionPayload(payload)
# )
# return rest_client.submit_bcs_transaction(signed_transaction)