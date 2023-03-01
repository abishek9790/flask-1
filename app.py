from flask import Flask

AI=Flask(__name__)

@AI.route('/wish')
def wish():
    return 'hello flash'

@AI.route('/second')
def second():
    return 'how are you'
@AI.route('/third')
def third():
    return 'hello python flask is a micro frame work'

if __name__=='__main__':
    AI.run(debug=True,host='192.168.11.62',port=5001)