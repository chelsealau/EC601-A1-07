# Robotic Helping Hand

*Project Definition:* 
Develop a robot hand that is able to use a controller for the user. 

The intention of this project is to make an articulate, responsive robot hand for users who have limited hand mobility. 
The current iteration of this project plays [Cuphead](https://www.gog.com/game/cuphead) with an *Xbox Core Wireless Controller* by tracking X input. 

*Design Requirements:*
- Must be a hands free game interaction 
- Is able to move a joystick with variable force
- Is able to pull a trigger and able to press a button
- Doesn’t break controller

## Controls
| Input | Controller setting | Game action |
| --- | --- | --- |
| N/a | Joystick | Move |
| N/a | X | Shoot |
| N/a | A | Jump |

## Testing and Results

| Requirement  | Testing standard | Testing result |
| --- | --- | --- |
| Hands free game interaction  | Complete one round in game task only using designated user input | Not yet tested |
| Move a joystick with variable force  | Move character up, down, left, right | Not yet tested |
| Pull a trigger and able to press a button  | Switch weapon, lockon to a target, and shoot  | Not yet tested |
| Doesn’t break controller | Hand holds controller for 15 minutes without dropping  | Not yet tested |
| Doesn’t break controller | Hand acts on controller for 15 minutes without dropping  | Not yet tested |

## Final Product and Insights

Further development recommendations include: 
- Testing how reactive the hand is with a combo based game (speed)
- Testing how much force is exerted by the hands to ensure that no damage (such as stuck buttons or stick drift) is done to the controller over time (actuation force vs applied force)

## Files
Agile Development
- [Slides](slides/) :  Sprint presentations

Documentation
- [Materials list](docs/) : List of purchased materials
- [References](docs/) : List of references used throughout project

Project files
- [CAD](CAD/) : CAD Files for 3D printed parts
- [Code](code/) : Control code


