# ✅ Diferencias entre HTTP y HTTPS

| Aspecto              | HTTP                                         | HTTPS                                       |
|---------------------|----------------------------------------------|---------------------------------------------|
| **Seguridad**        | Los datos se transmiten en texto plano        | Los datos están cifrados usando SSL/TLS       |
| **Número de puerto** | Usa el puerto 80                              | Usa el puerto 443                            |
| **Protección de datos** | Vulnerable a intercepciones y ataques "man-in-the-middle" | Protegido contra espionaje y manipulación de datos |
| **Prefijo de URL**   | `http://`                                     | `https://`                                   |
| **Certificado**      | No utiliza certificados SSL                   | Requiere un certificado SSL de una autoridad de certificación |

---

## 📝 Estructura de una Solicitud y Respuesta HTTP

### 🚀 Solicitud HTTP

1. **Línea de solicitud:** Contiene el método HTTP, la ruta (URI) y la versión HTTP.  
   ```
   GET /index.html HTTP/1.1
   ```
2. **Encabezados:** Información adicional sobre la solicitud y el cliente.  
   ```
   Host: www.example.com
   User-Agent: Mozilla/5.0
   Accept: text/html
   ```
3. **Cuerpo:** (Opcional) Utilizado principalmente con métodos como `POST` o `PUT` para enviar datos.  
   ```
   name=John&age=30
   ```

---

### 📩 Respuesta HTTP

1. **Línea de estado:** Indica la versión HTTP, el código de estado y el mensaje.  
   ```
   HTTP/1.1 200 OK
   ```
2. **Encabezados:** Información adicional sobre la respuesta.  
   ```
   Content-Type: text/html
   Content-Length: 1024
   ```
3. **Cuerpo:** El contenido que el servidor envía al cliente, como HTML o JSON.  
   ```html
   <html>
       <body>Hello World!</body>
   </html>
   ```

---

## 🗃️ Métodos HTTP Comunes

| Método | Descripción                                 | Ejemplo de Uso                                   |
|-------|---------------------------------------------|--------------------------------------------------|
| **GET**   | Recupera datos del servidor                  | Obtener información de una página web o API       |
| **POST**  | Envía datos al servidor para ser procesados  | Enviar formularios o subir archivos               |
| **PUT**   | Actualiza o reemplaza un recurso en el servidor | Actualizar datos de un usuario en una aplicación  |
| **DELETE**| Elimina un recurso en el servidor             | Borrar una cuenta o un archivo almacenado         |

---

## 🚦 Códigos de Estado HTTP Comunes

| Código | Descripción                  | Ejemplo de Escenario                                              |
|-------|------------------------------|------------------------------------------------------------------|
| **200 OK**     | Solicitud exitosa             | Al acceder correctamente a una página web                        |
| **301 Moved Permanently** | El recurso ha sido movido a otra URL | Redireccionar a un nuevo dominio                                   |
| **404 Not Found** | Recurso no encontrado         | Al intentar acceder a una página inexistente                      |
| **403 Forbidden** | Acceso denegado               | Intentar acceder a una página restringida sin permisos             |
| **500 Internal Server Error** | Error en el servidor      | Un fallo en la configuración del servidor o en el procesamiento de la solicitud |

---
