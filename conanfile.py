#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostNumeric_ConversionConan(base.BoostBaseConan):
    name = "boost_numeric_conversion"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_numeric_conversion"
    lib_short_names = ["numeric_conversion"]
    header_only_libs = ["numeric_conversion"]
    b2_requires = [
        "boost_config",
        "boost_conversion",
        "boost_core",
        "boost_mpl",
        "boost_preprocessor",
        "boost_throw_exception",
        "boost_type_traits"
    ]
