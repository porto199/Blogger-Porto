from flask import Flask, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename
from PIL import Image