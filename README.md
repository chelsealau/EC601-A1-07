# Robotic Helping Hand

#### Project Definition:
Develop a robot hand that is able to use a controller for the user. 

The intention of this project is to make an articulate, responsive robot hand for users who have limited hand mobility. 
The current iteration of this project plays [Super Hexagon](https://superhexagon.com/) with an *Xbox Core Wireless Controller* by tracking head input. 

#### Design Requirements:
- Must be a hands free game interaction 
- Is able to move a joystick with variable force
- Is able to pull a trigger and able to press a button
- Doesn’t break controller

## Controls
| Input | Controller setting | Game action |
| Head left | Left joystick pointing left | Move CCW |
| Head right | Left joystick pointing right | Move CW |
| N/a | A | Start |
| N/a | B | Back |

## Testing and Results

| Requirement  | Testing standard | Testing result |
| --- | --- | --- |
| Hands free game interaction  | Complete one round only using user input | Achieved 12/8 |
| Move a joystick with variable force  | Move joystick left and right | Achieved 12/6 |
| Pull a trigger and able to press a button  | Start game  | N/a |
| Doesn’t break controller | Hand holds controller for 15 minutes without dropping  | Achieved 12/6 |

## Final Product and Insights


#### Further development recommendations include: 
- Testing how much force is exerted by the hands to ensure that no damage (such as stuck buttons or stick drift) is done to the controller over time (actuation force vs applied force)
- Expand controller integration by adding more buttons/user inputs
- Add granularity to control with regard to joystick movement
- Adapt physical build to work with any controller 

## Files
Agile Development
- [Slides](slides/) :  Sprint presentations

Documentation
- [Final solution video](/) : View the project responding to head movements
- [Materials list](docs/) : List of purchased materials
- [References](docs/) : List of references used throughout project

Project files
- [Code](code/) : Control code


