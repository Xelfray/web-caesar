from flask import Flask, request
from caesar import rotate_string

app=Flask(__name__)
app.config['DEBUG']=True

# form="""
# <!DOCTYPE html>
# <html>
#     <head>
#         <style> form {{background-color: #eee;
#                 padding: 20px;
#                 margin: 0 auto;
#                 width: 540px;
#                 font: 16px sans-serif;
#                 border-radius: 10px;
#             }}

#             textarea {{
#                 margin: 10px 0;
#                 width: 540px;
#                 height: 120px;
#             }}
#         </style>
#         <title>Web-Caesar</title>
#     </head>
#     <body>
#         <form method="POST">
#             <label>Rotate by:
#                 <input type="text" name="rot" value='0' />
#             </label></br>
#             <textarea  name='text' value=''>{0}</textarea>
#             <input type="submit" />
#         </form>
#     </body>
# </html>
# """

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="POST">
            <label>Rotate by:
                <input type="text" name="rot" value={0} />
            </label></br>
            <textarea  name='text'>{1}</textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format(0, '')

@app.route('/', methods=["POST"])
def encrypt():
    rot= int(request.form['rot'])
    text= request.form['text']
    encrypted_text=rotate_string(text, rot)

    return form.format(rot, encrypted_text)
    
app.run()