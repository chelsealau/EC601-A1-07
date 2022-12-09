# Robotic Helping Hand For Adaptive Gaming

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
| --- | --- | --- |
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
![This is a video of the solution](IMG-9222.mov)

From this project, it is clear that using head tracking as a user input for assistive gaming is achievable. In this project, we were able to move a joystick left and right from the user moving their head left or right. Using ML allows for more adaptive solutions to gaming based on the library used. However there is a design tradeoff we encountered in this project between the complexity of the design (IE amount of user inputs) and integration (IE physical design of controller). 

#### Further development recommendations include: 
From this project, we were able to actualize a hands free gaming experience, but there is more that can be achieved. Some possible ideas include. 
- Testing how much force is exerted by the hands to ensure that no damage (such as stuck buttons or stick drift) is done to the controller over time (actuation force vs applied force)
- Expand controller integration by adding more buttons/user inputs
  - This can be done by tracking user eye movements or user expressions. However, this is where the design tradeoff comes in between integration and complexity of the physical build.
- Add granularity to control with regard to joystick movement
  - Currently the design moves left and right dramatically, not allowing for subtle left/right movement. This can be addressed either with improving the ML library used or changing the servo code. 
- Adapt physical build to work with any controller 

## Files
Agile Development
- [Slides](slides/) :  Sprint presentations

Documentation
- [Final solution video](IMG-9222.mov) : View the project responding to head movements
- [Materials list](docs/parts.md) : List of purchased materials
- [References](docs/ref.md) : List of references used throughout project

Project files
- [Code](src/) : Control code
