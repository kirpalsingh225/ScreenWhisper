from langchain_core.tools import tool # type: ignore
import pyautogui
import time


@tool   
def wait() -> str:
    '''
    Useful to wait

    Args:
        None

    Output:
        String indicating whether the action was completed or not
    '''
    try:
        time.sleep(5)
        return f"Successful to wait"
    except Exception as e:
        return f"Unsuccessful to wait because of {e}"

# @tool
# def open_application(app_name: str) -> str:
#     """
#     Useful to open application

#     Args:
#         app_name (str): The name of the application to be opened

#     Output:
#         String containing whether the application opened or not
#     """

#     try:
#         pyautogui.press('win')
#         time.sleep(2) 
#         pyautogui.write(app_name)
#         time.sleep(2)
#         pyautogui.press('enter')

#         return "Application successfully opened"
#     except Exception as e:
#         return f"Got an error beacuse of {e}"
    
@tool
def click_at(x : int, y : int) -> str:
    '''
    Useful to click an element on screen

    Args:
        x (int): the x coordinate of the element
        y (int): the y coordinate of the element

    Output:
        String indicating whether the action was completed or not
    '''
    try:
        pyautogui.click(x, y)
        return f"Successfully clicked on the {x} and {y} coordinates"
    except Exception as e:
        return f"Unsuccessfull to click on the {x} and {y} coordinates because of {e}"
    
@tool
def scroll() -> str:
    '''
    Useful to scroll the screen

    Args:
        None

    Output:
        String indicating whether the action was completed or not
    '''
    try:
        pyautogui.scroll(-200)
        return f"Successfully abled to scroll"
    except Exception as e:
        return f"Unsuccessfull to scroll because of {e}"
    
@tool
def type_text_at(text : str, x: int, y: int) -> str:
    '''
    Useful to write text on screen at certain coordinates

    Args:
        text(string) : the text that need to be typed
        x(int) : center x coordinate of element
        y(int) : center y coordinate of element

    Output:
        String indicating whether the action was completed or not
    '''
    try:
        pyautogui.write(text)
        return f"Successful to write the {text}"
    except Exception as e:
        return f"Unsuccessful to write the {text} because of {e}"
    
@tool
def press_key(key: str) -> str:
    '''
    Useful to press key

    Args:
        key(string) : name of the key to press

    Output:
        String indicating whether the action was completed or not
    '''
    try:
        pyautogui.press(key)
        time.sleep(5)
        return f"Successful to press the {key}"
    except Exception as e:
        return f"Unsuccessful to press the {key} because of {e}"

