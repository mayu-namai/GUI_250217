def set_selected_images(character, stage):
    global selected_character, selected_stage
    selected_character = character
    selected_stage = stage

def get_selected_images():
    return selected_character, selected_stage


def set_selected_all_images(character, stage, vignette):
    global selected_character, selected_stage, selected_vignette
    selected_character = character
    selected_stage = stage
    selected_vignette = vignette

def get_selected_all_images():
    return selected_character, selected_stage, selected_vignette

SEND_FILE_MAX_AGE_DEFAULT = 0
STATIC_PATH = '/static/'
CHARACTER_PATH = STATIC_PATH + 'ccfs/'
STAGE_PATH = STATIC_PATH + 'csfs/'
VIGNETTE_PATH = STATIC_PATH + 'outputs/'
NO_IMAGE_PATH = STATIC_PATH + 'no_image.png'

#ユーザによる代表フレームの抽出
selected_character = None
selected_stage = None
selected_vignette = None