from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello_cloud():
  return 'Hello Cloud!'

if __name__ == '__main__':
    # Get port from environment variable, default to 8080
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
