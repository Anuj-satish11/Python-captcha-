from PIL import Image, ImageDraw, ImageFont
import random
import string
import re

def generate_captcha():
    # generate a random string of 5 characters
    captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return captcha

def verify_captcha(user_input, captcha):
    # compare the user input with the generated captcha
    if (user_input == captcha):
        return True
    else:
        return False

def validate_email(email):
    # use a regular expression to validate email format
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False

def create_captcha_image(captcha_text):
    # create a new image
    image = Image.new('RGB', (200, 50), color = (73, 109, 137))

    # create a draw object
    draw = ImageDraw.Draw(image)

    # select a font
    font = ImageFont.truetype('arial.ttf', 36)

    # draw the captcha text
    draw.text((10,10), captcha_text, fill=(255, 255, 255), font=font)

    # save the image
    image.save("captcha.png")

# generate a new captcha
captcha = generate_captcha()

# create an image of the captcha
create_captcha_image(captcha)

# prompt the user to enter the email
email = input("Enter your email: ")

# validate the email
if validate_email(email):
    # display the CAP
    captcha_image = Image.open("captcha.png")
    captcha_image.show()
# prompt the user to enter the captcha
user_input = input("Enter the CAPTCHA text: ")
# verify the captcha
if verify_captcha(user_input, captcha):
    print("CAPTCHA verified successfully.")
    # prompt the user to enter the password
    password = input("Enter your password: ")
    # do something with the email and password
    print("Your email is: ", email)
    print("Your password is: ", password)
else:
    print("Incorrect CAPTCHA, please try again.")
