# 🎯 Resultado Esperado: curl

---

## ✅ Comprobación de la Instalación

```bash
curl --version
```

**Resultado esperado:**
```
curl 7.68.0 (x86_64-pc-linux-gnu) libcurl/7.68.0
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 pop3s rtsp smb smbs smtp smtps telnet tftp
Features: AsynchDNS HTTPS-proxy IPv6 Largefile libz TLS-SRP UnixSockets
```

---

## 🌐 Ejecución de Solicitudes Básicas

**Obtener el contenido de una página web:**
```bash
curl http://example.com
```

**Resultado esperado:**
```html
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
</head>
<body>
    <p>This domain is for use in illustrative examples.</p>
</body>
</html>
```

---

## 📝 Recuperar Datos desde una API

**Recuperar publicaciones desde JSONPlaceholder:**
```bash
curl https://jsonplaceholder.typicode.com/posts
```

**Resultado esperado:**
```json
[
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit..."
    },
    {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore..."
    }
]
```

---

## 📨 Uso de Encabezados y Solicitud POST

**Obtener solo los encabezados:**
```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

**Resultado esperado:**
```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 29211
Connection: keep-alive
```

**Realizar una solicitud POST:**
```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

**Resultado esperado:**
```json
{
    "title": "foo",
    "body": "bar",
    "userId": 1,
    "id": 101
}
```
