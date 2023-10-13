from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import urllib.parse

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # retrieves parameters from the URL
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        if 'name' in params:
            LastName = params['name'][0]
        else:
            LastName = ''
        
        # Database connection and query
        conn = sqlite3.connect('university.db')
        cursor = conn.cursor()

        # Execute the query to get course information
        query = "SELECT Teacher.FirstName, Teacher.LastName, Course.CourseName "
        query += "FROM Teacher INNER JOIN Course ON TeacherID = CourseTeacher "
        query += f"WHERE Teacher.LastName='{LastName}'"
        
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        # http response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        # allows a request originating from another website
        self.send_header('Access-Control-Allow-Origin', '*')  
        self.end_headers()

        # set the HTML response
        response = '<html>\n<body>\n'
        
        if result:
            response += f'<h1>Teacher {LastName} courses:</h1>\n'
            response += '<ul>\n'
            for row in result:
                response += f'<li>Teacher: {row[0]} {row[1]} - Course: {row[2]}</li>\n'
            response += '</ul>\n'
        else:
            response += f'<h1>No courses found for the teacher {LastName}</h1>\n'

        response += '</body>\n</html>\n'

        # Send response to client
        self.wfile.write(response.encode())

def start_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server started on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    start_server()
