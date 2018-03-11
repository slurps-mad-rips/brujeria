from brujeria.command.ninja import BuildNinjaExt as build_ninja_ext
from brujeria.command.ninja import BuildNinjaLib as build_ninja_clib
from brujeria import Distribution, Library, Extension, setup as setuptools
import pytest
import pdb

@pytest.fixture
def clib ():
    dist = Distribution()
    return build_ninja_clib(dist)
 
@pytest.fixture
def ext ():
    dist = Distribution()
    dist.ext_modules = [Extension('test', ['tests/test.cxx'])]
    return build_ninja_ext(dist)

@pytest.fixture
def module (module):
    options = dict(
        ext_modules=[module],
        script_name='test_build_ninja.py',
        script_args='build',
        cmdclass=dict(build_ext=build_ninja_ext))
    dist = Distribution(options)
    mod = build_ninja_ext(dist)
    mod.finalize_options()
    return mod

class TestNinjaExt:

    def test_ninja_ext_writer (self, ext):
        assert hasattr(ext, 'writer')

    def test_ninja_ext (self, ext: build_ninja_ext, tempdir):
        ext.build_temp = ext.build_lib = 'build'
        ext.finalize_options()
        ext.run()

    def test_ninja_ext_module (self, module: build_ninja_ext):
        module.run()

class TestNinjaLib:

    def test_ninja_clib_writer (self, clib):
        assert hasattr(clib, 'writer')
    
    def test_ninja_clib (self, clib: build_ninja_clib, tempdir):
        clib.build_temp = clib.build_clib = 'build'
        clib.finalize_options()
        clib.libraries = [Library('test', ['tests/test.cxx'])]
        clib.run()
