"""Параметры проекции SVG-карты (генерируются вместе с templates/svg/map_kyrgyzstan.html)."""
import math

WIDTH = 1000
HEIGHT = 504
_PAD = 8
_MIN_LON = 69.2649523
_MAX_LAT = 43.2667971
_K = 0.7521870026190208
_SCALE = 119.30960597366389


def project(lat, lon):
    """Широта/долгота → координаты x, y во viewBox карты."""
    x = _PAD + (float(lon) - _MIN_LON) * _K * _SCALE
    y = _PAD + (_MAX_LAT - float(lat)) * _SCALE
    return round(x, 1), round(y, 1)
