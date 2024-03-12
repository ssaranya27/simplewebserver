from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<title align="center"> TOP SOFTWARE COMPANIES WITH REVENUE </title>
<h1>TOP FIVE REVENUE GENERATING SOFTWARE COMPANIES</h1>
<h2 align="center">COMPANIES REVENUE IN 2022</h2>
<body>
<table border="4" align="center">
<caption> TOP FIVE REVENUE GENERATING SOFTWARE COMPANIES</caption>
<tr>    
  <th>Name</th>
  <th>Country</th>
  <th>sales</th>
  <th>market value</th>
</tr>
<tr>
  <td>Apple</td>
  <td>United States</td>
  <td>$378.7 billion </td>
  <td>$2.6 trillion </td>
</tr>
<tr>
  <td>Alphabet inc.</td>
  <td>United United States</td>
  <td>$257.5 billion </td>
  <td>$1.6 trillion </td>
</tr>
<tr>
  <td>Microsoft corporation </td>
  <td>United States</td>
  <td>$184.5 billion </td>
  <td>$2.1 trillion </td>
</tr>
<tr>
  <td>Samsaung Group</td>
  <td>South Korea</td>
  <td>$244.2 billion </td>
  <td>$67.3 billion </td>
</tr>
<tr>
  <td>IBM</td>
  <td>United States</td>
  <td>$67.3 billion </td>
  <td>$124.3 billion </td>
</tr>

</table>
</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()