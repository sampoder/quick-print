const S1 = require('s1db')
const https = require('https');
const db = new S1(process.env.S1_TOKEN)

export default async (req, res) => {
	let url = await db.get(req.headers.host.split(".")[0])
	if(!url){
		return res.send("Invalid URL.")
	}
	res.redirect(`${url}/${req.query.path == "index" ? "" : req.query.path}`)
}