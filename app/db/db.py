# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

import logging
import pymysql
from flask import current_app as app
from app.db import sql
from app.models.restrictions import Restrictions

LOGGER = logging.getLogger(__name__)


def create_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        port=app.config['MYSQL_PORT'],
        database=app.config['MYSQL_DB'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        cursorclass=pymysql.cursors.DictCursor
    )


def get_countries():
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql.get_countries)
            return cursor.fetchall()
    finally:
        conn.close()


def get_country_details(country_id):
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql.get_country_details, country_id)
            details = cursor.fetchone()
            details["restrictions"] = {key: details.pop(key) for key
                                       in Restrictions.get_attrs()}
            return details
    finally:
        conn.close()


def get_country_timeseries(country_id):
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql.get_country_timeseries, country_id)
            return cursor.fetchall()
    finally:
        conn.close()
