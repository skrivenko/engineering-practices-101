# -*- coding: utf-8 -*-

import os
import pytest


@pytest.fixture()
def change_test_dir(request):
    os.chdir(request.fspath.dirname)
    yield
    os.chdir(request.config.invocation_dir)


@pytest.fixture()
def text(change_test_dir):
    with open('./Kolobok.md', mode='r', encoding='utf-8') as output_file:
        return output_file.read()

def test_has_header(text):
    assert '# Сказка про колобка' in text

def test_has_subtitle1(text):
    assert '## 1. Как колобок появился' in text

def test_has_subtitle2(text):
    assert '## 2. Как колобок убежал' in text

def test_has_location(text):
    assert ('огород' in text) and ('лес' in text)