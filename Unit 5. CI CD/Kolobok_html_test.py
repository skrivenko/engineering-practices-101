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
    with open('./build/kolobok.html', mode='r', encoding='utf-8') as output_file:
        return output_file.read()


def test_has_header(text):
    assert '<h1>Сказка про колобка</h1>' in text
