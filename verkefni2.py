from bottle import *
import os

@route('/')
def index():
    return '''
          <div>
          <a href='/sida/sida1'>Sida 1</a> </b><a href='/sida/sida2'>Sida 2</a> <a href='/sida/sida3'>Sida 3</a>
          </div>

          <div>
          <a href='/sida/mynd1'><img src='myndir/One.png'>
          <a href='/sida/mynd2'><img src='myndir/Two.png'>
          <a href='/sida/mynd3'><img src='myndir/Three.png'>          
          </div>
          '''

#run()
run(host="0.0.0.0", port=os.environ.get('PORT'))
