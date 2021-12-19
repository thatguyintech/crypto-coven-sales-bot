async (event, steps) => {
	const txns = event.body.activity;
	console.log(txns);
	const fields = [];

	for (const t of txns) {
	  console.log("looping through txn", t);
	  fields.push({
	    "name": "From",
	    "value": t.fromAddress,
	    "inline": true
	  });
	  fields.push({
	    "name": "To",
	    "value": t.toAddress,
	    "inline": true
	  });
	  fields.push({
	    "name": "Cost",
	    "value": String(t.value) + " " + t.asset,
	  });
	  fields.push({
	    "name": "View on Etherscan",
	    "value": "https://etherscan.io/tx/" + t.hash
	  });
	}

	this.embeds = [
	  {
	    "title": "Crypto Coven Sales Bot",
	    "description": "**Another witch has taken flight!**",
	    "color": 8734182,
	    "fields": fields,
	  }];

	console.log(this.embeds);
	console.log(fields);
};
