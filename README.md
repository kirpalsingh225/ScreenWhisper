
## ScreenWhisper

ScreenWhisper is an intelligent computer use agent designed to assist visually impaired individuals in navigating and interacting with basic computer tools. By leveraging advanced screen understanding techniques, ScreenWhisper makes everyday computer tasks more accessible and intuitive.

## Overview

ScreenWhisper captures the computer screen, analyzes it, and enables natural, action-driven interaction for users. It relies on Microsoft OmniParser to understand the screen contents and uses an Agent (built with CrewAI) that leverages different tools to plan and perform actions. The agent continuously monitors the screen state after each action, ensuring accurate and adaptive behavior.

## Components


- **Screen Parsing with Microsoft OmniParser**
  
  ScreenWhisper captures a screenshot and passes it through Microsoft OmniParser, which parses the screen into a structured set of screen elements like buttons, text fields, windows, and menus. This structured data provides a rich and detailed understanding of the screen state.

- **Agent and Tool-Based Action Handling (CrewAI)**

    Using CrewAI, ScreenWhisper creates an Agent that reasons about the current screen and the user's goal.
    The agent is equipped with specialized tools (e.g., click handler, text input simulator, OCR enhancer) to interact with the screen. It plans actions, executes them (e.g., mouse movement, clicks, typing), and re-analyzes the screen after each interaction.

## OmniParser 

![img](https://github.com/kirpalsingh225/ScreenWhisper/blob/main/artifacts/output.png)

- **Output**
  [{'type': 'text', 'bbox': [0.0052083334885537624, 0.7124999761581421, 0.05416666716337204, 0.7350000143051147], 'interactivity': False, 'content': 'dataset.zip', 'source': 'box_ocr_content_ocr'}, {'type': 'icon', 'bbox': [0.056129395961761475, 0.0037542819045484066, 0.11762545257806778, 0.11289024353027344], 'interactivity': True, 'content': '.pdf ', 'source': 'box_yolo_content_ocr'}, {'type': 'icon', 'bbox': [0.0007807731744833291, 0.003377351677045226, 0.058777738362550735, 0.11484784632921219], 'interactivity': True, 'content': 'Recycle Bin ', 'source': 'box_yolo_content_ocr'}]

## Architecture

![img](https://github.com/kirpalsingh225/ScreenWhisper/blob/main/artifacts/cua.png)

```
    Screenshot 
        ↓
    Microsoft OmniParser 
        ↓
    Parsed Screen Elements 
        ↓
    CrewAI Agent + Tools 
        ↓
    Planned Action 
        ↓
    Mouse Movements and Interactions
```


## Run Locally

Clone the project

```bash
  git clone git clone https://github.com/kirpalsingh225/ScreenWhisper

```

Go to the project directory

```bash
  cd ScreenWhisper
```

Install dependencies

```bash
  pip install -r requirements.txt
```

## References
[1] Microsoft Research. OmniParser: Screen Understanding through Structured Parsing.
Available: [https://www.microsoft.com/en-us/research/project/omniparser/](https://github.com/microsoft/OmniParser)


