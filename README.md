# MDI-212_TeamProject
After recieving task and some brainstorming our team decided to create a Telegram bot which convertd written en/ru text 
into as if it was written with wrong keyboard layout. Our motivation to choose such bot was that everyone of us has been 
in a situation when you accidentaly print something with Russian keyboard layout instead of English (or vice versa), 
andwith our bot this problem will be solved. Our bot is deployed with the nickname "@TranslitRUENbot" and becomes 
active as the Python script is turned on. The ui is quite intuitive, after pressing the start button you either press 
"help" to get the instructions or choose "ru" or "en" as the desired output language. Then enter the text and bot will 
automatically convert it. The vital point that should be mentioned is that our bot converts such symbols as '$' or '&' 
to corresponding ones on the target layout (leaving the keys shared by layouts, such as numbers or '!', as they are).
The length of text is only limited with telegram message size. Simple as that. As a result of this project we recieved 
an opportunity to use the knowledge which was given to us during the course and recieved some new knowledge especially 
about writing bots. 