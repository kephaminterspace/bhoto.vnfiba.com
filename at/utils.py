# - *- coding: utf- 8 - *-
import unicodedata

# Help select Box
def select_box_by_objects(objects=None, field_key="id", field_value="name", selected="",  name="", id="", cls="", style="", first_option_text=""):
    results = '<select name="'+name+'" id="'+id+'" class="'+cls+'" style="'+style+'">'
    if first_option_text:
        results += '<option value=''> -- '+first_option_text+' -- </option>'
    if objects:
        for item in objects:
            key = str(getattr(item, field_key))
            value = str(getattr(item, field_value))
            if key == str(selected):
                results += '<option value="' + key + '" selected="selected">' + value.encode('utf-8') + '</option>'
            else:
                results += '<option value="' + key + '">' + value + '</option>'
    results += '</select>'
    return results


def select_box_by_list_disabled(list=None, selected="", name="", id="", cls="", style="", first_option_text=""):
    results = '<select name="'+name+'" id="'+id+'" class="'+cls+'" style="'+style+'">'
    if first_option_text:
        results += '<option disabled> '+first_option_text+' </option>'
    if list:
        for item in list:
            key, value = item
            if str(key) == str(selected):
                results += '<option value="'+str(key)+'" selected="selected">' + value.encode('utf-8') + '</option>'
            else:
                results += '<option value="' + str(key) + '">' + value.encode('utf-8') + '</option>'
    results += '</select>'
    return results

def select_box_by_list(list=None, selected="", name="", id="", cls="", style="", first_option_text=""):
    required_text = first_option_text+ ' là bắt buộc'
    results = '<select name="'+name+'" id="'+id+'" class="'+cls+'" style="'+style+'" required oninvalid="setCustomValidity(\''+required_text+'\')" oninput="setCustomValidity(\'\')">'
    if first_option_text:
        results += '<option value=''> '+first_option_text+' </option>'
    if list:
        for item in list:
            key, value = item
            if str(key) == str(selected):
                results += '<option value="'+str(key)+'" selected="selected">' + value.encode('utf-8') + '</option>'
            else:
                results += '<option value="' + str(key) + '">' + value.encode('utf-8') + '</option>'
    results += '</select>'
    return results

# Constant
LEVEL_INSURRANCE=[
    (1,u"110 Triệu"),
    (2,u"220 Triệu"),
    (3,u"330 Triệu")
]

NUMBER_PERSION=[
    (1, u'1 Người'),
    (2, u'2 Người'),
    (3, u'3 Người'),
    (4, u'4 Người'),
    (5, u'5 Người'),
    (6, u'6 Người'),
    (7, u'7 Người'),
    (8, u'8 Người'),
    (9, u'9 Người'),
    (10, u'10 Người')
]

