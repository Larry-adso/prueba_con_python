// pages/api/callback.js (si usas Next.js en Vercel)

export default async function handler(req, res) {
    const { code } = req.query;

    if (code) {
        // Intercambia el código de autorización por un token de acceso
        const response = await fetch('https://accounts.zoho.com/oauth/v2/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                client_id: process.env.ZOHO_CLIENT_ID,
                client_secret: process.env.ZOHO_CLIENT_SECRET,
                grant_type: 'authorization_code',
                code: code,
                redirect_uri: process.env.ZOHO_REDIRECT_URI,
            }),
        });

        const data = await response.json();
        
        // Aquí puedes manejar el token de acceso, almacenarlo, etc.
        res.status(200).json(data);
    } else {
        res.status(400).json({ error: 'Código de autorización no proporcionado' });
    }
}
