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
   return '''<html> <head> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <style>body{background-color: #2a13ff; color: #b9abff; display: grid; font-family: "Work Sans", sans-serif; height: calc(100vh - 8rem); padding: 4rem; place-content: center;}.input-group{display: inline-block; margin-bottom: 2rem; position: relative;}label{display: block; height: 4rem; position: relative;}.input{background-color: transparent; border: none; border-radius: 5px; color: transparent; font-family: "Work Sans", sans-serif; font-size: 1.5rem; font-weight: bold; height: 100%; line-height: 4rem; outline: none; padding: 0 1rem;}.input:focus + .input-after{animation: type 1.25s ease 0.5s infinite; box-shadow: none; height: calc(100% - 1rem); margin-left: 1rem; top: 50%; transform: translateY(-50%); width: 2px;}.input:focus::placeholder{opacity: 0; transition: 0.15s ease;}.input-after{background-color: #fcfcff; border-radius: 5px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.15); height: 100%; left: 0; position: absolute; top: 0; transition: 0.25s ease; width: 100%; z-index: -1;}.input-text{display: inline-block; font-size: 1.5rem; left: 1rem; position: absolute; top: 50%; transform: translateY(-50%); white-space: nowrap; pointer-events: none;}.input-text-short{display: inline-block; font-size: 1.5rem; left: 0; position: absolute; top: 0; visibility: hidden; white-space: nowrap;}@keyframes type{50%{opacity: 0;}100%{opacity: 1;}}#input-1{color: white;}.btn{box-sizing: border-box; -webkit-appearance: none; -moz-appearance: none; appearance: none; background-color: transparent; border: 2px solid #e74c3c; border-radius: 0.6em; color: #e74c3c; cursor: pointer; display: flex; align-self: center; font-size: 1rem; font-weight: 400; line-height: 1; margin: 20px; padding: 1.2em 2.8em; text-decoration: none; text-align: center; text-transform: uppercase; font-family: 'Montserrat', sans-serif; font-weight: 700;}.btn:hover, .btn:focus{color: #fff; outline: 0;}.third{border-color: #3498db; color: #fff; box-shadow: 0 0 40px 40px #3498db inset, 0 0 0 0 #3498db; transition: all 150ms ease-in-out;}.third:hover{box-shadow: 0 0 10px 0 #3498db inset, 0 0 10px 4px #3498db;}</style> <script>function blinkInput(){const blinkInputs=[ ...document.querySelectorAll("[data-module='blink-input']")]; blinkInputs.forEach(function(input){const elInput=input.querySelector("[data-module='blink-input-el']"); const inputCursor=input.querySelector( "[data-module='blink-input-cursor']" ); const inputText=input.querySelector("[data-module='blink-input-text']"); const inputTextShort=input.querySelector( "[data-module='blink-input-text-short']" ); const inputWarning=input.querySelector( "[data-module='blink-input-warning']" ); let inputActive; const findPosition=function(isDelete){let textArray=[]; for (let i=0; i < elInput.selectionStart; i++){textArray.push(elInput.value[i]);}elInput.selectionStart=textArray.length; inputTextShort.innerText=textArray.join(""); inputCursor.setAttribute( "style", `left: ${inputTextShort.clientWidth}px` );}; elInput.addEventListener("focusout", ()=> inputCursor.setAttribute("style", `left: 0`) ); elInput.addEventListener("click", findPosition); input.addEventListener("keyup", function(event){const charCode=event.which || event.keyCode; const charStr=String.fromCharCode(charCode); if (charCode===8){findPosition("isDelete"); inputText.innerText=elInput.value;}if (!/[a-z0-9]/i.test(charStr) || charCode !==32){inputActive=true; findPosition();}}); elInput.addEventListener("keyup", function(event){if (inputActive){inputText.innerText=elInput.value; inputTextShort.innerText=elInput.value; inputCursor.setAttribute("style", `left: ${inputText.clientWidth}px`);}});});}blinkInput(); </script> </head> <body> <form action="http://localhost:5000/index" method="post"> <h1>Text to audio</h1><div class="input-group"> <label for="input-1" data-module="blink-input"> <input class="input" id="input-1" placeholder="Enter text" name="nm" data-module="blink-input-el"/> <div class="input-after" data-module="blink-input-cursor"></div><div class="input-text" data-module="blink-input-text"></div><div class="input-text-short" data-module="blink-input-text-short"></div></label></div><p><input type="submit" value="convert" class="btn third"/></p></form> </body></html>'''
   

   


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
