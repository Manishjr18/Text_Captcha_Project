# Text_Captcha

**CAPTCHA Generation**

Random Text Generation:
Create a random string of characters (alphanumeric or numeric) that will be displayed as the CAPTCHA.

Image Creation:
Generate an image with the generated text, applying various distortions (noise, rotation, font variations, etc.) to make it challenging for automated systems to recognize.

Storage:
Store the generated CAPTCHA text and image for subsequent validation.

**CAPTCHA Validation**

User Input:
Capture the user's input for the CAPTCHA.

Comparison:
Compare the user's input with the stored CAPTCHA text.

Response:
Return a success or failure response based on the comparison.
