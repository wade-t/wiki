this is now a pretty neat little trikc and I want to experiment with something:

|name|items|passes|fails|nNA|error|warning|expression|
|:--------|:--------|:--------|:--------|:--------|:--------|:--------|:--------|
|ValidContractEndDate|15569|6288|1556|7725|FALSE|FALSE|check_date_after_refdate(contract_end_date, key_date) == T|
|ValidContractNextTerminationDate|15569|1750|65|13754|FALSE|FALSE|check_date_after_refdate(contract_next_possible_termination, key_date) == T|
|ValidContractTerminationDate|15569|1637|208|13724|FALSE|FALSE|check_date_after_refdate(contract_termination_until, key_date) == T|
|AssetIdCorrect|15569|15569|0|0|FALSE|FALSE|check_asset_idcode(asset_idcode) == T|
