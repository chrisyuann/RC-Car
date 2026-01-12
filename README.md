# Remote Controlled Self-Designed Car

## Intro
I want to create a remote controlled car intended for audiences of kids and teenagers. The goal is to make the car fun and easy to drive and control with a remote. I want my car to be unique, and I'm coming up with original ideas to create the main aspects of the car: the steering and differential. For the steering, I will create a belt-and-pulley system operated by a servo, rotating a four-bar linkage system. The car will be a rear wheel differential, preventing slippage when the car is making sharp turns.

<img width="534" height="593" alt="Screenshot 2026-01-12 at 11 40 28 AM" src="https://github.com/user-attachments/assets/0cc0a0cf-3c2e-47b2-8449-dd32e2059b85" />

^^Steering System^^

## Research
I researched about the differential. The basics include a pinion gear that rotates the sun gear, rotating the differential housing. The inner gears rotate along with the housing. When the car is turning, the differential allows the wheels to spin at different speeds with two different D-shafts.

<img width="291" height="173" alt="image" src="https://github.com/user-attachments/assets/ad7b7e8b-af74-48aa-b0dc-0ec20650f13e" />



The steering system also required research. The most common type of steering is the rack and pinion. This design is used on the majority of produced cars, which solidifies reliability. I looked at other steering systems as well. The crank and slider system also turns the wheels and is used in some vehicles. However, I decided to build my own, using a belt-and-pulley that rotates the wheels.

<img width="247" height="204" alt="image" src="https://github.com/user-attachments/assets/d8893e0c-6da0-4dbe-b867-1e10dbf8865b" />

(Rack and Pinion)

<img width="259" height="194" alt="image" src="https://github.com/user-attachments/assets/59370417-70ca-4139-9217-7bbf7a5f0dbc" />

(Crank and Slider)

<img width="240" height="210" alt="image" src="https://github.com/user-attachments/assets/1d401b83-85e0-4b81-80c7-36ef841c4a62" />

(Belt and Pulley: My idea)

## Sketches, Modelling, Technical Specifications

### Steering System

Created rough sketching of the four-bar linkage system

<img width="167" height="54" alt="Screenshot 2026-01-12 at 12 11 48 PM" src="https://github.com/user-attachments/assets/5f244ef8-99b2-4efb-899e-be9c7b0aa38f" />

Used existing hubs to mount the wheels to the shafts:

<img width="370" height="208" alt="Screenshot 2026-01-12 at 12 12 19 PM" src="https://github.com/user-attachments/assets/62867c4e-69ed-4dc4-8496-c417ee5bef3d" />

Wheel leg:

<img width="173" height="100" alt="Screenshot 2026-01-12 at 12 12 39 PM" src="https://github.com/user-attachments/assets/ccad616e-3564-4cb7-aadb-63774db6d0ab" />

Assy:

<img width="245" height="167" alt="Screenshot 2026-01-12 at 12 12 48 PM" src="https://github.com/user-attachments/assets/7db43eb2-df18-491a-bf73-ea2327d814ac" />


I needed to figure out the ideal distance between the pulleys and I modeled it in CAD.

<img width="204" height="124" alt="Screenshot 2026-01-12 at 12 02 50 PM" src="https://github.com/user-attachments/assets/bfb3f2d8-2f64-47a0-bf87-07e00e5bbd41" />

(At the point of intersection, the servo head and turning joint will be ideally placed)

I made my servo mount on that point.

<img width="164" height="110" alt="Screenshot 2026-01-12 at 12 05 25 PM" src="https://github.com/user-attachments/assets/19bc1a1f-136c-4275-95c3-44a18ce1f7e6" />

Result:

<img width="206" height="132" alt="Screenshot 2026-01-12 at 12 05 57 PM" src="https://github.com/user-attachments/assets/c4b8548d-14f0-4e56-8034-eb1c0d4180b1" />

<img width="177" height="217" alt="Screenshot 2026-01-12 at 12 07 01 PM" src="https://github.com/user-attachments/assets/6a0a8fac-1ba2-4d3d-b890-dc93a4d1dd25" />

### Differential

I used bevel gears found on McMaster Carr.

<img width="161" height="162" alt="Screenshot 2026-01-12 at 12 08 12 PM" src="https://github.com/user-attachments/assets/89235dc1-94a9-4cd1-af21-54b8a3b8c5c0" />

Created a rough outline of the inner gears.

<img width="294" height="204" alt="Screenshot 2026-01-12 at 12 09 36 PM" src="https://github.com/user-attachments/assets/b29e6f0d-546a-4b88-b196-9debab81bd33" />

## Electrical Components

My Main electrical components:

Servo -

<img width="206" height="203" alt="Screenshot 2026-01-12 at 12 14 45 PM" src="https://github.com/user-attachments/assets/ce783ff6-3476-4cbd-bae5-359588201035" />

Raspberry pi - 

<img width="270" height="177" alt="Screenshot 2026-01-12 at 12 15 00 PM" src="https://github.com/user-attachments/assets/5b978e61-a70f-441e-88ff-dcfb0b52efbd" />

DC Motor - 

<img width="230" height="184" alt="Screenshot 2026-01-12 at 12 15 17 PM" src="https://github.com/user-attachments/assets/f7d22fff-3163-4e24-a428-ac84174bca60" />

H-Bridge Motor Driver -

<img width="211" height="198" alt="Screenshot 2026-01-12 at 12 15 37 PM" src="https://github.com/user-attachments/assets/529fb610-2f2b-4122-a5ea-22efb43f2dd2" />

Buck Converter (12 V to 5 V) -

<img width="215" height="153" alt="Screenshot 2026-01-12 at 12 15 56 PM" src="https://github.com/user-attachments/assets/27814178-1b28-4dfd-a4af-2f42eb797b39" />

OAK-D Camera (Potential Addition) -

<img width="227" height="150" alt="Screenshot 2026-01-12 at 12 16 20 PM" src="https://github.com/user-attachments/assets/c0af2057-3c51-4669-8ffc-fe3c137ead75" />

Rough electrical diagram:

<img width="430" height="331" alt="Screenshot 2026-01-12 at 12 16 35 PM" src="https://github.com/user-attachments/assets/2b355a26-9445-444b-9a71-a95657f0c16b" />

## Reflection as of 1/12/26)
I finished my steering system and have developed my chassis. I am currently mounting my components and troubleshooting the differential. I am still working on making my car into something tangible, but as of now, the steering system is working successfully.











