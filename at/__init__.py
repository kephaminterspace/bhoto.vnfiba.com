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
    if request.method == 'POST':
        if form.validate_on_submit():
            data = {
                "properties": [
                    {"property": "firstname", "value": form.name.data},
                    {"property": "phone", "value": form.phone.data},
                    {"property": "car_type", "value": form.car_type.data},
                    {"property": "year_make", "value": form.year_make.data},
                    {"property": "code_promotion", "value": form.code_promotion.data},
                    {"property": "hs_lead_status", "value": "NEW"}
                ]
            }
            url = "https://api.hubapi.com/contacts/v1/contact/?hapikey=6a51ae32-e594-41f3-9c8b-f35401a1f4eb"
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

                        return render_template('index.html', form=form)
                else:
                    return render_template('thankyou.html')

            form.email.errors.append("Invalid data!")
            return render_template('index.html', form=form)

        else:
            return render_template('index.html', form=form)

    return render_template('index.html', form=form)


