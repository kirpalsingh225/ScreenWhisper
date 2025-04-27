from crewai.tools import tool # type: ignore
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
        time.sleep(8)
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
        pyautogui.click(x, y)
        time.sleep(5)
        pyautogui.write(text)
        time.sleep(8)
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
    


@tool
def take_screenshot():
    '''
    Useful to tell the screen information

    Args:
        None

    Output:
        Returns information about the screen elements and coordinates to click them
    '''


    image = pyautogui.screenshot("screen.jpg")
    image_path = "screen.jpg"
    image = Image.open(image_path)
    image_rgb = image.convert('RGB')
    print('image size:', image.size)

    box_overlay_ratio = max(image.size) / 3200
    draw_bbox_config = {
        'text_scale': 0.8 * box_overlay_ratio,
        'text_thickness': max(int(2 * box_overlay_ratio), 1),
        'text_padding': max(int(3 * box_overlay_ratio), 1),
        'thickness': max(int(3 * box_overlay_ratio), 1),
    }
    BOX_TRESHOLD = 0.05

    import time
    start = time.time()
    ocr_bbox_rslt, is_goal_filtered = check_ocr_box(image_path, display_img = False, output_bb_format='xyxy', goal_filtering=None, easyocr_args={'paragraph': False, 'text_threshold':0.9}, use_paddleocr=True)
    text, ocr_bbox = ocr_bbox_rslt
    cur_time_ocr = time.time() 

    dino_labled_img, label_coordinates, parsed_content_list = get_som_labeled_img(image_path, som_model, BOX_TRESHOLD = BOX_TRESHOLD, output_coord_in_ratio=True, ocr_bbox=ocr_bbox,draw_bbox_config=draw_bbox_config, caption_model_processor=caption_model_processor, ocr_text=text,use_local_semantics=True, iou_threshold=0.7, scale_img=False, batch_size=128)
    cur_time_caption = time.time() 

    screen_width = 1920
    screen_height = 1200

    center_coords_and_content_str = "\n".join(
    f"Content: {item['content']} | type: {item['type']} | Center: ({int((item['bbox'][0] + item['bbox'][2]) / 2 * screen_width)}, {int((item['bbox'][1] + item['bbox'][3]) / 2 * screen_height)})"
    for item in parsed_content_list
    )
    print(center_coords_and_content_str)

    return f"The current screen contains these elements Content is the name of the element, type of element and coordinates to click the element {center_coords_and_content_str}"

    