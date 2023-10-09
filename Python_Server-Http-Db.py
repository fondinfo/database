from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import json

# Class that handles HTTP requests
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Decode JSON data
        data = json.loads(post_data)

        # Extracts the teacher's name from JSON data
        LastName = data['name']

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
        self.end_headers()

        # Costruisce la risposta HTML
        response = '<html>\n<body>\n'
        
        if result:
            response += f'<h1>{LastName} couses:</h1>\n'
            response += '<ul>\n'
            for row in result:
                response += f'<li>Teacher: {row[0]} {row[1]} - Course: {row[2]}</li>\n'
            response += '</ul>\n'
        else:
            response += f'<h1>Teacher {LastName} not found</h1>\n'

        response += '</body>\n</html>\n'

        # Send response
        self.wfile.write(response.encode())

# Start the server on port 8000
def start_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server started ... port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    start_server()
