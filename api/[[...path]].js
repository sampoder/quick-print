const S1 = require('s1db')
const https = require('https');
const db = new S1(process.env.S1_TOKEN)
import httpProxy from 'http-proxy'

const proxy = httpProxy.createProxyServer()

// Make sure that we don't parse JSON bodies on this route:
export const config = {
	api: {
		bodyParser: false,
	},
}

export default async (req, res) => {
	let url = await db.get(req.headers.host.split(".")[0])
	console.log(url)
	if(!url){
		return res.send("Invalid URL.")
	}
	res.redirect(`${url}/${req.query.path.join("/")}`)
}