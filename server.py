from flask import Flask
import random

answer = random.randint(0, 9)
print(answer)
app = Flask(__name__)


@app.route('/')
def guess_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

# def decorator(function):
#     def wrapper(**kwargs):
#         if "is too low" in function(kwargs["number"]):
#             return f'<h1 style="color: red">Too bad, {function(kwargs["number"])}</h1>' \
#                    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
#         elif "is too high" in function(kwargs["number"]):
#             return f'<h1 style="color: blue">Too bad, {function(kwargs["number"])}</h1>' \
#                    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
#         else:
#             return f'<h1 style="color: green">Congrats! {function(kwargs["number"])}</h1>' \
#                    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
#     return wrapper
#
#
# @app.route('/<int:number>')
# @decorator
# def check_answer(number):
#     if number < answer:
#         return f'{number} is too low!'
#     elif number > answer:
#         return f'{number} is too high!'
#     else:
#         return f'{number} is just right!'

def decorator(function):
    def wrapper(number):
        if "is too low" in function(number):
            return f'<h1 style="color: red">Too bad, {function(number)}</h1>' \
                   '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
        elif "is too high" in function(number):
            return f'<h1 style="color: blue">Too bad, {function(number)}</h1>' \
                   '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
        else:
            return f'<h1 style="color: green">Congrats! {function(number)}</h1>' \
                   '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return wrapper


@app.route('/<int:number>')
@decorator
def check_answer(number):
    if number < answer:
        return f'{number} is too low!'
    elif number > answer:
        return f'{number} is too high!'
    else:
        return f'{number} is just right!'


if __name__ == "__main__":
    app.run(debug=True)




