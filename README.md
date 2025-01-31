# Simulation Flashlight App

## Overview
The **Simulation Flashlight App** is a powerful tool that simulates a flashlight with enhanced features, including multiple light modes (regular and strobe), brightness control, customizable light color, and an SOS signal. It also includes an emergency contact management system, battery simulation with low battery warnings, and usage tracking.

## Features
- **Light Modes**: Toggle between regular flashlight mode and strobe light mode.
- **Brightness Control**: Adjust the brightness of the flashlight from 0% to 100%.
- **Color Customization**: Select your desired flashlight color using a color picker.
- **SOS Signal**: Send an SOS signal in Morse code for emergency situations.
- **Emergency Contacts**: Manage and store emergency contacts to send alerts when SOS is activated.
- **Battery Simulation**: Simulate battery usage and display low battery warnings.
- **Usage Tracking**: Track how long the flashlight has been used, with updates every minute.

## Requirements
- Python 3.x
- `tkinter`
- `threading`
- `json`
- `datetime`

## Installation

1. Clone or download the repository.
2. Ensure that you have Python 3.x installed on your computer.
3. Run the app.

## Usage

- **Turn On/Off the Flashlight**: Click the "Turn On" button to activate the flashlight. The button will change to "Turn Off" when the light is on.
- **Adjust Brightness**: Use the brightness slider to control the light's brightness from 0% to 100%.
- **Change Flashlight Color**: Click the "Choose Color" button to pick a custom color for the flashlight.
- **Activate Strobe Mode**: Click the "Strobe Light" button to start/stop the strobe effect.
- **Send SOS Signal**: Click the "SOS Signal" button to activate the SOS signal in Morse code. This also sends a simulated emergency alert to your contacts.
- **Manage Emergency Contacts**: Click the "Manage Emergency Contacts" button to add, view, or remove emergency contacts for SOS alerts.

## Battery and Usage Tracking
- The app simulates battery usage, reducing the battery level when the flashlight is on. The battery level will be displayed at the top.
- A low battery warning will appear when the battery drops below 20%.
- The app tracks how long the flashlight has been in use, showing the usage time in minutes.

## Notes
- Emergency alerts are simulated when the SOS signal is activated.
- All settings, including brightness, color, and emergency contacts, are saved automatically.
