# conan-chakracore

[Conan.io](https://conan.io) package for the ChakraCore library.

**Warning:** this project is, right now, only a little test project, for learning how to use [Conan.io](https://conan.io). Although ChakraCode is suppose to be availabue under MacOS and Linux, this package is working under Windows only.

## Building

Run `conan test_package` to download the sources and build de package.

run `python build.py` for building all the packages. Dor building for an specific visual studio (for example, only one installed), set CONAN_VISUAL_VERSIONS before (`set CONAN_VISUAL_VERSIONS=12 for Visual studio 2013, for example, and then `python build.py` ).
