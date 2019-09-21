from flask import Flask, redirect, url_for, request
from gtts import gTTS
import os
import cv2
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   text = '%s' % name
   tts = gTTS(text=text, lang='en')
   tts.save("test.mp3")
   os.system("mpg321 test.mp3")
   return '''<html>
   <body>
      <form action = "http://localhost:5000/index" method = "post">
         <p>Enter text:</p>
         <p><input type = "text" name = "nm" required/></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>'''

@app.route('/index',methods = ['POST', 'GET'])
def index():
   if request.method == 'POST':
      in_text = request.form['nm']
      return redirect(url_for('success',name = in_text))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)
