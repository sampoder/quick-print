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
	let url = await db.get(req.headers.host)
	return new Promise((resolve, reject) => {
		proxy.web(req, res, { target: url, changeOrigin: true }, (err) => {
			if (err) {
				return reject(err)
			}
			resolve()
		})
	})
}