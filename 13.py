from flask import Flask

app= Flask(__name__)
@app.route('/prime_num/<num1>')
def determine(num1):
    try:
        num1 = input("Enter a number")
        quotient = num1/num1

        if quotient != 1:
           is_prime= False
        else:
            is_prime = True
    finally:

        print(f"Number: {num1} , is_prime :{is_prime}")

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, host='127.0.0.1', port= 5000)







a