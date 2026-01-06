def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	if not isinstance(seq, list) or len(seq) == 0:
		return False

	for item in seq:
		if not isinstance(item, dict):
			return False

		if 'fill' not in item.keys():
			return False

		if 'request_id' not in item.keys() or not isinstance(item['request_id'], int):
			return False

		if 'timestamp' not in item.keys() or not isinstance(item['timestamp'], float):
			return False

		if 'symbol' not in item.keys() or not isinstance(item['symbol'], str):
			return False

		if 'quantity' not in item.keys() or not isinstance(item['quantity'], float):
			return False

		if 'price' not in item.keys() or not isinstance(item['price'], float):
			return False

		if 'commission' not in item.keys() or not isinstance(item['commission'], float):
			return False

		if 'commission_asset' not in item.keys() or not isinstance(item['commission_asset'], str):
			return False

		if 'order_type' not in item.keys() or not isinstance(item['order_type'], str):
			return False

		if 'client_order_id' not in item.keys() or not isinstance(item['client_order_id'], str):
			return False

		if 'exchange' not in item.keys() or not isinstance(item['exchange'], str):
			return False

		if 'status' not in item.keys() or not isinstance(item['status'], str):
			return False

		if 'time_in_force' not in item.keys() or not isinstance(item['time_in_force'], str):
			return False

		if 'side' not in item.keys() or not isinstance(item['side'], str):
			return False

		if 'stop_price' not in item.keys() or not isinstance(item['stop_price'], float):
			return False

		if 'trigger_condition' not in item.keys() or not isinstance(item['trigger_condition'], str):
			return False

		if 'trailing_stop_price' not in item.keys() or not isinstance(item['trailing_stop_price'], float):
			return False

		if 'iceberg_quantity' not in item.keys() or not isinstance(item['iceberg_quantity'], float):
			return False

		if 'iceberg_side' not in item.keys() or not isinstance(item['