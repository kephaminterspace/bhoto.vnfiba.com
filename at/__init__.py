# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask, Blueprint, request, render_template, url_for, send_from_directory
import logging
import datetime
import requests
import urllib
import json
import uuid

from .forms import BankForm
from .utils import *

logger = logging.getLogger(__name__)
app = Flask(__name__, template_folder="templates", static_folder="statics")
#app.config.from_object("at.config")
app.secret_key = 'ptifajdslkf'

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route("/", methods=['POST', 'GET'])
def index():
    form = BankForm()
    slbox_level_insurrance = select_box_by_list(LEVEL_INSURRANCE, form.level_insurrance.data, 'level_insurrance', 'level_insurrance', 'form-control styled', '',
                                      'Chọn mức bảo hiểm')
    slbox_number_persion = select_box_by_list(NUMBER_PERSION, form.number_persion.data, 'number_persion', 'number_persion', 'form-control styled', '',
                                      'Số lượng người tham gia')

    print()

    if request.method == 'POST':
        if form.validate_on_submit():
            data = {
                "properties": [
                    {"property":"identifier", "value":str(uuid.uuid4())},
                    {"property":"firstname", "value":form.name.data},
                    {"property":"lastname", "value":""},
                    {"property":"email", "value":str(uuid.uuid4())+'@interspace.vn'},
                    {"property":"phone", "value":form.phone.data},
                    {"property":"hs_lead_status", "value":"NEW"},
                    {"property":"level_insurrance", "value": int(form.level_insurrance.data)},
                    {"property":"code_promotion", "value": form.code_promotion.data},
                    {"property":"number_persion", "value":int(form.number_persion.data)},
                    {"property":"aff_source", "value":form.aff_source.data},
                    {"property":"aff_sid", "value":form.aff_sid.data},
                ]
            }

            url = "https://api.hubapi.com/contacts/v1/contact/?hapikey=533a6212-82d7-412a-9443-79507074efe7"
            header = {'Content-Type': 'application/json'}
            print json.dumps(data)
            res = requests.post(url=url, data=json.dumps(data), headers=header)
            res_json = res.json()

            if res_json:
                if "status" in res_json and res_json["status"] == "error":
                    if "error" in res_json and res_json["error"] == "CONTACT_EXISTS":
                        form.email.errors.append(u"Email đã tồn tại")
                    else:
                        form.email.errors.append(res_json["message"])

                        return render_template('index.html', form=form, slbox_level_insurrance=slbox_level_insurrance,
                                               slbox_number_persion=slbox_number_persion)
                else:
                    return render_template('thankyou.html')

            form.email.errors.append("Invalid data!")
            return render_template('index.html', form=form, slbox_level_insurrance=slbox_level_insurrance,
                                   slbox_number_persion=slbox_number_persion)

        else:
            return render_template('index.html', form=form, slbox_level_insurrance=slbox_level_insurrance,
                                   slbox_number_persion=slbox_number_persion)

    return render_template('index.html', form=form, slbox_level_insurrance=slbox_level_insurrance,
                               slbox_number_persion=slbox_number_persion)


